#from flask import Blueprint
from .models import Commodity,ContinualContract,Contract
from flask_restful import fields, marshal_with,reqparse,Resource, Api
#from flask import jsonify
#futures_bp = Blueprint("futures",__name__)
from quotation.extensions import db

api = Api()

parser_commodity = reqparse.RequestParser()
parser_commodity.add_argument('name')
parser_commodity.add_argument('code')

commodity_fields = {
    'code': fields.String,
    'name': fields.String,
}

class CommodityResource(Resource):

    @marshal_with(commodity_fields)
    def get(self,code):
        commodity1 = Commodity.find_by_code(code)
        return commodity1

    def put(self, code):
        args = parser_commodity.parse_args()
        print(args)
        commodity1 = Commodity.find_by_code(code)
        if commodity1:
            print('update...')
            commodity1.code,commodity1.name = args.code,args.name
        else:
            print('add...')
            commodity1 = Commodity(code=args.code,name=args.name)
            db.session.add(commodity1)
        db.session.commit()
        print(commodity1)

parser_continual_contract = reqparse.RequestParser()
parser_continual_contract.add_argument('commodity_code')
parser_continual_contract.add_argument('month')

class ContinualContractResource(Resource):
    def get(self,commodity_code,month):
        # cc1 = ContinualContract(code=code,name='铁矿1月')
        # res = {'hello 1':cc1.__repr__()}
        # #print(res)
        # return jsonify(res)
        pass

    def put(self,commodity_code,month):
        args = parser_continual_contract.parse_args()
        print(args)
        #print('哈哈')

        cc1 = ContinualContract.find_by_commodity_month(commodity_code,month)
        if cc1:
            print('update...')
            cc1.month = args.month
        else:
            print('add...')
            cc1 = ContinualContract(commodity_code=commodity_code,month=month)
            db.session.add(cc1)
        db.session.commit()
        print(cc1)

parser_contract = reqparse.RequestParser()
parser_contract.add_argument('commodity_code')
parser_contract.add_argument('year')
parser_contract.add_argument('month')


class ContractResource(Resource):
    def get(self,commodity_code,year,month):
        pass

    def put(self,commodity_code,year,month):
        args = parser_continual_contract.parse_args()
        print(args)
        #print('哈哈')

        contract1 = Contract.find_by_commodity_year_month(commodity_code, year, month)
        if contract1:
            print('update...')
            #cc1.month = args.month
        else:
            print('add...')
            contract1 = Contract(
                commodity_code = commodity_code,
                year = year, 
                month = month)
            db.session.add(contract1)
        db.session.commit()
        print(contract1)


api.add_resource(CommodityResource, '/futures/commodity/<string:code>')

api.add_resource(ContinualContractResource, '/futures/continual/<string:commodity_code>/<int:month>')

api.add_resource(ContractResource, '/futures/contract/<string:commodity_code>/<int:year>/<int:month>')
