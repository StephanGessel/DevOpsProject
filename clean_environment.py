import requests


def close_servers():

    try:
        requests.get('http://127.0.0.1:5000/stop_server')
        requests.get('http://127.0.0.1:5001/stop_server')
        return 'Success'
    except Exception as e:
        print(e.__traceback__)
        return 'Error while stopping servers'