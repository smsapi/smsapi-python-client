from smsapi.models import Model
from smsapi.utils import convert_iso8601_str_to_datetime


class BlacklistPhoneNumber(Model):

    def __init__(self, **kwargs):
        super(BlacklistPhoneNumber, self).__init__()

        self.id = kwargs.get('id')
        self.phone_number = kwargs.get('phone_number')
        self.expire_at = kwargs.get('expire_at')
        self.created_at = kwargs.get('created_at')

        if self.expire_at:
            self.expire_at = convert_iso8601_str_to_datetime(self.expire_at)

        if self.created_at:
            self.created_at = convert_iso8601_str_to_datetime(self.created_at)
