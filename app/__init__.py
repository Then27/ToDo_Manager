# __init__.py
# ToDo Application
# Created by: Thenmozhi Singaravel

from flask import Flask, render_template
from flask import request
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

#Creating a list of tasks i.e list of objects of the class Tasks
taskList = []

#Taking the list and the status as parameters and returning the dictionary
def convertListToDict (list, stat):
	dict = {}
	for iterator_list in list:
		if iterator_list.status == stat:
			dict[len(dict) + 1 ] = iterator_list
	return dict

#Function to find a particular task in the taskList and returning the index of the task in the list	
def findTask (list, value):
	taskDict = {}
	slNo = 0
	indexNo = 0
	indexChoice = 0

#checking the serial number of the unfinished task with the id of the selected task obtained from webpage	
	for iterator_list in list:
		if iterator_list.status == 0:
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
		#Passing the description and the local date and time as parameters
		taskList.append(Tasks(desc, time.strftime("%c") ))
			
		#Converting the list of unfinished tasks into dictionary, taskDict
		taskDict = {}
		for iterator_list in taskList:
			if iterator_list.status == 0:
				taskDict[len(taskDict) + 1 ] = iterator_list

		#Converting the list of completed tasks into dictionary, complDict
		complDict = {}
		for iterator_list in taskList:
			if iterator_list.status == 1:
				complDict[len(complDict) + 1 ] = iterator_list
	
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
	
	#Getting URL values
	url_then = request.url
	valueToDelete = urlparse.parse_qs(urlparse.urlparse(url_then).query)['id'][0]

	indexNo = findTask (taskList, valueToDelete)
	del taskList[indexNo]
	
	taskDict = convertListToDict(taskList, 0)
	complDict = convertListToDict(taskList, 1)
		
	return render_template('createTable.html', taskDict= taskDict, complDict= complDict)
	
	
if __name__ == '__main__':
	app.run()
