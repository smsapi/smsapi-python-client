# -*- coding: utf-8 -*-


class Model(object):

    @classmethod
    def from_dict(cls, data, **kwargs):
        args = {}

        for k,v in data.items():
            args[str(k)] = v

        return cls(**args)

    def __repr__(self):
        return "<%s %s>" % (self.__class__.__name__, self.__dict__)

    def __eq__(self, other):
        return other and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)


class ModelCollection(object):

    def __init__(self, size, collection):
        super(ModelCollection, self).__init__()

        self.size = size

        self.collection = collection

        self._current = None
        self._index = 0

    @classmethod
    def parse(cls, response, model):
        size = response.get('size')
        collection = response.get('collection', [])

        c = [model.from_dict(d) for d in collection]

        return cls(size, c)

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        try:
            self._current = self.collection[self._index]
            self._index += 1
        except IndexError:
            raise StopIteration

        return self._current

    def __repr__(self):
        return "<%s [%s]> %s" % (self.__class__.__name__, self.size, self.collection)

    def __eq__(self, other):
        return other and self.__dict__ == other.__dict__


class ResultCollection(object):

    def __init__(self, count, results):
        super(ResultCollection, self).__init__()

        self.count = count
        self.results = results

        self._current = None
        self._index = 0

    @classmethod
    def parse(cls, content, model):
        collection = []

        if isinstance(content, dict):
            count = content.get('count')
            content = content.get('list', [])
        else:
            count = len(content)

        for data in content:
            m = model.from_dict(data)
            collection.append(m)

        return cls(count, collection)

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        try:
            self._current = self.results[self._index]
            self._index += 1
        except IndexError:
            raise StopIteration

        return self._current

    def __repr__(self):
        return "<%s [%s]> %s" % (self.__class__.__name__, self.count, self.results)

    def __eq__(self, other):
        return other and self.__dict__ == other.__dict__


class SendResult(Model):

    def __init__(self, id=None, points=None, number=None,
                 date_sent=None, submitted_number=None,
                 status=None, idx=None, error=None):

        super(SendResult, self).__init__()

        self.id = id
        self.points = points
        self.number = number
        self.date_sent = date_sent
        self.submitted_number = submitted_number
        self.status = status
        self.idx = idx
        self.error = error


class RemoveMessageResult(Model):

    def __init__(self, id=None):
        super(RemoveMessageResult, self).__init__()

        self.id = id


class InvalidNumber(object):

    def __init__(self, number, submitted_number, reason):
        super(InvalidNumber, self).__init__()

        self.number = number
        self.submitted_number = submitted_number
        self.reason = reason

    @classmethod
    def from_dict(cls, data):
        return cls(data.get('number'), data.get('submitted_number'), data.get('message'))

    def __eq__(self, other):
        return other and self.__dict__ == other.__dict__


class HeaderDirectResult(object):

    def __init__(self, header):
        super(HeaderDirectResult, self).__init__()

        self.header = header

    def from_dict(self, _, **kwargs):
        r = kwargs.get('raw_response')
        return r.headers.get(self.header)