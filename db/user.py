# -*- coding: utf-8 -*-
from database import db


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		print "<User: id='%d', name='%s'>" % (self.id, self.name)