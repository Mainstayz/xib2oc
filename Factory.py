#!/usr/bin/python
# -*- coding: UTF-8 -*-

from ViewComponent import *
import json

with open('test.json', 'r') as f:
	data = json.load(f)


objects = data['document']['objects']['view']

component = View('rr',objects)

for key in objects:
	value = component.appendCode(key, objects[key]) 
	print(key,value)






#一个简单的递归
u = '2222_'

def jigui(s):
	if len(s) == 0:
		return ''
	return s + jigui(s[1:])

u = jigui(u)

print(u)	


#print(component.clsInfo)
#rect = component.clsInfo['rect']
#print(component.generateInitializeCode())


#view = v('pite',data)
#
#print(view.name)
#print(view.clsInfo)
#			


