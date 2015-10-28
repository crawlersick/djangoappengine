import urllib2
from StringIO import StringIO
import gzip
import re
import logging
def ana(urlstr,expstr):
    print "this is ana moudle start",urlstr,expstr
    try:
        headers = {  
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
        }  
        req = urllib2.Request(  
                                url = urlstr,  
                                #data = postdata,  
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
        matlist=['sick_tako_reply_code_000_0_004','url error!']
    finally:
        return matlist

#resu=ana("http://share.popgo.org",'(?<=<td class="inde_tab_hot"><a href=").*?(?=&)')
#print resu
