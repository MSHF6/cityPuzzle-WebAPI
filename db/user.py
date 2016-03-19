# -*- coding: utf-8 -*-
from database import db
from db.common import SystemInfo


class User(SystemInfo):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	last_use_time = db.Column(db.DateTime)

	visit_records = db.relationship(
		'VisitRecord',
		# 使用者只對應到一位
		backref=db.backref('user')
	)

	# 虛擬反向關聯，使用者所擁有的所有優惠資料
	user_discounts = db.relationship(
		'UserDiscounts',
		backref=db.backref('users')
	)

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		print "<User: id='%d', name='%s', datetime='%s'>" % (
			self.id, self.name, self.last_use_time
		)