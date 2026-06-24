from django.urls import path
from feedback_app import views

app_name = 'feedback'
urlpatterns = [
    path("", views.FeedbackView.as_view(), name="feedback_page"),
    path('success/', views.FeedbackSuccessView.as_view(), name='feedback_success')
]
