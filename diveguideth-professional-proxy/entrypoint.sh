#!/bin/sh

# Get the IP address of the nginx container
NGINX_IP=$(getent hosts nginx | awk '{ print $1 }')

# Set the API_HOST environment variable
export API_HOST=$NGINX_IP

# Execute the given command
exec "$@"

python /code/app/unary_server.py &
python /code/app/util/loop.py &

wait