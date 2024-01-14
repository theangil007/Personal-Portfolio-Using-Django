from django.shortcuts import render
from .models import *


def homepageview(request):
    about_me_data = about_me.objects.first()
    print("about_me_data:", about_me_data)

    experience_data = experience.objects.all()
    print("experience_data:", experience_data)

    education_data = education.objects.all()
    print("education_data:", education_data)

    skills_data = skills.objects.all()
    print("skills_data:", skills_data)

    certifications_data = certifications.objects.all()
    print("certifications_data:", certifications_data)

    project_data = project.objects.all()
    print("project_data:", project_data)

    color_data = color.objects.first()
    print("color_data:", color_data)

    context = {
        "about_me_data": about_me_data,
        "experience_data": experience_data,
        "education_data": education_data,
        "skills_data": skills_data,
        "certifications_data": certifications_data,
        "project_data": project_data,
        "color_data": color_data,
    }

    return render(request, "index.html", context)
