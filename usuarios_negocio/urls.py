# negocio_usuario/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, listar_usuarios,login, agregar_usuario, editar_usuario,eliminar_usuario, home, panel_usuario, logout
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/usuarios/list_usuarios/', UsuarioViewSet.as_view({'get': 'list_usuarios'}), name='list-usuarios',), # URL para listar usuarios DRF
    path('api/usuarios/create_usuario/', UsuarioViewSet.as_view({'post': 'create_usuario'}), name='create-usuario'), # URL para crear usuarios DRF
    path('api/usuarios/update/<int:pk>/', UsuarioViewSet.as_view({'put': 'update_usuario'}), name='update-usuario'), # URL para editar usuarios DRF
    path('api/usuarios/delete/<int:pk>/', UsuarioViewSet.as_view({'delete': 'delete_usuario'}), name='delete-usuario'), # URL para eliminar usuarios DRF
    path('usuarios/', listar_usuarios, name='listar-usuarios'),  # URL para listar usuarios 
    path('usuarios/agregar-usuario/', agregar_usuario, name='agregar-usuario'),  # URL para agregar usuarios
    path('usuarios/editar-usuario/<int:pk>/', editar_usuario, name='editar-usuario'), # URL para editar usuarios
    path('usuarios/eliminar-usuario/<int:pk>/', eliminar_usuario, name='eliminar-usuario'), # URL para eliminar usuarios
    path('usuarios/panel',panel_usuario, name='panel_usuario'),
    path('usuarios/login/', login, name='login'),
    path('usuarios/logout/',logout, name='logout'),
    
]
