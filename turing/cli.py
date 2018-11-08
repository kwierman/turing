# -*- coding: utf-8 -*-

import click
import logging
import tornado
from .webserver import make_app
from tornado.ioloop import IOLoop


@click.command()
def main(files=None):
    logging.basicConfig(level=logging.INFO)
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8888)
    server.start(0)  # forks one process per cpu
    IOLoop.current().start()

    
if __name__ == "__main__":
    main()
