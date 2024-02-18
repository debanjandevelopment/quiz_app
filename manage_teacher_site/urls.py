from django.urls import path
from .views import dashboard,CreateQuestionPaperView

app_name = "teacher_manage_app"
urlpatterns=[
    path(
        route='',
        view=dashboard,
        name='teacher_dashboard'
    ),
    path(
        route='add_question_paper/',
        view=CreateQuestionPaperView.as_view(),
        name='add_question_paper'
    ),
]