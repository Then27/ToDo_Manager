# __init__.py
# ToDo Application
# Created by: Thenmozhi Singaravel

from flask import Flask, render_template
from flask import request, redirect, url_for
import time
import urlparse
app = Flask(__name__)

class Tasks:

	#This function initialises new tasks with status as 0 or incomplete
	def __init__(self, desc, startDate):
		self.desc = desc
		self.initDate = startDate
		self.status = 0 
	
	#This function sets the status of tasks to 1 or complete 
	def editStatus(self, finDate):
		self.status = 1
		self.endDate = finDate

taskList = []

#Taking the list and the status as parameters and returning the dictionary
def convertListToDict (list, stat):
	dict = {}
	for i in list:
		if i.status == stat:
			dict[len(dict) + 1 ] = i
	return dict

#Function to find a particular task in the taskList and returning the index of the task in the list	
def findTask (list, value):
	taskDict = {}
	slNo = 0
	indexNo = 0
	indexChoice = 0
	
	for i in list:
		
		if i.status == 0:
			slNo+=1
			if (slNo == int(value)):
				slChoice = slNo
				indexChoice = indexNo
		indexNo+=1
		
	return indexChoice

@app.route('/')
def homepage():
	return render_template("index.html")
	 
# Takes care of the functionality of adding new tasks 
@app.route('/', methods=['POST'])
def addButton():
	taskDict = {}
	if request.method == 'POST':
		
		#Getting the user input from the request 
		desc = request.form['addTask'] 
		taskList.append(Tasks(desc, time.strftime("%c") ))
		
		
		#Converting the list of unfinished tasks into dictionary, taskDict
		taskDict = {}
		for i in taskList:
			if i.status == 0:
				taskDict[len(taskDict) + 1 ] = i

		#Converting the list of completed tasks into dictionary, complDict
		complDict = {}
		for i in taskList:
			if i.status == 1:
				complDict[len(complDict) + 1 ] = i
	
	return render_template('createTable.html', taskDict= taskDict, complDict= complDict)
    
# Changing the status of a particular task to completed
@app.route('/markCompleted')
def markAsCompleted():
	taskDict = {}
	complDict = {}

	#Getting URL values
	url_then = request.url
	valueToConvert = urlparse.parse_qs(urlparse.urlparse(url_then).query)['id'][0]
	
	indexNo = findTask (taskList, valueToConvert)
	taskList[indexNo].editStatus(time.strftime("%c"))
	
	taskDict = convertListToDict(taskList, 0)
	complDict = convertListToDict(taskList, 1)
	
	return render_template('createTable.html', taskDict= taskDict, complDict= complDict)

# Deleting a particular task	
@app.route('/deleteTask')
def deleteTask():
	taskDict = {}
	complDict = {}
	
	#getting url values
	url_then = request.url
	valueToDelete = urlparse.parse_qs(urlparse.urlparse(url_then).query)['id'][0]

	indexNo = findTask (taskList, valueToDelete)
	del taskList[indexNo]
	
	taskDict = convertListToDict(taskList, 0)
	complDict = convertListToDict(taskList, 1)
		
	return render_template('createTable.html', taskDict= taskDict, complDict= complDict)
	
	
if __name__ == '__main__':
	app.run()
