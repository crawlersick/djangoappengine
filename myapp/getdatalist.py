from django.http import HttpResponse, HttpResponseNotFound
import json
import logging
import sys
from myapp.models import histobj
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#this is config to be called by /app_getdata?reqobj=histobj
def getdata(request):
    logging.info("getdatastart!!")
    reqobj=request.GET.get('reqobj')
    if (reqobj is None):
        resplist=['sick_tako_reply_code_000_0_010','no input for reqobj']
    else:
        genobj=getattr(sys.modules[__name__],reqobj)
        #resplist=list(genobj.objects.all())
        resplist=[]
        for m in genobj.objects.iterator():
            resplist.append(to_dict(m))
    resplist_json=json.dumps(resplist)
    logging.info(resplist_json)
    return HttpResponse(resplist_json)

#this is config to be called by /app_getdata_p?reqobj=histobj&p=1
def getdata_p(request):
    logging.info("getdata_pstart!!")
    reqobj=request.GET.get('reqobj')
    pagenum=request.GET.get('p')
    resplist=[]
    if (pagenum is None or not isinstance(pagenum,int)):
        pagenum=1
    if (reqobj is None):
        resplist=['sick_tako_reply_code_000_0_010','no input for reqobj']
    else:
        genobj=getattr(sys.modules[__name__],reqobj)
        tempresplist=list(genobj.objects.all())
        paginator = Paginator(tempresplist,5)
        try:
            presult=paginator.page(pagenum)
        except PageNotAnInteger:
            presult=paginator.page(1)
        except EmptyPage:
            presult=paginator.page(paginator.num_pages)
        for m in presult.object_list:
            resplist.append(to_dict(m))
    resplist_json=json.dumps(resplist)
    logging.info(resplist_json)
    return HttpResponse(resplist_json)

import inspect
def to_dict(instance):
    data={}
    #data=(instance.__dict__).copy()
    for a in instance.__dict__:
        if not a.startswith('_') and a!='date' and a!='id':
            data[a]=instance.__dict__[a]
    return data 
