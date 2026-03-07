from django.shortcuts import render, redirect

from .models import About

def home(request):
    return render(request, "home/index.html")

def about(request):

    if request.method == "POST":
        person_name = request.POST.get("input_name")
        person_email = request.POST.get("input_email")
        person_college = request.POST.get("input_college")
        peroson_course = request.POST.get("input_course")
        person_phone = request.POST.get("input_phone")
        person_year = request.POST.get("input_year")
        person_gender = request.POST.get("input_gender")

        About.objects.create(
            name = person_name,
            college = person_college,
            course = peroson_course,
            email = person_email,
            phone_no = person_phone,
            year = person_year,
            gender = person_gender
        )
        return redirect("home")

    return render(request, "home/about.html")
