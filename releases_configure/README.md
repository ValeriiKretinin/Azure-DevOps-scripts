# Update Approvers Script

This script facilitates the process of updating approvers across all releases within a specified Azure DevOps project.

## Overview

The script automates the following operations:

- Fetching all release pipelines based on their `definitionId`.
- Iterating over the pipelines and updating the approvers for a specified environment.
- Applying the updated definition to the release pipelines.

## Prerequisites

- Python3
- `requests` Python library

## Configuration

Before running the script, you need to set the following configuration variables at the beginning of the script:

- `organization`: Name of your Azure DevOps organization.
- `project`: Name of your Azure DevOps project.
- `pat`: Your Personal Access Token for authentication.
- `displayName`: Display name of the new approver.
- `uniqueName`: Unique name of the new approver.
- `imageUrl`: (Optional) Image URL of the new approver.
- `descriptor`: (Optional) Descriptor for the new approver.

Also, specify the environment name you are interested in by updating the `env['name']` check within the script.

## Usage

1. Ensure you have Python3 and the `requests` library installed.
2. Configure the script as described above.
3. Execute the script.

```bash
python3 update_approvers.py
```

## Warning
Use this script with caution, as it will modify the release definitions in your Azure DevOps project. Always backup your configuration and test in a safe environment first.