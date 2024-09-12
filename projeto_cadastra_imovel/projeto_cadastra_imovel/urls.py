from django.urls import path
from app_imobiliaria import views
from app_imobiliaria.views import cadastro_visitas, lista_visitas, filtrar_imoveis,lista_imoveis
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('imoveis/',views.imoveis,name='listagem_imoveis'),
    path('cadatro_visitas/',views.cadastro_visitas,name='cadastro_visitas'),
    path('filtrar_imoveis/', views.filtrar_imoveis, name='filtrar_imoveis'),
    path('lista_visitas/', lista_visitas, name='lista_visitas'),
    path('lista_imoveis/', lista_imoveis, name='lista_imoveis'),
    path('imovel/<int:id_imovel>/', views.imovel_detalhes, name='imovel_detalhes'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
