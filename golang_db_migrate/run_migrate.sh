# Get variables from .env file
set -o allexport
source .env
set +o allexport


# Get latest version of golang-migrate app
curl -L https://github.com/golang-migrate/migrate/releases/latest/download/migrate.linux-amd64.tar.gz | tar xvz

# Run golang-migrate
$(golang-start-command)
