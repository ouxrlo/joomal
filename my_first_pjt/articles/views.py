## 요청을 처리하고 처리한 결과를 반환하는 파일

from django.shortcuts import render



def index(request):
    return render(request, 'index.html')

def users(request):
    return render(request, 'user.html')

def hello(request):

    name = "정은"
    tags = ['python', 'django', 'funny']
    books = ['헨젤과 그레텔', '피노키오', '피터팬', '백설공주', '어린왕자']
    context = {
        "name": name,
        "tags": tags,
        "books": books,

    }
    return render(request, 'hello.html', context)


def data_throw(request):
    return render(request, 'data_throw.html')

def data_catch(request):
    return render(request, 'data_catch.html')