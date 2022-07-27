from logging import exception
from celery import task
import time
import requests

@task()
def test ():
    time.sleep(5)
    print("hello world")

# this task takes the url link from a url and then create an object of dogModel in eventControler
# to run it periodically run command: celery -A mysite beat -l info (see settings.py)
@task()
def populate_dog():
    url = "https://dog.ceo/api/breeds/image/random"

    try:
        res = requests.get(url)
    except requests.ConnectionError as e:
        raise Exception("Failer operations",e)

    if res.status_code in [200,201]:
        # dog entry created
        data = res.json()
        image_url = data.get('message', "")
        from eventControler.models import DogsModel
        DogsModel.objects.create(url=image_url)

