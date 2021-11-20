
# Suggesty Web Application

# Introduction
Suggesty is an web application that gives a playlist of top 10 songs of random artist/band according to the given input from spotify.

After setup application can be accessed from
http://localhost 
http://localhost:4200

### Modules
Suggesty consists of two modules; Frontend and Backend applications.

In this repository, both of the modules bundled together to ease deployment process.
#### Backend[^1].
Backend application developed with Django, a Python web framework.

#### Frontend[^1].
Frontend application developed with Angular, a Typescript web framework

[^1]: Detailed package data related to the applications can be found their own ReadMe file that in the application's folder.

# Requirements

### Spotify API Key
    
Application uses Spotify API with Client Credentials Flow. In current project, there are default keys already located in the env files(test purposes) that might not valid in future.
To avoid problems, developer must create account and generate key for self from https://developer.spotify.com/ and change Backend .env and env.sh files values accordingly.



### Ports
To able to reach Dockerized applications or to locally hosted applications be able to run; following ports must be open and not in use. (with current configuration)
* 80
* 8000
* 4200


All the given packages and their versions are used packagaes in the development environment so it is known working configuration. Any version above or below from given might work but not tested.
### Without Docker
* Python 3.9.9
* pip 21.2.1
* Django 3.2.8 (via pip)
* django-cors-headers 3.10.0 (via pip)
* requests 2.25.1 (via pip)
* npm 8.1.1

     The npm manages packages related with Frontend. Those packages are not listed in this file, they can be found in package.json file inside Frontend applicaiton folder
* nginx 1.17.1

### With Docker
* Docker 20.10.7
* npm 8.1.1

     The npm manages packages related with Frontend. Those packages are not listed in this file, they can be found in package.json file inside Frontend applicaiton folder

# Setup
This application includes Docker configuration files and compose file to be deployed via Docker seamlessly.
Despite it is not mandatory, it is recommended to use automated option to run application given below.

Current configuration of application is for local execution. For public access; Frontend envorinment values should be configured accordingly (BaseURL). 
Application can be deployed/run with one of the options below:

* Clone the repository into the desired folder.

#### Option 1: Full Automated (With Docker)
#### 1.1. First Run
This path can be used every time but if executed once and there is no change in files, to avoid build-time it is recommended to use option [1.2. Run]

* Open Terminal, navigate project's folder(root) and execute:

If Windows:

      StartUp_Windows.bat    

If Linux [Not Tested]: 
      
      StartUp_Linux.sh

The script file will installs relevant dependencies via NPM, build the Angular application, and execute Docker to run the applications with given configuration.

#### 1.2. Just Start Application 
If there is no change since last build or execuding Option 1.1, this option is more viable to avoid waiting for build time of frontend application.
* Open Terminal navigate project's folder(root) and execute:

        docker-compose -f .\docker-compose-django-angular.yml up --build -d

This option will execute Docker agaist the configuration files and will run the applications with given settings.

### Option 2: Manual (Without Docker)
Instead of using docker, application can be executed on local machine, without docker as well.
To achieve this: 

Open Terminal, navigate project's folder(root) and execute following lines in order:

        cd suggesty_backend_django
        chmod +x ./env.sh
        ./env.sh
        pip install --upgrade pip
        pip install -r ./requirements.txt
        python manage.py run server 0.0.0.0:8000
Backend started and running at this point.

Nginx assumed installed and already running for executing lines below

        cd ..
        cd suggesty_frontend_angular
        npm install
        ng build suggestyangular --configuration=development
        cp /dist/suggestyangular /usr/share/nginx/html

At this point, both Backend and Frontend applications should be up and running. 

# Test
Backend application files has tests included. In case of any problem with Backend or after any change on code; as a first check the test can be executed as:
Open Terminal navigate project folder(root) and execute:

                cd suggesty_backend_django
                python manage.py test

Results will printed on the terminal.
