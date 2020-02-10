from django.shortcuts import render
from django.http  import HttpResponse, Http404
import datetime as dt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def search_user(request):
    if request.method == "GET":
        search_term = request.GET.get('search')
        message = '{}'.format(search_term)
        # searched_user = User.objects.filter(username=search_term).all()
        try:
            searched_user = User.objects.filter(username=search_term)
            searched_posts = Image.objects.filter(user=searched_user)[::-1]
        except DoesNotExist:
            raise Http404()
            return HttpResponseRedirect('homePage')
    context={
        'user':searched_user,
        'message':message,
        'posts':searched_posts
    }

    return render(request, 'searchh.html',context)