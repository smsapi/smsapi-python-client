# -*- coding: utf-8 -*-

from .action import ApiAction
from .message import ApiSendAction


class CheckAction(ApiSendAction, ApiAction):

    def __init__(self, proxy, uri):
        super(CheckAction, self).__init__(proxy, uri)

    def set_numbers(self, *args):
        self._data['number'] = ','.join([str(num) for num in args])
        return self

    def set_idx(self, *args):
        self._data['idx'] = '|'.join([str(id) for id in args])
        return self
