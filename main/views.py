from main.forms import EducationForm, ProjectForm
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.models import Experience, Education,Project


def show_main(request):
    context = {
        "name": "Kayla Alifah Khairunisa",
        "npm": "2506611931",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Kayla Alifah Khairunisa",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


def show_education(request):
    json_response = get_education_json(request)

    education = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    education = [edu.object for edu in education]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Kayla Alifah Khairunisa",
        "education_list": education,
        "title_query": title_query,
    }
    return render(request, "education.html", context)
def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pendidikan baru berhasil ditambahkan!")
        return redirect("main:show_education")
    else:
            print("ERROR FORM:", form.errors)

    context = {
        "name": "Kayla Alifah Khairunisa",
        "form": form,
    }
    return render(request, "education_form.html", context)
def get_education_json(request):
    title_query = request.GET.get("title", "").strip()
    education = Education.objects.all()

    if title_query:
        education = education.filter(title__icontains=title_query)

    education_json = serializers.serialize("json", education)
    return HttpResponse(education_json, content_type="application/json")
def delete_education(request, education_id):
    edu= get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        edu.delete()
        messages.success(request, "Education berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")
def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Kayla Alifah Khairunisa",
        "form": form,
    }
    return render(request, "projects_form.html", context)
def show_projects(request):
    context = {
        "name": "Kayla Alifah Khairunisa",
        "project_list": Project.objects.all(),
    }
    return render(request, "project.html", context)