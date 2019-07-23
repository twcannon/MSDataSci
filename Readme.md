# MSDataSci
A repo for the ETL processes that the analysts will use for in-taking and processing client data

## Getting Started 

### Prerequisites

- [Git](https://git-scm.com/)
- [Python 3](https://www.python.org/)
    - Pip (should be an option to include in the python download)
    - virtual env: ```pip install virtualenv```
    - unix virtual env wrapper: ```pip install virtualenvwrapper```
    - windows virtual env wrapper: ```pip install virtualenvwrapper-win```

#### Python Environment Setup

- ```mkvirtualenv MSDataSci```
    - the comand prompt prefix should now be changed to somthing like ```(MSDataSci) C:\path```
    - if this is not the case, try ```workon MSDataSci```
- ```cd``` to the main MSDataSci directory - normally ```C:\eSite\MSDataSci```
- set this environment to the project directory with ```setvirtualenvproject``` or ```setprojectdir .``` for windows
- type ```deactivate``` to exit the virtual environment
- you can now type ```workon MSDataSci``` from anywhere and it will open the virtual environment and move you to the top eSiteTEL directory
- Here is a general [setup tutorial](http://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/) that gives a little more detail about the process above. Although we only really care about the virtual environment sections.

Install the python dependencies with ```pip install -r config\requirements.txt```

## Developing

Develop environment will be local, There is no production
When developing in python, use ```workon MSDataSci``` to activate the vurtual environment.



### Deployment

Pull from git master branch.