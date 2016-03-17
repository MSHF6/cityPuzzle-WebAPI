# -*- coding: utf-8 -*-
from database import db
from db.common import SystemInfo

class Shape(db.Model):
	__tablename__ = 'shapes'
	id = db.Column(db.Integer, primary_key=True)
	# 一些形狀的描述
	desciption = db.Column(db.String(20), nullable=True)
	# 記錄路徑，無順序，陣列，用,區分
	path = db.Column(db.String(255))

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		print "<User: id='%d', desciption='%s', path='%s'>" % (
			self.id, self.desciption, self.path
		)



class Discount(SystemInfo):
	__tablename__ = 'discounts'
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.UincodeText, nullable=True)
	store_id = db.Column(db.Intger, db.ForeignKey('stores.id'))


	# 虛擬反向關聯，使用者折扣對應，找到有哪些使用者擁有哪些折扣
	users = db.relationship(
		'UserDiscounts',
		backref=db.backref('user_discounts')
	)

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		print "<User: id='%d', content='%s', store_id='%d'>" % (
			self.id, self.content, self.store_id
		)


class UserDiscounts(SystemInfo):
	__tablename__ = 'user_discounts_mapping'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Intger, db.ForeignKey('users.id'))
	discount_id = db.Column(db.Intger, db.ForeignKey('discounts.id'))
	# 使用的截止日期
	end_time = db.Column(db.DateTime)
	# 折扣優惠的類型
	discount_type = db.Column(db.String(45))
	# 是否使用過此折扣
	used = db.Column(db.Boolean, default=False)

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		print "<User: id='%d', content='%s', store_id='%d'>" % (
			self.id, self.content, self.store_id
		)