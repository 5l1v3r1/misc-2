#coding:utf-8

import requests
import sys
import re
import options

class RMUsernameNotFound(Exception):
	def __init__(self, OutputCondition=None):
		self.OutputCondition = OutputCondition

#options.ServicePollers()
USER = options.PollersUser
LANG = options.PollersLang

def PollersPoint():
	'''
		This function will consist
		of seeing the points of the user
	'''
	ModelReqs = requests.get('https://www.root-me.org/'+USER).text
	ModelSpan = re.findall('(<span>[0-9]+<\/span>)', ModelReqs)

	# He looks for the right value in the source of the page
	# The condition it tests if the user is existing.

	if(type(ModelSpan) == list and len(ModelSpan) != 0):
		BertModel = ModelSpan[0].replace("<span>", "")
		BertModel = BertModel.replace("</span>", "")
		print BertModel
    
if __name__ == "__main__":
  PollersPoint()