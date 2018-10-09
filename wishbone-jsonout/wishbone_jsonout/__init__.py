import gevent
import uuid
import sys
import os
import os.path
import simplejson as json
from wishbone.module import OutputModule


class FileOut(OutputModule):

    def __init__(self, actor_config, path, selection="data", payload=None, native_events=False, parallel_streams=1, **kw):
        """
        wishbone output module to consume data as string and dump it into json 
        it differs from built in module by writing different events to different files
        """
        OutputModule.__init__(self, actor_config)
        self.pool.createQueue("inbox")
        self.registerConsumer(self.consume, "inbox")
        gevent.sleep(0)
        if not os.path.exists(self.kwargs.path):
            try:
                os.makedirs(self.kwargs.path)
            except (OSError, IOError) as e:
                self.logging.error("Unable to create destination directory. Error {}".format(
                    e
                ))
                sys.exit(1)

    def consume(self, event):
        data = event.get(self.kwargs.selection)
        if not path:
            self.logging.warn("Empty data... skipping...")
            return
        try:
            if isinstance(data, dict):
                id = data.get('id', uuid.uuid4().hex)
            else:
                id = uuid.uuid4().hex
            import pdb; pdb.set_trace()
            filename = "{}.json".format(os.path.join(self.kwargs.path, id))
            with open(filename, 'w') as fd:
                simplejson.dump(data, fd)
        except Exception as e:
            self.logging.error("failed to reaf file in {}".format(path))
            return
