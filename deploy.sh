#PYTHONPATH=. python django/bin/django-admin.py startproject \
#   --name=app.yaml --template=djangoappengine/conf/project_template myapp .
#      
#      set up shadowsocks at 1080,then:   
#      delegated -P8998 SERVER=http SOCKS=localhost:1080
#      delegated -P8999 SERVER=https SOCKS=localhost:1080
#      export http_proxy=http://127.0.0.1:8998
#      export https_proxy=http://127.0.0.1:8999
#      python2.7 /home/john/code/devpkg/python/google_appengine/appcfg.py --no_cookies --noisy --noauth_local_webserver update app.yaml
python2.7 /home/john/code/devpkg/python/google_appengine/appcfg.py  --noisy --noauth_local_webserver update app.yaml
