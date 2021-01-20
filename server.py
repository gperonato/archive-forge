import falcon
from wsgiref.simple_server import make_server
from .flow import createPackage

api = falcon.API()

# This is a basic definition of a Falcon service. For a working example see https://github.com/loleg/baumkataster-data

class FlowResource:

    def __init__(self, data):
        # Here we would initialise the template etc.
        pass

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        # Get the client's JSON request
        resp.body = get_paginated_json(req, df)
        # Now run the DataFlow
        createPackage(csvpath, outpath, fields) ...

data = None
api.add_route('/prepare', FlowResource(data))

if __name__ == '__main__':
    with make_server('', 8000, api) as httpd:
        print('Serving on port 8000...')
        httpd.serve_forever()
