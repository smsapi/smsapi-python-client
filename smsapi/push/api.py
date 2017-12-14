# -*- coding: utf-8 -*-

from collections import defaultdict

from smsapi.api import Api
from smsapi.endpoint import bind_api_endpoint
from smsapi.exception import EndpointException
from smsapi.push.models import PushShipment

accept_parameters = [
    'app_id',
    'channels',
    'device_ids',
    'device_type',
    'scheduled_date',
    'alert',
    'badge',
    'sound',
    'category',
    'content-available',
    'title',
    'uri',
    'fallback_message',
    'fallback_delay',
    'fallback_from',
]


def parameters_transformer(_, parameters):

    def dict_nest_keys(d, nest_key, keys_to_nest):
        dc = defaultdict(lambda: {})
        for k, v in d.items():
            if k in keys_to_nest:
                dc[nest_key][k] = v
            else:
                dc[k] = v
        return dc

    data_keys = ['alert', 'badge', 'sound', 'category', 'content-available', 'title', 'uri']

    parameters = dict_nest_keys(parameters, 'data', data_keys)

    compiled_parameters = defaultdict(lambda: {})

    for k, v in parameters.items():
        sk = 'fallback_'
        if k.startswith(sk):
            compiled_parameters['fallback'][k[len(sk):]] = v
        else:
            compiled_parameters[k] = v

    return compiled_parameters


class Push(Api):

    send = bind_api_endpoint(
        method='POST',
        path='push',
        mapping=PushShipment,
        exception_class=EndpointException,
        accept_parameters=accept_parameters,
        parameters_transformer=parameters_transformer
    )
