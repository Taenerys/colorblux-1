from django.urls import path
from .views import CreatePostView, ResultView

urlpatterns = [
    path('', CreatePostView.as_view(), name='add_post'),
    path('/<pk>',ResultView.as_view(), name='result')
] 