# -*- coding: utf-8 -*-

from smsapi.api import Api
from smsapi.endpoint import bind_api_endpoint
from smsapi.exception import EndpointException
from smsapi.models import Model
from smsapi.sms import response_format_param
from smsapi.utils import join_params


def parameters_transformer(_, parameters):
    join_params(parameters, ['idx'], '|')
    return parameters


class HlrResult(Model):

    def __init__(self, status=None, number=None, id=None, price=None):
        super(HlrResult, self).__init__()

        self.status = status
        self.number = number
        self.id = id
        self.price = price


class Hlr(Api):

    path = 'hlr.do'

    check_number = bind_api_endpoint(
        method='GET',
        path=path,
        mapping=HlrResult,
        accept_parameters=['number', 'idx'],
        force_parameters=response_format_param,
        exception_class=EndpointException,
        parameters_transformer=parameters_transformer
    )
