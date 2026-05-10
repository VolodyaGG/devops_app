check_var() {
    local var_name=$1
    local default_value=$2

    if [ -z "${!var_name}" ]; then
        export "$var_name"="$default_value"
        echo "$var_name is absent. Using default value: $default_value"
    fi
}

check_var "DOCKER_LOGIN" "volodyagg"
check_var "PORT" "8000"
check_var "IMAGE_TAG" "production-636dd0c40f3e639aa61531e4d49436bed53d5d3f"
check_var "HOST" "cbr-app.local"

echo "Running helm deploy"

helm upgrade --install cbr-release ./k8s/cbr-app \
    --set image.repository="docker.io/${DOCKER_LOGIN}/client_server_app" \
    --set image.tag="${IMAGE_TAG}" \
    --set service.targetPort="${PORT}" \
    --set ingress.host="${HOST}" \
    --wait
