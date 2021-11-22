cd ../../k8s
ECHO "Starting: Frontend and Backend Deployment
kubectl apply -f fe-depl.yaml & kubectl apply -f be-depl.yaml
ECHO  "Starting: Loadbalancers Deployment 
kubectl apply -f loadbalancers.yaml








