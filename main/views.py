from django.shortcuts import render

from main.models import Experience


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