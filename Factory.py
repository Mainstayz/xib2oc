#!/usr/bin/python
# -*- coding: UTF-8 -*-

from ViewComponent import *
import json

with open('test.json', 'r') as f:
	data = json.load(f)


objects = data['document']['objects']

component = View('rr',objects)
print(component.clsInfo)
#rect = component.clsInfo['rect']
#print(component.generateInitializeCode())


#view = v('pite',data)
#
#print(view.name)
#print(view.clsInfo)
#			


