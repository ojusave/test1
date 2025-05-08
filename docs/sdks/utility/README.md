# Utility
(*utility*)

## Overview

These utility endpoints allow you to check the results of submitted tasks and to manage your finetunes.

### Available Operations

* [get_result_v1_get_result_get](#get_result_v1_get_result_get) - Get Result
* [finetune_details_v1_finetune_details_get](#finetune_details_v1_finetune_details_get) - Finetune Details
* [my_finetunes_v1_my_finetunes_get](#my_finetunes_v1_my_finetunes_get) - My Finetunes
* [delete_finetune_v1_delete_finetune_post](#delete_finetune_v1_delete_finetune_post) - Delete Finetune

## get_result_v1_get_result_get

An endpoint for getting generation task result.

### Example Usage

```python
import os
from testdk import Testdk


with Testdk(
    server_url="https://api.example.com",
    api_key_header=os.getenv("TESTDK_API_KEY_HEADER", ""),
) as t_client:

    res = t_client.utility.get_result_v1_get_result_get(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ResultResponse](../../models/resultresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## finetune_details_v1_finetune_details_get

Get details about the training parameters and other metadata connected to a specific finetune_id that was created by the user.

### Example Usage

```python
import os
from testdk import Testdk


with Testdk(
    server_url="https://api.example.com",
    api_key_header=os.getenv("TESTDK_API_KEY_HEADER", ""),
) as t_client:

    res = t_client.utility.finetune_details_v1_finetune_details_get(finetune_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `finetune_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FinetuneDetailResponse](../../models/finetunedetailresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## my_finetunes_v1_my_finetunes_get

List all finetune_ids created by the user

### Example Usage

```python
import os
from testdk import Testdk


with Testdk(
    server_url="https://api.example.com",
    api_key_header=os.getenv("TESTDK_API_KEY_HEADER", ""),
) as t_client:

    res = t_client.utility.my_finetunes_v1_my_finetunes_get()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MyFinetunesResponse](../../models/myfinetunesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_finetune_v1_delete_finetune_post

Delete a finetune_id that was created by the user

### Example Usage

```python
import os
from testdk import Testdk


with Testdk(
    server_url="https://api.example.com",
    api_key_header=os.getenv("TESTDK_API_KEY_HEADER", ""),
) as t_client:

    res = t_client.utility.delete_finetune_v1_delete_finetune_post(finetune_id="my-finetune")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `finetune_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | ID of the fine-tuned model you want to delete.                      | my-finetune                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteFinetuneResponse](../../models/deletefinetuneresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |