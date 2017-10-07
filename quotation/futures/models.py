from quotation.extensions import db

class ContinualContract(db.Model):
    '''战场 同月份跨年Contract拼接而成'''
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    #email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<期货品种 {self.code},{self.name}>'

# class Quotation(db.Model):
#     '''1个单位时间的 行情 构成地形的元素'''
#     id = db.Column(db.Integer, primary_key=True)
#     datetime = db.Column(db, nullable=False)
#     open = db.Column(db.Float, unique=True, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username