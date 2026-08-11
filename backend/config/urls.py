from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from django.views.generic import RedirectView


def api_docs(request):
    return JsonResponse({
        'message': 'API documentation',
        'endpoints': {
            'register': '/api/auth/register/',
            'login': '/api/auth/login/',
            'refresh': '/api/auth/refresh/',
            'verify': '/api/auth/verify/',
            'current_user': '/api/auth/me/',
            'users': '/api/users/',
        },
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', api_docs, name='api-docs'),
    path('api/', include('users.urls')),
    path('', RedirectView.as_view(url='/api/users/', permanent=False)),
]
