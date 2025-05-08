<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import os
from testdk import Testdk

async def main():

    async with Testdk(
        server_url="https://api.example.com",
        api_key_header=os.getenv("TESTDK_API_KEY_HEADER", ""),
    ) as t_client:

        res = await t_client.utility.get_result_v1_get_result_get_async(id="<id>")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->