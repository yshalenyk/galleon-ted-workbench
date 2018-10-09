from gevent import monkey; monkey.patch_all()
import pytest
import os.path
import shutil
import simplejson as json
import gevent
from functools import partial
from wishbone.event import Event
from wishbone.actor import ActorConfig
from wishbone.utils.test import getter
from wishbone_jsonout import FileOut

here = os.path.dirname(os.path.abspath(__file__))
DATA = {
    "id": "1111",
    'data': 'data'
}


@pytest.fixture
def module(request):
    
    m = FileOut(
        ActorConfig("jsonout", 100, 1, {}, ""),
        path=os.path.join(here, 'results')
    )
    m.pool.queue.inbox.disableFallThrough()
    request.addfinalizer(partial(shutil.rmtree, os.path.join(
        here, 'results'
    )))
    return m

def test_fileread(module):
    module.start()
    module.pool.queue.inbox.put(Event(DATA))
    #gevent.sleep(10)
    #import pdb; pdb.set_trace()
    with open(os.path.join(here, 'results', '1111.json')) as df:
        data = json.load(df)
    assert data == DATA

    
