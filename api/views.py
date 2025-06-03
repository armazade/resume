from django.shortcuts import render
from rest_framework import viewsets
from .models import Skill, Experience, Education
from .serializers import SkillSerializer, ExperienceSerializer, EducationSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

# Create your views here.
