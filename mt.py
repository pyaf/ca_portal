import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ca_portal.settings")
application = get_wsgi_application()
import requests


requests.post(
        "https://api.mailgun.net/v3/mg.technex.in/messages",
        auth=("api", "key-cf7f06e72c36031b0097128c90ee896a"),

        data={"from": "Publicity Team Technex'17<publicity@technex.in>",
              "to": "rishabh.agrahari.eee15@iitbhu.ac.in",
              "subject": "Technex CA Dashboard live!",
              "html": """
                    <html>
                      <head>
                      </head>
                      <body>
                        </div>
                        <div >
                          <h1>Hi %s!</h1>
                          <p>
                          <h3>The Dashboard is live!!</h3>
                          <h3> Visit your dashboard to complete your first task.</h3>
                          </p>
                          <p>
                          <a class="btn btn-primary btn-lg" href="http://ca.technex.in" role="button">Technex'17 CA Dashboard.</a>
                          (http://ca.technex.in/login)
                          </p>
                          <hr>
                          <br>
                          <p>
                          Regards<br>
                          Publicity Team <br>
                          Technex'17 <br>
                        </div>
                      </body>
                    </html>
                    """ %('rishabh')
                    }
        )
