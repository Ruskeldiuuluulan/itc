
# from course.views import BranchDetailView

from django.urls import path, include
from course import views

urlpatterns = [
    path('', views.my_main_page, name='my_main_page'),
    path('branches/', views.BranchListView.as_view(), name='branches_list'),
    path('branches/create/', views.BranchCreateView.as_view(), name='branch_create'),
    path('branches/<int:branch_id>/', views.BranchDetailView.as_view(), name='branch_detail'),
    path('branches/<int:branch_id>/edit/', views.BranchUpdateView.as_view(), name='branch_edit'),

    path('groups/', views.group_list, name='group_list'),
    path('groups/<int:group_id>/', views.group_detail, name='group_detail'),
    path('groups/create/', views.BranchCreateView.as_view(), name='group_create'),

    path('students/create/', views.student_create, name='student_create'),
    path('students/', views.student_list, name='student_list'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('students/<int:student_id>/delete', views.student_delete, name='student_delete'),
    # path('student/random/', views.as_view(), name='student_random'),

    path('api/', include('course.api.urls'))
]