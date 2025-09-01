from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews_home, name='reviews_home'),
    path('create_review/', views.create_review, name='create_review'),
    path('<int:pk>/', views.ReviewDetailView.as_view(), name='review_detail'),
    path('<int:pk>/update/', views.ReviewUpdateView.as_view(), name='review_update'),
    path('<int:pk>/delete/', views.ReviewDeleteView.as_view(), name='review_delete'),
]
