# -*- coding: utf-8 -*-

import os
import json

from smsapi.models import ModelCollection


def create_collection_from_fixture(fixture, model):
    list_contacts = open(os.path.join(os.path.dirname(__file__), 'fixtures/%s.json' % fixture))

    r = json.load(list_contacts).get('response')

    c = ModelCollection(r['size'], list(map(lambda x: model(**x), r['collection'])))

    return c
