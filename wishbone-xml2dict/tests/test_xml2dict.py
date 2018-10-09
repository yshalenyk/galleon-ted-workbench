import pytest
from wishbone.event import Event
from wishbone.actor import ActorConfig
from wishbone.utils.test import getter

from wishbone_xml2dict import Xml2DictModule


XML = """
<mydocument has="an attribute">
  <and>
    <many>elements</many>
    <many>more elements</many>
  </and>
  <plus a="complex">
    element as well
  </plus>
</mydocument>
"""


@pytest.fixture
def module():
    m = Xml2DictModule(ActorConfig("xml2dict", 100, 1, {}, ""))
    m.pool.queue.inbox.disableFallThrough()
    m.pool.queue.outbox.disableFallThrough()
    return m

def test_xml2dict(module):
    module.start()
    e = Event(XML)
    module.pool.queue.inbox.put(e)
    doc = getter(module.pool.queue.outbox).get()
    if not doc:
        assert False
    assert doc['mydocument']['@has'] == 'an attribute'
    assert doc['mydocument']['and']['many'] == ['elements', 'more elements']
    assert doc['mydocument']['plus']['@a'] == 'complex'
    assert doc['mydocument']['plus']['#text'] == 'element as well'

    
