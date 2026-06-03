import logging
from logging.handlers import TimedRotatingFileHandler

# 设置日志器名称为api-test，并配置日志的输出级别≥DEBUG
logger = logging.getLogger("api-test")
logger.setLevel(logging.DEBUG)

# 设置“控制台输出”，同时也设置日志输出级别≥DEBUG
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

info_handler = TimedRotatingFileHandler("logs/info.log", when="midnight", backupCount=7)
info_handler.setLevel(logging.INFO)
info_handler.addFilter(lambda r:r.levelno < logging.WARNING)

error_handler = TimedRotatingFileHandler("logs/error.log", when="midnight",backupCount=7)
error_handler.setLevel(logging.WARNING)

fmt = logging.Formatter("%(asctime)s %(name)s [%(levelname)s] %(message)s")
stream_handler.setFormatter(fmt)
info_handler.setFormatter(fmt)
error_handler.setFormatter(fmt)

# 将日志器注册到Logger
logger.addHandler(stream_handler)
logger.addHandler(info_handler)
logger.addHandler(error_handler)
