from django.http import HttpResponse
from sqlalchemy import exc
import logging

# writes to spam.log in NAV directory
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

logger.info("new instance")
logger.info("run from database middleware")



class MyExceptionMiddleware(object):
    logger.info("run from CLASS")

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        logger.info("run from FUNCTON")

        if not isinstance(exception, ValueError):
            return HttpResponse('some message')
        return HttpResponse('some message')