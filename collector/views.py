from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from .models import Link


# Create your views here.

def scrape(request):
    if request.method == "POST":
        site = request.POST.get('site', '')

        try:
            page = requests.get(site)
        except:
            return render(request, 'collector/main-page.html')

        soup = BeautifulSoup(page.text, 'html.parser')
        content_type = request.POST.get('content_type')
        if content_type == 'link':
            for link in soup.find_all('a'):
                link_address = link.get('href')
                link_text = link.string

                Link.objects.create(address=link_address, name=link_text)
        elif content_type == 'image':
            for img_tag in soup.find_all('img'):
                image_src = site + img_tag.get('src')

                # Set the name of the image to "Image"
                image_name = "Image"

                Link.objects.create(address=image_src, name=image_name)
        elif content_type == 'video':
            for video_tag in soup.find_all('video'):
                video_src = site + video_tag.get('src')

                # Set the name of the video to "Video"
                video_name = "Video"
                Link.objects.create(address=video_src, name=video_name)

        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()

    return render(request, 'collector/main-page.html', {'data': data})


def clear(request):
    Link.objects.all().delete()
    return render(request, 'collector/main-page.html')
