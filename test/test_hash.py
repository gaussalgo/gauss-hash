# -*- coding: utf-8 -*-

from gauss_hash import GuassHashSha256
from gauss_hash import GaussTextProcessor


def test_null():
    pass

def test_basic():
    h = GuassHashSha256()
    assert h is not None

def test_simple_string():
    h = GuassHashSha256('my_best_salt')
    assert h.get_hash('123456') == 'c910f6df33395b2b4ac54f99d79cdf0561524013e86b9efaa4d7c421e4b336fa'

def test_simple_number():
    h = GuassHashSha256('my_best_salt')
    assert h.get_hash(123456) == 'c910f6df33395b2b4ac54f99d79cdf0561524013e86b9efaa4d7c421e4b336fa'

def test_simple_string_unicode():
    h = GuassHashSha256()
    assert h.get_hash(u'ježe Ček') == '183cb95160ade393e47418f39b4191ce585a2511bd6a323623c44b0644305b7e'

def test_simple_string_str():
    h = GuassHashSha256()
    assert h.get_hash('  ježeČek') == '183cb95160ade393e47418f39b4191ce585a2511bd6a323623c44b0644305b7e'

def test_coor():
    h = GuassHashSha256()
    assert h.get_hash('41°24\'12.2"N 2°10\'26.5"E') == '23922c2870b76d210a1405d4e0df62dd7787e1b13ce6310df4d1ff63c9fbf1f8'

def test_float():
    h = GuassHashSha256()
    assert h.get_hash(1.0) == 'd0ff5974b6aa52cf562bea5921840c032a860a91a3512f7fe8f768f6bbe005f6'

def test_dummy():
    h = GuassHashSha256(salt='my_best_salt', processor=GaussTextProcessor.dummy)
    assert h.get_hash('Krystof Harant z Polzic a Bezdruzic') == '70196dd57853b2c397e3d35ac4943c4b09002a0b9b835b5f43ceadbfdb30b51e'

def test_none():
    h = GuassHashSha256(processor=None)
    assert h.get_hash('ježeČek') == '183cb95160ade393e47418f39b4191ce585a2511bd6a323623c44b0644305b7e'


# vim: set cin et ts=4 sw=4 ft=python :

