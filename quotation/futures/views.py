#from flask import Blueprint
from .models import ContinualContract
from flask_restful import Resource, Api
from flask import jsonify
#futures_bp = Blueprint("futures",__name__)
api = Api()

#@api.resource('/foo')
class Foo(Resource):
    def get(self):
        cc1 = ContinualContract(code='i01',name='铁矿1月')
        res = {'hello 1':cc1.__repr__()}
        #print(res)
        return jsonify(res)

    def post(self):
        pass


api.add_resource(Foo, '/Foo')
