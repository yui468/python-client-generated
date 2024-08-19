# swagger_client.DefaultApi

All URIs are relative to *https://pokeapi.co/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pokemon_by_id**](DefaultApi.md#get_pokemon_by_id) | **GET** /pokemon/{id} | Get a Pokémon by ID

# **get_pokemon_by_id**
> InlineResponse200 get_pokemon_by_id(id)

Get a Pokémon by ID

Fetches details of a specific Pokémon by its ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 56 # int | The ID of the Pokémon to fetch

try:
    # Get a Pokémon by ID
    api_response = api_instance.get_pokemon_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_pokemon_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the Pokémon to fetch | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

