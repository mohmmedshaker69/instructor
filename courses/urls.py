from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('chapter_detail/<int:chapter_id>/', views.chapter_detail, name='chapter_detail'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('create_course/', views.create_course, name='create_course'),
    path('create_chapter/<int:course_id>/', views.create_chapter, name='create_chapter'),
    path('create_lesson/<int:chapter_id>/', views.create_lesson, name='create_lesson'),
    path('instructor/<int:instructor_id>/', views.create_instructor, name='create_instructor'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('edit/<int:course_id>/', views.edit_course, name='edit_course'),
    # path('lesson/<int:lesson_id>/video/', views.lesson_video, name='lesson_video'),
    path('add_chapter/<int:course_id>/', views.add_chapters, name='add_chapters'),
    path('add_lessons/<int:chapter_id>/', views.add_lessons, name='add_lessons'),
    path('delete_chapter/<int:chapter_id>/', views.delete_chapter, name='delete_chapter'),




]