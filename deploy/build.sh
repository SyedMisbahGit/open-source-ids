#!/bin/bash

# Build Docker image
docker build -t ghcr.io/SyedMisbahGit/open-source-ids:latest .

# Push to GitHub Container Registry
docker login ghcr.io -u ${{ secrets.GITHUB_USERNAME }} -p ${{ secrets.GITHUB_TOKEN }}
docker push ghcr.io/SyedMisbahGit/open-source-ids:latest

# Apply Kubernetes deployment
kubectl apply -f deploy/kubernetes/deployment.yaml
