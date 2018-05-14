# -*- coding: utf-8 -*-

from smsapi.models import Model


class SenderNameResult(Model):

    def __init__(self, sender=None, status=None, default=None, **kwargs):
        super(SenderNameResult, self).__init__()

        self.sender = sender or kwargs.get('name')
        self.status = status
        self.default = default


class SenderNameSuccessResult(Model):

    def __init__(self, count=None):
        super(SenderNameSuccessResult, self).__init__()

        self.count = count
