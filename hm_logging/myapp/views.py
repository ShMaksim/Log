import logging
from django.http import HttpResponse

logger = logging.getLogger('django')

def test_logging(request):
    logger.debug("Это DEBUG сообщение")
    logger.info("Это INFO сообщение")
    logger.warning("Это WARNING сообщение")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.error("Это ERROR сообщение с ошибкой", exc_info=True)
    logger.critical("Это CRITICAL сообщение")
    return HttpResponse("Логи отправлены, проверьте файлы логов и консоль")