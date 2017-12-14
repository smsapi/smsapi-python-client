# -*- coding: utf-8 -*-

from smsapi.models import Model


class AccountBalanceResult(Model):

    def __init__(self, points = None, pro_count = None, eco_count = None,
                 mms_count = None, vms_gsm_count = None, vms_land_count = None):

        super(AccountBalanceResult, self).__init__()

        self.points = points
        self.pro_count = pro_count
        self.eco_count = eco_count
        self.mms_count = mms_count
        self.vms_gsm_count = vms_gsm_count
        self.vms_land_count = vms_land_count

    @classmethod
    def from_dict(cls, data, **kwargs):
        return cls(
            points=data.get('points'),
            pro_count=data.get('proCount'),
            eco_count=data.get('ecoCount'),
            mms_count=data.get('mmsCount'),
            vms_gsm_count=data.get('vmsGsmCount'),
            vms_land_count=data.get('vmsLandCount')
        )


class UserResult(Model):

    def __init__(self, username=None, limit=None, month_limit=None,
                 senders=None, phonebook=None, active=None, info=None):

        super(UserResult, self).__init__()

        self.username = username
        self.limit = limit
        self.month_limit = month_limit
        self.senders = senders
        self.phonebook = phonebook
        self.active = active
        self.info = info
