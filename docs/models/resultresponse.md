# ResultResponse


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `id`                                                     | *str*                                                    | :heavy_check_mark:                                       | Task id for retrieving result                            |
| `status`                                                 | [models.StatusResponse](../models/statusresponse.md)     | :heavy_check_mark:                                       | N/A                                                      |
| `result`                                                 | *OptionalNullable[Any]*                                  | :heavy_minus_sign:                                       | N/A                                                      |
| `progress`                                               | *OptionalNullable[float]*                                | :heavy_minus_sign:                                       | N/A                                                      |
| `details`                                                | [OptionalNullable[models.Details]](../models/details.md) | :heavy_minus_sign:                                       | N/A                                                      |