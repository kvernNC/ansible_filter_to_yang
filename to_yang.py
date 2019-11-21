#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# dependency : pip3 install ntc-rosetta

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from functools import partial
import types
from ansible.module_utils import six

from ntc_rosetta import get_driver

from ansible import errors

import json

def to_yang(file_path, driver="ios"):

    ios = get_driver(driver, "openconfig")
    ios_driver = ios()
    with open(file_path, "r") as f:
        config = f.read()

    parsed = ios_driver.parse(native={"dev_conf": config})
    return (json.dumps(parsed.raw_value(), indent=4))

class FilterModule(object):
    ''' A filter chek if an ip is part of a subnet '''
    def filters(self):
        return {
            'to_yang': to_yang
        }
