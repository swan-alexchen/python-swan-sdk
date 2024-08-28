# PYTHON SWAN SDK <!-- omit in toc -->

[![Made by FilSwan](https://img.shields.io/badge/made%20by-FilSwan-green.svg)](https://www.filswan.com/) 
[![Chat on discord](https://img.shields.io/badge/join%20-discord-brightgreen.svg)](https://discord.com/invite/swanchain)

## Table Of Contents<!-- omit in toc -->

- [Quickstart](#quickstart)
  - [Installation](#installation)
  - [Get Orchestrator API Key](#get-orchestrator-api-key)
  - [Using Swan](#using-swan)
- [A Sample Tutorial](#a-sample-tutorial)
  - [Orchestrator](#orchestrator)
  - [Fetch available instance resources](#fetch-available-instance-resources)
  - [Create and deploy a task](#create-and-deploy-a-task)
  - [Check information of an existing task](#check-information-of-an-existing-task)
  - [Access application instances of an existing task](#access-application-instances-of-an-existing-task)
  - [Renew an existing task](#renew-an-existing-task)
  - [Terminate an existing task](#terminate-an-existing-task)
- [Code Examples](#code-examples)
  - [Chain Node Web Application](#chain-node-web-application)
    - [Create Task and Deploy Application Instances](#create-task-and-deploy-application-instances)
    - [Renew Application Instances](#renew-application-instances)
    - [View Running Application](#view-running-application)
- [License](#license)


## Quickstart

This guide details the steps needed to install or update the SWAN SDK for Python. The SDK is a comprehensive toolkit designed to facilitate seamless interactions with the SwanChain API.

### Installation

To use Swan SDK, you first need to install it and its dependencies. Before installing Swan SDK, install Python 3.8 or later and web3.py (>=6.15,<7.0).


Install the latest Swan SDK release via **pip**:

```bash
pip install swan-sdk
```

Or install via GitHub:

```bash
git clone https://github.com/swanchain/python-swan-sdk.git
cd python-swan-sdk
pip install .
```

### Get Orchestrator API Key

To use `swan-sdk`, an Orchestrator API key is required. 

Steps to get an API Key:

- Go to [Orchestrator Dashboard](https://orchestrator.swanchain.io/provider-status), switch network to Mainnet.
- Login through MetaMask.
- Click the user icon on the top right.
- Click 'Show API-Key' -> 'New API Key'
- Store your API Key safely, do not share with others.


### Using Swan

To use Swan SDK, you must first import it and indicate which service you're going to use:

```python
import swan

swan_orchestrator = swan.resource(api_key='<SWAN_API_KEY>', service_name='Orchestrator')
```

Now that you have an `Orchestrator` service, you can create and deploy instance applications as an Orchestrator task with the service.

```python
result = swan_orchestrator.create_task(
    app_repo_image='hello_world',
    wallet_address='<WALLET_ADDRESS>',
    private_key='<PRIVATE_KEY>',
)
task_uuid = result['task_uuid']
```

Then you can follow up task deployment information and the URL for running applications.

```python
# Get task deployment info
task_deployment_info = swan_orchestrator.get_deployment_info(task_uuid=task_uuid)
print(json.dumps(task_deployment_info, indent=2))

# Get application instances URL
app_urls = swan_orchestrator.get_real_url(task_uuid)
print(app_urls)
```

## A Sample Tutorial

### Orchestrator

Orchestrator allows you to create task to run application instances to the powerful distributed computing providers cloud.

### Fetch available instance resources

Before using Orchestrator to deploy task, it is necessary to know which instance resources are available. Through `get_instance_resources` you can get a list of available instance resources including their `region` information.

```python
import json
import swan

swan_orchestrator = swan.resource(api_key='<SWAN_API_KEY>', service_name='Orchestrator')

available_resources = swan_orchestrator.get_instance_resources()
print(json.dumps(available_resources, indent=2, ensure_ascii=False))
```

Sample output:

```
[
  {
    "hardware_id": 0,
    "instance_type": "C1ae.small",
    "description": "CPU only · 2 vCPU · 2 GiB",
    "type": "CPU",
    "region": [
      "North Carolina-US",
      "Quebec-CA"
    ],
    "price": "0.0",
    "status": "available"
  },
  //...
  {
    "hardware_id": 12,
    "instance_type": "G1ae.small",
    "description": "Nvidia 3080 · 4 vCPU · 8 GiB",
    "type": "GPU",
    "region": [
      "North Carolina-US",
      "Quebec-CA"
    ],
    "price": "10.0",
    "status": "available"
  },
  //...
]
```


### Create and deploy a task

To deploy a simple application with Swan SDK (see [Get Orchestrator API Key](#get-orchestrator-api-key)):

```python
import json
import swan

swan_orchestrator = swan.resource(api_key='<SWAN_API_KEY>', service_name='Orchestrator')

result = swan_orchestrator.create_task(
    app_repo_image='hello_world',
    wallet_address='<WALLET_ADDRESS>',
    private_key='<PRIVATE_KEY>',
)
task_uuid = result['task_uuid']
# Get task deployment info
task_deployment_info = swan_orchestrator.get_deployment_info(task_uuid=task_uuid)
print(json.dumps(task_deployment_info, indent=2))
```

It may take up to 5 minutes to get the deployment result:

```python
# Get application instances URL
app_urls = swan_orchestrator.get_real_url(task_uuid)
print(app_urls)
```
A sample output:

```
['https://krfswstf2g.anlu.loveismoney.fun', 'https://l2s5o476wf.cp162.bmysec.xyz', 'https://e2uw19k9uq.cp5.node.study']
```

It shows the this task has been deployed to 3 computing providers. If one of the app links is up, open it in the browser will show some simple information.

### Check information of an existing task

With Orchestrator, you can check information for an existing task to follow up or view task deployment.

```python
import json
import swan

swan_orchestrator = swan.resource(api_key='<SWAN_API_KEY>', service_name='Orchestrator')

# Get an existing task deployment info
task_deployment_info = swan_orchestrator.get_deployment_info(<task_uuid>)
print(json.dumps(task_deployment_info, indent=2))
```

### Access application instances of an existing task

With Orchestrator, you can easily get the deployed application instances for an existing task.

```python
import json
import swan

swan_orchestrator = swan.resource(api_key='<SWAN_API_KEY>', service_name='Orchestrator')

# Get application instances URL
app_urls = swan_orchestrator.get_real_url(<task_uuid>)
print(app_urls)
```

### Renew an existing task

If you have already submitted payment for the renewal of a task, you can use the `tx_hash` with `renew_task` to extend the task.

```python
import json
import swan

swan_orchestrator = swan.resource(api_key='<SWAN_API_KEY>', service_name='Orchestrator')

renew_result = swan_orchestrator.renew_task(
    task_uuid=<task_uuid>, 
    duration=3600, # Optional: default 3600 seconds (1 hour)
    auto_pay=True, 
    private_key=<PRIVATE_KEY>,
    instance_type=<instance_type> 
)

if renew_result and renew_result['status'] == 'success':
    print(f"successfully renewed {<task_uuid>}")
else:
    print(f"Unable to renew {<task_uuid>}")
```

### Terminate an existing task

You can also early terminate an existing task and its application instances. By terminating task, you will stop all the related running application instances and thus you will get refund of the remaining task duration.

```python
import json
import swan

swan_orchestrator = swan.resource(api_key='<SWAN_API_KEY>', service_name='Orchestrator')

# Terminate an existing task (and its application instances)
swan_orchestrator.terminate_task(<task_uuid>)
```

## Code Examples

### Chain Node Web Application

In this example, you will deploy a simple web application on the distributed computing provider network using Swan SDK. At the end of this example, you will have a Chain Node Frontend application running on the Swan network.

#### Create Task and Deploy Application Instances

```python
import swan
import json

api_key = '<your_api_key>'
wallet_address = '<WALLET_ADDRESS>'
private_key = '<PRIVATE_KEY>'

swan_orchestrator = swan.resource(
    api_key=api_key, 
    service_name='Orchestrator'
)

result = swan_orchestrator.create_task(
    repo_uri='https://github.com/swanchain/awesome-swanchain/tree/main/ChainNode',
    wallet_address=wallet_address,
    private_key=private_key,
    auto_pay=True,
    instance_type='C1ae.medium',
)

task_uuid = result['task_uuid']
instance_type = result['instance_type']
task_info = swan_orchestrator.get_deployment_info(task_uuid=task_uuid)
print(json.dumps(task_info, indent=2))

### get real url (if no url, please wait for a while, then check again)
result_url = swan_orchestrator.get_real_url(task_uuid)
print(result_url)
```

Sample URL output:

```
['https://0sz7wqp79q.dev2.crosschain.computer', 'https://grxfl2u0cu.cp.filezoo.com.cn', 'https://0ux851gqmz.pvm.nebulablock.com']
```

#### Renew Application Instances

```py
renew_result = swan_orchestrator.renew_task(
    task_uuid=task_uuid, 
    duration=3600,  # seconds
    auto_pay=True, 
    private_key=private_key,
    instance_type=instance_type
)
```

#### View Running Application

Screenshot:

![Chain Node App](./docs/res/app_running.png)

For more examples consult [examples](https://github.com/swanchain/python-swan-sdk/tree/main/examples).

## License

The PYTHON SWAN SDK is released under the **MIT** license, details of which can be found in the LICENSE file.
