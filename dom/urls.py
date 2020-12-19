from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import CategoriView, DomDokumentView, AdresView, ArtikulView

urlpatterns = [
    # path('', views.index, name='index'),
    # path('news/', views.news, name='news'),
    # path('base/', views.base, name='base'),
    # path('search/', views.SearchResultsView.as_view(template_name='dom/list_nedvijimost.html'),
    #      name='search'),
    path('add_categori/', CategoriView.as_view(template_name='dom/forms/categori_form.html'),
         name='new_categori'),
    path('add_document/', DomDokumentView.as_view(template_name='dom/forms/document_form.html'),
         name='new_document'),
    path('adres/', AdresView.as_view(template_name='dom/forms/adres_form.html'), name='adres'),
    path('artikul/', ArtikulView.as_view(template_name='dom/forms/articul_form.html'), name='artikul'),
    #      name='dokument'),
    # path('nedvijimost/', views.nedvijimostlist, name='nedvijimost'),
    # path('nedvijimost/<int:pk>/', HouseLokationDetailView.as_view(), name='detail'),
    # # path('nedvijimost/<int:pk>/', FotoDomDetailView.as_view(), name='foto' ),
    # path('nedvijimost/<slug:slug>/', HouseLokationDetailView.as_view(), name='sluga'),
    # path('nedvijimost/info/<slug:slug>/', MenegerDetailView.as_view(), name='meneger'),
    # path('poisk/', views.poisk, name='poisk'),
    # path('bigpoisk/', Bigpoisk.as_view(), name='bigpoisk'),
    # path('shablon/', views.shablon, name='shablon'),
    # # path('search/', )
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)