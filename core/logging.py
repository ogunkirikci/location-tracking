import logging
from datetime import datetime

from elasticsearch_dsl import Date, Document, Keyword, Text, connections


class LogEntry(Document):
    timestamp = Date()
    level = Keyword()
    logger = Keyword()
    message = Text()

    class Index:
        name = "logs"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}


class ElasticsearchLogHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.es = connections.get_connection()
        LogEntry.init()

    def emit(self, record):
        try:
            log_entry = LogEntry(
                timestamp=datetime.utcnow(), level=record.levelname, logger=record.name, message=self.format(record)
            )
            log_entry.save()
        except Exception:
            self.handleError(record)
