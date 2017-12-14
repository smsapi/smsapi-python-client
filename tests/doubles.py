# -*- coding: utf-8 -*-

import os
import json
import types

from smsapi.compat import urlparse


class RequestFake(object):

    last_called_api_method = None

    fixtures_base_dir = None

    def __call__(self, *args, **kwargs):
        self.http_method, self.url = args
        self.headers = kwargs.get('headers')
        self.data = kwargs.get('data')
        self.files = kwargs.get('files')
        self.params = kwargs.get('params')

        dir = os.path.abspath(os.path.dirname(__file__))

        parsed_url = urlparse(self.url)

        if self.fixtures_base_dir:
            api = self.fixtures_base_dir
        else:
            api = parsed_url.path.split("/")[1].split('.')[0]

        with open('%s/%s/fixtures/%s.json' % (dir, api, self.last_called_api_method)) as f:
            response = json.loads(f.read())

        status_code = response.get('status_code')
        content = response.get('response')
        headers = response.get('headers')

        self.last_called_api_method = None
        self.fixtures_base_dir = None

        return ResponseMock(status_code, content, headers)


class ResponseMock(object):

    force_status_code = None

    def __init__(self, status_code, content, headers):
        super(ResponseMock, self).__init__()

        self.code = status_code
        self.content = content
        self.headers = headers or {}

    @property
    def status_code(self):
        if self.force_status_code:
            return self.force_status_code
        return self.code

    def json(self):
        return self.content


class ApiSpy(object):

    def __init__(self, api):
        super(ApiSpy, self).__init__()

        self.api = api

    def __getattr__(self, item):

        attr = getattr(self.api, item)

        if isinstance(attr, types.MethodType) and request_fake.last_called_api_method is None:
            request_fake.last_called_api_method = item

        return attr


def api_response_fixture(fixture, dir = None):
    def decorator(func):
        def func_wrapper(name):
            request_fake.fixtures_base_dir = dir
            request_fake.last_called_api_method = fixture
            return func(name)
        return func_wrapper
    return decorator


request_fake = RequestFake()