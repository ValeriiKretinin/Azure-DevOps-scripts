import requests
import json
import base64


# Настройка
organization = 'your_org'
project = "your_project"
pat = 'your_token'
displayName = 'display_name_of_new_approver'
uniqueName = 'uniqueName_of_new_approver'
imageUrl = 'image_url_optional'
descriptor = 'optional'

base_url = f"https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/releases?"
encoded_pat = base64.b64encode(f":{pat}".encode()).decode("utf-8")
headers = {
    "Authorization": f"Basic {encoded_pat}",
    "Content-Type": "application/json"
}

# Получите все release pipelines по definitionId
response = requests.get(f"{base_url}/definitions?api-version=7.0", headers=headers)
pipelines_ids = [pipeline['releaseDefinition']['id'] for pipeline in response.json()['value']]

for pipeline_id in pipelines_ids:
    try:
        response = requests.get(f"https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/definitions/{pipeline_id}?api-version=7.0", headers=headers)
        pipeline_detail = response.json()

        # Обновление approvers для шага p011
        for env in pipeline_detail['environments']:
            if env['name'] == "your_env_name":
                for approval in env['preDeployApprovals']['approvals']:
                    approval['approver'] = {
                        "displayName": displayName,
                        "uniqueName": uniqueName,
                        "imageUrl": imageUrl,
                        "descriptor": descriptor
                    }
    except Exception as e:
        print(f"Error processing pipeline ID {pipeline_id}. Error: {e}")

    # 3. Обновите определение релиза с новым JSON
response = requests.put(f"https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/definitions/{pipeline_id}?api-version=7.0", headers=headers, data=json.dumps(pipeline_detail))
print("Server Response:", response.text)
