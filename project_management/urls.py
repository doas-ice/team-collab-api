from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    RegisterUserView,
    LoginUserView,
    UserDetailView,
    ListProjectsView,
    ProjectDetailsView,
    ListProjectMembersView,
    ListTasksView,
    TaskDetailView,
    ListCommentsView,
    CommentDetailsView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/register/', RegisterUserView.as_view(), name='register_user'),
    path('users/login/', LoginUserView.as_view(), name='login_user'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('projects/', ListProjectsView.as_view(), name='list_projects'),
    path('projects/<int:pk>/', ProjectDetailsView.as_view(), name='project_detail'),
    path('projects/<int:pk>/members/', ListProjectMembersView.as_view(), name='list_project_members'),
    path('projects/<int:project_id>/tasks/', ListTasksView.as_view(), name='list_tasks'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/<int:task_id>/comments/', ListCommentsView.as_view(), name='list_comments'),
    path('comments/<int:pk>/', CommentDetailsView.as_view(), name='comment_detail'),
]
