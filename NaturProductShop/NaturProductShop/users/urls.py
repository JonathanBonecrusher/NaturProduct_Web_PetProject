from django.urls import path, include
from . import views
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
    path('history/<user>', views.HistoryView, name='history'),
    path('request/<user>', views.UserRequestView, name='request'),
    path('your_requests/<user>', views.YourRequestsView, name='your_request'),
    path('users_requests', views.UsersRequestsView, name='users_requests'),
    path('answer_to_request/<req>', views.AnswerToRequestView, name='answer_to'),
]
