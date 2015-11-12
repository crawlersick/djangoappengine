# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseNotFound
import json
import logging
import sys
from myapp.models import histobj
sys.path.append('core_ms')
import anaurl
def MainPage(request):
    logging.info("xxxxxxxxxx")
    return HttpResponse('<h1>Page was found</h1>')
def process_command(request):
    logging.info("process_command started")
    cmdstr=request.GET.get('cmd')
    expstr=request.GET.get('exp')
    cksstr=request.GET.get('cks')
    poststr=request.GET.get('poststr')
    logging.info(cmdstr)
    logging.info(expstr)
    if cksstr is not None:
        logging.info('getcks '+cksstr)
    if poststr is not None:
        logging.info('getpostdata'+poststr)
    if (cmdstr is None) or (expstr is None):
        resplist=['sick_tako_reply_code_000_0_000','no input for exp and cmd']
    else:
        cmdlist=request.GET.get('cmd').split()
        expre=request.GET.get('exp').strip()
        if len(cmdlist)>1:
            logging.info("cmdlist part1 "+cmdlist[0])
            logging.info("cmdlist part2 "+cmdlist[1])
            logging.info("expre "+expre)
            hobj=histobj(cmd_action=cmdlist[0],cmd_target=cmdlist[1],expre=expre,author='233_233_null')
            hobj.save()
            if cmdlist[0]=='test':
                resplist=anaurl.ana(cmdlist[1],expre,cksstr,poststr)
            else:
                resplist=['sick_tako_reply_code_000_0_002','cmdlist first element can not recognized']
        else:
            resplist=['sick_tako_reply_code_000_0_001','cmdlist have less element than 2']
    resplist_json=json.dumps(resplist)
    logging.info(resplist_json)
    return HttpResponse(resplist_json)
