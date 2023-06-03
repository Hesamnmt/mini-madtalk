from django.forms import ValidationError
from rest_framework import generics
from rest_framework.response import Response
from .models import Section,School,Subject,Article,Homework,Question,Exam,Teacher
from . import serializers 
from django.shortcuts import get_object_or_404
from account.models import User
from .permissions import IsManagerOrTeacher, IsManager
from rest_framework import status

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
            user = request.user
            if user.type == "Student":
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                raise Response("cant",status=status.HTTP_404_NOT_FOUND)
        
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
    
class ExamListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.ExamSerializer

# # 'ExamListCreateView' should either include a `queryset` attribute, or override the `get_queryset()` method.
#     def get_queryset(self):
#         return Exam.objects.all()

    def perform_create(self, serializer):
        section_id = self.request.data.get('section_id')
        try:
            section = Section.objects.get(id=section_id)
        except Section.DoesNotExist:
            raise ValidationError('Section does not exist')

#     def create(self, request, *args, **kwargs):
#         exam_name = request.data.get('exam_name', None)
#         subject_id = request.data.get('subject_id', None)
#         teacher_id = request.data.get('teacher_id', None)
#         question_bank_id = request.data.get('question_bank_id', None)
#         duration = request.data.get('duration', None)
#         total_marks = request.data.get('total_marks', None)
#         section_id = self.kwargs['section_id']
    
#         if not all([exam_name, subject_id, teacher_id, question_bank_id, duration, total_marks]):
#             return Response({'message': 'Please provide all required fields'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             subject = Subject.objects.get(id=subject_id)
#             teacher = Teacher.objects.get(id=teacher_id)
#             question_bank = Question.objects.get(id=question_bank_id)
#         except Exception as e:
#             return Response({'message': 'Invalid subject, teacher or question bank provided'}, status=status.HTTP_400_BAD_REQUEST)

#         exam = Exam(
#             name=exam_name,
#             subject=subject,
#             teacher=teacher,
#             question_bank=question_bank,
#             duration=duration,
#             total_marks=total_marks
#         )
#         exam.save()
        
#         #for
        
#         students = Section.objects.get(student=section__student.id)
#         for student_id in students:
#             try:
#                 student = User.objects.get(id=student_id)
#             except Exception as e:
#                 continue

#             exam.students.add(student)

#         exam.save()

#         serializer = self.get_serializer(exam)
#         # return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return self.queryset.filter(section__id=section_id)

    
#             # students = request.data.get('students', [])
