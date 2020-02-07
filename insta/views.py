from django.shortcuts import render
from django.http  import HttpResponse, Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to Le`Insta')
def post_today(request):
    date = dt.date.today()
    # images = Image.get_images()
    return render(request, 'all-posts/today-post.html', {"date": date,"image":image})


def convert_dates(dates):
    
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_post(request,past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

        except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

        if date == dt.date.today():
            return redirect(post_today)  
          
    return HttpResponse(html)