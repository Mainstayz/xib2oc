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
	def generateHierarchy(self,superView,key,dic):
		instance = self.map(key)
		instance.clsInfo = dic
		instance.name = dic['id']
		instance.superView = superView
		codes = instance.generateInitializeCode([])
		codes = instance.generateCode(codes)
		codes = instance.addedSubview(codes)
		codes.append('\n')
		return codes
	
	def map(self,key):
		return View()
		if key == 'view':
			return View()
		else:
			return None
				
	# 递归，从最顶部视图开始
	# views 每个视图的代码
	# className 类名
	def recursionViews(self,codes,cls,infoDic,superViewName):
		for key in infoDic:
			print(cls,key,' == ')
		
		print('=========')
		
		codes.append(self.generateHierarchy(superViewName, cls, infoDic))
		if 'subviews' in infoDic:
			for key in infoDic['subviews']:
				clsDic = infoDic['subviews'][key]		
				if type(clsDic) == dict:
					self.recursionViews(codes, key, clsDic,infoDic['id'])					
				if type(clsDic) == list:
					for dic in clsDic:
						self.recursionViews(codes, key, dic,dic['id'])					

							

		
		return codes;			
	


with open('test.json', 'r') as f:
	data = json.load(f)

objects = data['document']['objects']['view']

#print(data)

f = Factory()
views = f.recursionViews([],'View',objects,'father')

#for subView in views:
#	print('  \n'.join(subView))
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


