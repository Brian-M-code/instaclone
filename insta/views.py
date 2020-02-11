from django.shortcuts import render
from django.http  import HttpResponseRedirect, Http404
from .models import Image, Profile, Comments
from .forms import UploadForm,ProfileUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request, **kwargs):
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


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    current_profile = Profile.objects.get(user=request.user)
    users_posts = Image.objects.filter(user=request.user)[::-1]
    update_form = ProfileUpdateForm(request.POST, instance=request.user)
    if request.method == "POST":
        if update_form.is_valid():
            update = update_form.save(commit=False)
            update.user = current_user
            update.save
            return HttpResponseRedirect(request.path_info)
    else:
        update_form = ProfileUpdateForm()
    context={
        'user':current_user,
        'profile':current_profile,
        'posts':users_posts,
        'form':update_form,
    }
    return render(request, 'profile.html', locals())


@login_required(login_url='/accounts/login/')
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

def comments(request,id):
    comments = Comments.get_comments(id)
    number = len(comments   )
    
    return render(request,'comments.html',{"comments":comments,"number":number})

@login_required (login_url='/accounts/register/')          
def like_images(request,id):
    image =  Image.get_single_photo(id)
    user = request.user
    user_id = user.id
    
    if user.is_authenticated:
        uplike = image.votes.up(user_id)
        image.likes = image.votes.count()
        image.save()
        
    return redirect('home')