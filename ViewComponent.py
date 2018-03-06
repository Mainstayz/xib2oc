#!/usr/bin/python
# -*- coding: UTF-8 -*-

class View:
	
	def __init__(self,superView,name,dic):
		self.superView = superView
		self.name = name
		self.clsInfo = dic
	
	def generateInitializeCode(self):
		return "UIView *{} = [[UIView alloc] init];".format(self.name)
	
		
	def generateCode(self, codeArray, level):
		
		code = list()
		init = self.generateInitializeCode()
		code.append(init)
		#contentModel
		if 'contentMode' in self.clsInfo:
			value = "{}.contentMode = {};".format(self.name,self.getContentModel(self.clsInfo['contentMode']))
			code.append(value)	
		
		
		#color
		if 'color' in self.clsInfo:
			value = self.clsInfo['color']
			if type(value) == dict:
					color = self.appendUIColor(value)
					code.append(color)
			if type(value) == list:
				for dic in value:
					color = self.appendUIColor(dic)
					code.append(color)
					
		#frame
		if 'rect' in self.clsInfo:
			value = self.clsInfo['rect']
			if type(value) == dict:
					rect = self.appendRect(value)
					code.append(rect)
			if type(value) == list:
				for dic in value:
					rect = self.appendRect(value)
					code.append(rect)
		
		
		if self.superView:
			print(self.superView)
		else:
			print('么哦有苏')
			
			
		codeArray.append(code) 
		return codeArray

	def appendRect(self,dic):
		if dic['key'] == 'frame' and 'fixedFrame' in self.clsInfo:
			return "{}.frame = CGRectMake({}, {}, {}, {});".format(self.name, value['x'], value['y'], value['width'], value['height'])
		else:
			return "{}.{} = CGRectMake({}, {}, {}, {});".format(self.name, dic['key'],dic['x'], dic['y'], dic['width'], dic['height'])

		
			
	def appendUIColor(self,dic):	
		code = str()		
		if 'colorSpace' in dic:
			if dic['colorSpace'] == 'calibratedRGB' or dic['colorSpace'] == 'deviceRGB':
				code = "[UIColor colorWithRed:{} green:{} blue:{} alpha:{}]".format(dic['red'], dic['green'],dic['blue'],dic['alpha'])
			elif dic['colorSpace'] == 'calibratedWhite':
				code = "[UIColor colorWithWhite:{} alpha:{}]".format(dic['white'], dic['alpha'])
		if 'customColorSpace' in dic:
			if dic['customColorSpace'] == 'sRGB':
				code = "[UIColor colorWithRed:{} green:{} blue:{} alpha:{}]".format(dic['red'], dic['green'],dic['blue'],dic['alpha'])
			elif dic['customColorSpace'] == 'genericGamma22GrayColorSpace':
				code = "[UIColor colorWithWhite:{} alpha:{}]".format(dic['white'], dic['alpha'])
		return "{}.{} = {};".format(self.name,dic['key'],code)
		
		
	def getContentModel(self,modelType):
		return 'UIViewContentMode'+modelType[:1].upper()+modelType[1:]


	def tabCode(self,level):
		return level * 4 * ' '
		
#dic = {
#	"autoresizesSubviews": "NO",
#	"opaque": "NO",
#	"hidden": "YES",
#	"color": [
#		{
#			"colorSpace": "custom",
#			"white": "0.66666666666666663",
#			"alpha": 1,
#			"customColorSpace": "genericGamma22GrayColorSpace",
#			"key": "backgroundColor"
#		},
#		{
#			"red": 1,
#			"colorSpace": "custom",
#			"green": "0.83015773116334923",
#			"blue": 0.39770596420388293,
#			"alpha": 1,
#			"customColorSpace": "sRGB",
#			"key": "tintColor"
#		}
#	],
#	"autoresizingMask": {
#		"flexibleMaxX": "YES",
#		"key": "autoresizingMask",
#		"flexibleMaxY": "YES"
#	},
#	"customModule": "Charts",
#	"multipleTouchEnabled": "YES",
#	"semanticContentAttribute": "forceLeftToRight",
#	"rect": [
#		{
#			"x": 61,
#			"width": 240,
#			"y": 225,
#			"key": "frame",
#			"height": 128
#		},
#		{
#			"x": "0.20000000000000001",
#			"width": "0.40000000000000002",
#			"y": "0.29999999999999999",
#			"key": "contentStretch",
#			"height": 0.5
#		}
#	],
#	"clearsContextBeforeDrawing": "NO",
#	"fixedFrame": "YES",
#	"translatesAutoresizingMaskIntoConstraints": "NO",
#	"contentMode": "scaleToFill",
#	"alpha": "0.94999999999999996",
#	"customClass": "BarChartView",
#	"userDefinedRuntimeAttributes": {
#		"userDefinedRuntimeAttribute": [
#			{
#				"keyPath": "pttt",
#				"type": "string",
#				"value": "asd"
#			},
#			{
#				"keyPath": "keyPath",
#				"type": "boolean",
#				"value": "YES"
#			}
#		]
#	},
#	"restorationIdentifier": 33,
#	"tag": 1220,
#	"id": "2Gd-j0-l11",
#	"clipsSubviews": "YES"
#}

#if hasattr(dic, 'tag'):
#print(dic['ttt'])
#a = [1,2,3,4]
#
#for b in a:
#	print(b)
#
#
#component = ViewComponent('rr',dic)
#rect = component.clsInfo['rect']
#print(component.generateInitializeCode())
#print(component.appendCode('rect',rect))
#print(component.appendCode('color',component.clsInfo['color']))
#str =  component.appendCode('rect', {'key':'frame','x':0,'y':0,'width':123,'height':3333})
#print(str)
#color =  component.appendCode('color', {
#	"red": 1,
#	"colorSpace": "calibratedRGB",
#	"green": 1,
#	"blue": 1,
#	"alpha": 1,
#	"customColorSpace": "sRGB",
#	"key": "backgroundColor"
#})
#print(color)
#content = component.getContentModel('scaleToFill')
#print(content)


#
#print(component.id)
#print(component.methodMap)
