from django.http import HttpResponse, HttpResponseNotFound
import json
import logging
import sys
from myapp.models import histobj
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

import inspect
def to_dict(instance):
    data={}
    #data=(instance.__dict__).copy()
    for a in instance.__dict__:
        if not a.startswith('_') and a!='date' and a!='id':
            data[a]=instance.__dict__[a]
    return data 
