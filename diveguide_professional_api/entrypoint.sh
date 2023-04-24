#!/bin/sh

# Get the IP address of the nginx container
NGINX_IP=$(getent hosts nginx | awk '{ print $1 }')

# Set the API_HOST environment variable
export NGINX_IP=$NGINX_IP

# Execute the given command
exec "$@"

python -m gunicorn diveguide_professional_api.wsgi:application --bind 0.0.0.0:8000

wait