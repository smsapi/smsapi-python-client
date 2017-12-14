# -*- coding: utf-8 -*-

from smsapi.models import Model


class PushShipment(Model):

    def __init__(self, id=None,  app_id=None, status=None, date_created=None,
                 scheduled_date=None, payload=None, summary=None,
                 dispatch_details=None, fallback=None, app=None):

        super(PushShipment, self).__init__()

        self.id = id
        self.app_id = app_id
        self.status = status
        self.date_created = date_created
        self.scheduled_date = scheduled_date
        self.payload = payload
        self.summary = summary
        self.dispatch_details = dispatch_details
        self.fallback = fallback
        self.app = app

    @classmethod
    def from_dict(cls, data, **kwargs):
        data.update({
            'app': PushApp.from_dict(data.pop('app', {})),
            'summary': PushShipmentSummary.from_dict(data.pop('summary', {})),
            'payload': PushShipmentPayload.from_dict(data.pop('payload', {})),
            'fallback': PushShipmentFallback.from_dict(data.pop('fallback', {})),
            'dispatch_details': PushShipmentDispatchDetails.from_dict(data.pop('dispatch_details', {})),
        })

        return cls(**data)


class PushShipmentDispatchDetails(Model):

    def __init__(self, channels=None, device_ids=None, device_type=None):
        super(PushShipmentDispatchDetails, self).__init__()

        self.device_type = device_type or []
        self.device_ids = device_ids or []
        self.channels = channels or []


class PushShipmentPayload(Model):

    def __init__(self, alert=None, badge=None, sound=None, category=None,
                 content_available=None, title=None, uri=None):
        super(PushShipmentPayload, self).__init__()

        self.alert = alert
        self.badge = badge
        self.sound = sound
        self.category = category
        self.content_available = content_available
        self.title = title
        self.uri = uri


class PushApp(Model):

    def __init__(self, id=None, name=None, icon=None):
        super(PushApp, self).__init__()

        self.id = id
        self.name = name
        self.icon = icon


class PushShipmentSummary(Model):

    def __init__(self, points=None, recipients_count=None, error_code=None):
        super(PushShipmentSummary, self).__init__()

        self.points = points
        self.recipients_count = recipients_count
        self.error_code = error_code


class PushShipmentFallback(Model):

    def __init__(self, message=None, from_=None, delay=None, status=None):
        super(PushShipmentFallback, self).__init__()

        self.message = message
        self.from_ = from_
        self.delay = delay
        self.status = status

    @classmethod
    def from_dict(cls, data, **kwargs):
        data['from_'] = data.pop('from', None)

        return super(PushShipmentFallback, cls).from_dict(data, **kwargs)
