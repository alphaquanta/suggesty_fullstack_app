#!/bin/bash
kubectl delete deploy suggesty-backend suggesty-frontend & kubectl delete service be-cluster-srv fe-cluster-srv fe-loadbalancer be-loadbalancer