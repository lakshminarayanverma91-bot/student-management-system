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

        Student.objects.create(
            name = request.POST.get("input_name"),
            email = request.POST.get("input_email"),
            phone_no = request.POST.get("input_phone"),
            image = request.FILES.get("input_image")
        )

        return redirect("student_home")
    

    return render(request, "student/add_student.html")

def delete_student(request, student_id):

    my_student = Student.objects.get(id = student_id)   # 1st id is the id that is present in model (db)
                                                        # 2nd id is the id that comes from html
    my_student.delete()

    return redirect("student_home")

def update_student(request, student_id):
    
    student = Student.objects.get(id = student_id)

    if request.method == "POST":
        
        student.name = request.POST.get("input_name")
        student.email = request.POST.get("input_email")
        student.phone_no = request.POST.get("input_phone")

        student.save()

        return redirect("student_home")
    
    parameters = {
        "student":student
    }

    return render(request, "student/update_student.html", parameters)