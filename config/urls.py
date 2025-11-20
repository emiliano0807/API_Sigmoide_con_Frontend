# config/urls.py
from django.contrib import admin
from django.urls import path
from core.views import index_view, SigmoideDesplazadaView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ruta para ver la web
    path('', index_view, name='home'),
    
    # Ruta para la API (JSON)
    path('api/sigmoide/', SigmoideDesplazadaView.as_view(), name='sigmoide-api'),
]