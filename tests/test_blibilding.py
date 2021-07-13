import pytest

from miu.colorbilding import ColorBilding

def testBliBilding():
    cb = ColorBilding(color=42)
    assert not cb.isBli()
    blib = ColorBilding()
    assert blib.isBli()
