from django.conf import settings
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
 

urlpatterns = [
    path('' ,views.business, name='business'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)