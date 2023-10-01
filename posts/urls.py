from django.urls import path
from .views import posts_list, post_details

app_name = 'posts'

urlpatterns = [
    path('all-posts', posts_list, name='posts_list'),
    path('post-details/<int:id>', post_details, name='post_details'),
]
