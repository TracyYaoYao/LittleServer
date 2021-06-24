from django.shortcuts import render, redirect
import django_redis
from django.http import HttpResponse, JsonResponse
# from .tinyurlScv import tinyurlSvcImpl
from django.views.decorators.csrf import csrf_exempt
from .Service.tinyurlScv import tinyurlSvcImpl


# Create your views here.


def home(request):
    return render(request, 'TinyURL/home.html')


def tinyurl(request):
    return render(request, 'TinyURL/tinyurl.html')


@csrf_exempt
def tinyurlEncode(request):
    url = request.POST.get('surl', None)
    if not url:
        return JsonResponse("Error: blank url...", safe=False)  # JsonResponse在抛出列表的时候需要将safe设置为False safe=False
    elif not url.startswith('http://') and not url.startswith('https://'):
        return JsonResponse("ERROR: url must start with http: / https:", safe=False)
    # res = tinyurlSvcImpl().EncodeURL(url)
    # return JsonResponse(res, safe=False)  # 用Json会返回字符串，但是只需要返回一个URL就可以
    return HttpResponse(tinyurlSvcImpl().EncodeURL(url))


@csrf_exempt
def tinyurlDecode(request):
    turl = request.POST.get('turl', None)
    return HttpResponse(tinyurlSvcImpl().DecodeURL(turl))