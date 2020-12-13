from django.shortcuts import render

# Create your views here.


def response(request):
    return render(request, 'response_page.html')

def register(request):
    if request.method=='POST':
        print(request.method)
        first_name = request.method.POST('name', None)
        last_name = request.method.POST('last_name', None)
        aadhar = request.method.POST('aadhar', None)
        Date_of_birth = request.method.POST('Date_of_birth', None)
        password = request.method.POST('password', None)
        password2 = request.method.POST('password2', None)
        return JsonResponse({'success': 'True'})
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def capture_image(request):
    return render(request, 'capture_image.html')

def cast_vote():
    return render(request, 'voting_page.html')
