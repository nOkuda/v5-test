"""Example script for launching under WSGI"""
import atexit
import signal

import apitess
from tesserae.utils.coordinate import JobQueue

# Give app chance to clean up when signal is sent
def raise_exit(*args):
    raise SystemExit()

for sig in [signal.SIGHUP, signal.SIGINT, signal.SIGTERM]:
    signal.signal(sig, raise_exit)


def start_app():
    db_config = {
        'MONGO_HOSTNAME': 'localhost',
        'MONGO_PORT': 27017,
        'MONGO_USER': 'me',
        'MONGO_PASSWORD': '',
        'DB_NAME': 'exampledb'
    }

    db_cred = {
        'host': db_config['MONGO_HOSTNAME'],
        'port': db_config['MONGO_PORT'],
        'user': db_config['MONGO_USER'],
        'password': db_config['MONGO_PASSWORD'],
        'db': db_config['DB_NAME']
    }

    a_searcher = JobQueue(5, db_cred)

    atexit.register(a_searcher.cleanup)

    app = apitess.create_app(a_searcher, db_config)
    print('hello world')


if __name__ == '__main__':
    start_app()
