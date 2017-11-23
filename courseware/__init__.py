#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask


# ------------------------------------------------------------------------------
# SETUP GENERAL APPLICATION
# ------------------------------------------------------------------------------

__version__ = '1.0'
app = Flask('ITIL-ServiceCatalog')
app.config.from_object('config')
app.debug = True

# ------------------------------------------------------------------------------
# SETUP JWT AUTHENTICATION
# ------------------------------------------------------------------------------

# Import all courseware controller files
from courseware.controllers import *

