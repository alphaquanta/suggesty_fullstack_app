#!/bin/bash
cd ..
cd ..
cd suggesty_backend_django
docker build  -t alphaquanta/suggestybackend:django .
cd ..
cd suggesty_frontend_angular
docker build  -t alphaquanta/suggestyfrontend:angular . 