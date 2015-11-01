import urllib2
from StringIO import StringIO
import gzip
import re
import logging
import urlparse
def ana(urlstr,expstr,cks=None,postdata=None):
    print "this is ana moudle start",urlstr,expstr
    try:
        print "1"
        headers = {  
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
        }  
        print "2"
        if (cks is not None and cks.strip() !=''):
            cks_dict=dict(item.strip().split("=") for item in cks.split(";"))
            logging.info('coockies passed in:')
            logging.info(cks)
            logging.info(cks_dict)
            headers.update({'Cookie':"; ".join('%s=%s' % (k,v) for k,v in cks_dict.items())})
            #headers.update({'Cookie':'a=b'})
        print "3"
        #if data=postdata is set, then it call POST, or it call GET
        logging.info('opening '+urlstr )
        req = urllib2.Request(  
                                url = urlstr,  
                                data = postdata,  
                                headers = headers  
        ) 
        resp=urllib2.urlopen(req)
        #print resp.read() 
        print resp.info()
        if resp.info().get('Content-Encoding') == 'gzip':
            buf=StringIO(resp.read())
            f=gzip.GzipFile(fileobj=buf)
            data=f.read()
        else:
            data=resp.read()
        #print data
        try:
            logging.info('start re')
            matlist=re.findall(expstr,data)
        except:
            logging.info('exception when findall')
            matlist=['sick_tako_reply_code_000_0_003','regex exception,illigle regex!']
    #except urllib2.URLError, e:
        #handleError(e)
    except:
        handleError(e)
        matlist=['sick_tako_reply_code_000_0_004','url error!']
    finally:
        return matlist

#resu=ana("http://share.popgo.org",'(?<=<td class="inde_tab_hot"><a href=").*?(?=&)')
#print resu
