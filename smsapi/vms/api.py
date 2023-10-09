import os

from smsapi.api import Api
from smsapi.endpoint import bind_api_endpoint
from smsapi.exception import EndpointException, SendException
from smsapi.models import SendResult, ResultCollection, RemoveMessageResult
from smsapi.sms import response_format_param
from smsapi.utils import join_params

accept_parameters = [
    'from',
    'tts',
    'file',
    'tts_lector',
    'date',
    'date_validate',
    'try_',
    'interval',
    'skip_gms',
    'idx',
    'check_idx',
    'notify_url',
    'test'
]


def parameters_transformer(api_endpoint, parameters):
    join_params(parameters, ['idx'], '|')

    if 'try_' in parameters:
        parameters['try'] = parameters.pop('try_')

    if 'file' in parameters and os.path.isfile(parameters.get('file')):
        api_endpoint.add_file(open(parameters.pop('file'), 'rb'))

    return parameters


def delete_sms_params_transformer(_, parameters):
    join_params(parameters, ['sch_del'])

    if 'id' in parameters:
        parameters['sch_del'] = parameters.pop('id')

        return parameters


class Vms(Api):

    path = 'vms.do'

    send = bind_api_endpoint(
        method='POST',
        path=path,
        mapping=(SendResult, ResultCollection),
        accept_parameters=accept_parameters + ['to'],
        force_parameters=response_format_param,
        exception_class=SendException,
        parameters_transformer=parameters_transformer
    )

    send_to_group = bind_api_endpoint(
        method='POST',
        path=path,
        mapping=(SendResult, ResultCollection),
        accept_parameters=accept_parameters + ['group'],
        force_parameters=response_format_param,
        exception_class=SendException,
        parameters_transformer=parameters_transformer
    )

    remove_scheduled = bind_api_endpoint(
        method='POST',
        path=path,
        mapping=(RemoveMessageResult, ResultCollection),
        accept_parameters=['id'],
        force_parameters=response_format_param,
        exception_class=EndpointException,
        parameters_transformer=delete_sms_params_transformer
    )

