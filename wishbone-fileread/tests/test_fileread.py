import pytest
import os.path
from wishbone.event import Event
from wishbone.actor import ActorConfig
from wishbone.utils.test import getter

from wishbone_fileread import FileRead

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, 'data.xml')) as fd:
    XML = fd.read()

@pytest.fixture
def module():
    m = FileRead(ActorConfig("fileread", 100, 1, {}, ""))
    m.pool.queue.inbox.disableFallThrough()
    m.pool.queue.outbox.disableFallThrough()
    return m

def test_fileread(module):
    module.start()
    path = os.path.join(here, 'data.xml')
    e = Event(path)
    module.pool.queue.inbox.put(e)
    doc = getter(module.pool.queue.outbox).get()
    if not doc:
        assert False
    assert doc == XML

    
