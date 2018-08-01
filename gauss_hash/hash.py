# -*- coding: utf-8 -*-

import logging
import re
import unidecode
import hashlib
import six


logger  = logging.getLogger(__name__)


class GaussTextProcessor:

    @staticmethod
    def make_unicode(s):
        if isinstance(s, six.text_type):
            return s
        if isinstance(s, six.binary_type):
            return s.decode('UTF-8')
        return six.text_type(s)

    @staticmethod
    def norm(s):
        u_s = GaussTextProcessor.make_unicode(s)
        return re.sub(r'\s+', '', unidecode.unidecode(u_s)).lower()

    @staticmethod
    def dummy(s):
        return s


class GuassHashSha256(object):

    def __init__(self, salt='', processor=GaussTextProcessor.norm):
        self.salt = salt
        if processor is None:
            processor = GaussTextProcessor.norm
        self.processor = processor
        logger.debug('%s: salt="%s", processor="%s"', self.__class__, self.salt, self.processor)

    def get_hash(self, value):
        preprocessed = self.processor(value)
        return hashlib.sha256(str(preprocessed+self.salt).encode('ascii')).hexdigest()


# vim: set cin et ts=4 sw=4 ft=python :

