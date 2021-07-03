from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Paste
from .Service.pasteSvc import PasteSvcImpl
from TinyURL.Service.tinyurlScv import tinyurlSvcImpl
from TinyURL.Service.configSvc import configSvcImpl
from django.utils import timezone
from .Service.pasteSvc import PasteSvcImpl
# Create your views here.

def pastebin(request):
    return render(request, 'PasteBin/pastebin.html')


@csrf_exempt
def pasteSubmit(request):
    try:
        poster = request.POST.get('poster', None)
        content = request.POST.get('content', None)
        syntax = request.POST.get('syntax', None)
        if not content:
            raise ValueError
    except(KeyError, ValueError):
        return render(request, 'PasteBin/pastebin.html',{'error_message': "Empty paste are not allowed." })
    else:
        turl = tinyurlSvcImpl().PasteEncode(content)
        paste = Paste(poster=poster, content=content, createTime=timezone.now(), syntax=syntax, TinyURL=turl)
        paste.save()
        return HttpResponse(configSvcImpl().GetDomainSite() + "/p/" + turl)



def syntaxShow(request, turl):
    pasteInfo = Paste.objects.get(TinyURL=turl)
    poster = pasteInfo.poster
    syntax = pasteInfo.syntax
    createTime = pasteInfo.createTime
    content = pasteInfo.content
    TinyURL = pasteInfo.TinyURL
    PasteBinContent = PasteSvcImpl().PasteBin(content)
    return render(request, 'PasteBin/syntaxshow.html', locals())

