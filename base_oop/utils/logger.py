from loguru import logger

logger.add(
    'logs/app.log',
    level='DEBUG',
    format="{time} | {level} | {message}",
    encoding='utf-8'
)
