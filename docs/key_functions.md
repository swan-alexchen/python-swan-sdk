
## Key Functions Details <!-- omit in toc -->

- [`create_task` Function Details](#create_task-function-details)
- [`submit_payment` Details](#submit_payment-details)
- [`renew_payment` Details](#renew_payment-details)
- [`validate_payment` Details](#validate_payment-details)
- [`get_app_repo_image` Details](#get_app_repo_image-details)
- [`get_source_uri` Details](#get_source_uri-details)
- [`renew_task` Details](#renew_task-details)
- [`terminate_task` Details](#terminate_task-details)
- [`get_deployment_info` Details](#get_deployment_info-details)
- [`get_real_url` Details](#get_real_url-details)


### `create_task` Function Details

```python
swan.resource(api_key="<your_api_key>", service_name='Orchestrator').create_task(**kwargs)
```

Creates task on SWAN orchestrator.

**Request Syntax**:

```python
response = swan.resource(api_key="<your_api_key>", service_name='Orchestrator').create_task(
  wallet_address="string", 
  hardware_id=0, 
  region="string",
  duration=3600,
  app_repo_image="string",
  job_source_uri="string",
  repo_uri="string",
  repo_branch="string",
  repo_owner="string", 
  repo_name="string",
  auto_pay=None,
  private_key="string"
)

# To get task_uuid
response['id']
```
PARAMETERS:
- **wallet_address** (string) **[REQUIRED]** - The wallet address to be asscioated with newly create task
- **hardware_id** (integer) - id of cp/hardware configuration set. Defaults to 0 (Free tier).
- **region** (string) - region of hardware. Defaults to global.
- **duration** (integer) - duration of service runtime in seconds. Defaults to 3600 seconds (1 hour).
- **app_repo_image** (string) - The name of a demo space. If app_repo_image is used, auto_pay will be True by default. To learn more about auto_pay, check out auto_pay parameter. If you want turn auto_pay off, set auto_pay to False
- **job_source_uri** (string) - The job source URI to be deployed. If this is provided, app_repo_image and repo_uri are ignored. The repository must contain a dockerfile
- **repo_uri** (string) - The The URI of the repo to be deployed. The repository must contain a dockerfile \
**IMPORTANT** Only one of job_source_uri, app_repo_image, and repo_uri will be used at a time, but at least 1 must be provided. The priority is job_source_uri. If job_source_uri is not provided, app_repo_image will be used. If app_repo_image is not provided, then repo_uri will be used.
- **repo_branch** (string) - branch of the repo to be deployed.
- **repo_owner** (string) - owner of the repo to be deployed.
- **repo_name** (string) - name of the repo to be deployed.
- **auto_pay** (Boolean) - Automatically pays to deploy task if set to True. If True, private_key must be provided.
- **private_key** (string) - Wallet's private_key, only used if auto_pay is True
- **preferred_cp_list**: (list) - A list of preferred cp account addresses.


### `submit_payment` Details

```python
swan.resource(api_key="<your_api_key>", service_name='Orchestrator').submit_payment(**kwargs)
```

Submit a payment to SWAN contract for a task

**Request Syntax**:

submit_payment(self, task_uuid, private_key, duration = 3600, hardware_id = None)
```python
response = swan.resource(api_key="<your_api_key>", service_name='Orchestrator').submit_payment(
  task_uuid="string",
  private_key="string", 
  duration = 3600, 
  hardware_id = 0
)
```
PARAMETERS:
- **task_uuid** (string) **[REQUIRED]** - task_uuid of task being paid for
- **private_key** (string) **[REQUIRED]** - Wallet's private_key
- **duration** (integer) - duration of service runtime in seconds. Defaults to 3600 seconds (1 hour).
- **hardware_id** (integer) - id of cp/hardware configuration set. Defaults to 0 (Free tier).

### `renew_payment` Details

```python
swan.resource(api_key="<your_api_key>", service_name='Orchestrator').renew_payment(**kwargs)
```

Submit a payment to SWAN contract for a task

**Request Syntax**:

renew_payment(self, task_uuid, private_key, duration = 3600, hardware_id = None)
```python
response = swan.resource(api_key="<your_api_key>", service_name='Orchestrator').renew_payment(
  task_uuid="string",
  private_key="string", 
  duration = 3600, 
  hardware_id = 0
)
```
PARAMETERS:
- **task_uuid** (string) **[REQUIRED]** - task_uuid of task being paid for
- **private_key** (string) **[REQUIRED]** - Wallet's private_key
- **duration** (integer) - duration of service runtime in seconds. Defaults to 3600 seconds (1 hour).
- **hardware_id** (integer) - id of cp/hardware configuration set. Defaults to 0 (Free tier).


### `validate_payment` Details
```python
swan.resource(api_key="<your_api_key>", service_name='Orchestrator').validate_payment(**kwargs)
```

Deploy task on orchestrator with proof of payment

**Request Syntax**:
submit_payment(self, task_uuid, private_key, duration = 3600, hardware_id = None)
```python
response = swan.resource(api_key="<your_api_key>", service_name='Orchestrator').validate_payment(
  tx_hash="string",
  task_uuid="string"
)
```
PARAMETERS:
- **tx_hash** (string) **[REQUIRED]** - tx_hash/receipt of payment to SWAN contract for task with task_uuid 
- **task_uuid** (string) **[REQUIRED]** - task_uuid of task being extended


### `get_app_repo_image` Details

```python
swan.resource(api_key="<your_api_key>", service_name='Orchestrator').get_app_repo_image(**kwargs)
```

Finds repository image of pre-defined applications

**Request Syntax**:

```python
response = swan.resource(api_key="<your_api_key>", service_name='Orchestrator').get_app_repo_image(
  name="string"
)
```
PARAMETERS:
- **name** (string) - If name is provided, it will return the repository image of pre-defined applications. If name is not provided, returns all repository image of pre-defined applications.

### `get_source_uri` Details
```python
swan.resource(api_key="<your_api_key>", service_name='Orchestrator').get_source_uri(**kwargs)
```

Creates a returns a lagrange image of github repository.

```python
response = swan.resource(api_key="<your_api_key>", service_name='Orchestrator').get_source_uri(
  repo_uri="string",
  wallet_address="string", 
  hardware_id=0, 
  repo_branch="string",
  repo_owner="string", 
  repo_name="string",
)
```

PARAMETERS:
- **wallet_address** (string) **[REQUIRED]** - The wallet address to be asscioated with newly create task
- **hardware_id** (integer) **[REQUIRED]** - id of cp/hardware configuration set. Defaults to 0 (Free tier).
- **repo_uri** (string) **[REQUIRED]** - The The URI of the repo to be deployed.
- **repo_branch** (string) - branch of the repo to be deployed.
- **repo_owner** (string) - owner of the repo to be deployed.
- **repo_name** (string) - name of the repo to be deployed.


### `renew_task` Details
```python
swan.resource(api_key="<your_api_key>", service_name='Orchestrator').renew_task(**kwargs)
```

Renews a task

```python
response = swan.resource(api_key="<your_api_key>", service_name='Orchestrator').renew_task(
  task_uuid="string"
  duration=3600, 
  tx_hash="string", 
  auto_pay = False, 
  private_key="string", 
  hardware_id=0
)
```

PARAMETERS:
- **task_uuid** (string) **[REQUIRED]** - The task_uuid to be extended
- **duration** (integer) - id of cp/hardware configuration set. Defaults to 0 (Free tier).
- **tx_hash** (string) - The tx_hash of payment
- **auto_pay** (Boolean) - Automatically pays to extend task if set to True. If True, private_key must be provided.
**IMPORTANT** If auto_pay if False, tx_hash must be provided
- **private_key** (string) - Wallet's private_key, only used if auto_pay is True
- **hardware_id** (integer) - id of cp/hardware configuration set. Defaults to 0 (Free tier).


### `terminate_task` Details

```python
swan.resource(api_key="<your_api_key>", service_name='Orchestrator').terminate_task(**kwargs)
```

Terminates a task and gives a refund based on time remaining

**Request Syntax**:

```python
response = swan.resource(api_key="<your_api_key>", service_name='Orchestrator').terminate_task(
  task_uuid="string"
)
```
PARAMETERS:
- **task_uuid** (string) **[REQUIRED]** - The task_uuid to be terminates


### `get_deployment_info` Details

```python
swan.resource(api_key="<your_api_key>", service_name='Orchestrator').get_deployment_info(**kwargs)
```

Get deployment information about a task

**Request Syntax**:

```python
response = swan.resource(api_key="<your_api_key>", service_name='Orchestrator').get_deployment_info(
  task_uuid="string"
)
```
PARAMETERS:
- **task_uuid** (string) **[REQUIRED]** - The task_uuid to get status of.


### `get_real_url` Details

```python
swan.resource(api_key="<your_api_key>", service_name='Orchestrator').get_real_url(**kwargs)
```

Get real url of task

**Request Syntax**:

```python
response = swan.resource(api_key="<your_api_key>", service_name='Orchestrator').get_real_url(
  task_uuid="string"
)
```
PARAMETERS:
- **task_uuid** (string) **[REQUIRED]** - Get real url of task at task_uuid