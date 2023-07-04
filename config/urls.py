from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/v1/', include('api.urls')),
    path('users/',include('auth.urls')),
    path('tasks/',include('todo.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('', include('main.urls'))  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
