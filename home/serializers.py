from rest_framework import serializers
from .models import Section,School,Subject,Article,Homework,Question,Exam,StudentSection,ExamStudent


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        
class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'
        


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        
class ExamSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True ,  read_only=True)

    class Meta:
        model = Exam
        fields = '__all__'
        
class StudentSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSection
        fields = '__all__'
        
class ExamStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamStudent
        fields = '__all__'
        
