import hvac
import os
from requests.exceptions import RequestException

# Set Vault Address and Port
vault_addr = 'https://localhost:8200'
role_id = os.getenv('VAULT-ROLE-ID')
role_pass = os.getenv('BASH2_VAULT-SECRET-ID')

# Creating a Vault Client
client = hvac.Client(url=vault_addr, verify=False)

# Log in to Vault using AppRole
def login_with_approle(role_id, secret_id):
    try:
        # Getting an authorization token
        response = client.auth.approle.login(role_id=role_id, secret_id=secret_id)
        if 'auth' in response:
            # Set the token for further operations
            client.token = response['auth']['client_token']
            print("Successful authorization in Vault.")
        else:
            print("Error when authorizing in Vault.")
    except (hvac.exceptions.VaultError, RequestException) as e:
        print(f"Error when authorizing in Vault: {str(e)}")

login_with_approle(role_id, role_pass)

# Getting authorization data
def read_secret(path):
    try:
        response = client.read(path)

        if 'data' in response:

            secret_data = response['data']['data']
            login = secret_data.get('login')
            password = secret_data.get('password')
            port = secret_data.get('port')
            host_list = secret_data.get('host', [])
            dbhost = host_list[0] if host_list else None

            if all((login, password, dbhost, port)):  # Check if all variables have non-empty values
                password = password.encode('unicode_escape').decode('utf-8')

                os.environ['LOGIN'] = login
                os.environ['PASSWORD'] = password
                os.environ['DBHOST'] = dbhost
                os.environ['PORT'] = str(port)

            else:
                print(f"Invalid secret format in path '{path}'")
        else:
            print(f"Error reading secret from Vault: {response}")
    except (hvac.exceptions.VaultError, RequestException) as e:
        print(f"Error reading secret from Vault: {str(e)}")

# Specify the secret path
read_secret('kv/your/path/$(Agent.JobName)/connections/$(database_name)')

# Write variables to env to use them in the next task
with open('.env', "w") as file:
    file.write(f"login={os.environ['LOGIN']}\n")
    file.write(f"password={os.environ['PASSWORD']}\n")
    file.write(f"dbhost={os.environ['DBHOST']}\n")
    file.write(f"port={os.environ['PORT']}\n")