### SkipQ [![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://www.skipq.org/)
# Web Health Monitoring
### SkipQ Cohort 2021: Sprint One 

This project implements a periodic lambda function to check website status. Main focus of the project is to use aws cdk to create cloud infrastructure,And Put Health Matric on Cloud Watch resource provided by aws and Alarms User via Email When Health Matrics Cross Certain Thresh hold values, and also Stores Store Alarm Values to DataBase.


### Motivation
Infrastructure as code has quickly become a go-to process to automatically provision and manage cloud resources. With increasing sophistication, engineers and DevOps teams are codifying infrastructure for greater application flexibility and functionality, with a single-source language across an organization.

The AWS CDK, an open source software development framework to define cloud infrastructure, addresses these weaknesses. The AWS CDK supports popular programming languages, which developers can use to build, automate and manage infrastructure based on an imperative approach. Finally, developers can provision these commands through CloudFormation.

<<<<<<< HEAD
## Project Functional Requirements [![Generic badge](https://img.shields.io/badge/Implemented-Yes-<COLOR>.svg)](https://github.com/aliskipq/sprint1)
=======
## Project Functional Requirements [![Generic badge](https://img.shields.io/badge/Implemented-Yes-<COLOR>.svg)]
>>>>>>> 576a8470aea4c8f03c5cb0761dc717856aaf3469
* Project is Available on Cloud9 Environment.
* Project is implemented in python
* Project displays WebHealth matrics on CloudWatch
* Project Sets Alarms on Cloud Watch Upon Certain ThreshHold Values.
* Project Notifies Subscribed Users via email About those Alarms.
* Project Stores Alarm Data in Database

## Technologies Used
* python [![Generic badge](https://img.shields.io/badge/Python.org--<COLOR>.svg)](https://www.python.org/)
* aws cloud9 
* aws_cdk 
* aws lambda


## To run 
#### 1. login to IAM account  [![Generic badge](https://img.shields.io/badge/Login--<COLOR>.svg)](https://us-east-2.console.aws.amazon.com/console/home?region=us-east-2)
#### 2. Create a virtual environment in Cloud9
#### 3. Check python version

`python --version`

if it is not python 3

`vim ~/.bashrc`

add this line of in the end of bash file

`alias python="/usr/bin/python3"`

#### 4. Start a virtual environment

`source .venv/bin/activate`

#### 4. Install requirements

`pip install -r requirements.txt`

#### 4. Create Cloud Formation

`cdk synth`
#### 4. Deploy Cloud Formation

`cdk deploy`
