# -*- coding: utf-8 -*-

from smsapi.account.models import AccountBalanceResult, UserResult
from smsapi.api import Api
from smsapi.endpoint import bind_api_endpoint
from smsapi.exception import EndpointException
from smsapi.models import ResultCollection
from smsapi.sms import response_format_param
from smsapi.utils import update_dict

accept_parameters = [
    'name',
    'password',
    'api_password',
    'limit',
    'month_limit',
    'senders',
    'phonebook',
    'active',
    'info',
    'without_prefix'
]


def parameters_transformer(mapping):
    def _parameters_transformer(_, parameters):
        for k, v in mapping.items():
            parameters[v] = parameters.pop(k)

        parameters['pass'] = parameters.pop('password', None)
        parameters['pass_api'] = parameters.pop('api_password', None)

        return parameters

    return _parameters_transformer


class Account(Api):

    path = 'user.do'

    balance = bind_api_endpoint(
        method='GET',
        path=path,
        mapping=AccountBalanceResult,
        force_parameters=update_dict(response_format_param, {'credits': 1, 'details': 1}),
        exception_class=EndpointException
    )

    user = bind_api_endpoint(
        method='GET',
        path=path,
        mapping=UserResult,
        accept_parameters=['name'],
        force_parameters=response_format_param,
        exception_class=EndpointException,
        parameters_transformer=parameters_transformer({'name': 'get_user'})
    )

    create_user = bind_api_endpoint(
        method='GET',
        path=path,
        mapping=UserResult,
        accept_parameters=accept_parameters,
        force_parameters=response_format_param,
        exception_class=EndpointException,
        parameters_transformer=parameters_transformer({'name': 'add_user'})
    )

    update_user = bind_api_endpoint(
        method='GET',
        path=path,
        mapping=UserResult,
        accept_parameters=accept_parameters,
        force_parameters=response_format_param,
        exception_class=EndpointException,
        parameters_transformer=parameters_transformer({'name': 'set_user'})
    )

    list_users = bind_api_endpoint(
        method='GET',
        path=path,
        mapping=(UserResult, ResultCollection),
        force_parameters=update_dict(response_format_param, {'list': 1}),
        exception_class=EndpointException
    )