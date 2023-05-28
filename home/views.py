from rest_framework import generics
from .models import Section,School,Subject,Article,Homework
from . import serializers 

class ListSection (generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = serializers.SectionSerializer

class DetailSection (generics.RetrieveDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = serializers.SectionSerializer

class ListSchool (generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = serializers.SchoolSerializer

class DetailSchool (generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = serializers.SchoolSerializer

class ListSubject (generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = serializers.SubjectSerializer

class DetailSubject (generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = serializers.SubjectSerializer

class ListArticle (generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer

class DetailArticle (generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer

class ListHomework (generics.ListCreateAPIView):
    queryset = Homework.objects.all()
    serializer_class = serializers.HomeworkSerializer

class DetailHomework (generics.RetrieveUpdateDestroyAPIView):
    queryset = Homework.objects.all()
    serializer_class = serializers.HomeworkSerializer

