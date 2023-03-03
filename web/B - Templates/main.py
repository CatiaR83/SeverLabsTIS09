from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi-chameleon import global_init
import uvicorn

from views import (
    home,
    courses,
    account,
)

app = FastAPI()

def main():
    config()
    start_server()
#:

def config():
    print("[+] Configuring server")
    config_routes()
    config_templates()
    print("[+] ...done configuring server")
#:

def config_routes():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    for view in [home, courses, account]:
        app.include_router(view.router)
#:

def config_templates():
    global_init('templates')
#:

def start_server():
    import uvicorn
    from docopt import docopt
    help_doc = """
A Web accessible FastAPI server that allow players to register/enroll for tournaments.

Usage:
  app.py [-p PORT] [-h HOST_IP] [-r]

Options:
  -p PORT, --port=PORT          Listen on this port [default: 8000]
  -h HOST_IP, --host=HOST_IP    Listen on this IP address []
  -r, --reload                  Reload server when a files change
"""
    args = docopt(help_doc)

    print("[+] Now starting server")
    uvicorn.run(
        'main:app',
        port = int(args['--port']),
        host = args['--host'],
        reload = args['--reload'],
        reload_includes = ['*.pt']
        )
#:

if __name__ == '__main__':
    main()
else:
    config()
#: