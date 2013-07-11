# -*- coding: utf-8 -*-

from .action import ApiAction
from .message import ApiSendAction
from smsapi.smil import Smil
from smsapi.responses import ApiResponse


class SendAction(ApiSendAction, ApiAction):
    
    def __init__(self, proxy, uri):
        super(SendAction, self).__init__(proxy, uri)
        
        self.message = Smil()
        
    def set_subject(self, subject):
        if len(subject) > 36:
            raise ValueError("Value error")
        self._data['subject'] = subject
        
        return self
        
    def add_image(self, image):        
        self.message.add_image(image)
        return self
    
    def add_audio(self, audio):
        self.message.add_audio(audio)
        return self
    
    def add_video(self, video):
        self.message.add_video(video)
        return self

    def add_text(self, text):
        self.message.add_text(text)
        return self

    def set_content(self, message):
        self.message = message
        return self
        
    def execute(self):        
        if isinstance(self.message, Smil):
            self._data['smil'] = self.message.render()
        else:
            self._data['smil'] = self.message

        api_response = self.proxy.execute(self.uri, self._data)
        return ApiResponse(api_response)


class GetAction(ApiAction):
    
    def set_id(self, message_id):
        self._data['status'] = message_id
        return self

    def execute(self):
        api_response = self.proxy.execute(self.uri, self._data)
        return ApiResponse(api_response)


class DeleteAction(ApiAction):

    def set_id(self, message_id):
        self._data['sch_del'] = message_id
    
    def execute(self):
        api_response = self.proxy.execute(self.uri, self._data)
        return ApiResponse(api_response)
