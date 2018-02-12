# -*- coding: utf-8 -*-

import os

from smsapi.api import Api
from smsapi.endpoint import bind_api_endpoint
from smsapi.exception import EndpointException
from smsapi.models import ModelCollection
from smsapi.short_url.models import ShortUrlClick, ShortUrlClickByMobileDevice, ShortUrl as ShortUrlModel

clicks_accept_parameters = [
    'date_from',
    'date_to',
    'links'
]

short_url_parameters = [
    'url',
    'file',
    'name',
    'expire',
    'description'
]


def parameters_transformer(api_endpoint, parameters):
    if 'file' in parameters and os.path.isfile(parameters.get('file')):
        api_endpoint.add_file(open(parameters.pop('file'), 'rb'))
    return parameters


def clicks_parameters_transformer(_, parameters):
    if 'links' in parameters:
        parameters['links[]'] = parameters.pop('links')
    return parameters


class ShortUrl(Api):

    get_clicks = bind_api_endpoint(
        method='GET',
        path='short_url/clicks',
        mapping=(ShortUrlClick, ModelCollection),
        exception_class=EndpointException,
        accept_parameters=clicks_accept_parameters,
        parameters_transformer=clicks_parameters_transformer
    )

    get_clicks_by_mobile_device = bind_api_endpoint(
        method='GET',
        path='short_url/clicks_by_mobile_device',
        mapping=(ShortUrlClickByMobileDevice, ModelCollection),
        exception_class=EndpointException,
        accept_parameters=clicks_accept_parameters,
        parameters_transformer=clicks_parameters_transformer
    )

    list_short_urls = bind_api_endpoint(
        method='GET',
        path='short_url/links',
        mapping=(ShortUrlModel, ModelCollection),
        exception_class=EndpointException
    )

    create_short_url = bind_api_endpoint(
        method='POST',
        path='short_url/links',
        mapping=ShortUrlModel,
        exception_class=EndpointException,
        accept_parameters=short_url_parameters,
        parameters_transformer=parameters_transformer
    )

    get_short_url = bind_api_endpoint(
        method='GET',
        path='short_url/links/{id}',
        mapping=ShortUrlModel,
        exception_class=EndpointException,
        accept_parameters=['id']
    )

    update_short_url = bind_api_endpoint(
        method='PUT',
        path='short_url/links/{id}',
        mapping=ShortUrlModel,
        exception_class=EndpointException,
        accept_parameters=['id']
    )

    remove_short_url = bind_api_endpoint(
        method='DELETE',
        path='short_url/links/{id}',
        exception_class=EndpointException,
        accept_parameters=['id']
    )
