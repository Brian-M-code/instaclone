from django.shortcuts import render
from django.http  import HttpResponseRedirect, Http404
from .models import Image, Profile, Comments
from .forms import UploadForm,ProfileUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from vote.managers import VotableManager

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

def login(request):
    next_page = request.GET['next']
    if request.user.is_authenticated():
        return HttpResponseRedirect(next_page)
    else:
        if request.method == 'POST':
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(email=username, password=password)
                if user is not None and user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(next_page)
                else:
                    error_msg = 'There was an error!'
                    return render(request, "login", {'form': form, 'error_msg': error_msg})
            else:
                error_msg = "There was an error!"
                return render(request, "login", {'form':form, 'error_msg':error_msg})
        else:
            form = LoginForm()
            return render(request, "login", {'form': form})


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

def add_comment(request,id):
    
    current_user = request.user
    image = Image.get_single_photo(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.image_id = id
            comment.save()
        return redirect('home')

    else:
        form = CommentForm()
        return render(request,'new_comment.html',{"form":form,"image":image})


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

def comment(request,id):
    comment = Comment.get_comments(id)
    number = len(comments   )
    
    return render(request,'comment.html',{"comments":comments,"number":number})

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

def follow(request,user_id):
    res = AjaxFollow(request.Get,request.user)
    context = { 'ajax_output': ajax_output()}
    return render(request,'profile.html',context)

@login_required(login_url='/accounts/login/')
def following(request, username):
    user = User.objects.get(username=username)
    user_profile = Profile.objects.get(user=user)
    profiles = user_profile.following.all

    context = {
        'header': 'Following',
        'profiles': profiles
    }
    return render(request, 'instagram/follow_list.html', context)