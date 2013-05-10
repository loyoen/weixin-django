import sae
from whulibrary import wsgi
application = sae.create_wsgi_app(wsgi.application)
