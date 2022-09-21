from django import forms
from .models import Poll


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields= ["organization","contribution","course_content","general","feedback"]
