from smsapi.models import ResultCollection


class SmsSendResult(ResultCollection):

    def __init__(self, count, results, message=None, length=None, parts=None):
        super(SmsSendResult, self).__init__(count, results)

        self.message = message
        self.parts = parts
        self.length = length

    @classmethod
    def parse(cls, json_response, model):
        count = json_response.get('count')
        message = json_response.get('message')
        length = json_response.get('length')
        parts = json_response.get('parts')

        sms_list = json_response.get('list', [])

        collection = []

        for sms in sms_list:
            m = model.from_dict(sms)
            collection.append(m)

        return cls(count, collection, message=message, length=length, parts=parts)
