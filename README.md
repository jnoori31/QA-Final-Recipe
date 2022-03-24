# QA-Final-Recipe
# Introduction to Project as set by QA:
This project is aimed to test three constituent parts as well as this README. 

 The first is predominantly written in python where I need to create a simple flask web application, that demonstrates CRUD functionality, and that integrates with a MySQL database. 

The second is to utilise containers, provided by cloud-based technologies such as Docker, Docker Swarm, virtual Machines from Microsoft Azure to host and deploy my application.

Finally, with webhooks and an orchestration tool, I demonstrate that my ongoing project can be continuously integrated and deployed (CI/CD) through a Jenkins pipeline that will automatically test, build and deploy my application. 

# Technical description of how the application works
My application is an online Cookbook that allows a user to log in, create and save recipes to their account. A user must have an account created and be logged in to see their recipes, update or delete them. If they choose they can also mark recipes as “cooked” “un-tired” in order to distinguish what they have not yet created as a meal.

The application will be running on a docker container on port 5000, communicating with a separate MySQL docker container on port 3306. A separate Nginx container runs a reverse proxy to the Flask app, effectively making the Flask application accessible on port 80 externally.
The use of Microsoft Azure, Docker, GitHub and Jenkins was a requirement from the specification for the final project by the course providers.
 
 
# Additional requirements
To complement what has already been mentioned in the brief below is more detail as to what was required for the project:
Jira board (track workflow process)
User Stories/points
Git and GitHub for my preference of a version control system
The use of both Git Branch and Smart Commits/(through Jira) 
A relational database, consisting of at least two tables that model a one-to-many  relationship
Clear documentation of the design phase, app architecture and risk assessment
A python-based functional application performing CRUD operations using Flask and MySQL.
Test for the application through Pytest, which will include automated tests for validation of the application
A front-end website created using Flask hosted on an Nginx container 
Code integrated into a Version Control System which will be built through a CI server and deployed to an Azure cloud-based virtual machine
CI/CD via Jenkins
Docker, Docker Swarm for configuration and orchestration for the use of separate VMs.
 
# Planning stage
In order to keep track of time as well understand what needs to be created, I had decided to plan in as much detail as possible what would be included in the application based on MOSCOW principles. Below is what is included in the planning:
project tracking board/ split into Epics
MoSCoW analysis (a way to prioritise what the MVP would be and create user stories) 
development board using Scrum
risk analysis
EDR diagram
 

# Epics
(please see images folder)
I had used the Backlog section to create a sprint, that was divided into an EPIC made up of user stories; that are numbered in order of priority for creation. 

Subsequently, for each user story, I created a git branch that was automatically named by JIRA so if I had additional contributors to this project they would be able to follow accurately what is has been done; especially if they are working remotely from me

# Development Board
(please see images folder)
And finally, a development board to view every story point in relation to each other through the development process. A good way to visualise the sprint. 

For this project I had created three stages:
To-Do- for tasks that have yet to be started
In Progress- for tasks that have had a branch created worked on but yet to be merged into the main repository on GitHub. These tasks are also smart committed using their unique identifier. 
Done- not only has the task been completed/ but in the particular context of CRUD I also tested the functionality to make sure it worked and therefore merged into main. 
 

 # Risk Assessment:
 (please see images for risk)
Below is a risk assessment carried out before the application was built to help mitigate any risks that could arise throughout the project. The assessment is crucial to know what those risks could be and also the steps are taken to reduce both impacts from occurring and understand better the overall time frame suited to the project. 


# EDR Diagram:
(Please see images) 
The Entity Diagram model for my project is a simple one-to-many relationship between two tables; the User and Recipes.


# CI/CD Infrastructure Pipeline illustrating cloud resources
(please see images)

I have attached an info graph that demonstrates the CI/CD pipeline. In short, the pipeline is triggered once a change in code has been made to the main branch and subsequently, via a webhook, Jenkins kicks into action in order to deploy the finished application on a cloud VM.

Jenkins is responsible for running a “job” with predefined build stages- my job has 4 build stages: Build (Python), 
Test(pytest and produce coverage report), 
Push(Docker) and finally;
 Deploy(application on host VM)
Once the app is considered stable and therefore customer-ready, it is then deployed to a separate VM (my swarm server) for deployment. This service is run using the Python-based HTTP web server which is designed around the concept of 'workers' who split the CPU resources of the VM equally. When users connect to the server, a worker is assigned to that connection with their dedicated resources, allowing the server to run faster for each user.
 
# Testing:
(please see images)
I used Pytest to run unit tests on the app. Jenkins produces console outputs (pictured below) that will inform the developer how many tests the code passed and which tests they failed. For my application, the testing for the CRUD functionality has been carried out.
Every time I push new code to GitHub, as I have used webhooks that connect to Jenkins, tests are automatically run in the CI/CD process run by Jenkins. 
Screenshots for test coverage reports show that coverage reached 81%:


# Future Improvements
Outside of any bugs- known and unknowns:
I would like to improve the application on the aesthetic end using REACT as a frontend Javascript Library.
From a functionality and automation perspective, there can be a major improvement. The user needs to manually type in the ingredients they have in order to create a recipe. This is time-consuming and cumbersome. If there was an option to select from a drop-down of pre-populated ingredients in the form when creating the recipe this would be ideal. 

In order for that to happen, I would need to create a many-to-many table comprised of Users, Recipes and additionally Ingredients. The recipe table would be connected by two foreign keys joining both tables. 
From a DevOps perspective, the creation of different pipelines for the different stages in Jenkins would be ideal to see and address any bugs- the more isolated the feedback could be the easier it is for the developer to allocate where things are going wrong.

Last but not least- Had I had the time for this project sprint I would like to improve the markdown so that I can add images as well as links using a markdown cheat sheet. 
 
Deployment Logs:
I have used one pipeline for all my stages- Set up, Test, Build, Push & Deploy. One of the best things about logs is again isolating bugs to each stage and tackling them when they arise. 

After 38 builds- I finally managed to deploy to Swarm and have a fully functioning application with all tests passed.
 
# Evidence of WebHook:
(please see images)
Automation of Build as soon as I push new code to Github- a trigger for Build is activated in Jenkins.
 

# Refactoring: 
I have attached a Link that demonstrates where the refactoring has occurred. In short, initially, I created my own environment variables by reading credentials from the Jenkins credentials manager. Subseutenitally I created a build.sh file that exported each variable for each step. However, in keeping with the spirit of DevOps and DRY code principles it would be quicker, less code and more efficient to use the Jenkins environment variables by default. So refactored to use jenkins.
 
Author Jnoori31, Version 1 March 2022
 
 

