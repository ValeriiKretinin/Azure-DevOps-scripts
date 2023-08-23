# Azure DevOps Releases Scripts Documentation

This README provides an overview of the scripts designed to run in Azure DevOps releases. They include functionalities for logging into HashiCorp's Vault, reading secrets from the Vault, and executing migrations with `golang-migrate`.

## Table of Contents
- [Scripts](#scripts)
    - [approle.py](#approlepy)
    - [init_env.sh](#init_envsh)
    - [run_migrate.sh](#run_migratesh)
- [Sample Values](#sample-values)
- [Usage](#how-to-use)
- [Note](#note)

## Scripts

### approle.py
This script is responsible for:
- Setting up the Vault Client
- Logging into Vault using AppRole
- Reading secrets from Vault and setting environment variables

**Requirements:**
- `hvac`: A Python client for HashiCorp Vault
- Library variables `vault-role-id` and `vault-secret-id` should be set.

### init_env.sh
This script:
- Installs necessary Python packages
- Sets Vault secret ID as an output variable
- Prints the Vault role ID and the database name

### run_migrate.sh
This script:
- Reads variables from the `.env` file
- Downloads the latest version of `golang-migrate`
- Runs migrations using the `golang-migrate` app

## Sample Values
- **database_name**: `clickhouse`
- **golang-start-command**:

`./migrate -source file://your/path/to/sql/files/ -database "clickhouse://$dbhost:$port?username=$login&password=$password&database=your_db" up`


## How to use:
1. Ensure that required environment variables are set.
2. Add these scripts as pipeline steps with task group (`init_env.sh` -> `approle.py` -> `run_migrate.sh`)
3. Run the `init_env.sh` script to set up the Python environment and display necessary information.
4. Execute the `approle.py` script to log into Vault and fetch the required secrets.
5. Run the `run_migrate.sh` script to perform migrations.

## Note
It's crucial to ensure that the Azure DevOps library variables are properly set and enabled for your stages.

