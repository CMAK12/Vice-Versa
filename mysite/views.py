from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'main.html')

def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    number_of_word = len(str(user_text).split())
    return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':reversed_text, 'quantityword':number_of_word})