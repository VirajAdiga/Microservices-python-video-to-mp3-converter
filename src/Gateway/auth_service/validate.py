import os
import requests


def token(request):
    if "Authorization" not in request.headers:
        return None, ("missing credentials", 401)

    access_token = request.headers["Authorization"]

    if not access_token:
        return None, ("missing credentials", 401)

    response = requests.post(
        f"http://{os.environ.get('AUTH_SERVICE_ADDRESS')}/validate",
        headers={"Authorization": access_token},
    )

    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)
