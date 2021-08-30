from django.shortcuts import render, redirect
import django_redis
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from .Service.tinyurlScv import TinyurlSvcImpl




# Create your views here.


def home(request):
    return render(request, 'TinyURL/home.html')


def tinyurl(request):
    return render(request, 'TinyURL/tinyurl.html')


@csrf_exempt
def tinyurlEncode(request):
    url = request.POST.get('surl', None)
    if not url:
        return JsonResponse(("ERROR: blank url..."), safe=False)  # JsonResponse在抛出列表的时候需要将safe设置为False safe=False
    elif not url.startswith('http://') and not url.startswith('https://'):
        return JsonResponse(("ERROR: url must be started with http:/https:"), safe=False)
    return HttpResponse(TinyurlSvcImpl().EncodeURL(url))  # 用Json会返回字符串，但是只需要返回一个URL就可以


@csrf_exempt
def tinyurlDecode(request):
    turl = request.POST.get('turl', None)
    if not turl:
        return HttpResponse(("ERROR: empty turl"))
    su = TinyurlSvcImpl().DecodeURL(turl)
    if su:
        return HttpResponse(su)
    return HttpResponse(("ERROR: invaild turl"))

def tinyurlRedirect(request, turl):
    tu = TinyurlSvcImpl().SearchURL(turl)
    if tu:
        return redirect(TinyurlSvcImpl().SearchURL(turl))
    return JsonResponse('ERROR: 404 turl not found', safe=False)

