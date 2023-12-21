from django.db import connection


class CloseConnectionMiddleware:
    """
    Create middleware class for closing database connections
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.close_database_connection()
        return response

    def close_database_connection(self):
        if connection and connection.connection:
            connection.close()
