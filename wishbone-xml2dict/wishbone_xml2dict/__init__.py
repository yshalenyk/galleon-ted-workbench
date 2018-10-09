import xmltodict
from wishbone.module import ProcessModule


class Xml2DictModule(ProcessModule):

    def __init__(self, actor_config, selection="data", destination="data"):
        """
        Process module responsible for converting passed xml data into native
        Python dicts
        """
        ProcessModule.__init__(self, actor_config)
        for name in ['inbox', 'outbox']:
            self.pool.createQueue(name)
        self.registerConsumer(self.consume, "inbox")

    def consume(self, event):
        data = event.get(self.kwargs.selection)
        if not data:
            return
        try:
            parsed = xmltodict.parse(data)
        except Exception as e:
            self.logging.error("failed parse xml data {}".format(data))
            return
        event.set(parsed, self.kwargs.destination)
        self.submit(event, "outbox")
