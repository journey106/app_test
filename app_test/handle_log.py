import logging, os
from handle_conf import do_config
import config


class LoggingHandle:

    def __init__(self):
        # 1. 创建日志收集器
        self.logger_case = logging.getLogger(do_config.get_value('log', 'log_name'))
        # 2. 设置日志收集器等级
        self.logger_case.setLevel(do_config.get_value('log', 'logger_level'))

        # 3.设置日志输出渠道
        console_logger = logging.StreamHandler()
        file_logger = logging.FileHandler(os.path.join(config.LOG_DIR, do_config.get_value('log', 'log_filename')), encoding='utf-8')

        # 4.设置日志输出渠道等级
        console_logger.setLevel(do_config.get_value('log', 'console_level'))
        file_logger.setLevel(do_config.get_value('log', 'file_level'))

        # 5.设置输出日志格式
        simple_format = logging.Formatter(do_config.get_value('log', 'simple_formatter'))
        verbose_format = logging.Formatter(do_config.get_value('log', 'verbose_formatter'))
        console_logger.setFormatter(simple_format)
        file_logger.setFormatter(verbose_format)

        # 6.连接日志收集器和输出渠道
        self.logger_case.addHandler(console_logger)
        self.logger_case.addHandler(file_logger)

    def get_logger(self):
        return self.logger_case


do_logger = LoggingHandle().get_logger()

if __name__ == '__main__':
    one_logger = LoggingHandle().get_logger()
    one_logger.info("这是一个info级别的日志信息")
    one_logger.debug("这是一个debug级别的日志信息")
    one_logger.warning("这是一个warning级别的日志信息")
    one_logger.error("这是一个error级别的日志信息")
    one_logger.critical("这是一个警告级别的日志信息")

