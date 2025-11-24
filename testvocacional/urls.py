from django.urls import path
from .views import TestVocacionalView

urlpatterns = [
    path("generar/", TestVocacionalView.as_view(), name="generar_testvocacional"),
]
