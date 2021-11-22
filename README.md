
# Suggesty Web Application

# Introduction
Suggesty is an web application that gives a playlist of top 10 songs of random artist/band according to the given input from spotify.

After setup application can be accessed from
http://localhost 
If Setting Host approved(Windows Only with Automated Configuration)
http://suggesty.com

## Modules
Suggesty consists of two modules; Frontend and Backend applications.

In this repository, both of the modules bundled together to ease deployment process.
### Backend[^1].
Backend application developed with Django, a Python web framework.

### Frontend[^1].
Frontend application developed with Angular, a Typescript web framework

[^1]: Detailed package data related to the applications can be found their own ReadMe file that in the application's folder.

# Requirements

## Spotify API Key
    
Application uses Spotify API with Client Credentials Flow. In current project, there are default keys already located in the env files(test purposes) that might not valid in future.
To avoid problems, developer must create account and generate key for self from https://developer.spotify.com/ and change Backend .env and env.sh files values accordingly.



## Ports
To able to reach Dockerized applications or to locally hosted applications be able to run; following ports must be open and not in use. (with current configuration)
* 80
* 8000
* 4200

All the given packages and their versions are used packagaes in the development environment so it is known working configuration. Any version above or below from given might work but not tested.
## Without Docker
* Python 3.9.9
* pip 21.2.1
* Django 3.2.8 (via pip)
* django-cors-headers 3.10.0 (via pip)
* requests 2.25.1 (via pip)
* Node.js 16.13.0
* npm 8.1.1

     The npm manages packages related with Frontend. Those packages are not listed in this file, they can be found in package.json file inside Frontend applicaiton folder
* nginx 1.17.1

## With Docker
* Docker 20.10.7

## With Kubernetes
Docker is pre-requirment. Check [### With Docker] section of requirements.
*kubectl 1.21 (both for client and server)


# Setup and Run
This application includes Docker configuration files and compose file and also Kubernetes configuration file as well to be deployed via Docker seamlessly.
Despite it is not mandatory, it is recommended to use automated option to run application given below.

With current configuration application can be deployed for public use after proper port forwardings.

**Note that most of the automated scripts are not available for Linux and existing ones are not tested. But commands are valid.**

Existing Linux scripts uses 
        
        #!/bin/bash

Application can be deployed/run with one of the options below:

* Clone the repository into the desired folder.

## Option 1. Docker_Compose (With Docker)
This method uses docker compose configuration to run application on Docker. Images of applications will be built locally.

With Script file(Recommended):

* Open Terminal, navigate project's folder(root)
* Navigate to the tools folder, then navigate folder that fits with your OS
* Execute **Start_DockerCompose** script.

With typing commands into terminal:

* Open Terminal, navigate project's folder(root) and execute:
        
      docker-compose -f docker-compose-django-angular.yml up --build -d 

Docker will execute and run containers that described in the yml file.


In both cases Docker download, build and run the applications inside containers.

## Option 2. Start Kubernetes Menaged Containers (With Docker and Kubernetes:kubectl)
This option will use kubectl; Kubernetes tool to build, run and menage application containers.

With Script file(Recommended):
* Open Terminal, navigate project's folder(root)
* Navigate to the tools folder, then navigate folder that fits with your OS
* Execute **Start_k8s** script.
  
  **to terminate the deployment, execute **Stop_k8s** script that in the tools.**

With typing commands into terminal:
*Open Terminal, navigate project's folder(root) and execute:
        
        cd k8s
        kubectl apply -f fe-depl.yaml & kubectl apply -f be-depl.yaml
        kubectl apply -f loadbalancers.yaml
Termination of Kubernetes deployment: 

        kubectl delete deploy suggesty-backend suggesty-frontend
        kubectl delete service be-cluster-srv fe-cluster-srv fe-loadbalancer be-loadbalancer

In both cases, with given configuration; Kubernetes will deploy applications withing menaged containers.

## Option 3: Local Run : Development (Without Docker)
This option suits best for development purposes. When instructions below executed; application will be up and running on local host and native OS. 
**See : Requirements/Without Docker section.

* Open Terminal, navigate project's folder(root) and execute:
        
        cd suggesty_frontend_angular
        npm install (Only for first run)
        ng serve suggestyangular --configuration=development
        cd ..
        cd suggesty_backend_django
        pip install --upgrade pip & pip install -r ./requirements.txt  (Only for first run)
        py manage.py runserver 0.0.0.0:8000 ( py can be python in some cases)

After given instructions executed, Backend will run on **localhost:8000** and Frontend will run on **localhost:4200**


### Option 4: Local Run : Nginx Deployment (Without Docker)
Instead of using docker, application can run on local native OS , without containers.

Open Terminal, navigate project's folder(root) and execute following lines in order:

        cd suggesty_backend_django
        chmod +x ./env.sh
        ./env.sh
        pip install --upgrade pip
        pip install -r ./requirements.txt
        python manage.py run server 0.0.0.0:8000
Backend started and running on **localhost:8000** at this point.

Nginx assumed installed and already running for executing lines below

        cd ..
        cd suggesty_frontend_angular
        npm install
        ng build suggestyangular --configuration=development
        cp /dist/suggestyangular /usr/share/nginx/html

At this point, both Backend and Frontend applications should be up and running. 
By default; Nginx serve frontend from **localhost:80**

## Configure hostfile
This part only for Windows users. By following this section, application can be accessed from http://suggesty.com adress locally.

With Script file(Recommended):

**SCRIPT MUST BE EXECUTED WITH ADMIN PRIVILEGES**
* Open Terminal, navigate project's folder(root)
* Navigate to the tools folder, then navigate folder that fits with your OS(Windows in this case)
* Execute **SetHostFile** script.
  
This will alter your hosts file that located in System32/drivers/etc and make your OS resolve the domain adress as localhost.

# Test
Backend application files has tests included. In case of any problem with Backend or after any change on code; as a first check the test can be executed as:
Open Terminal navigate project folder(root) and execute:

        cd suggesty_backend_django
        python manage.py test

Results will printed on the terminal.

# Known Issues and TODOs

[ ] Better request management in Angular

[ ] Environment values passed to the containers yet after application's execution. Current default values are recovers the situation but to change another set of environment values not possibl e with automation in current case.

[ ] Reverse proxy and Kubernetes communication within clusters/pods not proper.

[ ] Another pattern or approach on SpotifyClient and HttpClient might be better. (Such as singleton, factory etc.)

[ ] All the Tool scripts should "translated" for linux as well.

[ ] API Keys and Secrets must be handled another way. Even for testing purposes.

[ ] Animations on Frontend would be nice.

