from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
# from .views import

urlpatterns = [
    path('', views.todo, name="TodoList"),
    path('category/', views.category, name="category"),


]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)












