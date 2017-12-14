# -*- coding: utf-8 -*-

from smsapi.models import Model


class ShortUrlClickByMobileDevice(Model):

    def __init__(self, link_id=None, android=None, ios=None, wp=None, other=None, sum=None):
        super(ShortUrlClickByMobileDevice, self).__init__()

        self.link_id = link_id
        self.android = android
        self.ios = ios
        self.wp = wp
        self.other = other
        self.sum = sum

    @classmethod
    def from_dict(cls, data, **kwargs):
        data.update(data.pop('clicks', {}))
        return super(ShortUrlClickByMobileDevice, cls).from_dict(data, **kwargs)


class ShortUrlClick(Model):

    def __init__(self, idzdo_id=None, phone_number=None, date_hit=None, name=None,
                 short_url=None, os=None, browser=None, device=None, suffix=None, message=None):

        super(ShortUrlClick, self).__init__()

        self.idzdo_id = idzdo_id
        self.phone_number = phone_number
        self.date_hit = date_hit
        self.name = name
        self.short_url = short_url
        self.os = os
        self.browser = browser
        self.device = device
        self.suffix = suffix
        self.message = message

    @classmethod
    def from_dict(cls, data, **kwargs):
        data['idzdo_id'] = data.pop('idz_do_id', None)
        data['message'] = ShortUrlClickMessage.from_dict(data.pop('message', {}))
        return super(ShortUrlClick, cls).from_dict(data, **kwargs)


class ShortUrlClickMessage(Model):

    def __init__(self, id=None, idx=None, recipient=None):
        super(ShortUrlClickMessage, self).__init__()

        self.id = id
        self.idx = idx
        self.recipient = recipient


class ShortUrl(Model):

    def __init__(self, id=None, name=None, url=None, short_url=None, filename=None,
                 type=None, expire=None, hits=None, hits_unique=None, description=None):

        super(ShortUrl, self).__init__()

        self.id = id
        self.name = name
        self.url = url
        self.short_url = short_url
        self.filename = filename
        self.type = type
        self.expire = expire
        self.hits = hits
        self.hits_unique = hits_unique
        self.description = description
