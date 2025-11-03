from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('papers/', views.RollingPaperList.as_view(), name='paper-index'),
    path('papers/<int:pk>/', views.RollingPaperDetail.as_view(), name='paper-detail'),
    path('papers/create/', views.RollingPaperCreate.as_view(), name='paper-create'),
    path('papers/<int:pk>/update/', views.RollingPaperUpdate.as_view(), name='paper-update'),
    path('papers/<int:pk>/delete/', views.RollingPaperDelete.as_view(), name='paper-delete'),
    path('brands/<int:pk>/', views.BrandDetail.as_view(), name='brand-detail'),
]