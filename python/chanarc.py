#!/usr/bin/env python
# -*- coding: utf-8 -*-
# chan.arc draft implementation

# NOTE: at this point, this is purely prototyping and brainstorming
# do not use this right now

from __future__ import print_function
from __future__ import absolute_import

import os

VERSION = 'draft-01'


class ChanArc(object):
    """Creates an imageboard archive file."""
    def __init__(self, base_path, manifest):
        self.base_path = base_path
        self.manifest = manifest
        self.version = VERSION


class ChanArcManifest(object):
    """Creates a chan.arc manifest."""
    def __init__(self):
        self.version = VERSION

    def write(self, filename):
        """Write manifest to given filename."""
        pass
