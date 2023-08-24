from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request,'examapp/home.html')

def begin_page(request):
    print(request.COOKIES)
    username=request.GET['name']
    print(username)
    response= render(request,'examapp/begin.html',{'name':username})
    response.set_cookie('name',username)
    return response


def q1_page(request):
    print(request.COOKIES)
    # username= request.COOKIES['name']
    # if int(answer1)== 3:
    #     request.COOKIES['score']= int(request.COOKIES['score']) + 1
    response = render(request,'examapp/question1.html')
    # response.set_cookie('score',0)
    return response

def q2_page(request):
    print(request.COOKIES)
    answer1=request.GET['answer1']  #value of answer1 from question1.html will be stored in the variable answer1
    # username= request.COOKIES['name']
    print(request.COOKIES)
    print(answer1)
    # if int(answer1)== 3:
    #     score= int(request.COOKIES['score']) + 1
    response = render(request,'examapp/question2.html')
    # response.set_cookie('score',score)
    response.set_cookie('answer1',answer1)

    return response


def q3_page(request):
    print(request.COOKIES)
    answer2=request.GET['answer2']  #value of answer2 from question2.html will be stored in the variable answer2
    # username= request.COOKIES['name']
    print(request.COOKIES)
    print(answer2)
    # if int(answer2)== 1:
    #     score= int(request.COOKIES['score']) + 1
    response = render(request,'examapp/question3.html')
    # response.set_cookie('score',score)
    response.set_cookie('answer2',answer2)

    return response

def result_page(request):
    print(request.COOKIES)
    score = 0
    answer3=request.GET['answer3']  #value of answer3 from question3.html will be stored in the variable answer3
    if int(answer3)== 3 :
        score= score+1

    answer1= request.COOKIES['answer1']
    if int(answer1)== 3 :
        score= score+1

    answer2= request.COOKIES['answer2']
    if int(answer2)== 1 :
        score= score+1

    username= request.COOKIES['name']

    print(request.COOKIES)

    # if int(answer3)== 3:
    #     score= score + 1
    # score = request.COOKIES['score']
    response = render(request,'examapp/result.html',{'name':username,'score':score,'answer1':answer1, 'answer2':answer2, 'answer3':answer3})
    # response.set_cookie('score',score)
    response.set_cookie('answer3',answer3)
    response.set_cookie('score',score)  # Adding Final Score to the response

    print("***********************")
    print("Final COOKIES:",request.COOKIES)
    print("***********************")
    return response
