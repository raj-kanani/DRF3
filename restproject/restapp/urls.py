from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('Api1', views.StudentApi1, basename='myapi')
router.register('StudentModel', views.StudentModel, basename='mystudent')

urlpatterns = [

    # function based
    path('api', views.student_api),
    path('api/<int:pk>/', views.student_api),

    # class based
    path('Api/', views.StudentApi.as_view()),
    path('Api/<int:pk>/', views.StudentApi.as_view()),

    # class based with viewset and router
    path('', include(router.urls))

]
