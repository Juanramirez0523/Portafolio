from django.urls import path
from .views import render_posts, post_detail


app_name = 'blog'

urlpatterns = [
    path('', render_posts, name='posts'),  # Esto manejará /blog/
    path('<int:post_id>/', post_detail, name='post_detail'),  # Esto manejará /blog/<post_id>/
]
