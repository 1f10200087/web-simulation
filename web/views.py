from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from django.views.generic import TemplateView

import csv
import json

# Create your views here.
def index(request):
	return render(request, 'index.html')

"""
def get_quiz():
	test_file = open('web/ques/ques-utf8.csv', encoding="utf-8")
	test_data = csv.reader(test_file)
	questions = []
	for row in test_data:
		if test_data.line_num == 1:
			continue
		questions.append(row)
	test_file.close()
	
	count = len(questions)
	for c in range(count):
		questions[c][2] = questions[c][2].split()
	
	return questions
"""

def get_quiz(thema):
    path = 'web/ques/' + thema + '_quiz.csv'
    test_file = open(path, encoding="utf-8")
    test_data = csv.reader(test_file)
    questions = []
    for row in test_data:
        if test_data.line_num == 1:
            continue
        questions.append(row)
    test_file.close()
    count = len(questions)
    for c in range(count):
        questions[c][2] = questions[c][2].split()
    return questions

#questions = get_quiz()
def sns(request):
    questions = get_quiz("sns")
    context = {
            "ques" : questions,
    }
    if request.method == "POST":
        for i in range(1, 11):
            for j in range(1, 5):
                ids = "answer-"+str(i)+"-"+str(j)
                if ids in request.POST:
                    ans = request.POST[ids]
                    if questions[i-1][3] == ans:
                        questions[i-1][4] = 1
                    else: 
                        questions[i-1][4] = 0
                        context = {
                            "ques" : questions,
                        }
    return render(request, 'sns.html', context)

def charge(request):
    questions = get_quiz("charge")
    context = {
        "ques" : questions,
    }
    if request.method == "POST":
        for i in range(1, 11):
            for j in range(1, 5):
                ids = "answer-"+str(i)+"-"+str(j)
                if ids in request.POST:
                    ans = request.POST[ids]
                    if questions[i-1][3] == ans:
                        questions[i-1][4] = 1
                    else: 
                        questions[i-1][4] = 0
                        context = {
                            "ques" : questions,
                        }
    return render(request, 'charge.html', context)

def fraud(request):
    questions = get_quiz("fraud")
    context = {
        "ques" : questions,
    }

    if request.method == "POST":
        for i in range(1, 11):
            for j in range(1, 5):
                ids = "answer-"+str(i)+"-"+str(j)
                if ids in request.POST:
                    ans = request.POST[ids]
                    if questions[i-1][3] == ans:
                        questions[i-1][4] = 1
                    else: 
                        questions[i-1][4] = 0
                        context = {
                            "ques" : questions,
                        }
    return render(request, 'fraud.html', context)

def oneclick_fraud(request):
	return render(request, 'oneclick_fraud.html')

def security(request):
    questions = get_quiz("security")
    context = {
        "ques" : questions,
    }
    if request.method == "POST":
        for i in range(1, 11):
            for j in range(1, 5):
                ids = "answer-"+str(i)+"-"+str(j)
                if ids in request.POST:
                    ans = request.POST[ids]
                    if questions[i-1][3] == ans:
                        questions[i-1][4] = 1
                    else: 
                        questions[i-1][4] = 0
                        context = {
                            "ques" : questions,
                        }
    return render(request, 'security.html', context)

def security_exp(request):
	return render(request, 'security_exp.html')

def test(request):
	return render(request, 'test.html')

def Diagnosis_charge(request):
	form = forms.SurveyForm
	answs = [0, 0, 0, 0, 0]
	context = {
		'form' : form,
	}
	if request.method == 'POST':
		form = forms.SurveyForm(request.POST)
		
		if form.is_valid():
			answs[0] = request.POST['ques1']
			answs[1] = request.POST['ques2']
			answs[2] = request.POST['ques3']
			answs[3] = request.POST['ques4']
			answs[4] = request.POST['ques5']
			result = calc_DegreeCharge(answs)
		#print(answs, result)
		context = {
			'form' : form,
			'result' : result[0],
            'advice' : result[1]
		}
	return render(request, 'Diagnosis_charge.html', context)

def calc_DegreeCharge(lst):
    if lst[0] == '2':
        return ["かなり低い", "キミは課金能力がないか、課金に興味がないみたい\nもし課金することがあれば親とお小遣いに相談して決めよう！"]
    else:
        if lst[1] == '2':
            return ["かなり低い", "キミは課金することに興味がないみたい\n自制ができるキミにアドバイスはいらないよね？"]
        else:
            if lst[2] == '1' and lst[3] == '2' and lst[4] == '2':
                return ["中", "キミの課金能力は高いみたい\nだけど、自分のお小遣いの中で課金しててえらい！\n我慢出来ずにキミの親に内緒で課金しないように気を付けてね！"]
            elif lst[3] == '1' and lst[4] == '2':
                return ["高い", "キミは課金する時に親に相談出来てえらい！\nだけど、我慢できずに親に内緒で課金しないように気を付けてね！"]
            else:
                return ["かなり高い", "キミの課金能力はかなり高いみたい\nだけど親に内緒で課金してはだめだよ？\nたくさん課金して楽しい瞬間はそのときだけ。あとで後悔してもお金は返ってこないよ！\nキミが高額課金していないことを信じてる！"]

"""
def quiz1(request):
	questions = get_quiz()
	context = {
        "ques" : questions,
    }
	if request.method == "POST":
		print(1)
	return render(request, 'quiz1.html', context)

def quiz2(request):
    context = {
        "ques" : questions,
    }
    if request.method == "POST":
        for i in range(1, 11):
            for j in range(1, 5):
                ids = "answer-"+str(i)+"-"+str(j)
                if ids in request.POST:
                    ans = request.POST[ids]
                    if questions[i-1][3] == ans:
                        questions[i-1][4] = 1
                    else: 
                        questions[i-1][4] = 0
                        context = {
                            "ques" : questions,
                        }
    return render(request, 'quiz2.html', context)
"""