from django.shortcuts import render

# Create your views here.


def index(request):
    context = {}
    if request.user.is_authenticated:
        context['username'] = request.user.username
    return render(request, 'common/base.html', context)