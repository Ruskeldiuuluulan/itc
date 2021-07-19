from django.urls import path
from course.api import views


urlpatterns = [
    path('v1/branches/',  views.BranchListView.as_view(), name='branches'),
    path('v1/branches/<int:pk>/', views.BranchDetailAPIView.as_view(), name='branch_detail')
]

