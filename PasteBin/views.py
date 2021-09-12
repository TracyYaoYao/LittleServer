from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Paste
from .Service.pasteSvc import PasteSvcImpl
from TinyURL.Service.tinyurlScv import TinyurlSvcImpl
from TinyURL.Service.configSvc import ConfigSvcImpl
from TinyURL.Service.redisScv import CacheScvImpl
from django.utils import timezone
from .Service.pasteSvc import PasteSvcImpl
from time import strftime
import time


# Create your views here.

def pastebin(request):
    return render(request, 'PasteBin/pastebin.html')


@csrf_exempt
def pasteSubmit(request):
    poster = request.POST.get('poster', None)
    content = request.POST.get('content', None)
    syntax = request.POST.get('syntax', None)
    if not content:
        return JsonResponse(("ERROR: Empty paste is not allowed"), safe=False)
    else:
        now_time = strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        turl = TinyurlSvcImpl().PasteEncode(content+now_time)
        CacheScvImpl().CreateURLCache(turl, turl)  # 写入redis
        paste = Paste(poster=poster, content=content, createTime=timezone.now(), syntax=syntax, TinyURL=turl)
        paste.save()
        return HttpResponse(ConfigSvcImpl().GetDomainSite() + "/p/" + turl)


def syntaxShow(request, turl):
    tu = TinyurlSvcImpl().SearchURL(turl)
    if not tu:
        return JsonResponse('ERROR: 404 paste-turl not found', safe=False)
    else:
        pasteInfo = Paste.objects.get(TinyURL=turl)
        poster = pasteInfo.poster
        syntax = pasteInfo.syntax
        createTime = pasteInfo.createTime
        content = pasteInfo.content
        TinyURL = pasteInfo.TinyURL
        PasteBinContent = PasteSvcImpl().PasteBin(content)
        return render(request, 'PasteBin/syntaxshow.html', locals())
