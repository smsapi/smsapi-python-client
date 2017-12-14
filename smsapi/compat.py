# -*- coding: utf-8 -*-

import sys

py_version = sys.version[:3]

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse
