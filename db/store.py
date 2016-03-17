# -*- coding: utf-8 -*-
from database import db
from db.common import SystemInfo

class Store(SystemInfo):
	__tablename__ = 'stores'
	# 同時作為 Shape 的路徑編號
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Unicode(45), nullable=True)
	description = db.Column(db.Unicode(45), nullable=True)
	location_lat = db.Column(db.Float, nullable=True)
	location_lng = db.Column(db.Float, nullable=True)

	visit_records = db.relationship(
		'VisitRecord',
		backref=db.backref('stores')
	)

	discounts = db.relationship(
		'Discount',
		backref=db.backref('stores')
	)

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		print "<Store: id='%d', title='%s', description='%s', location_lat='%s', location_lng='%s'>" % (
			self.id, self.title, self.description, self.last_use_time,
			self.location_lat, self.location_lng
		)


class VisitRecord(SystemInfo):
	__tablename__ = 'visit_records'
	id = db.Column(db.Integer, primary_key=True)
	# 光顧的次數，取得折扣後會歸0
	times = db.Column(db.Integer)
	# 上次光顧的時間
	last_visit_time = db.Column(db.DateTime)
	user_id = db.Column(db.Intger, db.ForeignKey('users.id'))
	store_id = db.Column(db.Intger, db.ForeignKey('stores.id'))

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		print "<Store: id='%d', times='%d', last_visit_time='%s', user_id='%d', store_id='%d'>" % (
			self.id, self.times, self.last_visit_time,
			self.user_id, self.store_id
		)
