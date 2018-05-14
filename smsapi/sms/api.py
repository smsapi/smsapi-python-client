# -*- coding: utf-8 -*-

from smsapi.api import Api
from smsapi.endpoint import bind_api_endpoint
from smsapi.exception import EndpointException, SendException
from smsapi.models import ResultCollection, SendResult, RemoveMessageResult
from smsapi.sms import response_format_param
from smsapi.utils import join_params

sms_parameters = [
    'message',
    'from_',
    'encoding',
    'details',
    'template',
    'date',
    'datacoding',
    'udh',
    'skip_foreign',
    'allow_duplicates',
    'idx',
    'check_idx',
    'nounicode',
    'normalize',
    'partner_id',
    'max_parts',
    'expiration_date',
    'discount_group',
    'notify_url',
    'param1',
    'param2',
    'param3',
    'param4',
    'test'
]

fast_force_params = {'fast': 1}
flash_force_params = {'flash': 1}

fast_force_params.update(response_format_param)
flash_force_params.update(response_format_param)


def parameters_transformer(_, parameters):

    join_params(parameters, ['to', 'id'])
    join_params(parameters, ['param1', 'param2', 'param3', 'param4', 'idx'], '|')

    if 'from_' in parameters:
        parameters['from'] = parameters.pop('from_')

    return parameters


class Sms(Api):

    path = 'sms.do'

    send = bind_api_endpoint(
        method='GET',
        path=path,
        mapping=(SendResult, ResultCollection),
        accept_parameters=sms_parameters + ['to'],
        force_parameters=response_format_param,
        exception_class=SendException,
        parameters_transformer=parameters_transformer
    )

    send_fast = bind_api_endpoint(
        method='GET',
        path=path,
        mapping=(SendResult, ResultCollection),
        accept_parameters=sms_parameters + ['to'],
        force_parameters=fast_force_params,
        exception_class=SendException,
        parameters_transformer=parameters_transformer
    )

    send_flash = bind_api_endpoint(
        method='GET',
        path=path,
        mapping=(SendResult, ResultCollection),
        accept_parameters=sms_parameters + ['to'],
        force_parameters=flash_force_params,
        exception_class=SendException,
        parameters_transformer=parameters_transformer
    )

    send_to_group = bind_api_endpoint(
        method='GET',
        path=path,
        mapping=(SendResult, ResultCollection),
        accept_parameters=sms_parameters + ['group'],
        force_parameters=response_format_param,
        exception_class=SendException,
        parameters_transformer=parameters_transformer
    )

    remove_scheduled = bind_api_endpoint(
        method='GET',
        path=path,
        mapping=(RemoveMessageResult, ResultCollection),
        accept_parameters=['id'],
        force_parameters=response_format_param,
        exception_class=EndpointException,
        parameters_transformer=parameters_transformer
    )
