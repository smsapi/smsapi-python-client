# -*- coding: utf-8 -*-

from smsapi.models import Model


class SenderNameResult(Model):

    def __init__(self, name=None, status=None, default=None):
        super(SenderNameResult, self).__init__()

        self.name = name
        self.status = status
        self.default = default


class SenderNameRemoveResult(Model):

    def __init__(self, count=None):
        super(SenderNameRemoveResult, self).__init__()

        self.count = count


class SenderNameSetAsDefaultResult(Model):

    def __init__(self, count=None):
        super(SenderNameSetAsDefaultResult, self).__init__()

        self.count = count