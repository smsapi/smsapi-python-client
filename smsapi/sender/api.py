# -*- coding: utf-8 -*-

from smsapi.api import Api
from smsapi.endpoint import bind_api_endpoint
from smsapi.exception import EndpointException
from smsapi.models import ResultCollection
from smsapi.sms import response_format_param
from smsapi.utils import update_dict
from smsapi.sender.models import SenderNameResult, SenderNameSuccessResult


def parameters_transformer(mapped_param):
    def _parameters_transformer(_, parameters):
        parameters[mapped_param] = parameters.pop('name', None)
        return parameters
    return _parameters_transformer


class Sender(Api):

    path = 'sender.do'

    add = bind_api_endpoint(
        method='GET',
        path=path,
        mapping=SenderNameSuccessResult,
        accept_parameters=['name'],
        force_parameters=response_format_param,
        exception_class=EndpointException,
        parameters_transformer=parameters_transformer('add')
    )

    check = bind_api_endpoint(
        method='GET',
        path=path,
        mapping=SenderNameResult,
        accept_parameters=['name'],
        force_parameters=response_format_param,
        exception_class=EndpointException,
        parameters_transformer=parameters_transformer('status')
    )

    remove = bind_api_endpoint(
        method='GET',
        path=path,
        mapping=SenderNameSuccessResult,
        accept_parameters=['name'],
        force_parameters=response_format_param,
        exception_class=EndpointException,
        parameters_transformer=parameters_transformer('delete')
    )

    list = bind_api_endpoint(
        method='GET',
        path=path,
        mapping=(SenderNameResult, ResultCollection),
        force_parameters=update_dict(response_format_param, {'list': True}),
        exception_class=EndpointException
    )

    default = bind_api_endpoint(
        method='GET',
        path=path,
        mapping=SenderNameSuccessResult,
        accept_parameters=['name'],
        force_parameters=response_format_param,
        exception_class=EndpointException,
        parameters_transformer=parameters_transformer('default')
    )
