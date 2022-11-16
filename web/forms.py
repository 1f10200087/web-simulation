from django import forms

CATEGORIES = [
    ('1', 'yes'),
    ('2', 'no')
]

class SurveyForm(forms.Form):
    ques1 = forms.ChoiceField(label="Q1", choices=CATEGORIES, widget=forms.RadioSelect)
    ques2 = forms.ChoiceField(label="Q2", choices=CATEGORIES, widget=forms.RadioSelect)
    ques3 = forms.ChoiceField(label="Q3", choices=CATEGORIES, widget=forms.RadioSelect)
    ques4 = forms.ChoiceField(label="Q4", choices=CATEGORIES, widget=forms.RadioSelect)
    ques5 = forms.ChoiceField(label="Q5", choices=CATEGORIES, widget=forms.RadioSelect)