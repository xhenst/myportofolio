from django.forms import ModelForm, TextInput, Textarea, NumberInput

from main.models import Education


class EducationForm(ModelForm):
    class Meta:
        model = Education

        fields = [
            "school",
            "degree",
            "description",
            "started_at",
            "ended_at",
        ]

        labels = {
            "school": "Sekolah / Universitas",
            "degree": "Jenjang / Gelar",
            "description": "Deskripsi",
            "started_at": "Tahun Mulai",
            "ended_at": "Tahun Selesai",
        }

        widgets = {
            "school": TextInput(),
            "degree": TextInput(),
            "started_at": TextInput(),
            "ended_at": TextInput(),
        }
