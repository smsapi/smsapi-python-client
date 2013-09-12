#!/usr/bin/env python

import os
import sys

from tests import run_tests

sys.path.insert(0, os.path.dirname(__file__))

run_tests()