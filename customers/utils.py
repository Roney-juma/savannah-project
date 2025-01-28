import http.client
import json
from django.conf import settings


def get_auth0_token():
    conn = http.client.HTTPSConnection(settings.AUTH0_DOMAIN)

    payload = json.dumps({
        "client_id": settings.AUTH0_CLIENT_ID,
        "client_secret": settings.AUTH0_CLIENT_SECRET,
        "audience": settings.AUTH0_AUDIENCE,
        "grant_type": "client_credentials"
    })

    headers = {'content-type': "application/json"}

    conn.request("POST", "/oauth/token", payload, headers)

    res = conn.getresponse()
    data = res.read()
    conn.close()

    token_data = json.loads(data.decode("utf-8"))
    return token_data.get("access_token")