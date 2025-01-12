from django.shortcuts import render



def users(request):
    return render(request, 'user.html')


def profile(request, username):
    context = {
        'username' : username,
    }
    return render(request, 'profile.html', context)
