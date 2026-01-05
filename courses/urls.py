from django.urls import path
from .views import theme_list, course_detail, lesson_detail, buy_course, buy_lesson, validate_lesson
from .views import my_certifications



urlpatterns = [
    path('', theme_list, name='theme_list'),
    path('course/<int:course_id>/', course_detail, name='course_detail'),
    path('lesson/<int:lesson_id>/', lesson_detail, name='lesson_detail'),
    path('course/<int:course_id>/buy/', buy_course, name='buy_course'),
    path('lesson/<int:lesson_id>/buy/', buy_lesson, name='buy_lesson'),
    path('lesson/<int:lesson_id>/validate/', validate_lesson, name='validate_lesson'),
    path('certifications/', my_certifications, name='my_certifications'),





]
