from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def registerUser(request):
    #return HttpResponse('This is the register user view.')
    return render(request, 'accounts/registerUser.html')