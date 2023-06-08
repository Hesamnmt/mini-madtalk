from django.forms import ValidationError
from django.urls import reverse
from rest_framework import generics
from rest_framework.response import Response
from .models import Section,School,Subject,Article,Homework,Question,Exam,StudentSection,Teacher,Student
from . import serializers
from django.shortcuts import get_object_or_404
from account.models import User
from .permissions import IsManagerOrTeacher, IsManager
from rest_framework import status
from random import choice
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated


class ListSection (generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = serializers.SectionSerializer

class DetailSection (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsManager]
    serializer_class = serializers.SectionSerializer
    queryset = Section.objects.all()
    lookup_field = "pk"
    
class ListSchool (generics.ListCreateAPIView):
    permission_classes = [IsManager]
    queryset = School.objects.all()
    serializer_class = serializers.SchoolSerializer

class DetailSchool (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsManager]
    queryset = School.objects.all()
    serializer_class = serializers.SchoolSerializer
    lookup_field = "pk"


class ListSubject (generics.ListCreateAPIView):
    permission_classes = [IsManagerOrTeacher]
    queryset = Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
    

class DetailSubject (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsManager]
    queryset = Subject.objects.all()
    lookup_field = "pk"
    serializer_class = serializers.SubjectSerializer

class ListArticle (generics.ListCreateAPIView):
    permission_classes = [IsManagerOrTeacher]
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    
    def perform_create(self, serializer):
        section = Section.objects.get(id=self.request.data.get('section'))
        author = Teacher.objects.get(user_id=self.request.data.get('author'))
        Article.objects.create(section=section , author=author)
        serializer.save()
        

class DetailArticle (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsManagerOrTeacher]
    queryset = Article.objects.all()
    lookup_field = "pk"
    serializer_class = serializers.ArticleSerializer

class ListHomework (generics.ListCreateAPIView):
    queryset = Homework.objects.all()
    serializer_class = serializers.HomeworkSerializer
    
    def perform_create(self, serializer):
        title = self.request.data.get('title')
        description = self.request.data.get('description')
        due_date = self.request.data.get('due_date')
        section = Section.objects.get(id=self.request.data.get('section'))
        teacher = Teacher.objects.get(user_id=self.request.data.get('teacher'))
        student = User.objects.get(id=self.request.data.get('student'))
        Homework.objects.create(title=title,due_date=due_date, description=description,section=section,teacher=teacher,student=student)
        serializer.save()

class DetailHomework (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsManagerOrTeacher]
    queryset = Homework.objects.all()
    lookup_field = "pk"
    serializer_class = serializers.HomeworkSerializer

class ListQuestion (generics.ListCreateAPIView):
    permission_classes = [IsManagerOrTeacher]
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer

class DetailQuestion (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsManagerOrTeacher]
    queryset = Question.objects.all()
    lookup_field = "pk"
    serializer_class = serializers.QuestionSerializer
    
class StudentSectionView(generics.ListCreateAPIView):
    serializer_class = serializers.StudentSectionSerializer
    queryset = StudentSection.objects.all()
    
    
class ExamListCreateView(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated,IsManagerOrTeacher]
    serializer_class = serializers.ExamSerializer
    # queryset = Exam.objects.all()
    
    def get_queryset(self):
        teacher_id = self.request.user.id
        queryset = Exam.objects.filter(teacher__user_id=teacher_id)
        return queryset


    def create(self, request, *args, **kwargs):
        exam_name = request.data.get('name')
        duration = self.request.data.get('duration')
        total_marks = self.request.data.get('total_marks')
        teacher = Teacher.objects.get(user_id=self.request.user.id)
        section = StudentSection.objects.get(id=self.request.data.get('section'))
        selected_questions = request.data.get('questions')

        exam = Exam.objects.create(name=exam_name, duration=duration, total_marks=total_marks,section=section,teacher=teacher)

        for question_id in selected_questions:
            question = Question.objects.get(id=question_id)
            # if question.secttion == section:
            exam.questions.add(question)

        serializer = self.get_serializer(exam)
        return Response(serializer.data)
