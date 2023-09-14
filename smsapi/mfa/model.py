from smsapi.models import ResultCollection


class SmsMFASendResult(ResultCollection):

    def __init__(self, count, results, code, phone_number, from_):
        super(SmsMFASendResult, self).__init__(count, results)

        self.code = code
        self.phone_number = phone_number
        self.from_ = from_

    @classmethod
    def parse(cls, json_response, model):
        code = json_response.get('code')
        phone_number = json_response.get('phone_number')
        from_ = json_response.get('from')

        sms_list = [json_response]

        collection = []

        for sms in sms_list:
            m = model.from_dict(sms)
            collection.append(m)

        return cls(1, collection, code=code, phone_number=phone_number, from_=from_)


class SmsMFAVerifyResult(ResultCollection):

    def __init__(self, count, results):
        super(SmsMFAVerifyResult, self).__init__(count, results)

    @classmethod
    def parse(cls, json_response, model):
        return cls(0, [])
