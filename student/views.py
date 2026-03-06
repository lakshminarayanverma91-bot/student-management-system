from django.shortcuts import render, redirect

from .models import Student

def student_home(request):

    students_data = Student.objects.all()

    data = {
        "students_data":students_data
    }

    return render(request, "student/student_home.html", data)

def add_student(request):

    if request.method == "POST":
        student_name = request.POST.get("input_name")
        student_email = request.POST.get("input_email")
        student_phone = request.POST.get("input_phone")
        student_image = request.FILES.get("input_image")

        Student.objects.create(
            name = student_name,
            email = student_email,
            phone_no = student_phone,
            image = student_image
        )

        return redirect("/student/std/")
    

    return render(request, "student/add_student.html")
