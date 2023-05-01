from django import forms

from contest.models import Contest


class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'cols': '22', 'rows': '5'}),
            'comment': forms.Textarea(attrs={'cols': '22', 'rows': '5'}),
        }
