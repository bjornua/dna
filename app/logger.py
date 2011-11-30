# -*- coding: utf-8 -*-
import logging
import sys
_logger = None
def get(name):
    global _logger

    if _logger is None:
        _logger = logging.getLogger()
        
        shdlr = logging.StreamHandler(sys.stderr)
        _logger.addHandler(shdlr)

    return _logger.getChild(name)
