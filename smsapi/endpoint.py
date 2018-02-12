# -*- coding: utf-8 -*-

import re
import requests
import uuid

from . import lib_info
from .compat import quote, py_version
from .utils import convert_to_utf8_str, is_http_success, filter_dict
from .exception import EndpointException


def bind_api_endpoint(**config):

    class ApiEndpoint(object):

        method = config.get('method')

        path = config.get('path')

        response_mapping = config.get('mapping')

        accept_parameters = config.get('accept_parameters', [])

        force_parameters = config.get('force_parameters')

        parameters_transformer = config.get('parameters_transformer')

        exception_class = config.get('exception_class')

        def __init__(self, api, parameters):

            super(ApiEndpoint, self).__init__()

            self.api = api

            self.files = None

            self.parameters = parameters

            self.filter_parameters()
            self.compile_path()

        def filter_parameters(self):

            compiled_parameters = {}

            for key, val in self.parameters.items():
                if key in self.accept_parameters:
                    compiled_parameters[key] = convert_to_utf8_str(val)

            if self.force_parameters:
                compiled_parameters.update(self.force_parameters)

            if self.parameters_transformer:
                compiled_parameters = self.parameters_transformer(compiled_parameters)

            compiled_parameters = filter_dict(compiled_parameters)

            self.parameters = compiled_parameters

        def compile_path(self):

            placeholder_pattern = re.compile('{\w+}')

            for placeholder in placeholder_pattern.findall(self.path):
                name = placeholder.strip('{}')

                if name in self.parameters:
                    param = quote(self.parameters.pop(name))
                    self.path = self.path.replace(placeholder, param)
                else:
                    raise EndpointException("No parameter found for path variable '%s'" % name)

        def send_request(self):

            url = '%s%s' % (self.api.client.domain, self.path)

            headers = {
                'User-Agent': '%s (Python%s)' % (lib_info, py_version),
                'X-Request-Id': str(uuid.uuid4())
            }

            kwargs = {
                'auth': self.api.client.auth,
                'headers': headers,
                'files': self.files}

            if self.method is 'GET':
                kwargs.update({'params': self.parameters})
            else:
                kwargs.update({'data': self.parameters})

            raw_response = requests.request(self.method, url, **kwargs)

            return self.process_response(raw_response, url=url)

        def process_response(self, raw_response, url=None):

            if not is_http_success(raw_response.status_code):
                raise EndpointException(raw_response.text, raw_response.status_code, url=url, http_method=self.method)

            try:
                response = raw_response.json()
            except ValueError as e:
                response = {}

            if self.exception_class and isinstance(response, dict) and response.get('error'):
                raise self.exception_class.from_dict(response)

            if isinstance(self.response_mapping, tuple):
                model, type = self.response_mapping
                response = type.parse(response, model)
            elif self.response_mapping:
                response = self.response_mapping.from_dict(response, raw_response=raw_response)

            return response

        def add_file(self, file):
            self.files = {'file': file}

    def __call(api, **kwargs):
        endpoint = ApiEndpoint(api, kwargs)
        return endpoint.send_request()

    return __call