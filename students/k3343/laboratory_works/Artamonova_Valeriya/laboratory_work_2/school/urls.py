from django.urls import path
from . import views

urlpatterns = [
    path("teacher/", views.TeacherViewSet.as_view({'get': 'list'})),
    path("teacher/<int:pk>/", views.TeacherViewSet.as_view({'get': 'retrieve'})),
    path("teacher/add", views.TeacherViewSet.as_view({'post': 'create'})),
    path("teacher/<int:pk>/update", views.TeacherViewSet.as_view({'post': 'update'})),
    path("teacher/<int:pk>/delete", views.TeacherViewSet.as_view({'delete': 'destroy'})),
    path("pupil/", views.PupilViewSet.as_view({'get': 'list'})),
    path("pupil/<int:pk>/", views.PupilViewSet.as_view({'get': 'retrieve'})),
    path("pupil/add", views.PupilViewSet.as_view({'post': 'create'})),
    path("pupil/<int:pk>/update", views.PupilViewSet.as_view({'post': 'update'})),
    path("pupil/<int:pk>/delete", views.PupilViewSet.as_view({'delete': 'destroy'})),
    path("grade/", views.GradeViewSet.as_view({'post': 'create'})),
    path("grade/<int:pk>/delete", views.GradeViewSet.as_view({'delete': 'destroy'})),
    path("grade/<int:pk>/update", views.GradeViewSet.as_view({'post': 'update'})),
    path("timetable/", views.TimetableViewSet.as_view({'get': 'list'})),
    path("timetable/<int:pk>", views.TimetableViewSet.as_view({'get': 'retrieve'})),
    path("timetable/add", views.TimetableViewSet.as_view({'post': 'create'})),
    path("timetable/<int:pk>/delete", views.TimetableViewSet.as_view({'delete': 'destroy'})),
    path("timetable/<int:pk>/update", views.TimetableViewSet.as_view({'post': 'update'})),
    path("klass/", views.KlassViewSet.as_view({'get': 'list'})),
    path("klass/<int:pk>/", views.KlassViewSet.as_view({'get': 'retrieve'})),
    path("klass/<int:pk>/delete", views.KlassViewSet.as_view({'delete': 'destroy'})),
    path("klass/add/", views.KlassViewSet.as_view({'post': 'create'})),
    path("subject/", views.SubjectViewSet.as_view({'get': 'list'})),
    path("cabinet/", views.CabinetViewSet.as_view({'get': 'list'})),
    ]
