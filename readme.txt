
 readme.txt
 ToDo Application
 Created by: Thenmozhi Singaravel 

The ToDo Manager has been built on Python and Flask,a lightweight Python web. 
The below installation steps are for Windows platform and are as per what has been done to create the application:

1. Installation of Python:
	a. Go to https://www.python.org/downloads/
	b. Click on "Download Python 2.7.9" and install the same.
	c. Add the path of the Python folder ("C:\Python27") to the environment variable, Path.	
	
2. Installation of Flask in the Virtualenv:
	a. Open Windows PowerShell
	b. Run the command "$ easy_install virtualenv" to install Virtualenv
	c. Setup the environment:
		i. Extract the todo zipped folder. 
		ii. $ cd todo
		iii. $ virtualenv env
		iv. $ env\scripts\activate
	d. Install Flask by running the command: "$ easy_install Flask"

For OS other than Windows, please see http://flask.readthedocs.org/en/0.3.1/installation/#windows-easy-install

3. Run the application:
	a. Run the command: "python .\app\__init__.py"
	b. Open the browser and go to "http://127.0.0.1:5000"
	
Go ahead and use the ToDo Manager to manage various tasks efficiently. 
