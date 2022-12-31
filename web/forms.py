from django import forms

CATEGORIES = [
    ('1', 'はい'),
    ('2', 'いいえ')
]

class SurveyForm(forms.Form):
    ques1 = forms.ChoiceField(label="Q1 課金のやり方を知っている", choices=CATEGORIES, widget=forms.RadioSelect(attrs={'class':'radios'}))
    ques2 = forms.ChoiceField(label="Q2 課金をしたことがある", choices=CATEGORIES, widget=forms.RadioSelect(attrs={'class':'radios'}))
    ques3 = forms.ChoiceField(label="Q3 自分のお金で課金をしたことがある", choices=CATEGORIES, widget=forms.RadioSelect(attrs={'class':'radios'}))
    ques4 = forms.ChoiceField(label="Q4 親のお金で課金をしたことがある", choices=CATEGORIES, widget=forms.RadioSelect(attrs={'class':'radios'}))
    ques5 = forms.ChoiceField(label="Q5 親に内緒で親のお金で課金をしたことがある", choices=CATEGORIES, widget=forms.RadioSelect(attrs={'class':'radios'}))