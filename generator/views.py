from django.shortcuts import render
import random

# Create your views here.
def home(request):
    '''Returns home page'''
    return render(request, 'generator/home.html')

def password(request):
    '''Returns random password page'''
    #create available chars list, init default list
    characters = list('abcdefghijklmnopqrstuvwxyz')

    #add extras requested
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special_chars'):
        characters.extend(list('~!@#$%^&*()_+'))

    #retrieve requested password length
    length = int(request.GET.get('length', 12))

    #create password
    password = ''
    for x in range(length):
        password += random.choice(characters)

    #send context
    context = {'password':password, 'length':length}
    return render(request, 'generator/password.html', context)

def about(request):
    '''Return about page'''
    return render(request, 'generator/about.html')