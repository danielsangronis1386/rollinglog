from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('papers/', views.RollingPaperList.as_view(), name='paper-index'),
    path('papers/<int:pk>/', views.RollingPaperDetail.as_view(), name='paper-detail'),
    path('papers/create/', views.RollingPaperCreate.as_view(), name='paper-create'),
    path('papers/<int:pk>/update/', views.RollingPaperUpdate.as_view(), name='paper-update'),
    path('papers/<int:pk>/delete/', views.RollingPaperDelete.as_view(), name='paper-delete'),
    path('brands/', views.BrandList.as_view(), name='brand-index'),
    path('brands/<int:pk>/', views.BrandDetail.as_view(), name='brand-detail'),
    path('brands/', views.BrandCreate.as_view(), name='brand-create'),
    path('brands/<int:pk>/update', views.BrandUpdate.as_view(), name='brand-update'),
    path('brands/<int:pk>/delete', views.BrandDelete.as_view(), name='brand-delete'),
    path('papers/<int:paper_id>/add_review/', views.add_review, name='add-review'),
]