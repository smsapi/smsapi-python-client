from smsapi.api import Api
from smsapi.endpoint import bind_api_endpoint
from smsapi.exception import EndpointException, SendException
from smsapi.models import SendResult
from smsapi.sms import response_format_param
from smsapi.mfa.model import SmsMFASendResult, SmsMFAVerifyResult

mfa_parameters = [
    'phone_number',
    'from',
    'from_',
    'content',
    'fast'
]

mfa_verify_parameters = [
    'phone_number',
    'code'
]


def parameters_transformer(_, parameters):
    if 'from_' in parameters:
        parameters['from'] = parameters.pop('from_')

    return parameters


class Mfa(Api):

    send_mfa = bind_api_endpoint(
        method='POST',
        path='mfa/codes',
        mapping=(SendResult, SmsMFASendResult),
        accept_parameters=mfa_parameters,
        force_parameters=response_format_param,
        exception_class=SendException,
        parameters_transformer=parameters_transformer
    )

    verify_mfa = bind_api_endpoint(
        method='POST',
        path='mfa/codes/verifications',
        mapping=(SendResult, SmsMFAVerifyResult),
        accept_parameters=mfa_verify_parameters,
        force_parameters=response_format_param,
        exception_class=EndpointException,
        parameters_transformer=parameters_transformer
    )



