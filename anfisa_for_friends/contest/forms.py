from django import forms

from contest.models import Contest


# class ContestForm(forms.Form):
#     title = forms.CharField(label='Название', max_length=20)
#     description = forms.CharField(
#         label='Описание',
#         widget=forms.Textarea({'cols': '22', 'rows': '5'}),
#     )
#     price = forms.IntegerField(
#         label='Цена',
#         min_value=10, max_value=100,
#         help_text='Рекомендованная розничная цена',
#     )
#     comment = forms.CharField(
#         label='Комментарий',
#         required=False,
#         widget=forms.Textarea({'cols': '22', 'rows': '5'}),
#     )
class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        fields = ('title', 'description', 'price', 'comment')
        widgets = {
            'description': forms.Textarea(attrs={'cols': '22', 'rows': '5'}),
            'comment': forms.Textarea(attrs={'cols': '22', 'rows': '5'}),
        }
