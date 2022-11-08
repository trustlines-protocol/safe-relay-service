#!/bin/bash

set -euo pipefail

if [ "$1" = "develop" -o "$1" = "master" ]; then
    # If image does not exist, don't use cache
    docker pull trustlines/$DOCKERHUB_PROJECT:$1 && \
    docker build -t $DOCKERHUB_PROJECT -f docker/web/Dockerfile . --cache-from trustlines/$DOCKERHUB_PROJECT:$1 || \
    docker build -t $DOCKERHUB_PROJECT -f docker/web/Dockerfile .
else
    docker pull trustlines/$DOCKERHUB_PROJECT:staging && \
    docker build -t $DOCKERHUB_PROJECT -f docker/web/Dockerfile . --cache-from trustlines/$DOCKERHUB_PROJECT:staging || \
    docker build -t $DOCKERHUB_PROJECT -f docker/web/Dockerfile .
fi
docker tag $DOCKERHUB_PROJECT trustlines/$DOCKERHUB_PROJECT:$1
docker push trustlines/$DOCKERHUB_PROJECT:$1