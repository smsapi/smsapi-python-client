from smsapi.api import Api
from smsapi.blacklist.models import BlacklistPhoneNumber
from smsapi.endpoint import bind_api_endpoint
from smsapi.exception import EndpointException
from smsapi.models import ModelCollection

list_params = ['q', 'offset', 'limit', 'orderBy']

accept_parameters = [
    'phone_number',
    'expire_at'
]


class Blacklist(Api):

    path = 'blacklist/phone_numbers'

    list_phone_numbers = bind_api_endpoint(
        method='GET',
        path=path,
        mapping=(BlacklistPhoneNumber, ModelCollection),
        accept_parameters=list_params,
        exception_class=EndpointException
    )

    add_phone_number = bind_api_endpoint(
        method='POST',
        path=path,
        mapping=BlacklistPhoneNumber,
        accept_parameters=accept_parameters,
        exception_class=EndpointException
    )

    delete_phone_number = bind_api_endpoint(
        method='DELETE',
        path="%s/{id}" % path,
        accept_parameters=['id'],
        exception_class=EndpointException
    )

    delete_all_phone_numbers = bind_api_endpoint(
        method='DELETE',
        path=path,
        exception_class=EndpointException
    )
