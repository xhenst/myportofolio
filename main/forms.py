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
            "school": TextInput(
                attrs={
                    "placeholder": "Universitas Indonesia",
                    "maxlength": 255,
                }
            ),
            "degree": TextInput(
                attrs={
                    "placeholder": "S1 Teknik Informatika",
                    "maxlength": 255,
                }
            ),
            "started_at": NumberInput(
                attrs={
                    "placeholder": "2022",
                }
            ),
            "ended_at": NumberInput(
                attrs={
                    "placeholder": "2026",
                }
            ),
        }
