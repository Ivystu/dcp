from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('select_animal_center/', views.select_animal_center, name="select_animal_center"),
    path('select_animal_common/', views.select_animal_common, name="select_animal_common"),
    path('aboutus_cat/', views.aboutus_cat, name="aboutus_cat"),
    path('aboutus_dog/', views.aboutus_dog, name="aboutus_dog"),
    path('list_cat/', views.list_cat, name="list_cat"),
    path('list_dog/', views.list_dog, name="list_dog"),
    path('story_cat/', views.story_cat, name="story_cat"),
    path('story_dog/', views.story_dog, name="story_dog"),
    path('kn_cat/', views.kn_cat, name="kn_cat"),
    path('kn_cat_1/', views.kn_cat_1, name="kn_cat_1"),
    path('kn_cat_2/', views.kn_cat_2, name="kn_cat_2"),
    path('kn_dog/', views.kn_dog, name="kn_dog"),
    path('kn_dog_1/', views.kn_dog_1, name="kn_dog_1"),
    path('kn_dog_2/', views.kn_dog_2, name="kn_dog_2"),
    path('instruction_cat/', views.instruction_cat, name="instruction_cat"),
    path('instruction_dog/', views.instruction_dog, name="instruction_dog"),
    path('quiz_cat_1/', views.quiz_cat_1, name="quiz_cat_1"),
    path('quiz_dog_1_new_2/', views.quiz_dog_1_new_2, name="quiz_dog_1_new_2"),
    path('test_result_cat/', views.test_result_cat, name="test_result_cat"),
    path('test_result_dog/', views.test_result_dog, name="test_result_dog"),
]