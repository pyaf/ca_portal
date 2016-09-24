import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ca_portal.settings")
application = get_wsgi_application()
import requests


requests.post(
        "https://api.mailgun.net/v3/mg.technex.in/messages",
        auth=("api", "key-cf7f06e72c36031b0097128c90ee896a"),

        data={"from": "Excited User <YOU@YOUR_DOMAIN_NAME>",
              "to": "rishabh.agrahari.eee15@iitbhu.ac.in",
              "subject": "Hello",
              "html": """
                    <html>
                      <head>
                      </head>
                      <body>
                        </div>
                        <div >
                          <h1 >Hi Technex'17 Campus Ambassadors!</h1>
                          <p>
                          <h3>The Dashboard is live!!</h3>
                          </p>
                          <hr >
                          <p>
                          <a class="btn btn-primary btn-lg" href="http://ca.technex.in" role="button">Technex'17 CA portal</a>
                          </p>
                        </div>
                      </body>
                    </html>
                    """
                    }
        )
