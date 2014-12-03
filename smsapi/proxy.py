# -*- coding: utf-8 -*-

import os
import sys
import mimetypes
from io import BytesIO

try:
    from urllib2 import Request, urlopen, URLError
    from urllib import urlencode
except ImportError:
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
    from urllib.error import URLError

try:
    from mimetools import choose_boundary
except ImportError:
    from uuid import uuid4
    
    def choose_boundary():
        return str(uuid4())
    

if sys.version_info[0] == 3:
    text_type = str
else:
    text_type = unicode


class ApiProxyError(Exception):
    pass


class ApiProxy(object):
    
    def __init__(self, hostname=None, data=None):
        super(ApiProxy, self).__init__()

        self.hostname = hostname

        self.data = data or {}

        self.files = []

    def set_hostname(self, hostname):
        self.hostname = hostname

    def execute(self):
        raise NotImplementedError


class ApiHttpProxy(ApiProxy):
    
    user_agent = 'PySmsAPI'
    
    def __init__(self, hostname=None, data=None):
        super(ApiHttpProxy, self).__init__(hostname, data)
        
        self.headers = {}
        
        self.body = {}
    
    def execute(self, uri=None, data=None):
        
        if isinstance(data, dict):
            self.data.update(data)        
        
        headers, body = self.prepare_request()

        response = None

        if isinstance(self.hostname, (list, tuple)):
            for host in self.hostname:
                response = self.connect(host, uri, body, headers)
                
                if response and response.getcode() == 200:
                    break
        else:
            response = self.connect(self.hostname, uri, body, headers)

        if not response:
            raise ApiProxyError("Unable connect to the specified url: %s" % str(self.hostname))
        
        return response
    
    def connect(self, hostname, uri, body, headers):
        try:
            uri = uri or ''
            if hostname.endswith('/'):
                url = hostname + uri
            else:
                url = '%s/%s' % (hostname, uri) 

            req = Request(url, body, headers)                
            response = urlopen(req)
            
            return response
        except (URLError, ValueError):
            return False

    def add_file(self, filepath):
        if os.path.isfile(filepath):
            self.files.append(filepath)
        else:
            raise ValueError('Argument must be a file.')
        
    def prepare_request(self):

        headers = {
            'User-Agent': self.user_agent,
        }

        if isinstance(self.data, dict):
            self.data.update(self.data)     
        
        if self.files:
            content_type, data = self.encode_multipart_data()

            headers.update({
                'Content-Type': content_type, 
                'Content-Length': str(len(data))
            })
        else:
            headers.update({
                'Content-type': "application/x-www-form-urlencoded; charset=utf-8"
            })
            
            data = urlencode(self.data).encode('utf-8')
            
        return headers, data

    def encode_multipart_data(self):

        def encode(data):
            if isinstance(data, text_type):
                data = data.encode('utf-8')
            return data
                
        boundary = choose_boundary()

        body = BytesIO()
        
        for (key, value) in self.data.items():
            body.write(encode('--%s\r\n' % boundary))
            body.write(encode('Content-Disposition: form-data; name="%s"' % key))
            body.write(encode('\r\n\r\n' + str(value) + '\r\n'))
            
        for _file in self.files:
            body.write(encode('--%s\r\n' % boundary))
            body.write(encode('Content-Disposition: form-data; name="file"; filename="%s"\r\n' % _file))
            body.write(encode('Content-Type: %s\r\n' % mimetypes.guess_type(_file)[0] or 'application/octet-stream'))
            body.write(encode('\r\n'))
            
            try:
                with open(_file, 'rb') as f:
                    data = f.read()
                    body.write(encode(data))
            except IOError:
                raise
            
            body.write(encode('\r\n'))            

        body.write(encode('--%s--\r\n\r\n' % boundary))

        content_type = 'multipart/form-data; boundary=%s' % boundary

        return content_type, body.getvalue()

