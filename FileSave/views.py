from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .Service import uploadSvc
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


# def filesave(request):
#     return render(request, 'FileSave/filesave.html')


def fileSave(request):
    return render(request, 'FileSave/filesave.html')


@csrf_exempt
def filePut(request):
    if request.method == 'POST':
        passKey = request.POST.get('key', None)
        if passKey != 'go':
            return JsonResponse(('pass key error, retry', 0), safe = False)
        else:
            myFile = request.FILES.get('file', None)  # 获取上传文件，没有文件的话，默认为False
        if not myFile:
            return JsonResponse(('upload failed', 0), safe = False)
        url = uploadSvc.Upload().upload(myFile)

        return HttpResponse(url)
    else:
        return JsonResponse("please upload with POST method")


