from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# Create your views here.
arr = ['BJP', 'TRS', 'Congress', 'TDP', 'AIADMK', 'SP', 'BSP', 'BJD', 'RJD', 'NCP']
globalcnt = dict()

def index(request):
    mydictionary = {
        "arr" : arr
    }
    return render(request,'index.html',context=mydictionary)

def getquery(request):
    q = request.GET['party']
    if q in globalcnt:
        # if already exist then increment the value
        globalcnt[q] = globalcnt[q] + 1
    else:
        # first occurrence
        globalcnt[q] = 1
    mydictionary = {
        "arr" : arr,
        "globalcnt" : globalcnt
    }
    return render(request,'index.html',context=mydictionary)

def sortdata(request):
    global globalcnt
    globalcnt = dict(sorted(globalcnt.items(),key=lambda x:x[1],reverse=True))
    mydictionary = {
        "arr" : arr,
        "globalcnt" : globalcnt
    }
    return render(request,'index.html',context=mydictionary)