
import requests
import threading

def make_request(name):
    while True:
        r = requests.get('Give your site here :)')
        print("Response code: {}".format(str(r.status_code)))


thread = 128
while thread >=1:
# while True:

    x = threading.Thread(target=make_request,args=(thread,))
    print("Starting thread {}".format(thread))
    x.start()
    thread-=1

