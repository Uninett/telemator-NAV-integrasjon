from django.http import HttpResponse
from sqlalchemy import exc


class DatabaseMiddleware(object):

    def process_exception(self, request, exception):
        if isinstance(exception, exc.OperationalError):
            return HttpResponse("Oops! Seems like something went wrong on the database connection. Try checking"
                            " your settings configuration. <br><br><br> Full message:<br> " + exception.message)
        return None