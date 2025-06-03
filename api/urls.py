from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import SkillViewSet, ExperienceViewSet, EducationViewSet

router = DefaultRouter()
router.register(r'skills', SkillViewSet)
router.register(r'experiences', ExperienceViewSet)
router.register(r'education', EducationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
