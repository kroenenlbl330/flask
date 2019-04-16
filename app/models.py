from app.exts import db

# class Cat(db.Model):
#   Cat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#   Cat_name = db.Column(db.String(12))
#   Cat_color = db.Column(db.String(12))

# class WaterMeter(db.Model):
#   __tablename__ = 'WaterMeter'
#   meter_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#   meter_code = db.Column(db.String(6)) # 表具编号
#   meter_name = db.Column(db.String(24)) # 表具名称
#   meter_site = db.Column(db.String(24)) # 表具位置

# class Session(db.Model):
#   __tablename__ = 'session'
#   meter_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#   meter_code = db.Column(db.String(6))
#   meter_name = db.Column(db.String(24))
#   meter_site = db.Column(db.String(24))