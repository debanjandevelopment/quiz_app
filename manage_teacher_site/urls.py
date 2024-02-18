from django.urls import path
from .views import dashboard,add_exam

app_name = "teacher_manage_app"
urlpatterns=[
    path(
        route='',
        view=dashboard,
        name='teacher_dashboard'
    ),
    path(
        route='add_question_paper/',
        view=add_exam,
        name='add_question_paper'
    ),
]