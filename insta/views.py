from django.shortcuts import render
from django.http  import HttpResponse, Http404
from .models import Image, Profile, Comments
from .forms import UploadForm,ProfileUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    posts=Image.objects.all()[::-1]
    current_profile=Profile.objects.exclude(id=request.user.id)
    upload_form = UploadForm(request.POST, request.FILES)
    comment_form = CommentForm(request.POST, request.FILES)
    if upload_form.is_valid():
        upload = upload_form.save(commit=False)
        upload.user = request.user
        upload.save()
        return HttpResponseRedirect(request.path_info)
    else:
        upload_form = UploadForm()
        comment_form = CommentForm()

    context ={
        'posts':posts,
        'upload_form':upload_form,
        'comment_form': comment_form,
        'user':current_profile,
    }
    return render(request, 'index.html', context)

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