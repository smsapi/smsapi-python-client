# -*- coding: utf-8 -*-

from requests.auth import AuthBase


class BearerAuth(AuthBase):

    def __init__(self, access_token):
        self.access_token = access_token

    def __eq__(self, other):
        return self.access_token == getattr(other, 'access_token', None)

    def __ne__(self, other):
        return not self == other

    def __call__(self, r):
        r.headers['Authorization'] = 'Bearer %s' % self.access_token
        return r
