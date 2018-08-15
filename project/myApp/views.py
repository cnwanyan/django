from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

#创建视图
def index(request):
    return HttpResponse("myApp index")

#带参数的视图
def detail(request,s):
    return HttpResponse("detail - %s" % s)

from .models import Grades,Students


#渲染template的视图
def grades(request):
    #查询数据
    gradesList = Grades.objects.all()
    #将数据传递给模板
    return render(request, "myApp/grades.html", {"grades": gradesList})


def students(request):
    studentList = Students.objects.all()
    return render(request, "myApp/students.html", {"students": studentList})

def gradesStudent(request,s):
    grades= Grades.objects.get(pk=s)
    studentList = grades.students_set.all()
    return render(request,"myApp/students.html",{"students":studentList})