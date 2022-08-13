import uuid
from django.urls import path, re_path
from . import views
from uuid import uuid5

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('add-blog/', views.BlogView.as_view(), name='add'),
    path(f'delete-{uuid5(uuid.NAMESPACE_URL, "https://localhost:8000/delete/<int:pk>/")}/<int:pk>/', views.BlogDelete.as_view(), name='delete'),
    path(f'{uuid5(uuid.NAMESPACE_URL, "https://localhost:8000/sertifikatlar/")}/certificates/', views.CertifView.as_view(), name='sertifik'),
    re_path(r'^blog/(?P<pk>\d+)$', views.blog_detail, name='blog-detail'),
]