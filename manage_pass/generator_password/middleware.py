from django.http import HttpResponseNotFound, JsonResponse
from django.urls import resolve


class Redirect404ToPostMiddleware:
    """
    Middleware для перехвата ошибки 404 и повторного отправления запроса как POST
    в случае несуществующего сервиса.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if isinstance(response, HttpResponseNotFound):
            url_resolved = resolve(request.path_info)

            if url_resolved.url_name == 'password-detail' and request.method == 'GET':
                request.method = 'POST'
                request.POST = {"password": "generated_default_password"}

                return self.get_response(request)

        return response
