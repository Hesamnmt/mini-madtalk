from django.db import models
from account.models import User


class School(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
class Subject(models.Model):
    name = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

class Section(models.Model):
    name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='article_files/',null=True,blank=True)

class Homework(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='homework_files/',null=True,blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    deliver_time = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

class Question(models.Model):
    question = models.TextField()
    choice_1 = models.TextField()
    choice_2 = models.TextField()
    choice_3 = models.TextField()
    choice_4 = models.TextField()
    correct_choice = models.IntegerField(choices=[(1, 'Choice 1'), (2, 'Choice 2'), (3, 'Choice 3'), (4, 'Choice 4')])
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    secttion = models.ForeignKey(Section,on_delete=models.CASCADE)



class StudentSection (models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    section = models.ForeignKey(Section,on_delete=models.CASCADE)


class Exam(models.Model):
    name = models.CharField(max_length=255)
    section = models.ForeignKey(StudentSection, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question)
    duration = models.IntegerField()
    total_marks = models.IntegerField()

    def __str__(self):
        return self.name
    
class ExamStudent(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.SmallIntegerField()