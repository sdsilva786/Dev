import logging
from logging.handlers import TimedRotatingFileHandler
from SourceCode.Utilities.ConfigHelper import ReadAppConfigHelper as ConHP


class LogException:
    _logger = logging.getLogger("Rotating Log")
    _logger.setLevel(logging.ERROR)

    def __init__(self):
        format_string = "%(asctime)s-%(levelname)s-%(filename)s-%(lineno)d-%(message)s"
        log_format = logging.Formatter(format_string)
        path = ConHP.get_config("error_logger_path")
        handler = TimedRotatingFileHandler(path,
                                           when="midnight",
                                           interval=1,
                                           backupCount=10)
        handler.setFormatter(log_format)
        self._logger.addHandler(handler)

    def Log(self, e):
        self._logger.exception(e)
