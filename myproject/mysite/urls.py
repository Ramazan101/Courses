from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (UserViewSet, CategoryViewSet, SubCategoryViewSet,
                    CourseViewSet, LessonViewSet, AssignmentViewSet,
                    QuestionViewSet, OptionViewSet, ExamViewSet,
                    CertificateViewSet, ReviewViewSet)

router = SimpleRouter()
router.register('users', UserViewSet)
router.register('categories', CategoryViewSet)
router.register('subcategories', SubCategoryViewSet)
router.register('course', CourseViewSet)
router.register('lesson', LessonViewSet)
router.register('assignment', AssignmentViewSet)
router.register('question', QuestionViewSet)
router.register('option', OptionViewSet)
router.register('exam', ExamViewSet)
router.register('certificate', CertificateViewSet)
router.register('review', ReviewViewSet)




urlpatterns = [
    path('', include(router.urls)),
]