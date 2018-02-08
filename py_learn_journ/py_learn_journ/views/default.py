from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import io
import os

HERE = os.path.dirname(__file__)

def list_view(request):
    """ View for the home/list page """
    imported_text = io.open(os.path.join(HERE, '../templates/index.html')).read()
    return Response(imported_text)

def detail_view(request):
    """View for the detail route."""
    imported_text = io.open(os.path.join(HERE, '../templates/detail.html')).read()
    return Response(imported_text)

def create_view(request):
    """View for the create route."""
    imported_text = io.open(os.path.join(HERE, '../templates/create.html')).read()
    return Response(imported_text)

def edit_view(request):
    """View for the update route."""
    imported_text = io.open(os.path.join(HERE, '../templates/edit.html')).read()
    return Response(imported_text)


if __name__ == '__main__':
    config = Configurator()
    app = config.make_wsgi_app()

    config.add_route('home', '/')
    config.add_view(list_view, route_name='home')

    config.add_route('detail', '/journal/{id:\d+}')
    config.add_view(detail_view, route_name='detail')

    config.add_route('create', '/journal/new-entry')
    config.add_view(create_view, route_name='create')

    config.add_route('edit', '/journal/{id:\d+}/edit')
    config.add_view(edit_view, route_name='edit')

    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()