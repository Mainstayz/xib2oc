#!/usr/bin/python
# -*- coding: UTF-8 -*-

from ViewComponent import *
import json

class Factory:
	# code 是递归的数组   
	# superView 父视图
	# name 
	# dic
	# level
	def generateHierarchy(self,code,superView,name,dic,level):
		instance = self.map('view', superView, name, dic)
		return instance.generateCode(code, 0)
	
	def map(self,cls,superView,name,dic):
		conponent = View(superView, name, dic)
		return conponent
	


with open('test.json', 'r') as f:
	data = json.load(f)

objects = data['document']['objects']['view']


f = Factory()
array = list()
v = f.generateHierarchy(array, '爸爸', 'root', objects, 0)

print(v)
#component = View('rr','wwww',objects)
##
#code = component.generateCode([], 1)
#
#print(code)
#
#for key in objects:
#	print(key,'=')
#
#一个简单的递归
#u = '2222_'
#
#def jigui(s):
#	if len(s) == 0:
#		return ''
#	return s + jigui(s[1:])
#
#u = jigui(u)
#
#print(u)	


#print(component.clsInfo)
#rect = component.clsInfo['rect']
#print(component.generateInitializeCode())


#view = v('pite',data)
#
#print(view.name)
#print(view.clsInfo)
#			


