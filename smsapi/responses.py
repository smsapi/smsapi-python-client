# -*- coding: utf-8 -*-

import json

class ApiError(Exception):        

    def __init__(self, data):
        super(ApiError, self).__init__()

        self.message = data.get('message')
        self.code = data.get('error')


class ApiResponse(object):
    
    def __init__(self, data):
        
        self.url = data.geturl()
        
        self.status_code = data.getcode()        

        self.index = -1

        self.count = None

        self.data = []
        
        self.current = {}
        
        data = data.read()
        
        if isinstance(data, bytes):
            data = data.decode('utf-8')

        try:
            data = json.loads(data)
        except ValueError:
            if data.startswith('ERROR'):
                raise ApiError({'error': data.split(':')[1]})
                
        if isinstance(data, dict):
            if data.get('error'):
                raise ApiError(data)

            self.count = data.get('count')
            
            if 'list' in data:
                self.data = data.get('list')
            else:
                self.data.append(data)
        else:
            self.data = data
            
        try:
            self.current = self.data[0]
        except IndexError:
            pass

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()
        
    def next(self):
        self.index += 1

        try:
            self.current = self.data[self.index]
        except IndexError:
            raise StopIteration

        return self        

    def __getattr__(self, attr):
        try:
            return self.current[attr]
        except KeyError:
            raise

