# ./swan/common/constant.py

ORCHESTRATOR_API_TESTNET = "https://orchestrator-api.swanchain.io"
ORCHESTRATOR_API_MAINNET = "https://orchestrator-mainnet-api.swanchain.io"

# Swan API
SWAN_APIKEY_LOGIN = "/login_by_api_key"
DEPLOY_TASK = "/v2/task_deployment"
DEPLOYMENT_INFO = "/v2/task_deployment/"
GET_CP_CONFIG = "/cp/machines"
PROVIDER_PAYMENTS = "/provider/payments"
CREATE_TASK = "/v2/task_deployment"
TERMINATE_TASK = "/terminate_task"
CLAIM_REVIEW = "/claim_review"
RENEW_TASK = "/v2/extend_task"
PREMADE_IMAGE = "/util/example_code_mapping"
CONFIG_ORDER_STATUS = "/v2/config_order_status"

GET_CONTRACT_INFO = "/contract_info"
GET_ABI_VERSION = "/abi_version"
GET_SOURCE_URI = "/v2/get_source_uri"
GET_PRIVATE_TASK_TEMPORARY_NODE_URI = "/task/private_task/temporary_node_uri"
UPLOAD_PRIVATE_PROJECT_PACK = "/task/upload_private_project_pack"

# API Syntax
GET = "GET"
PUT = "PUT"
POST = "POST"
DELETE = "DELETE"

# Contract
PAYMENT_CONTRACT_ABI = "PaymentContract.json"
SWAN_TOKEN_ABI = "SwanToken.json"
CLIENT_CONTRACT_ABI = "ClientPayment.json"

# Other
CONTRACT_TIMEOUT = 300
MAX_DURATION = 1209600
ORCHESTRATOR_PUBLIC_ADDRESS_TESTNET = "0x29eD49c8E973696D07E7927f748F6E5Eacd5516D"
ORCHESTRATOR_PUBLIC_ADDRESS_MAINNET = "0x4B98086A20f3C19530AF32D21F85Bc6399358e20"