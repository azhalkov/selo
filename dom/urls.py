# dom/urls
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import CategoriView, DomDokumentView, AdresView, ArtikulView, AdresDetailView, SearchResultsView

urlpatterns = [
    path('', views.index, name='index'),
    path('add_categori/', CategoriView.as_view(template_name='dom/forms/categori_form.html'),
         name='new_categori'),
    path('add_document/', DomDokumentView.as_view(template_name='dom/forms/document_form.html'),
         name='new_document'),
    path('adres/', AdresView.as_view(template_name='dom/forms/adres_form.html'), name='adres'),
    path('artikul/', ArtikulView.as_view(template_name='dom/forms/articul_form.html'), name='artikul'),
    path('adresa/', views.AdresListView.as_view(), name='adresa'),
    # path('nedvijimost/<int:pk>/', HouseLokationDetailView.as_view(), name='detail'),
    # # path('nedvijimost/<int:pk>/', FotoDomDetailView.as_view(), name='foto' ),
    path('adresa/<slug:slug>/', AdresDetailView.as_view(), name='adresa_detail'),
    # path('poisk/', PoiskArtikula.as_view(), name='poisk'),
    path('search/', SearchResultsView.as_view(), name='search'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)