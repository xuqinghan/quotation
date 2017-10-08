from quotation.extensions import db

class Commodity(db.Model):
    '''商品 品种'''
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True,nullable=False)
    name = db.Column(db.String(20), unique=True,nullable=False)

    continual_contracts = db.relationship('ContinualContract', backref='commodity')

    contracts = db.relationship('Contract', backref='commodity')


    @classmethod
    def find_by_code(cls, code):
        commodity1 = cls.query.filter_by(code=code).first()
        assert(commodity1!=None,AssertionError('期货商品代码{commodity_code}不存在!'))
        return commodity1

    def __repr__(self):
        return f'<期货商品品种 {self.name},代码:{self.code}>'

class ContinualContract(db.Model):
    '''战场 同月份跨年Contract拼接而成'''
    id = db.Column(db.Integer, primary_key=True)
    id_commodity = db.Column(db.Integer,db.ForeignKey(Commodity.id))
    month = db.Column(db.Integer, nullable=False)

    def __init__(self,commodity_code,month):
        commodity1 = Commodity.find_by_code(commodity_code)
        self.id_commodity = commodity1.id
        self.month = month
    
    @classmethod
    def find_by_commodity_month(cls,commodity_code,month):

        commodity1 = Commodity.find_by_code(commodity_code)
        return cls.query.filter_by(id_commodity=commodity1.id).filter_by(month=month).first()


    def __repr__(self):
        return f'<期货连续行情 {self.commodity.name},{self.month}月交割>'


class Contract(db.Model):
    '''每一份合约 品种+交割年月'''
    id = db.Column(db.Integer, primary_key=True)
    id_commodity = db.Column(db.Integer,db.ForeignKey(Commodity.id))
    year = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)

    def __init__(self,commodity_code,year,month):
        commodity1 = Commodity.find_by_code(commodity_code)
        self.id_commodity = commodity1.id
        self.year = year
        self.month = month

    @classmethod
    def find_by_commodity_year_month(cls,commodity_code,year,month):
        commodity1 = Commodity.find_by_code(commodity_code)
        return cls.query.filter_by(id_commodity=commodity1.id).filter_by(year=year).filter_by(month=month).first()

    def __repr__(self):
        return '<期货合约 {code}{year_str}{month_str}>'.format(code = self.commodity.name,
        year_str = str(self.year)[-2:],
        month_str = str(self.month).zfill(2)
        )


# class Quotation(db.Model):
#     '''1个单位时间的 行情 构成地形的元素'''
#     id = db.Column(db.Integer, primary_key=True)
#     id_contract = db.Column(db.Integer,db.ForeignKey('Contract.id'))
#     datetime = db.Column(db, nullable=False)
#     open = db.Column(db.Integer, nullable=False)
#     high = db.Column(db.Integer, nullable=False)
#     low = db.Column(db.Integer, nullable=False)
#     close = db.Column(db.Integer, nullable=False)
#     vol = db.Column(db.Integer, nullable=False)
#     open_interest = db.Column(db.Integer, nullable=False)

#     contract = db.relationship("Contract", back_populates="quotations")

#     def __repr__(self):
#         return '<行情 %r>' % self.username
