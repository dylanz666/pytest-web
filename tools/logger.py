import os
from loguru import logger
from time import strftime

log_path = os.path.join(os.getcwd(), 'logs')


class Logger:
    __instance = None
    __initialized_flag = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__initialized_flag:
            return
        date_str = strftime('%Y-%m-%d')
        logger.remove()
        log_format = "[{time:YYYY-MM-DD HH:mm:ss.SSS}] [{level}] {message}"
        log_filename = os.path.join(log_path, f"{date_str}.log")
        # save log message to log file
        logger.add(log_filename, format=log_format, level="DEBUG", rotation="1 day", encoding="utf-8")
        # output log to console
        logger.add(lambda msg: print(msg, end=''), format=log_format, level="DEBUG")
        self.__initialized_flag = True

    @classmethod
    def format_and_log_messages(cls, level, *messages):
        formatted_message = ' '.join(str(message_item) for message_item in messages)
        logger.log(level, formatted_message)

    @classmethod
    def info(cls, *messages) -> None:
        cls.format_and_log_messages("INFO", *messages)

    @classmethod
    def warning(cls, *messages) -> None:
        cls.format_and_log_messages("WARNING", *messages)

    @classmethod
    def critical(cls, *messages) -> None:
        cls.format_and_log_messages("CRITICAL", *messages)

    @classmethod
    def error(cls, *messages) -> None:
        cls.format_and_log_messages("ERROR", *messages)

    @classmethod
    def debug(cls, *messages) -> None:
        cls.format_and_log_messages("DEBUG", *messages)


if __name__ == "__main__":
    logger_1 = Logger()

    # test: log different kind of logs
    logger_1.info('this is an info log')
    logger_1.debug('this is a debug log')
    logger_1.error('this is an error log')
    logger_1.critical('this is a critical log')
    logger_1.warning('this is a warn log')
    # test: log multiple messages
    logger_1.info("Multiple", "info", "messages", 123)

    # test: singleton mode
    logger_2 = Logger()
    logger_2.info("this is from logger_2")
    assert id(logger_1) == id(logger_2), "Singleton mode is not ok!"
