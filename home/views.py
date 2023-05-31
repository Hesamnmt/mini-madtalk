from rest_framework import generics
from rest_framework.response import Response
from .models import Section,School,Subject,Article,Homework,Question,Choice
from . import serializers 
from django.shortcuts import get_object_or_404
from account.models import User
from .permissions import IsManagerOrTeacher, IsManager

class ListSection (generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = serializers.SectionSerializer

class DetailSection (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsManager]
    serializer_class = serializers.SectionSerializer
    queryset = Section.objects.all()
    lookup_field = "pk"
    
class ListSchool (generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = serializers.SchoolSerializer

class DetailSchool (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsManager]
    queryset = School.objects.all()
    serializer_class = serializers.SchoolSerializer
    lookup_field = "pk"


class ListSubject (generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
    

class DetailSubject (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsManager]
    queryset = Subject.objects.all()
    lookup_field = "pk"
    serializer_class = serializers.SubjectSerializer

class ListArticle (generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer

class DetailArticle (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsManagerOrTeacher]
    queryset = Article.objects.all()
    lookup_field = "pk"
    serializer_class = serializers.ArticleSerializer

class ListHomework (generics.ListCreateAPIView):
    queryset = Homework.objects.all()
    serializer_class = serializers.HomeworkSerializer
        
    def post(self, request, *args, **kwargs):
        file_serializer = self.serializer_class(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save(user=request.user)
            return Response(file_serializer.data, status=201)
        else:
            return Response(file_serializer.errors, status=400)

class DetailHomework (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsManagerOrTeacher]
    queryset = Homework.objects.all()
    lookup_field = "pk"
    serializer_class = serializers.HomeworkSerializer

class ListQuestion (generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer

class DetailQuestion (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsManagerOrTeacher]
    queryset = Question.objects.all()
    lookup_field = "pk"
    serializer_class = serializers.QuestionSerializer
    
class ListChoice (generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = serializers.ChoiceSerializer

class DetailChoice (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsManagerOrTeacher]
    queryset = Choice.objects.all()
    lookup_field = "pk"
    serializer_class = serializers.ChoiceSerializer
    
    