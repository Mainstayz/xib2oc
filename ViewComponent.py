#!/usr/bin/python
# -*- coding: UTF-8 -*-

class ViewComponent:

	id = '' #唯一标识符
	name = '' #实例名字
	
	
	def __init__(self,name):
		self.name = name
#		self.creatInitializeCode()
#		if 'id' in dic:
#			self.id = dic['id']
#		if 'contentMode' in dic:
#			self.contentMode = self.getContentModel(dic['contentMode'])
#		if 'fixedFrame' in dic:
#			self.fixedFrame = dic['fixedFrame']
#		if 'verticalHuggingPriority' in dic:
#			self.verticalHuggingPriority = dic['verticalHuggingPriority']
#		if 'horizontalHuggingPriority' in dic:
#			self.horizontalHuggingPriority = dic['horizontalHuggingPriority']
#		if 'horizontalCompressionResistancePriority' in dic:
#			self.horizontalCompressionResistancePriority = dic['horizontalCompressionResistancePriority']
#		if 'verticalCompressionResistancePriority' in dic:
#			self.verticalCompressionResistancePriority = dic['verticalCompressionResistancePriority']
	
	
	def createCode(self):
		return "UIView *{} = [[UIView alloc] init];".format(self.name)
	
		
	def appendCode(self, prop, value):
		if prop == 'rect':
			if type(value) == dict:
				if value['key'] == 'frame':
 					return "{}.frame = CGRectMake({:.2f}, {:.2f}, {:.2f}, {:.2f});".format(self.name, value['x'], value['y'], value['width'], value['height'])

		elif prop == 'color':
			if type(value) == dict:
				if value['key'] == 'backgroundColor': 
					color = self.appendUIColor(value)
					return "{}.backgroundColor = {};".format(self.name, color)
					
			
	def appendUIColor(self,dic):			
		if 'colorSpace' in dic:
			if dic['colorSpace'] == 'calibratedRGB' or dic['colorSpace'] == 'deviceRGB':
				return "[UIColor colorWithRed:{:.2f} green:{:.2f} blue:{:.2f} alpha:{}]".format(dic['red'], dic['green'],dic['blue'],dic['alpha'])
			elif dic['colorSpace'] == 'calibratedWhite':
				return "[UIColor colorWithWhite:{:.2f} alpha:{}]".format(dic['white'], dic['alpha'])
		if 'customColorSpace' in dic:
			if dic['customColorSpace'] == 'sRGB':
				return "[UIColor colorWithRed:{:.2f} green:{:.2f} blue:{:.2f} alpha:{}]".format(dic['red'], dic['green'],dic['blue'],dic['alpha'])
			elif dic['customColorSpace'] == 'genericGamma22GrayColorSpace':
				return "[UIColor colorWithWhite:{:.2f} alpha:{}]".format(dic['white'], dic['alpha'])
		
		
	def getContentModel(self,modelType):
		return 'UIViewContentMode'+modelType[:1].upper()+modelType[1:]



component = ViewComponent('rr')
print(component.createCode())
str =  component.appendCode('rect', {'key':'frame','x':0,'y':0,'width':123,'height':3333})
print(str)
color =  component.appendCode('color', {
	"red": 1,
	"colorSpace": "calibratedRGB",
	"green": 1,
	"blue": 1,
	"alpha": 1,
	"customColorSpace": "sRGB",
	"key": "backgroundColor"
})
print(color)
content = component.getContentModel('scaleToFill')
print(content)


#
#print(component.id)
#print(component.methodMap)
