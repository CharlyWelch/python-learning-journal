from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import io
import os

def list_view(request):
    pass

def detail_view(request):
    pass

def create_view(request):
    pass

def update_view(request):
    pass 

def includeme(config):
    config.add_route('home', '/')
    config.add_view(list_view, route_name='home')

    config.add_route('detail', '/journal/{id:\d+}')
    config.add_view(detail_view, route_name='detail')

    config.add_route('create', '/journal/new-entry')
    config.add_view(create_view, route_name='create')

    config.add_route('update', '/journal/{id:\d+}/edit-entry')
    config.add_view(create_view, route_name='update')


if __name__ == '__main__':
    config = Configurator()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()