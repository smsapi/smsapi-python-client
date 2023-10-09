from smsapi.api import Api
from smsapi.endpoint import bind_api_endpoint
from smsapi.exception import EndpointException, SendException
from smsapi.models import ResultCollection, SendResult, RemoveMessageResult
from smsapi.sms import response_format_param
from smsapi.utils import join_params

accept_parameters = [
    'subject',
    'smil',
    'date',
    'date_validate',
    'idx',
    'check_idx',
    'notify_url',
    'test'
]


def parameters_transformer(_, parameters):
    join_params(parameters, ['idx'], '|')

    return parameters


def delete_sms_params_transformer(_, parameters):
    join_params(parameters, ['sch_del'])

    if 'id' in parameters:
        parameters['sch_del'] = parameters.pop('id')

        return parameters


class Mms(Api):

    path = 'mms.do'

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
