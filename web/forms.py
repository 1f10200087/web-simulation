from django import forms

class SurveyForm(forms.Form):
    ques1 = forms.BooleanField(label="Q1")
    ques2 = forms.BooleanField(label="Q2")
    ques3 = forms.BooleanField(label="Q3")
    ques4 = forms.BooleanField(label="Q4")
    ques5 = forms.BooleanField(label="Q5")