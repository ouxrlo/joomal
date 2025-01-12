## 요청을 처리하고 처리한 결과를 반환하는 파일

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    response = HttpResponse("<h1> Hello, Django! </h1>")
    return response