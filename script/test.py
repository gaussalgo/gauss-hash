#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gauss_hash import GuassHashSha256
from gauss_hash import GaussTextProcessor


gh = GuassHashSha256(salt='salt', processor=GaussTextProcessor.norm)
value = ' Ježečlů'
print(gh.get_hash(value))

