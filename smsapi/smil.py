# -*- coding: utf-8 -*-

import os
import re
import base64
import mimetypes
import xml.etree.ElementTree as ET

try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen

from .mime_types import mime_types


class SmilError(Exception):
    pass


class SmilElement(object):
    
    def render(self):
        raise NotImplementedError
    
    def get_element(self):
        return self.element


class Smil(object):
    
    def __init__(self):
        super(Smil, self).__init__()
         
        self.root = ET.Element('smil')
        
        self.head = SmilHead()
        self.body = SmilBody()
        
        self.subelements = list()

        self.subelements.append(self.head)
        self.subelements.append(self.body)
        
        self._tree = None
        
        self.update = False
        
    def set_width(self, width):
        self.head.set_width(width)

    def set_height(self, height):
        self.head.set_height(height)
    
    def add_image(self, image, attributes=None):
        
        if not isinstance(image, SmilImage):
            media_element = SmilImage(image, attributes)
        else:
            media_element = image
        
        self.notify(media_element, attributes)

    def add_text(self, text, attributes=None):

        if not isinstance(text, SmilText):
            media_element = SmilText(text, attributes)
        else:
            media_element = text
        
        self.notify(media_element, attributes)
    
    def add_audio(self, audio, attributes=None):
        
        if not isinstance(audio, SmilAudio):
            media_element = SmilAudio(audio, attributes)
        else:
            media_element = audio

        self.notify(media_element, attributes)
            
    def add_video(self, video, attributes=None):

        if not isinstance(video, SmilVideo):
            media_element = SmilVideo(video, attributes)
        else:
            media_element = video
            
        self.notify(media_element, attributes)
                        
    def notify(self, element, attributes=None):
        self.update = True
        
        for elem in self.subelements:
            if hasattr(elem, 'register'):
                elem.register(element)
        
    @property
    def tree(self):
        if self.update or self._tree is None:
            self._tree = self.root
            
            for sub_element in self.subelements:
                self._tree.append(sub_element.get_element())
                
            self.update = False                
        
        return self._tree
        
    def render(self, pretty_print=False):
        if pretty_print:
            for elem in self.tree.iter():
                elem.tail = "\n"

        return ET.tostring(self.tree)

    def __str__(self):
        return self.render()
    

class SmilHead(SmilElement):
    
    __attrs__ = ('id', 'height', 'width', 'fit')
    
    def __init__(self):
        self.element = ET.Element('head')
        self.layout = ET.SubElement(self.element, 'layout')
        self.root_layout = ET.SubElement(self.layout, 'root-layout')
        
    def register(self, media, attributes=None):
                
        attributes = attributes or {}
                
        if isinstance(attributes, dict):
            attributes = dict((n, v) for (n, v) in attributes.items() if n in self.__attrs__)
        
        if 'id' not in attributes:    
            attributes['id'] = media.id
        
        region = ET.Element('region', attributes)
        
        self.layout.append(region)

    def set_width(self, width):
        self.root_layout.set('width', width)

    def set_height(self, height):
        self.root_layout.set('width', height)


class SmilBody(SmilElement):
    
    def __init__(self):
        self.element = ET.Element('body')

        self.animation = ET.SubElement(self.element, 'par')
        
    def register(self, media):
        elem = media.get_element()
        
        if isinstance(media, (SmilMedia, SmilAnimation)):
            self.animation.append(elem)


class SmilAnimation(SmilElement):
    pass


class SmilMedia(SmilElement):

    __attrs__ = ('id', 'type', 'region', 'dur')
    
    def __init__(self, src=None, attributes=None):
        super(SmilMedia, self).__init__()
        
        self.mime_type = None
        
        self.attributes = attributes or {}

        self.mime_detector = mimetypes.MimeTypes()
        
        for mime, ext in mime_types.items():
            self.mime_detector.add_type(mime, ext)  

        if src is not None:
            self.set_src(src)
            
        self.set_attributes(self.attributes)
        
    def set_attributes(self, attributes):
        if not isinstance(attributes, dict):
            raise TypeError("Attributes must by a dictionary.")
        
        if 'region' not in attributes:
            attributes.update({'region': self.id})        
            
        attrs = {}
            
        for name, value in attributes.items():
            if name in SmilMedia.__attrs__:
                attrs[name] = value
                
                if hasattr(self, 'set_' + name):
                    getattr(self, 'set_' + name)(value)
                else:
                    self.element.set(name, value)
                    
        self.attributes = attrs

    def set_src(self, src):
        
        data = None
        
        source = ''

        if os.path.isfile(src):
            try:
                with open(src, 'rb') as image_file:
                    data = image_file.read()
            except IOError:
                raise SmilError("Cant't read file.")
        elif src.startswith(('http://', 'https://')):
            try:
                http_resp = urlopen(src)
                
                if http_resp.getcode() == 200:
                    data = http_resp.read()
            except ValueError:
                raise SmilError("Unable to fetch resource.")   
        
        if data:
            self.mime_type = self.detect_mime_type(src)
            source = self.encode_data(data)
        elif re.match('data:%s/[^\W\d_]+;base64,[\w]+' % self.mime_prefix, src):
            source = data

        self.element.set('src', source)
        
    def detect_mime_type(self, src):    
        
        mime_type, encoding = self.mime_detector.guess_type(src)

        if not mime_type or not mime_type.startswith(self.mime_prefix):
            raise SmilError("Unrecognized data type.")
        
        return mime_type

    def encode_data(self, data, force_mime_type=None):
        mime_type = force_mime_type or self.mime_type
        
        if not isinstance(data, bytes):
            data = data.encode('utf-8')
        
        data = base64.b64encode(data)
        
        return 'data:%s;base64,%s' % (mime_type, data)
           
    def render(self):
        return ET.tostring(self.element)


class SmilImage(SmilMedia):
    
    index = 1
    
    mime_prefix = 'image'
    
    def __init__(self, src=None, attributes=None):
        self.element = ET.Element('img')
        
        self.id = 'Image%s' % SmilImage.index           
        
        super(SmilImage, self).__init__(src, attributes)          


class SmilAudio(SmilMedia):

    index = 1

    mime_prefix = 'audio'
    
    def __init__(self, src=None, attributes=None):
        self.element = ET.Element('audio')
        
        self.id = 'Audio%s' % SmilAudio.index           
        
        super(SmilAudio, self).__init__(src, attributes)

        SmilAudio.index += 1


class SmilText(SmilMedia):

    index = 1

    mime_prefix = 'text'

    def __init__(self, src=None, attributes=None):
        self.element = ET.Element('text')
        
        self.id = 'Text%s' % SmilText.index        
        
        super(SmilText, self).__init__(src, attributes)
        
        SmilText.index += 1    

    def set_src(self, src):
        super(SmilText, self).set_src(src)
        
        if src and not self.element.get('src'):
            self.element.set('src', self.encode_data(src, 'text/plain'))


class SmilVideo(SmilMedia):

    index = 1

    mime_prefix = 'video'

    def __init__(self, src=None, attributes=None):
        self.element = ET.Element('video')
        
        self.id = 'Video%s' % SmilVideo.index        

        super(SmilVideo, self).__init__(src, attributes)
        
        SmilVideo.index += 1

