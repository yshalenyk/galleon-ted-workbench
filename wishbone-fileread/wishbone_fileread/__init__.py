from wishbone.module import ProcessModule


class FileRead(ProcessModule):

    def __init__(self, actor_config, selection="data", destination="data"):
        """
        Process module to read file content from path givent in event
        Python dicts
        """
        ProcessModule.__init__(self, actor_config)
        for name in ['inbox', 'outbox']:
            self.pool.createQueue(name)
        self.registerConsumer(self.consume, "inbox")

    def consume(self, event):
        path = event.get(self.kwargs.selection)
        if not path:
            self.logging.warn("Empty path... skipping...")
            return
        try:
            with open(path) as fd:
                data = fd.read()
                event.set(data, self.kwargs.destination)
                self.submit(event, "outbox")
        except Exception as e:
            self.logging.error("failed to reaf file in {}".format(path))
            return
