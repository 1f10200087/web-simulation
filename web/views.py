from django.shortcuts import render
from django.http import HttpResponse

import csv
import json

# Create your views here.
def index(request):
	return render(request, 'index.html')

def sns(request):
	return render(request, 'sns.html')

def charge(request):
	return render(request, 'charge.html')

def fraud(request):
	return render(request, 'fraud.html')

def oneclick_fraud(request):
	return render(request, 'oneclick_fraud.html')

def security(request):
	return render(request, 'security.html')

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

def quiz1(request):
	questions = get_quiz()
	context = {
        "ques" : questions,
    }
	if request.method == "POST":
		print(1)
	return render(request, 'quiz1.html', context)

questions = get_quiz()
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