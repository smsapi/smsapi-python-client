# -*- coding: utf-8 -*-

import warnings
from functools import wraps


def obj_full_name(obj):
    return '.'.join((obj.__module__, obj.__name__))


def deprecated():
    """Decorator for deprecated functions."""

    def decorator_func(func):
        @wraps(func)
        def decorated_func(*args, **kwargs):
            warnings.simplefilter('always', DeprecationWarning)
            warnings.warn("Function is deprecated %s" % obj_full_name(func),
                          category=DeprecationWarning)
            return func(*args, **kwargs)
        return decorated_func
    return decorator_func
