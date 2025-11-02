from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('papers/', views.paper_index, name='paper-index'),
    path('papers/<int:paper_id>/', views.paper_detail, name='paper-detail'),
    path('papers/create/', views.RollingPaperCreate.as_view(), name='paper-create'),
    path('papers/<int:pk>/update/', views.RollingPaperUpdate.as_view(), name='paper-update'),
    path('papers/<int:pk>/delete/', views.RollingPaperDelete.as_view(), name='paper-delete'),
]