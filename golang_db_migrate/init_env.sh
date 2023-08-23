# You need to set library variables in Azure DevOps and enable it for your stages

/usr/bin/python3 -m pip install --user --upgrade setuptools pip hvac
echo "##vso[task.setvariable variable=vault-secret-id;isOutput=true]$(vault-secret-id)"
echo $(vault-role-id)
echo $(database_name)