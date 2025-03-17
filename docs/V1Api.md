# signals_api_client.V1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_file**](V1Api.md#upload_file) | **POST** /signals/v1/public/signals/{uuid}/attachments/ | 
[**v1_my_signals_history_list**](V1Api.md#v1_my_signals_history_list) | **GET** /signals/v1/my/signals/{uuid}/history/ | 
[**v1_my_signals_list**](V1Api.md#v1_my_signals_list) | **GET** /signals/v1/my/signals/ | 
[**v1_my_signals_me_retrieve**](V1Api.md#v1_my_signals_me_retrieve) | **GET** /signals/v1/my/signals/me | 
[**v1_my_signals_request_auth_token_create**](V1Api.md#v1_my_signals_request_auth_token_create) | **POST** /signals/v1/my/signals/request-auth-token | 
[**v1_my_signals_retrieve**](V1Api.md#v1_my_signals_retrieve) | **GET** /signals/v1/my/signals/{uuid}/ | 
[**v1_private_areas_geography_retrieve**](V1Api.md#v1_private_areas_geography_retrieve) | **GET** /signals/v1/private/areas/geography/ | 
[**v1_private_areas_list**](V1Api.md#v1_private_areas_list) | **GET** /signals/v1/private/areas/ | 
[**v1_private_autocomplete_usernames_list**](V1Api.md#v1_private_autocomplete_usernames_list) | **GET** /signals/v1/private/autocomplete/usernames/ | 
[**v1_private_categories_history_list**](V1Api.md#v1_private_categories_history_list) | **GET** /signals/v1/private/categories/{id}/history/ | 
[**v1_private_categories_icon_destroy**](V1Api.md#v1_private_categories_icon_destroy) | **DELETE** /signals/v1/private/categories/{category_id}/icon | 
[**v1_private_categories_icon_partial_update**](V1Api.md#v1_private_categories_icon_partial_update) | **PATCH** /signals/v1/private/categories/{category_id}/icon | 
[**v1_private_categories_icon_retrieve**](V1Api.md#v1_private_categories_icon_retrieve) | **GET** /signals/v1/private/categories/{category_id}/icon | 
[**v1_private_categories_icon_update**](V1Api.md#v1_private_categories_icon_update) | **PUT** /signals/v1/private/categories/{category_id}/icon | 
[**v1_private_categories_list**](V1Api.md#v1_private_categories_list) | **GET** /signals/v1/private/categories/ | 
[**v1_private_categories_partial_update**](V1Api.md#v1_private_categories_partial_update) | **PATCH** /signals/v1/private/categories/{id}/ | 
[**v1_private_categories_retrieve**](V1Api.md#v1_private_categories_retrieve) | **GET** /signals/v1/private/categories/{id}/ | 
[**v1_private_categories_update**](V1Api.md#v1_private_categories_update) | **PUT** /signals/v1/private/categories/{id}/ | 
[**v1_private_csv_retrieve**](V1Api.md#v1_private_csv_retrieve) | **GET** /signals/v1/private/csv/ | 
[**v1_private_departments_create**](V1Api.md#v1_private_departments_create) | **POST** /signals/v1/private/departments/ | 
[**v1_private_departments_list**](V1Api.md#v1_private_departments_list) | **GET** /signals/v1/private/departments/ | 
[**v1_private_departments_partial_update**](V1Api.md#v1_private_departments_partial_update) | **PATCH** /signals/v1/private/departments/{id}/ | 
[**v1_private_departments_retrieve**](V1Api.md#v1_private_departments_retrieve) | **GET** /signals/v1/private/departments/{id}/ | 
[**v1_private_departments_update**](V1Api.md#v1_private_departments_update) | **PUT** /signals/v1/private/departments/{id}/ | 
[**v1_private_expressions_context_retrieve**](V1Api.md#v1_private_expressions_context_retrieve) | **GET** /signals/v1/private/expressions/context/ | 
[**v1_private_expressions_create**](V1Api.md#v1_private_expressions_create) | **POST** /signals/v1/private/expressions/ | 
[**v1_private_expressions_destroy**](V1Api.md#v1_private_expressions_destroy) | **DELETE** /signals/v1/private/expressions/{id}/ | 
[**v1_private_expressions_list**](V1Api.md#v1_private_expressions_list) | **GET** /signals/v1/private/expressions/ | 
[**v1_private_expressions_partial_update**](V1Api.md#v1_private_expressions_partial_update) | **PATCH** /signals/v1/private/expressions/{id}/ | 
[**v1_private_expressions_retrieve**](V1Api.md#v1_private_expressions_retrieve) | **GET** /signals/v1/private/expressions/{id}/ | 
[**v1_private_expressions_update**](V1Api.md#v1_private_expressions_update) | **PUT** /signals/v1/private/expressions/{id}/ | 
[**v1_private_expressions_validate_retrieve**](V1Api.md#v1_private_expressions_validate_retrieve) | **GET** /signals/v1/private/expressions/validate/ | 
[**v1_private_me_filters_create**](V1Api.md#v1_private_me_filters_create) | **POST** /signals/v1/private/me/filters/ | 
[**v1_private_me_filters_destroy**](V1Api.md#v1_private_me_filters_destroy) | **DELETE** /signals/v1/private/me/filters/{id}/ | 
[**v1_private_me_filters_list**](V1Api.md#v1_private_me_filters_list) | **GET** /signals/v1/private/me/filters/ | 
[**v1_private_me_filters_partial_update**](V1Api.md#v1_private_me_filters_partial_update) | **PATCH** /signals/v1/private/me/filters/{id}/ | 
[**v1_private_me_filters_retrieve**](V1Api.md#v1_private_me_filters_retrieve) | **GET** /signals/v1/private/me/filters/{id}/ | 
[**v1_private_me_filters_update**](V1Api.md#v1_private_me_filters_update) | **PUT** /signals/v1/private/me/filters/{id}/ | 
[**v1_private_me_retrieve**](V1Api.md#v1_private_me_retrieve) | **GET** /signals/v1/private/me/ | 
[**v1_private_permissions_list**](V1Api.md#v1_private_permissions_list) | **GET** /signals/v1/private/permissions/ | 
[**v1_private_permissions_retrieve**](V1Api.md#v1_private_permissions_retrieve) | **GET** /signals/v1/private/permissions/{id}/ | 
[**v1_private_reports_signals_open_list**](V1Api.md#v1_private_reports_signals_open_list) | **GET** /signals/v1/private/reports/signals/open/ | 
[**v1_private_reports_signals_reopen_requested_list**](V1Api.md#v1_private_reports_signals_reopen_requested_list) | **GET** /signals/v1/private/reports/signals/reopen-requested/ | 
[**v1_private_roles_create**](V1Api.md#v1_private_roles_create) | **POST** /signals/v1/private/roles/ | 
[**v1_private_roles_destroy**](V1Api.md#v1_private_roles_destroy) | **DELETE** /signals/v1/private/roles/{id}/ | 
[**v1_private_roles_list**](V1Api.md#v1_private_roles_list) | **GET** /signals/v1/private/roles/ | 
[**v1_private_roles_partial_update**](V1Api.md#v1_private_roles_partial_update) | **PATCH** /signals/v1/private/roles/{id}/ | 
[**v1_private_roles_retrieve**](V1Api.md#v1_private_roles_retrieve) | **GET** /signals/v1/private/roles/{id}/ | 
[**v1_private_roles_update**](V1Api.md#v1_private_roles_update) | **PUT** /signals/v1/private/roles/{id}/ | 
[**v1_private_search_list**](V1Api.md#v1_private_search_list) | **GET** /signals/v1/private/search/ | 
[**v1_private_signals_attachments_create**](V1Api.md#v1_private_signals_attachments_create) | **POST** /signals/v1/private/signals/{parent_lookup__signal__pk}/attachments/ | 
[**v1_private_signals_attachments_destroy**](V1Api.md#v1_private_signals_attachments_destroy) | **DELETE** /signals/v1/private/signals/{parent_lookup__signal__pk}/attachments/{id}/ | 
[**v1_private_signals_attachments_list**](V1Api.md#v1_private_signals_attachments_list) | **GET** /signals/v1/private/signals/{parent_lookup__signal__pk}/attachments/ | 
[**v1_private_signals_attachments_partial_update**](V1Api.md#v1_private_signals_attachments_partial_update) | **PATCH** /signals/v1/private/signals/{parent_lookup__signal__pk}/attachments/{id}/ | 
[**v1_private_signals_attachments_retrieve**](V1Api.md#v1_private_signals_attachments_retrieve) | **GET** /signals/v1/private/signals/{parent_lookup__signal__pk}/attachments/{id}/ | 
[**v1_private_signals_attachments_update**](V1Api.md#v1_private_signals_attachments_update) | **PUT** /signals/v1/private/signals/{parent_lookup__signal__pk}/attachments/{id}/ | 
[**v1_private_signals_category_removed_list**](V1Api.md#v1_private_signals_category_removed_list) | **GET** /signals/v1/private/signals/category/removed/ | 
[**v1_private_signals_children_list**](V1Api.md#v1_private_signals_children_list) | **GET** /signals/v1/private/signals/{id}/children/ | 
[**v1_private_signals_context_near_geography_retrieve**](V1Api.md#v1_private_signals_context_near_geography_retrieve) | **GET** /signals/v1/private/signals/{id}/context/near/geography/ | 
[**v1_private_signals_context_reporter_list**](V1Api.md#v1_private_signals_context_reporter_list) | **GET** /signals/v1/private/signals/{id}/context/reporter/ | 
[**v1_private_signals_context_retrieve**](V1Api.md#v1_private_signals_context_retrieve) | **GET** /signals/v1/private/signals/{id}/context/ | 
[**v1_private_signals_create**](V1Api.md#v1_private_signals_create) | **POST** /signals/v1/private/signals/ | 
[**v1_private_signals_email_preview_create**](V1Api.md#v1_private_signals_email_preview_create) | **POST** /signals/v1/private/signals/{id}/email/preview/ | 
[**v1_private_signals_geography_retrieve**](V1Api.md#v1_private_signals_geography_retrieve) | **GET** /signals/v1/private/signals/geography/ | 
[**v1_private_signals_history_list**](V1Api.md#v1_private_signals_history_list) | **GET** /signals/v1/private/signals/{id}/history/ | 
[**v1_private_signals_list**](V1Api.md#v1_private_signals_list) | **GET** /signals/v1/private/signals/ | 
[**v1_private_signals_partial_update**](V1Api.md#v1_private_signals_partial_update) | **PATCH** /signals/v1/private/signals/{id}/ | 
[**v1_private_signals_pdf_retrieve**](V1Api.md#v1_private_signals_pdf_retrieve) | **GET** /signals/v1/private/signals/{id}/pdf/ | 
[**v1_private_signals_promoted_parent_list**](V1Api.md#v1_private_signals_promoted_parent_list) | **GET** /signals/v1/private/signals/promoted/parent/ | 
[**v1_private_signals_reporters_cancel_create**](V1Api.md#v1_private_signals_reporters_cancel_create) | **POST** /signals/v1/private/signals/{parent_lookup__signal_id}/reporters/{id}/cancel/ | 
[**v1_private_signals_reporters_create**](V1Api.md#v1_private_signals_reporters_create) | **POST** /signals/v1/private/signals/{parent_lookup__signal_id}/reporters/ | 
[**v1_private_signals_reporters_list**](V1Api.md#v1_private_signals_reporters_list) | **GET** /signals/v1/private/signals/{parent_lookup__signal_id}/reporters/ | 
[**v1_private_signals_retrieve**](V1Api.md#v1_private_signals_retrieve) | **GET** /signals/v1/private/signals/{id}/ | 
[**v1_private_sources_list**](V1Api.md#v1_private_sources_list) | **GET** /signals/v1/private/sources/ | 
[**v1_private_sources_retrieve**](V1Api.md#v1_private_sources_retrieve) | **GET** /signals/v1/private/sources/{id}/ | 
[**v1_private_status_messages_category_create**](V1Api.md#v1_private_status_messages_category_create) | **POST** /signals/v1/private/status-messages/category/{category_id}/ | 
[**v1_private_status_messages_create**](V1Api.md#v1_private_status_messages_create) | **POST** /signals/v1/private/status-messages/ | 
[**v1_private_status_messages_destroy**](V1Api.md#v1_private_status_messages_destroy) | **DELETE** /signals/v1/private/status-messages/{id}/ | 
[**v1_private_status_messages_list**](V1Api.md#v1_private_status_messages_list) | **GET** /signals/v1/private/status-messages/ | 
[**v1_private_status_messages_partial_update**](V1Api.md#v1_private_status_messages_partial_update) | **PATCH** /signals/v1/private/status-messages/{id}/ | 
[**v1_private_status_messages_retrieve**](V1Api.md#v1_private_status_messages_retrieve) | **GET** /signals/v1/private/status-messages/{id}/ | 
[**v1_private_status_messages_search_retrieve**](V1Api.md#v1_private_status_messages_search_retrieve) | **GET** /signals/v1/private/status-messages/search/ | 
[**v1_private_status_messages_update**](V1Api.md#v1_private_status_messages_update) | **PUT** /signals/v1/private/status-messages/{id}/ | 
[**v1_private_terms_categories_status_message_templates_create**](V1Api.md#v1_private_terms_categories_status_message_templates_create) | **POST** /signals/v1/private/terms/categories/{slug}/status-message-templates/ | 
[**v1_private_terms_categories_status_message_templates_retrieve**](V1Api.md#v1_private_terms_categories_status_message_templates_retrieve) | **GET** /signals/v1/private/terms/categories/{slug}/status-message-templates/ | 
[**v1_private_terms_categories_sub_categories_status_message_templates_create**](V1Api.md#v1_private_terms_categories_sub_categories_status_message_templates_create) | **POST** /signals/v1/private/terms/categories/{slug}/sub_categories/{sub_slug}/status-message-templates/ | 
[**v1_private_terms_categories_sub_categories_status_message_templates_retrieve**](V1Api.md#v1_private_terms_categories_sub_categories_status_message_templates_retrieve) | **GET** /signals/v1/private/terms/categories/{slug}/sub_categories/{sub_slug}/status-message-templates/ | 
[**v1_private_translations_create**](V1Api.md#v1_private_translations_create) | **POST** /signals/v1/private/translations/ | 
[**v1_private_users_create**](V1Api.md#v1_private_users_create) | **POST** /signals/v1/private/users/ | 
[**v1_private_users_history_retrieve**](V1Api.md#v1_private_users_history_retrieve) | **GET** /signals/v1/private/users/{id}/history/ | 
[**v1_private_users_list**](V1Api.md#v1_private_users_list) | **GET** /signals/v1/private/users/ | 
[**v1_private_users_partial_update**](V1Api.md#v1_private_users_partial_update) | **PATCH** /signals/v1/private/users/{id}/ | 
[**v1_private_users_retrieve**](V1Api.md#v1_private_users_retrieve) | **GET** /signals/v1/private/users/{id}/ | 
[**v1_public_areas_geography_retrieve**](V1Api.md#v1_public_areas_geography_retrieve) | **GET** /signals/v1/public/areas/geography/ | 
[**v1_public_areas_list**](V1Api.md#v1_public_areas_list) | **GET** /signals/v1/public/areas/ | 
[**v1_public_feedback_forms_partial_update**](V1Api.md#v1_public_feedback_forms_partial_update) | **PATCH** /signals/v1/public/feedback/forms/{token}/ | 
[**v1_public_feedback_forms_retrieve**](V1Api.md#v1_public_feedback_forms_retrieve) | **GET** /signals/v1/public/feedback/forms/{token}/ | 
[**v1_public_feedback_forms_update**](V1Api.md#v1_public_feedback_forms_update) | **PUT** /signals/v1/public/feedback/forms/{token}/ | 
[**v1_public_feedback_standard_answers_list**](V1Api.md#v1_public_feedback_standard_answers_list) | **GET** /signals/v1/public/feedback/standard_answers/ | 
[**v1_public_questions_list**](V1Api.md#v1_public_questions_list) | **GET** /signals/v1/public/questions/ | 
[**v1_public_reporter_verify_email_create**](V1Api.md#v1_public_reporter_verify_email_create) | **POST** /signals/v1/public/reporter/verify-email | 
[**v1_public_signals_create**](V1Api.md#v1_public_signals_create) | **POST** /signals/v1/public/signals/ | 
[**v1_public_signals_geography_retrieve**](V1Api.md#v1_public_signals_geography_retrieve) | **GET** /signals/v1/public/signals/geography/ | 
[**v1_public_signals_retrieve**](V1Api.md#v1_public_signals_retrieve) | **GET** /signals/v1/public/signals/{uuid}/ | 
[**v1_public_terms_categories_list**](V1Api.md#v1_public_terms_categories_list) | **GET** /signals/v1/public/terms/categories/ | 
[**v1_public_terms_categories_retrieve**](V1Api.md#v1_public_terms_categories_retrieve) | **GET** /signals/v1/public/terms/categories/{slug}/ | 
[**v1_public_terms_categories_sub_categories_list**](V1Api.md#v1_public_terms_categories_sub_categories_list) | **GET** /signals/v1/public/terms/categories/{parent_lookup_parent__slug}/sub_categories/ | 
[**v1_public_terms_categories_sub_categories_retrieve**](V1Api.md#v1_public_terms_categories_sub_categories_retrieve) | **GET** /signals/v1/public/terms/categories/{parent_lookup_parent__slug}/sub_categories/{slug}/ | 
[**v1_public_translations_json_retrieve**](V1Api.md#v1_public_translations_json_retrieve) | **GET** /signals/v1/public/translations.json | 
[**v1_relations_retrieve**](V1Api.md#v1_relations_retrieve) | **GET** /signals/v1/relations/ | 


# **upload_file**
> PublicSignalAttachment upload_file(uuid, display, links, location, is_image, created_at, file)

### Example


```python
import signals_api_client
from signals_api_client.models.public_signal_attachment import PublicSignalAttachment
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    uuid = 'uuid_example' # str | 
    display = 'display_example' # str | 
    links = 'links_example' # str | 
    location = 'location_example' # str | 
    is_image = True # bool | 
    created_at = '2013-10-20T19:20:30+01:00' # datetime | 
    file = 'file_example' # str | 

    try:
        api_response = await api_instance.upload_file(uuid, display, links, location, is_image, created_at, file)
        print("The response of V1Api->upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->upload_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **display** | **str**|  | 
 **links** | **str**|  | 
 **location** | **str**|  | 
 **is_image** | **bool**|  | 
 **created_at** | **datetime**|  | 
 **file** | **str**|  | 

### Return type

[**PublicSignalAttachment**](PublicSignalAttachment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_my_signals_history_list**
> List[HistoryLogHal] v1_my_signals_history_list(uuid, what=what)

Retrieve the history of a Signal for the currently logged in Reporter

### Example

* Api Key Authentication (tokenAuth):

```python
import signals_api_client
from signals_api_client.models.history_log_hal import HistoryLogHal
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    uuid = 'uuid_example' # str | 
    what = 'what_example' # str | Filters a specific \"action\" (optional)

    try:
        api_response = await api_instance.v1_my_signals_history_list(uuid, what=what)
        print("The response of V1Api->v1_my_signals_history_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_my_signals_history_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **what** | **str**| Filters a specific \&quot;action\&quot; | [optional] 

### Return type

[**List[HistoryLogHal]**](HistoryLogHal.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_my_signals_list**
> PaginatedSignalListList v1_my_signals_list(ordering=ordering, page=page, page_size=page_size, status=status)

List all Signals, created in the past year, for the currently logged in Reporter

### Example

* Api Key Authentication (tokenAuth):

```python
import signals_api_client
from signals_api_client.models.paginated_signal_list_list import PaginatedSignalListList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    status = 'status_example' # str | Melding status  * `open` - Open * `closed` - Closed (optional)

    try:
        api_response = await api_instance.v1_my_signals_list(ordering=ordering, page=page, page_size=page_size, status=status)
        print("The response of V1Api->v1_my_signals_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_my_signals_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **status** | **str**| Melding status  * &#x60;open&#x60; - Open * &#x60;closed&#x60; - Closed | [optional] 

### Return type

[**PaginatedSignalListList**](PaginatedSignalListList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_my_signals_me_retrieve**
> MySignalsLoggedInReporter v1_my_signals_me_retrieve()

Detail for the currently logged in Reporter

### Example

* Api Key Authentication (tokenAuth):

```python
import signals_api_client
from signals_api_client.models.my_signals_logged_in_reporter import MySignalsLoggedInReporter
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)

    try:
        api_response = await api_instance.v1_my_signals_me_retrieve()
        print("The response of V1Api->v1_my_signals_me_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_my_signals_me_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MySignalsLoggedInReporter**](MySignalsLoggedInReporter.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_my_signals_request_auth_token_create**
> MySignalsToken v1_my_signals_request_auth_token_create(my_signals_token)

Always return an HTTP 200 response without body

### Example


```python
import signals_api_client
from signals_api_client.models.my_signals_token import MySignalsToken
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    my_signals_token = signals_api_client.MySignalsToken() # MySignalsToken | 

    try:
        api_response = await api_instance.v1_my_signals_request_auth_token_create(my_signals_token)
        print("The response of V1Api->v1_my_signals_request_auth_token_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_my_signals_request_auth_token_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **my_signals_token** | [**MySignalsToken**](MySignalsToken.md)|  | 

### Return type

[**MySignalsToken**](MySignalsToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_my_signals_retrieve**
> SignalDetail v1_my_signals_retrieve(uuid)

Retrieve a Signal for the currently logged in Reporter

### Example

* Api Key Authentication (tokenAuth):

```python
import signals_api_client
from signals_api_client.models.signal_detail import SignalDetail
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    uuid = 'uuid_example' # str | 

    try:
        api_response = await api_instance.v1_my_signals_retrieve(uuid)
        print("The response of V1Api->v1_my_signals_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_my_signals_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**SignalDetail**](SignalDetail.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_areas_geography_retrieve**
> AreaGeo v1_private_areas_geography_retrieve(geopage=geopage, page_size=page_size)

Retrieve a paginated list of area geographies.

Returns a paginated response with area geographies.

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.area_geo import AreaGeo
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    geopage = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = await api_instance.v1_private_areas_geography_retrieve(geopage=geopage, page_size=page_size)
        print("The response of V1Api->v1_private_areas_geography_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_areas_geography_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geopage** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**AreaGeo**](AreaGeo.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_areas_list**
> PaginatedAreaList v1_private_areas_list(code=code, ordering=ordering, page=page, page_size=page_size, type_code=type_code)

A ViewSet for retrieving areas.

Inherits from PublicAreasViewSet and adds authentication.

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.paginated_area_list import PaginatedAreaList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    code = ['code_example'] # List[str] |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    type_code = ['type_code_example'] # List[str] |  (optional)

    try:
        api_response = await api_instance.v1_private_areas_list(code=code, ordering=ordering, page=page, page_size=page_size, type_code=type_code)
        print("The response of V1Api->v1_private_areas_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_areas_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | [**List[str]**](str.md)|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **type_code** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**PaginatedAreaList**](PaginatedAreaList.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_autocomplete_usernames_list**
> PaginatedUserNameListList v1_private_autocomplete_usernames_list(is_active=is_active, page=page, page_size=page_size, profile_department_code=profile_department_code, username=username)

Returns a list of usernames filtered by username
The username filter needs to provide at least 3 characters or more

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.paginated_user_name_list_list import PaginatedUserNameListList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    is_active = True # bool |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    profile_department_code = ['profile_department_code_example'] # List[str] |  (optional)
    username = 'username_example' # str |  (optional)

    try:
        api_response = await api_instance.v1_private_autocomplete_usernames_list(is_active=is_active, page=page, page_size=page_size, profile_department_code=profile_department_code, username=username)
        print("The response of V1Api->v1_private_autocomplete_usernames_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_autocomplete_usernames_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_active** | **bool**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **profile_department_code** | [**List[str]**](str.md)|  | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**PaginatedUserNameListList**](PaginatedUserNameListList.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_categories_history_list**
> List[PrivateCategoryHistoryHal] v1_private_categories_history_list(id)

The change log of the selected Category instance
This is read-only!

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.private_category_history_hal import PrivateCategoryHistoryHal
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this category.

    try:
        api_response = await api_instance.v1_private_categories_history_list(id)
        print("The response of V1Api->v1_private_categories_history_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_categories_history_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this category. | 

### Return type

[**List[PrivateCategoryHistoryHal]**](PrivateCategoryHistoryHal.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_categories_icon_destroy**
> v1_private_categories_icon_destroy(category_id)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    category_id = 'category_id_example' # str | 

    try:
        await api_instance.v1_private_categories_icon_destroy(category_id)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_categories_icon_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_categories_icon_partial_update**
> PrivateCategoryIcon v1_private_categories_icon_partial_update(category_id, icon=icon)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.private_category_icon import PrivateCategoryIcon
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    category_id = 'category_id_example' # str | 
    icon = 'icon_example' # str |  (optional)

    try:
        api_response = await api_instance.v1_private_categories_icon_partial_update(category_id, icon=icon)
        print("The response of V1Api->v1_private_categories_icon_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_categories_icon_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 
 **icon** | **str**|  | [optional] 

### Return type

[**PrivateCategoryIcon**](PrivateCategoryIcon.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_categories_icon_retrieve**
> PrivateCategoryIcon v1_private_categories_icon_retrieve(category_id)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.private_category_icon import PrivateCategoryIcon
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    category_id = 'category_id_example' # str | 

    try:
        api_response = await api_instance.v1_private_categories_icon_retrieve(category_id)
        print("The response of V1Api->v1_private_categories_icon_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_categories_icon_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 

### Return type

[**PrivateCategoryIcon**](PrivateCategoryIcon.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_categories_icon_update**
> PrivateCategoryIcon v1_private_categories_icon_update(category_id, icon)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.private_category_icon import PrivateCategoryIcon
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    category_id = 'category_id_example' # str | 
    icon = 'icon_example' # str | 

    try:
        api_response = await api_instance.v1_private_categories_icon_update(category_id, icon)
        print("The response of V1Api->v1_private_categories_icon_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_categories_icon_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 
 **icon** | **str**|  | 

### Return type

[**PrivateCategoryIcon**](PrivateCategoryIcon.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_categories_list**
> PaginatedPrivateCategoryList v1_private_categories_list(page=page, page_size=page_size)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.paginated_private_category_list import PaginatedPrivateCategoryList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = await api_instance.v1_private_categories_list(page=page, page_size=page_size)
        print("The response of V1Api->v1_private_categories_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_categories_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedPrivateCategoryList**](PaginatedPrivateCategoryList.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_categories_partial_update**
> PrivateCategory v1_private_categories_partial_update(id, patched_private_category=patched_private_category)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.patched_private_category import PatchedPrivateCategory
from signals_api_client.models.private_category import PrivateCategory
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this category.
    patched_private_category = signals_api_client.PatchedPrivateCategory() # PatchedPrivateCategory |  (optional)

    try:
        api_response = await api_instance.v1_private_categories_partial_update(id, patched_private_category=patched_private_category)
        print("The response of V1Api->v1_private_categories_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_categories_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this category. | 
 **patched_private_category** | [**PatchedPrivateCategory**](PatchedPrivateCategory.md)|  | [optional] 

### Return type

[**PrivateCategory**](PrivateCategory.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_categories_retrieve**
> PrivateCategory v1_private_categories_retrieve(id)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.private_category import PrivateCategory
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this category.

    try:
        api_response = await api_instance.v1_private_categories_retrieve(id)
        print("The response of V1Api->v1_private_categories_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_categories_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this category. | 

### Return type

[**PrivateCategory**](PrivateCategory.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_categories_update**
> PrivateCategory v1_private_categories_update(id, private_category)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.private_category import PrivateCategory
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this category.
    private_category = signals_api_client.PrivateCategory() # PrivateCategory | 

    try:
        api_response = await api_instance.v1_private_categories_update(id, private_category)
        print("The response of V1Api->v1_private_categories_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_categories_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this category. | 
 **private_category** | [**PrivateCategory**](PrivateCategory.md)|  | 

### Return type

[**PrivateCategory**](PrivateCategory.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_csv_retrieve**
> v1_private_csv_retrieve()

Private ViewSet to retrieve generated csv files
https://stackoverflow.com/a/51936269

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)

    try:
        await api_instance.v1_private_csv_retrieve()
    except Exception as e:
        print("Exception when calling V1Api->v1_private_csv_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_departments_create**
> PrivateDepartmentSerializerDetail v1_private_departments_create(private_department_serializer_list)

Create a department

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.private_department_serializer_detail import PrivateDepartmentSerializerDetail
from signals_api_client.models.private_department_serializer_list import PrivateDepartmentSerializerList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    private_department_serializer_list = signals_api_client.PrivateDepartmentSerializerList() # PrivateDepartmentSerializerList | 

    try:
        api_response = await api_instance.v1_private_departments_create(private_department_serializer_list)
        print("The response of V1Api->v1_private_departments_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_departments_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **private_department_serializer_list** | [**PrivateDepartmentSerializerList**](PrivateDepartmentSerializerList.md)|  | 

### Return type

[**PrivateDepartmentSerializerDetail**](PrivateDepartmentSerializerDetail.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_departments_list**
> PaginatedPrivateDepartmentSerializerListList v1_private_departments_list(can_direct=can_direct, page=page, page_size=page_size)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.paginated_private_department_serializer_list_list import PaginatedPrivateDepartmentSerializerListList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    can_direct = True # bool |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = await api_instance.v1_private_departments_list(can_direct=can_direct, page=page, page_size=page_size)
        print("The response of V1Api->v1_private_departments_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_departments_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **can_direct** | **bool**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedPrivateDepartmentSerializerListList**](PaginatedPrivateDepartmentSerializerListList.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_departments_partial_update**
> PrivateDepartmentSerializerDetail v1_private_departments_partial_update(id, patched_private_department_serializer_list=patched_private_department_serializer_list)

Partial update a department

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.patched_private_department_serializer_list import PatchedPrivateDepartmentSerializerList
from signals_api_client.models.private_department_serializer_detail import PrivateDepartmentSerializerDetail
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this department.
    patched_private_department_serializer_list = signals_api_client.PatchedPrivateDepartmentSerializerList() # PatchedPrivateDepartmentSerializerList |  (optional)

    try:
        api_response = await api_instance.v1_private_departments_partial_update(id, patched_private_department_serializer_list=patched_private_department_serializer_list)
        print("The response of V1Api->v1_private_departments_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_departments_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this department. | 
 **patched_private_department_serializer_list** | [**PatchedPrivateDepartmentSerializerList**](PatchedPrivateDepartmentSerializerList.md)|  | [optional] 

### Return type

[**PrivateDepartmentSerializerDetail**](PrivateDepartmentSerializerDetail.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_departments_retrieve**
> PrivateDepartmentSerializerDetail v1_private_departments_retrieve(id)

Retrieve a department

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.private_department_serializer_detail import PrivateDepartmentSerializerDetail
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this department.

    try:
        api_response = await api_instance.v1_private_departments_retrieve(id)
        print("The response of V1Api->v1_private_departments_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_departments_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this department. | 

### Return type

[**PrivateDepartmentSerializerDetail**](PrivateDepartmentSerializerDetail.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_departments_update**
> PrivateDepartmentSerializerDetail v1_private_departments_update(id, private_department_serializer_list)

Update a department

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.private_department_serializer_detail import PrivateDepartmentSerializerDetail
from signals_api_client.models.private_department_serializer_list import PrivateDepartmentSerializerList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this department.
    private_department_serializer_list = signals_api_client.PrivateDepartmentSerializerList() # PrivateDepartmentSerializerList | 

    try:
        api_response = await api_instance.v1_private_departments_update(id, private_department_serializer_list)
        print("The response of V1Api->v1_private_departments_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_departments_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this department. | 
 **private_department_serializer_list** | [**PrivateDepartmentSerializerList**](PrivateDepartmentSerializerList.md)|  | 

### Return type

[**PrivateDepartmentSerializerDetail**](PrivateDepartmentSerializerDetail.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_expressions_context_retrieve**
> Expression v1_private_expressions_context_retrieve(type)

Returns available identifers for expression type

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.expression import Expression
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    type = 'type_example' # str | The expression type

    try:
        api_response = await api_instance.v1_private_expressions_context_retrieve(type)
        print("The response of V1Api->v1_private_expressions_context_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_expressions_context_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The expression type | 

### Return type

[**Expression**](Expression.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_expressions_create**
> Expression v1_private_expressions_create(expression)

private ViewSet to display/process expressions in the database

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.expression import Expression
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    expression = signals_api_client.Expression() # Expression | 

    try:
        api_response = await api_instance.v1_private_expressions_create(expression)
        print("The response of V1Api->v1_private_expressions_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_expressions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expression** | [**Expression**](Expression.md)|  | 

### Return type

[**Expression**](Expression.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_expressions_destroy**
> v1_private_expressions_destroy(id)

private ViewSet to display/process expressions in the database

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this Expression.

    try:
        await api_instance.v1_private_expressions_destroy(id)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_expressions_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Expression. | 

### Return type

void (empty response body)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_expressions_list**
> PaginatedExpressionList v1_private_expressions_list(name=name, page=page, page_size=page_size, type_name=type_name)

private ViewSet to display/process expressions in the database

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.paginated_expression_list import PaginatedExpressionList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    name = 'name_example' # str |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    type_name = ['type_name_example'] # List[str] |  (optional)

    try:
        api_response = await api_instance.v1_private_expressions_list(name=name, page=page, page_size=page_size, type_name=type_name)
        print("The response of V1Api->v1_private_expressions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_expressions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **type_name** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**PaginatedExpressionList**](PaginatedExpressionList.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_expressions_partial_update**
> Expression v1_private_expressions_partial_update(id, patched_expression=patched_expression)

private ViewSet to display/process expressions in the database

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.expression import Expression
from signals_api_client.models.patched_expression import PatchedExpression
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this Expression.
    patched_expression = signals_api_client.PatchedExpression() # PatchedExpression |  (optional)

    try:
        api_response = await api_instance.v1_private_expressions_partial_update(id, patched_expression=patched_expression)
        print("The response of V1Api->v1_private_expressions_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_expressions_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Expression. | 
 **patched_expression** | [**PatchedExpression**](PatchedExpression.md)|  | [optional] 

### Return type

[**Expression**](Expression.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_expressions_retrieve**
> Expression v1_private_expressions_retrieve(id)

private ViewSet to display/process expressions in the database

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.expression import Expression
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this Expression.

    try:
        api_response = await api_instance.v1_private_expressions_retrieve(id)
        print("The response of V1Api->v1_private_expressions_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_expressions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Expression. | 

### Return type

[**Expression**](Expression.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_expressions_update**
> Expression v1_private_expressions_update(id, expression)

private ViewSet to display/process expressions in the database

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.expression import Expression
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this Expression.
    expression = signals_api_client.Expression() # Expression | 

    try:
        api_response = await api_instance.v1_private_expressions_update(id, expression)
        print("The response of V1Api->v1_private_expressions_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_expressions_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Expression. | 
 **expression** | [**Expression**](Expression.md)|  | 

### Return type

[**Expression**](Expression.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_expressions_validate_retrieve**
> Expression v1_private_expressions_validate_retrieve(expression, type)

Validate expression for a certain expression type

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.expression import Expression
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    expression = 'expression_example' # str | The expression to validate
    type = 'type_example' # str | The expression type

    try:
        api_response = await api_instance.v1_private_expressions_validate_retrieve(expression, type)
        print("The response of V1Api->v1_private_expressions_validate_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_expressions_validate_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expression** | **str**| The expression to validate | 
 **type** | **str**| The expression type | 

### Return type

[**Expression**](Expression.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_me_filters_create**
> StoredSignalFilter v1_private_me_filters_create(stored_signal_filter)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.stored_signal_filter import StoredSignalFilter
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    stored_signal_filter = signals_api_client.StoredSignalFilter() # StoredSignalFilter | 

    try:
        api_response = await api_instance.v1_private_me_filters_create(stored_signal_filter)
        print("The response of V1Api->v1_private_me_filters_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_me_filters_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stored_signal_filter** | [**StoredSignalFilter**](StoredSignalFilter.md)|  | 

### Return type

[**StoredSignalFilter**](StoredSignalFilter.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_me_filters_destroy**
> v1_private_me_filters_destroy(id)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this stored signal filter.

    try:
        await api_instance.v1_private_me_filters_destroy(id)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_me_filters_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this stored signal filter. | 

### Return type

void (empty response body)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**500** |  |  -  |
**400** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_me_filters_list**
> PaginatedStoredSignalFilterList v1_private_me_filters_list(page=page, page_size=page_size)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.paginated_stored_signal_filter_list import PaginatedStoredSignalFilterList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = await api_instance.v1_private_me_filters_list(page=page, page_size=page_size)
        print("The response of V1Api->v1_private_me_filters_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_me_filters_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedStoredSignalFilterList**](PaginatedStoredSignalFilterList.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_me_filters_partial_update**
> StoredSignalFilter v1_private_me_filters_partial_update(id, patched_stored_signal_filter=patched_stored_signal_filter)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.patched_stored_signal_filter import PatchedStoredSignalFilter
from signals_api_client.models.stored_signal_filter import StoredSignalFilter
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this stored signal filter.
    patched_stored_signal_filter = signals_api_client.PatchedStoredSignalFilter() # PatchedStoredSignalFilter |  (optional)

    try:
        api_response = await api_instance.v1_private_me_filters_partial_update(id, patched_stored_signal_filter=patched_stored_signal_filter)
        print("The response of V1Api->v1_private_me_filters_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_me_filters_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this stored signal filter. | 
 **patched_stored_signal_filter** | [**PatchedStoredSignalFilter**](PatchedStoredSignalFilter.md)|  | [optional] 

### Return type

[**StoredSignalFilter**](StoredSignalFilter.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_me_filters_retrieve**
> StoredSignalFilter v1_private_me_filters_retrieve(id)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.stored_signal_filter import StoredSignalFilter
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this stored signal filter.

    try:
        api_response = await api_instance.v1_private_me_filters_retrieve(id)
        print("The response of V1Api->v1_private_me_filters_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_me_filters_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this stored signal filter. | 

### Return type

[**StoredSignalFilter**](StoredSignalFilter.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_me_filters_update**
> StoredSignalFilter v1_private_me_filters_update(id, stored_signal_filter)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.stored_signal_filter import StoredSignalFilter
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this stored signal filter.
    stored_signal_filter = signals_api_client.StoredSignalFilter() # StoredSignalFilter | 

    try:
        api_response = await api_instance.v1_private_me_filters_update(id, stored_signal_filter)
        print("The response of V1Api->v1_private_me_filters_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_me_filters_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this stored signal filter. | 
 **stored_signal_filter** | [**StoredSignalFilter**](StoredSignalFilter.md)|  | 

### Return type

[**StoredSignalFilter**](StoredSignalFilter.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_me_retrieve**
> UserDetailHAL v1_private_me_retrieve()

Detail for the currently logged in user

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.user_detail_hal import UserDetailHAL
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)

    try:
        api_response = await api_instance.v1_private_me_retrieve()
        print("The response of V1Api->v1_private_me_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_me_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserDetailHAL**](UserDetailHAL.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_permissions_list**
> PaginatedPermissionList v1_private_permissions_list(page=page, page_size=page_size)

List all permissions

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.paginated_permission_list import PaginatedPermissionList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = await api_instance.v1_private_permissions_list(page=page, page_size=page_size)
        print("The response of V1Api->v1_private_permissions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_permissions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedPermissionList**](PaginatedPermissionList.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_permissions_retrieve**
> Permission v1_private_permissions_retrieve(id)

Retrieve a permission

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.permission import Permission
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this recht.

    try:
        api_response = await api_instance.v1_private_permissions_retrieve(id)
        print("The response of V1Api->v1_private_permissions_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_permissions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this recht. | 

### Return type

[**Permission**](Permission.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_reports_signals_open_list**
> List[ReportSignalsPerCategory] v1_private_reports_signals_open_list(end=end, start=start)

Count all Signals that have an "open" state and return a summary per Category.

It is also possible to filter on a period using the "start" and "end" filters (query params)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.report_signals_per_category import ReportSignalsPerCategory
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = await api_instance.v1_private_reports_signals_open_list(end=end, start=start)
        print("The response of V1Api->v1_private_reports_signals_open_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_reports_signals_open_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end** | **datetime**|  | [optional] 
 **start** | **datetime**|  | [optional] 

### Return type

[**List[ReportSignalsPerCategory]**](ReportSignalsPerCategory.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_reports_signals_reopen_requested_list**
> List[ReportSignalsPerCategory] v1_private_reports_signals_reopen_requested_list(end=end, start=start)

Count all Signals that are in the "reopen requested" state and return a summary per Category.

It is also possible to filter on the period the state change was made using the "start" and
"end" filters (query params)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.report_signals_per_category import ReportSignalsPerCategory
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = await api_instance.v1_private_reports_signals_reopen_requested_list(end=end, start=start)
        print("The response of V1Api->v1_private_reports_signals_reopen_requested_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_reports_signals_reopen_requested_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end** | **datetime**|  | [optional] 
 **start** | **datetime**|  | [optional] 

### Return type

[**List[ReportSignalsPerCategory]**](ReportSignalsPerCategory.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_roles_create**
> Role v1_private_roles_create(role)

Create a role

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.role import Role
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    role = signals_api_client.Role() # Role | 

    try:
        api_response = await api_instance.v1_private_roles_create(role)
        print("The response of V1Api->v1_private_roles_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_roles_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | [**Role**](Role.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_roles_destroy**
> v1_private_roles_destroy(id)

Delete a role

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this groep.

    try:
        await api_instance.v1_private_roles_destroy(id)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_roles_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this groep. | 

### Return type

void (empty response body)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_roles_list**
> PaginatedRoleList v1_private_roles_list(page=page, page_size=page_size)

List all roles

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.paginated_role_list import PaginatedRoleList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = await api_instance.v1_private_roles_list(page=page, page_size=page_size)
        print("The response of V1Api->v1_private_roles_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_roles_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedRoleList**](PaginatedRoleList.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_roles_partial_update**
> Role v1_private_roles_partial_update(id, patched_role=patched_role)

Update a role

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.patched_role import PatchedRole
from signals_api_client.models.role import Role
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this groep.
    patched_role = signals_api_client.PatchedRole() # PatchedRole |  (optional)

    try:
        api_response = await api_instance.v1_private_roles_partial_update(id, patched_role=patched_role)
        print("The response of V1Api->v1_private_roles_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_roles_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this groep. | 
 **patched_role** | [**PatchedRole**](PatchedRole.md)|  | [optional] 

### Return type

[**Role**](Role.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_roles_retrieve**
> Role v1_private_roles_retrieve(id)

Retrieve a role

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.role import Role
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this groep.

    try:
        api_response = await api_instance.v1_private_roles_retrieve(id)
        print("The response of V1Api->v1_private_roles_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_roles_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this groep. | 

### Return type

[**Role**](Role.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_roles_update**
> Role v1_private_roles_update(id, role)

Update a role

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.role import Role
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this groep.
    role = signals_api_client.Role() # Role | 

    try:
        api_response = await api_instance.v1_private_roles_update(id, role)
        print("The response of V1Api->v1_private_roles_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_roles_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this groep. | 
 **role** | [**Role**](Role.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_search_list**
> PaginatedPrivateSignalSerializerListList v1_private_search_list(ordering=ordering, page=page, page_size=page_size, q=q)

Add custom serializer for detail view

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.paginated_private_signal_serializer_list_list import PaginatedPrivateSignalSerializerListList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    ordering = 'ordering_example' # str | Order the results by a specific field. Currently the only valid options are \"created_at\" and \"-created_at\". (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    q = 'q_example' # str | The search term. (optional)

    try:
        api_response = await api_instance.v1_private_search_list(ordering=ordering, page=page, page_size=page_size, q=q)
        print("The response of V1Api->v1_private_search_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_search_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Order the results by a specific field. Currently the only valid options are \&quot;created_at\&quot; and \&quot;-created_at\&quot;. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **q** | **str**| The search term. | [optional] 

### Return type

[**PaginatedPrivateSignalSerializerListList**](PaginatedPrivateSignalSerializerListList.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_attachments_create**
> PrivateSignalAttachment v1_private_signals_attachments_create(parent_lookup__signal__pk, display, links, location, is_image, created_at, file, created_by, public=public, caption=caption)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.links5 import Links5
from signals_api_client.models.private_signal_attachment import PrivateSignalAttachment
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    parent_lookup__signal__pk = 'parent_lookup__signal__pk_example' # str | 
    display = 'display_example' # str | 
    links = signals_api_client.Links5() # Links5 | 
    location = 'location_example' # str | 
    is_image = True # bool | 
    created_at = '2013-10-20T19:20:30+01:00' # datetime | 
    file = 'file_example' # str | 
    created_by = 'created_by_example' # str | 
    public = True # bool |  (optional)
    caption = 'caption_example' # str |  (optional)

    try:
        api_response = await api_instance.v1_private_signals_attachments_create(parent_lookup__signal__pk, display, links, location, is_image, created_at, file, created_by, public=public, caption=caption)
        print("The response of V1Api->v1_private_signals_attachments_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_attachments_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup__signal__pk** | **str**|  | 
 **display** | **str**|  | 
 **links** | [**Links5**](Links5.md)|  | 
 **location** | **str**|  | 
 **is_image** | **bool**|  | 
 **created_at** | **datetime**|  | 
 **file** | **str**|  | 
 **created_by** | **str**|  | 
 **public** | **bool**|  | [optional] 
 **caption** | **str**|  | [optional] 

### Return type

[**PrivateSignalAttachment**](PrivateSignalAttachment.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_attachments_destroy**
> v1_private_signals_attachments_destroy(id, parent_lookup__signal__pk)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this attachment.
    parent_lookup__signal__pk = 'parent_lookup__signal__pk_example' # str | 

    try:
        await api_instance.v1_private_signals_attachments_destroy(id, parent_lookup__signal__pk)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_attachments_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this attachment. | 
 **parent_lookup__signal__pk** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_attachments_list**
> PaginatedPrivateSignalAttachmentList v1_private_signals_attachments_list(parent_lookup__signal__pk, page=page, page_size=page_size)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.paginated_private_signal_attachment_list import PaginatedPrivateSignalAttachmentList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    parent_lookup__signal__pk = 'parent_lookup__signal__pk_example' # str | 
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = await api_instance.v1_private_signals_attachments_list(parent_lookup__signal__pk, page=page, page_size=page_size)
        print("The response of V1Api->v1_private_signals_attachments_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_attachments_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup__signal__pk** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedPrivateSignalAttachmentList**](PaginatedPrivateSignalAttachmentList.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_attachments_partial_update**
> PrivateSignalAttachmentUpdate v1_private_signals_attachments_partial_update(id, parent_lookup__signal__pk, patched_private_signal_attachment_update=patched_private_signal_attachment_update)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.patched_private_signal_attachment_update import PatchedPrivateSignalAttachmentUpdate
from signals_api_client.models.private_signal_attachment_update import PrivateSignalAttachmentUpdate
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this attachment.
    parent_lookup__signal__pk = 'parent_lookup__signal__pk_example' # str | 
    patched_private_signal_attachment_update = signals_api_client.PatchedPrivateSignalAttachmentUpdate() # PatchedPrivateSignalAttachmentUpdate |  (optional)

    try:
        api_response = await api_instance.v1_private_signals_attachments_partial_update(id, parent_lookup__signal__pk, patched_private_signal_attachment_update=patched_private_signal_attachment_update)
        print("The response of V1Api->v1_private_signals_attachments_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_attachments_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this attachment. | 
 **parent_lookup__signal__pk** | **str**|  | 
 **patched_private_signal_attachment_update** | [**PatchedPrivateSignalAttachmentUpdate**](PatchedPrivateSignalAttachmentUpdate.md)|  | [optional] 

### Return type

[**PrivateSignalAttachmentUpdate**](PrivateSignalAttachmentUpdate.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_attachments_retrieve**
> PrivateSignalAttachment v1_private_signals_attachments_retrieve(id, parent_lookup__signal__pk)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.private_signal_attachment import PrivateSignalAttachment
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this attachment.
    parent_lookup__signal__pk = 'parent_lookup__signal__pk_example' # str | 

    try:
        api_response = await api_instance.v1_private_signals_attachments_retrieve(id, parent_lookup__signal__pk)
        print("The response of V1Api->v1_private_signals_attachments_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_attachments_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this attachment. | 
 **parent_lookup__signal__pk** | **str**|  | 

### Return type

[**PrivateSignalAttachment**](PrivateSignalAttachment.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_attachments_update**
> PrivateSignalAttachmentUpdate v1_private_signals_attachments_update(id, parent_lookup__signal__pk, private_signal_attachment_update=private_signal_attachment_update)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.private_signal_attachment_update import PrivateSignalAttachmentUpdate
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this attachment.
    parent_lookup__signal__pk = 'parent_lookup__signal__pk_example' # str | 
    private_signal_attachment_update = signals_api_client.PrivateSignalAttachmentUpdate() # PrivateSignalAttachmentUpdate |  (optional)

    try:
        api_response = await api_instance.v1_private_signals_attachments_update(id, parent_lookup__signal__pk, private_signal_attachment_update=private_signal_attachment_update)
        print("The response of V1Api->v1_private_signals_attachments_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_attachments_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this attachment. | 
 **parent_lookup__signal__pk** | **str**|  | 
 **private_signal_attachment_update** | [**PrivateSignalAttachmentUpdate**](PrivateSignalAttachmentUpdate.md)|  | [optional] 

### Return type

[**PrivateSignalAttachmentUpdate**](PrivateSignalAttachmentUpdate.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_category_removed_list**
> PaginatedSignalIdListList v1_private_signals_category_removed_list(after=after, before=before, category_slug=category_slug, page=page, page_size=page_size)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.paginated_signal_id_list_list import PaginatedSignalIdListList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    category_slug = ['category_slug_example'] # List[str] |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = await api_instance.v1_private_signals_category_removed_list(after=after, before=before, category_slug=category_slug, page=page, page_size=page_size)
        print("The response of V1Api->v1_private_signals_category_removed_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_category_removed_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **datetime**|  | [optional] 
 **before** | **datetime**|  | [optional] 
 **category_slug** | [**List[str]**](str.md)|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedSignalIdListList**](PaginatedSignalIdListList.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_children_list**
> PaginatedAbridgedChildSignalList v1_private_signals_children_list(id, page=page, page_size=page_size)

Show abridged version of child signals for a given parent signal.

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.paginated_abridged_child_signal_list import PaginatedAbridgedChildSignalList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this signal.
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = await api_instance.v1_private_signals_children_list(id, page=page, page_size=page_size)
        print("The response of V1Api->v1_private_signals_children_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_children_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this signal. | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedAbridgedChildSignalList**](PaginatedAbridgedChildSignalList.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_context_near_geography_retrieve**
> V1PrivateSignalsContextNearGeographyRetrieve200Response v1_private_signals_context_near_geography_retrieve(id)

Get an overview of signals in the same category and within a certain radius of the signal

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.v1_private_signals_context_near_geography_retrieve200_response import V1PrivateSignalsContextNearGeographyRetrieve200Response
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.v1_private_signals_context_near_geography_retrieve(id)
        print("The response of V1Api->v1_private_signals_context_near_geography_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_context_near_geography_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**V1PrivateSignalsContextNearGeographyRetrieve200Response**](V1PrivateSignalsContextNearGeographyRetrieve200Response.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_context_reporter_list**
> PaginatedSignalContextReporterList v1_private_signals_context_reporter_list(id, page=page, page_size=page_size)

Get an overview of signals from the same reporter

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.paginated_signal_context_reporter_list import PaginatedSignalContextReporterList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 'id_example' # str | 
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = await api_instance.v1_private_signals_context_reporter_list(id, page=page, page_size=page_size)
        print("The response of V1Api->v1_private_signals_context_reporter_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_context_reporter_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedSignalContextReporterList**](PaginatedSignalContextReporterList.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_context_retrieve**
> SignalContext v1_private_signals_context_retrieve(id)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.signal_context import SignalContext
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 'id_example' # str | 

    try:
        api_response = await api_instance.v1_private_signals_context_retrieve(id)
        print("The response of V1Api->v1_private_signals_context_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_context_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SignalContext**](SignalContext.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_create**
> PrivateSignalSerializerList v1_private_signals_create(private_signal_serializer_list)

Create a new signal

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.private_signal_serializer_list import PrivateSignalSerializerList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    private_signal_serializer_list = signals_api_client.PrivateSignalSerializerList() # PrivateSignalSerializerList | 

    try:
        api_response = await api_instance.v1_private_signals_create(private_signal_serializer_list)
        print("The response of V1Api->v1_private_signals_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **private_signal_serializer_list** | [**PrivateSignalSerializerList**](PrivateSignalSerializerList.md)|  | 

### Return type

[**PrivateSignalSerializerList**](PrivateSignalSerializerList.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_email_preview_create**
> EmailPreview v1_private_signals_email_preview_create(id, email_preview_post)

Render the email preview before transitioning to a specific status.

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.email_preview import EmailPreview
from signals_api_client.models.email_preview_post import EmailPreviewPost
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this signal.
    email_preview_post = signals_api_client.EmailPreviewPost() # EmailPreviewPost | 

    try:
        api_response = await api_instance.v1_private_signals_email_preview_create(id, email_preview_post)
        print("The response of V1Api->v1_private_signals_email_preview_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_email_preview_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this signal. | 
 **email_preview_post** | [**EmailPreviewPost**](EmailPreviewPost.md)|  | 

### Return type

[**EmailPreview**](EmailPreview.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_geography_retrieve**
> V1PrivateSignalsGeographyRetrieve200Response v1_private_signals_geography_retrieve()

GeoJSON of all signals

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.v1_private_signals_geography_retrieve200_response import V1PrivateSignalsGeographyRetrieve200Response
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)

    try:
        api_response = await api_instance.v1_private_signals_geography_retrieve()
        print("The response of V1Api->v1_private_signals_geography_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_geography_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1PrivateSignalsGeographyRetrieve200Response**](V1PrivateSignalsGeographyRetrieve200Response.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_history_list**
> List[HistoryLogHal] v1_private_signals_history_list(id, created_after=created_after, what=what)

History endpoint filterable by action.

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.history_log_hal import HistoryLogHal
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this signal.
    created_after = '2013-10-20T19:20:30+01:00' # datetime | Filters actions created after a certain timestamp (ISO 8601) (optional)
    what = 'what_example' # str | Filters a specific \"action\" (optional)

    try:
        api_response = await api_instance.v1_private_signals_history_list(id, created_after=created_after, what=what)
        print("The response of V1Api->v1_private_signals_history_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_history_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this signal. | 
 **created_after** | **datetime**| Filters actions created after a certain timestamp (ISO 8601) | [optional] 
 **what** | **str**| Filters a specific \&quot;action\&quot; | [optional] 

### Return type

[**List[HistoryLogHal]**](HistoryLogHal.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_list**
> PaginatedPrivateSignalSerializerListList v1_private_signals_list(address_text=address_text, area_code=area_code, area_type_code=area_type_code, assigned_user_email=assigned_user_email, buurt_code=buurt_code, category_id=category_id, category_slug=category_slug, contact_details=contact_details, created_after=created_after, created_before=created_before, directing_department=directing_department, feedback=feedback, has_changed_children=has_changed_children, id=id, incident_date=incident_date, incident_date_after=incident_date_after, incident_date_before=incident_date_before, kind=kind, maincategory_slug=maincategory_slug, note_keyword=note_keyword, ordering=ordering, page=page, page_size=page_size, priority=priority, punctuality=punctuality, reporter_email=reporter_email, routing_department_code=routing_department_code, source=source, stadsdeel=stadsdeel, status=status, type=type, updated_after=updated_after, updated_before=updated_before)

List of signals

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.paginated_private_signal_serializer_list_list import PaginatedPrivateSignalSerializerListList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    address_text = 'address_text_example' # str |  (optional)
    area_code = ['area_code_example'] # List[Optional[str]] |  (optional)
    area_type_code = 'area_type_code_example' # str |  (optional)
    assigned_user_email = 'assigned_user_email_example' # str |  (optional)
    buurt_code = ['buurt_code_example'] # List[Optional[str]] |  (optional)
    category_id = [56] # List[int] |  (optional)
    category_slug = ['category_slug_example'] # List[str] |  (optional)
    contact_details = ['contact_details_example'] # List[str] |  (optional)
    created_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    created_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    directing_department = ['directing_department_example'] # List[str] |  (optional)
    feedback = 'feedback_example' # str |  (optional)
    has_changed_children = [True] # List[bool] | * `True` - True * `true` - true * `True` - True * `1` - 1 * `False` - False * `false` - false * `False` - False * `0` - 0 (optional)
    id = 56 # int |  (optional)
    incident_date = '2013-10-20' # date |  (optional)
    incident_date_after = '2013-10-20' # date |  (optional)
    incident_date_before = '2013-10-20' # date |  (optional)
    kind = ['kind_example'] # List[str] |  (optional)
    maincategory_slug = ['maincategory_slug_example'] # List[str] |  (optional)
    note_keyword = 'note_keyword_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    priority = ['priority_example'] # List[str] | * `low` - Low * `normal` - Normal * `high` - High (optional)
    punctuality = 'punctuality_example' # str | Punctuality (optional)
    reporter_email = 'reporter_email_example' # str |  (optional)
    routing_department_code = ['routing_department_code_example'] # List[str] |  (optional)
    source = ['source_example'] # List[str] |  (optional)
    stadsdeel = ['stadsdeel_example'] # List[Optional[str]] |  (optional)
    status = ['status_example'] # List[str] | Melding status (optional)
    type = ['type_example'] # List[str] | * `SIG` - Signal * `REQ` - Request * `QUE` - Question * `COM` - Complaint * `MAI` - Maintenance (optional)
    updated_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    updated_before = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = await api_instance.v1_private_signals_list(address_text=address_text, area_code=area_code, area_type_code=area_type_code, assigned_user_email=assigned_user_email, buurt_code=buurt_code, category_id=category_id, category_slug=category_slug, contact_details=contact_details, created_after=created_after, created_before=created_before, directing_department=directing_department, feedback=feedback, has_changed_children=has_changed_children, id=id, incident_date=incident_date, incident_date_after=incident_date_after, incident_date_before=incident_date_before, kind=kind, maincategory_slug=maincategory_slug, note_keyword=note_keyword, ordering=ordering, page=page, page_size=page_size, priority=priority, punctuality=punctuality, reporter_email=reporter_email, routing_department_code=routing_department_code, source=source, stadsdeel=stadsdeel, status=status, type=type, updated_after=updated_after, updated_before=updated_before)
        print("The response of V1Api->v1_private_signals_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_text** | **str**|  | [optional] 
 **area_code** | [**List[Optional[str]]**](str.md)|  | [optional] 
 **area_type_code** | **str**|  | [optional] 
 **assigned_user_email** | **str**|  | [optional] 
 **buurt_code** | [**List[Optional[str]]**](str.md)|  | [optional] 
 **category_id** | [**List[int]**](int.md)|  | [optional] 
 **category_slug** | [**List[str]**](str.md)|  | [optional] 
 **contact_details** | [**List[str]**](str.md)|  | [optional] 
 **created_after** | **datetime**|  | [optional] 
 **created_before** | **datetime**|  | [optional] 
 **directing_department** | [**List[str]**](str.md)|  | [optional] 
 **feedback** | **str**|  | [optional] 
 **has_changed_children** | [**List[bool]**](bool.md)| * &#x60;True&#x60; - True * &#x60;true&#x60; - true * &#x60;True&#x60; - True * &#x60;1&#x60; - 1 * &#x60;False&#x60; - False * &#x60;false&#x60; - false * &#x60;False&#x60; - False * &#x60;0&#x60; - 0 | [optional] 
 **id** | **int**|  | [optional] 
 **incident_date** | **date**|  | [optional] 
 **incident_date_after** | **date**|  | [optional] 
 **incident_date_before** | **date**|  | [optional] 
 **kind** | [**List[str]**](str.md)|  | [optional] 
 **maincategory_slug** | [**List[str]**](str.md)|  | [optional] 
 **note_keyword** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **priority** | [**List[str]**](str.md)| * &#x60;low&#x60; - Low * &#x60;normal&#x60; - Normal * &#x60;high&#x60; - High | [optional] 
 **punctuality** | **str**| Punctuality | [optional] 
 **reporter_email** | **str**|  | [optional] 
 **routing_department_code** | [**List[str]**](str.md)|  | [optional] 
 **source** | [**List[str]**](str.md)|  | [optional] 
 **stadsdeel** | [**List[Optional[str]]**](str.md)|  | [optional] 
 **status** | [**List[str]**](str.md)| Melding status | [optional] 
 **type** | [**List[str]**](str.md)| * &#x60;SIG&#x60; - Signal * &#x60;REQ&#x60; - Request * &#x60;QUE&#x60; - Question * &#x60;COM&#x60; - Complaint * &#x60;MAI&#x60; - Maintenance | [optional] 
 **updated_after** | **datetime**|  | [optional] 
 **updated_before** | **datetime**|  | [optional] 

### Return type

[**PaginatedPrivateSignalSerializerListList**](PaginatedPrivateSignalSerializerListList.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_partial_update**
> PrivateSignalSerializerDetail v1_private_signals_partial_update(id, patched_private_signal_serializer_list=patched_private_signal_serializer_list)

Partial update a signal

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.patched_private_signal_serializer_list import PatchedPrivateSignalSerializerList
from signals_api_client.models.private_signal_serializer_detail import PrivateSignalSerializerDetail
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this signal.
    patched_private_signal_serializer_list = signals_api_client.PatchedPrivateSignalSerializerList() # PatchedPrivateSignalSerializerList |  (optional)

    try:
        api_response = await api_instance.v1_private_signals_partial_update(id, patched_private_signal_serializer_list=patched_private_signal_serializer_list)
        print("The response of V1Api->v1_private_signals_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this signal. | 
 **patched_private_signal_serializer_list** | [**PatchedPrivateSignalSerializerList**](PatchedPrivateSignalSerializerList.md)|  | [optional] 

### Return type

[**PrivateSignalSerializerDetail**](PrivateSignalSerializerDetail.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_pdf_retrieve**
> v1_private_signals_pdf_retrieve(id)

Download the Signal as a PDF.

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this signal.

    try:
        await api_instance.v1_private_signals_pdf_retrieve(id)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_pdf_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this signal. | 

### Return type

void (empty response body)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_promoted_parent_list**
> PaginatedSignalIdListList v1_private_signals_promoted_parent_list(after=after, page=page, page_size=page_size)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.paginated_signal_id_list_list import PaginatedSignalIdListList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = await api_instance.v1_private_signals_promoted_parent_list(after=after, page=page, page_size=page_size)
        print("The response of V1Api->v1_private_signals_promoted_parent_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_promoted_parent_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **datetime**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedSignalIdListList**](PaginatedSignalIdListList.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_reporters_cancel_create**
> SignalReporter v1_private_signals_reporters_cancel_create(id, parent_lookup__signal_id, cancel_signal_reporter=cancel_signal_reporter)

Cancel a reporter, this allows cancelling a reporter update.
Cancelling is allowed, when the state of the reporter is "new" or "verification_email_sent"
and the reporter is not the original/first reporter of the signal.
Optionally a reason for the cancellation can be provided using the reason field.

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.cancel_signal_reporter import CancelSignalReporter
from signals_api_client.models.signal_reporter import SignalReporter
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this reporter.
    parent_lookup__signal_id = 'parent_lookup__signal_id_example' # str | 
    cancel_signal_reporter = signals_api_client.CancelSignalReporter() # CancelSignalReporter |  (optional)

    try:
        api_response = await api_instance.v1_private_signals_reporters_cancel_create(id, parent_lookup__signal_id, cancel_signal_reporter=cancel_signal_reporter)
        print("The response of V1Api->v1_private_signals_reporters_cancel_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_reporters_cancel_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this reporter. | 
 **parent_lookup__signal_id** | **str**|  | 
 **cancel_signal_reporter** | [**CancelSignalReporter**](CancelSignalReporter.md)|  | [optional] 

### Return type

[**SignalReporter**](SignalReporter.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_reporters_create**
> SignalReporter v1_private_signals_reporters_create(parent_lookup__signal_id, signal_reporter)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.signal_reporter import SignalReporter
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    parent_lookup__signal_id = 'parent_lookup__signal_id_example' # str | 
    signal_reporter = signals_api_client.SignalReporter() # SignalReporter | 

    try:
        api_response = await api_instance.v1_private_signals_reporters_create(parent_lookup__signal_id, signal_reporter)
        print("The response of V1Api->v1_private_signals_reporters_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_reporters_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup__signal_id** | **str**|  | 
 **signal_reporter** | [**SignalReporter**](SignalReporter.md)|  | 

### Return type

[**SignalReporter**](SignalReporter.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_reporters_list**
> PaginatedSignalReporterList v1_private_signals_reporters_list(parent_lookup__signal_id, page=page, page_size=page_size, state=state)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.paginated_signal_reporter_list import PaginatedSignalReporterList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    parent_lookup__signal_id = 'parent_lookup__signal_id_example' # str | 
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    state = 'state_example' # str | * `new` - New * `verification_email_sent` - Verification email sent * `cancelled` - Cancelled * `approved` - Approved (optional)

    try:
        api_response = await api_instance.v1_private_signals_reporters_list(parent_lookup__signal_id, page=page, page_size=page_size, state=state)
        print("The response of V1Api->v1_private_signals_reporters_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_reporters_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup__signal_id** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **state** | **str**| * &#x60;new&#x60; - New * &#x60;verification_email_sent&#x60; - Verification email sent * &#x60;cancelled&#x60; - Cancelled * &#x60;approved&#x60; - Approved | [optional] 

### Return type

[**PaginatedSignalReporterList**](PaginatedSignalReporterList.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_signals_retrieve**
> PrivateSignalSerializerDetail v1_private_signals_retrieve(id)

Retrieve a signal

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.private_signal_serializer_detail import PrivateSignalSerializerDetail
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this signal.

    try:
        api_response = await api_instance.v1_private_signals_retrieve(id)
        print("The response of V1Api->v1_private_signals_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_signals_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this signal. | 

### Return type

[**PrivateSignalSerializerDetail**](PrivateSignalSerializerDetail.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_sources_list**
> PaginatedSourceList v1_private_sources_list(can_be_selected=can_be_selected, is_active=is_active, page=page, page_size=page_size)

Display all sources

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.paginated_source_list import PaginatedSourceList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    can_be_selected = True # bool |  (optional)
    is_active = True # bool |  (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = await api_instance.v1_private_sources_list(can_be_selected=can_be_selected, is_active=is_active, page=page, page_size=page_size)
        print("The response of V1Api->v1_private_sources_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_sources_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **can_be_selected** | **bool**|  | [optional] 
 **is_active** | **bool**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedSourceList**](PaginatedSourceList.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_sources_retrieve**
> Source v1_private_sources_retrieve(id)

Display all sources

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.source import Source
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this source.

    try:
        api_response = await api_instance.v1_private_sources_retrieve(id)
        print("The response of V1Api->v1_private_sources_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_sources_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this source. | 

### Return type

[**Source**](Source.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_status_messages_category_create**
> StatusMessageCategoryPosition v1_private_status_messages_category_create(category_id, status_message_category_position)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.status_message_category_position import StatusMessageCategoryPosition
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    category_id = 'category_id_example' # str | 
    status_message_category_position = signals_api_client.StatusMessageCategoryPosition() # StatusMessageCategoryPosition | 

    try:
        api_response = await api_instance.v1_private_status_messages_category_create(category_id, status_message_category_position)
        print("The response of V1Api->v1_private_status_messages_category_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_status_messages_category_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 
 **status_message_category_position** | [**StatusMessageCategoryPosition**](StatusMessageCategoryPosition.md)|  | 

### Return type

[**StatusMessageCategoryPosition**](StatusMessageCategoryPosition.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_status_messages_create**
> StatusMessage v1_private_status_messages_create(status_message)

Endpoint to manage status messages.

A status message can be used as a template for a response to a reporter on a state
transition of a signal.

Status messages contain a state field that links it to the
state that the signal will be transitioned to and can be attached to multiple
categories. Within each category it has a position, that can be used to determine
the order in which the status messages should be displayed to the user.

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.status_message import StatusMessage
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    status_message = signals_api_client.StatusMessage() # StatusMessage | 

    try:
        api_response = await api_instance.v1_private_status_messages_create(status_message)
        print("The response of V1Api->v1_private_status_messages_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_status_messages_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_message** | [**StatusMessage**](StatusMessage.md)|  | 

### Return type

[**StatusMessage**](StatusMessage.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_status_messages_destroy**
> v1_private_status_messages_destroy(id)

Endpoint to manage status messages.

A status message can be used as a template for a response to a reporter on a state
transition of a signal.

Status messages contain a state field that links it to the
state that the signal will be transitioned to and can be attached to multiple
categories. Within each category it has a position, that can be used to determine
the order in which the status messages should be displayed to the user.

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this Standaardtekst.

    try:
        await api_instance.v1_private_status_messages_destroy(id)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_status_messages_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Standaardtekst. | 

### Return type

void (empty response body)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_status_messages_list**
> PaginatedStatusMessageList v1_private_status_messages_list(active=active, category_id=category_id, ordering=ordering, page=page, page_size=page_size, state=state)

Endpoint to manage status messages.

A status message can be used as a template for a response to a reporter on a state
transition of a signal.

Status messages contain a state field that links it to the
state that the signal will be transitioned to and can be attached to multiple
categories. Within each category it has a position, that can be used to determine
the order in which the status messages should be displayed to the user.

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.paginated_status_message_list import PaginatedStatusMessageList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    active = True # bool |  (optional)
    category_id = 56 # int |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    state = ['state_example'] # List[str] |  (optional)

    try:
        api_response = await api_instance.v1_private_status_messages_list(active=active, category_id=category_id, ordering=ordering, page=page, page_size=page_size, state=state)
        print("The response of V1Api->v1_private_status_messages_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_status_messages_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **bool**|  | [optional] 
 **category_id** | **int**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **state** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**PaginatedStatusMessageList**](PaginatedStatusMessageList.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_status_messages_partial_update**
> StatusMessage v1_private_status_messages_partial_update(id, patched_status_message=patched_status_message)

Endpoint to manage status messages.

A status message can be used as a template for a response to a reporter on a state
transition of a signal.

Status messages contain a state field that links it to the
state that the signal will be transitioned to and can be attached to multiple
categories. Within each category it has a position, that can be used to determine
the order in which the status messages should be displayed to the user.

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.patched_status_message import PatchedStatusMessage
from signals_api_client.models.status_message import StatusMessage
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this Standaardtekst.
    patched_status_message = signals_api_client.PatchedStatusMessage() # PatchedStatusMessage |  (optional)

    try:
        api_response = await api_instance.v1_private_status_messages_partial_update(id, patched_status_message=patched_status_message)
        print("The response of V1Api->v1_private_status_messages_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_status_messages_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Standaardtekst. | 
 **patched_status_message** | [**PatchedStatusMessage**](PatchedStatusMessage.md)|  | [optional] 

### Return type

[**StatusMessage**](StatusMessage.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_status_messages_retrieve**
> StatusMessage v1_private_status_messages_retrieve(id)

Endpoint to manage status messages.

A status message can be used as a template for a response to a reporter on a state
transition of a signal.

Status messages contain a state field that links it to the
state that the signal will be transitioned to and can be attached to multiple
categories. Within each category it has a position, that can be used to determine
the order in which the status messages should be displayed to the user.

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.status_message import StatusMessage
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this Standaardtekst.

    try:
        api_response = await api_instance.v1_private_status_messages_retrieve(id)
        print("The response of V1Api->v1_private_status_messages_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_status_messages_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Standaardtekst. | 

### Return type

[**StatusMessage**](StatusMessage.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_status_messages_search_retrieve**
> StatusMessageList v1_private_status_messages_search_retrieve(active=active, page=page, page_size=page_size, q=q, state=state)

This will perform a lookup using elasticsearch using a "fuzzy" search, which allows
for typos, misspelling, pluralization, etc...
It allows for filtering based on the 'state' key and by the 'active' state by using
querystring parameters 'state' and 'active' respectively.
When no search term is provided using querystring parameter 'q', all status messages
will be returned (optionally filtered using the 'state' and 'active' filters).
When a search term is provided a 'highlight' section is available for both the 'title'
and 'text' field, which can be used to display the title and text of the status messages
in the results with the search term highlighted.
Pagination is provided using the 'page_size' and 'page' querystring parameters.
In the results there is a 'facets' section available, which provides counts for every
filter option.

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.status_message_list import StatusMessageList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    active = True # bool | Filter the search results on the \"active\" state of the status message. (optional)
    page = 56 # int | The page number of the paginated results. (optional)
    page_size = 56 # int | Number of results returned per page. (optional)
    q = 'q_example' # str | The search term. (optional)
    state = 'state_example' # str | Filter the search results on state code (add parameter to querystring multiple times to filter on multiple states). (optional)

    try:
        api_response = await api_instance.v1_private_status_messages_search_retrieve(active=active, page=page, page_size=page_size, q=q, state=state)
        print("The response of V1Api->v1_private_status_messages_search_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_status_messages_search_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **bool**| Filter the search results on the \&quot;active\&quot; state of the status message. | [optional] 
 **page** | **int**| The page number of the paginated results. | [optional] 
 **page_size** | **int**| Number of results returned per page. | [optional] 
 **q** | **str**| The search term. | [optional] 
 **state** | **str**| Filter the search results on state code (add parameter to querystring multiple times to filter on multiple states). | [optional] 

### Return type

[**StatusMessageList**](StatusMessageList.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_status_messages_update**
> StatusMessage v1_private_status_messages_update(id, status_message)

Endpoint to manage status messages.

A status message can be used as a template for a response to a reporter on a state
transition of a signal.

Status messages contain a state field that links it to the
state that the signal will be transitioned to and can be attached to multiple
categories. Within each category it has a position, that can be used to determine
the order in which the status messages should be displayed to the user.

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.status_message import StatusMessage
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this Standaardtekst.
    status_message = signals_api_client.StatusMessage() # StatusMessage | 

    try:
        api_response = await api_instance.v1_private_status_messages_update(id, status_message)
        print("The response of V1Api->v1_private_status_messages_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_status_messages_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Standaardtekst. | 
 **status_message** | [**StatusMessage**](StatusMessage.md)|  | 

### Return type

[**StatusMessage**](StatusMessage.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_terms_categories_status_message_templates_create**
> StateStatusMessageTemplate v1_private_terms_categories_status_message_templates_create(slug, state_status_message_template)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.state_status_message_template import StateStatusMessageTemplate
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    slug = 'slug_example' # str | 
    state_status_message_template = signals_api_client.StateStatusMessageTemplate() # StateStatusMessageTemplate | 

    try:
        api_response = await api_instance.v1_private_terms_categories_status_message_templates_create(slug, state_status_message_template)
        print("The response of V1Api->v1_private_terms_categories_status_message_templates_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_terms_categories_status_message_templates_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **state_status_message_template** | [**StateStatusMessageTemplate**](StateStatusMessageTemplate.md)|  | 

### Return type

[**StateStatusMessageTemplate**](StateStatusMessageTemplate.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_terms_categories_status_message_templates_retrieve**
> StateStatusMessageTemplate v1_private_terms_categories_status_message_templates_retrieve(slug)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.state_status_message_template import StateStatusMessageTemplate
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = await api_instance.v1_private_terms_categories_status_message_templates_retrieve(slug)
        print("The response of V1Api->v1_private_terms_categories_status_message_templates_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_terms_categories_status_message_templates_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**StateStatusMessageTemplate**](StateStatusMessageTemplate.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_terms_categories_sub_categories_status_message_templates_create**
> StateStatusMessageTemplate v1_private_terms_categories_sub_categories_status_message_templates_create(slug, sub_slug, state_status_message_template)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.state_status_message_template import StateStatusMessageTemplate
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    slug = 'slug_example' # str | 
    sub_slug = 'sub_slug_example' # str | 
    state_status_message_template = signals_api_client.StateStatusMessageTemplate() # StateStatusMessageTemplate | 

    try:
        api_response = await api_instance.v1_private_terms_categories_sub_categories_status_message_templates_create(slug, sub_slug, state_status_message_template)
        print("The response of V1Api->v1_private_terms_categories_sub_categories_status_message_templates_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_terms_categories_sub_categories_status_message_templates_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **sub_slug** | **str**|  | 
 **state_status_message_template** | [**StateStatusMessageTemplate**](StateStatusMessageTemplate.md)|  | 

### Return type

[**StateStatusMessageTemplate**](StateStatusMessageTemplate.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_terms_categories_sub_categories_status_message_templates_retrieve**
> StateStatusMessageTemplate v1_private_terms_categories_sub_categories_status_message_templates_retrieve(slug, sub_slug)

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.state_status_message_template import StateStatusMessageTemplate
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    slug = 'slug_example' # str | 
    sub_slug = 'sub_slug_example' # str | 

    try:
        api_response = await api_instance.v1_private_terms_categories_sub_categories_status_message_templates_retrieve(slug, sub_slug)
        print("The response of V1Api->v1_private_terms_categories_sub_categories_status_message_templates_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_terms_categories_sub_categories_status_message_templates_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **sub_slug** | **str**|  | 

### Return type

[**StateStatusMessageTemplate**](StateStatusMessageTemplate.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_translations_create**
> v1_private_translations_create()

Create an I18Next translation file from the JSON data.

Args:
    request (Request): The incoming request containing JSON data.

Returns:
    Response: A success response with the created JSON data.

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)

    try:
        await api_instance.v1_private_translations_create()
    except Exception as e:
        print("Exception when calling V1Api->v1_private_translations_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_users_create**
> UserDetailHAL v1_private_users_create(user_detail_hal)

Create a user

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.user_detail_hal import UserDetailHAL
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    user_detail_hal = signals_api_client.UserDetailHAL() # UserDetailHAL | 

    try:
        api_response = await api_instance.v1_private_users_create(user_detail_hal)
        print("The response of V1Api->v1_private_users_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_detail_hal** | [**UserDetailHAL**](UserDetailHAL.md)|  | 

### Return type

[**UserDetailHAL**](UserDetailHAL.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_users_history_retrieve**
> PrivateUserHistoryHal v1_private_users_history_retrieve(id)

The change log of the selected User instance
This is read-only!

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.private_user_history_hal import PrivateUserHistoryHal
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this gebruiker.

    try:
        api_response = await api_instance.v1_private_users_history_retrieve(id)
        print("The response of V1Api->v1_private_users_history_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_users_history_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this gebruiker. | 

### Return type

[**PrivateUserHistoryHal**](PrivateUserHistoryHal.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_users_list**
> PaginatedUserListHALList v1_private_users_list(id=id, is_active=is_active, order=order, page=page, page_size=page_size, profile_department_code=profile_department_code, role=role, username=username)

List all users

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.paginated_user_list_hal_list import PaginatedUserListHALList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int |  (optional)
    is_active = True # bool |  (optional)
    order = ['order_example'] # List[str] | Volgorde  * `username` - Gebruikersnaam * `-username` - Gebruikersnaam (aflopend) * `is_active` - Is active * `-is_active` - Is active (aflopend) (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    profile_department_code = ['profile_department_code_example'] # List[str] |  (optional)
    role = ['role_example'] # List[str] |  (optional)
    username = 'username_example' # str |  (optional)

    try:
        api_response = await api_instance.v1_private_users_list(id=id, is_active=is_active, order=order, page=page, page_size=page_size, profile_department_code=profile_department_code, role=role, username=username)
        print("The response of V1Api->v1_private_users_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_users_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | [optional] 
 **is_active** | **bool**|  | [optional] 
 **order** | [**List[str]**](str.md)| Volgorde  * &#x60;username&#x60; - Gebruikersnaam * &#x60;-username&#x60; - Gebruikersnaam (aflopend) * &#x60;is_active&#x60; - Is active * &#x60;-is_active&#x60; - Is active (aflopend) | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **profile_department_code** | [**List[str]**](str.md)|  | [optional] 
 **role** | [**List[str]**](str.md)|  | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**PaginatedUserListHALList**](PaginatedUserListHALList.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_users_partial_update**
> UserDetailHAL v1_private_users_partial_update(id, patched_user_detail_hal=patched_user_detail_hal)

Update a user

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.patched_user_detail_hal import PatchedUserDetailHAL
from signals_api_client.models.user_detail_hal import UserDetailHAL
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this gebruiker.
    patched_user_detail_hal = signals_api_client.PatchedUserDetailHAL() # PatchedUserDetailHAL |  (optional)

    try:
        api_response = await api_instance.v1_private_users_partial_update(id, patched_user_detail_hal=patched_user_detail_hal)
        print("The response of V1Api->v1_private_users_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_users_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this gebruiker. | 
 **patched_user_detail_hal** | [**PatchedUserDetailHAL**](PatchedUserDetailHAL.md)|  | [optional] 

### Return type

[**UserDetailHAL**](UserDetailHAL.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_users_retrieve**
> UserDetailHAL v1_private_users_retrieve(id)

Retrieve a user

### Example

* Bearer (JWT) Authentication (JWTAuthBackend):

```python
import signals_api_client
from signals_api_client.models.user_detail_hal import UserDetailHAL
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuthBackend
configuration = signals_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    id = 56 # int | A unique integer value identifying this gebruiker.

    try:
        api_response = await api_instance.v1_private_users_retrieve(id)
        print("The response of V1Api->v1_private_users_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_private_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this gebruiker. | 

### Return type

[**UserDetailHAL**](UserDetailHAL.md)

### Authorization

[JWTAuthBackend](../README.md#JWTAuthBackend)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_areas_geography_retrieve**
> AreaGeo v1_public_areas_geography_retrieve(geopage=geopage, page_size=page_size)

Retrieve a paginated list of area geographies.

Returns a paginated response with area geographies.

### Example


```python
import signals_api_client
from signals_api_client.models.area_geo import AreaGeo
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    geopage = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = await api_instance.v1_public_areas_geography_retrieve(geopage=geopage, page_size=page_size)
        print("The response of V1Api->v1_public_areas_geography_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_public_areas_geography_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geopage** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**AreaGeo**](AreaGeo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_areas_list**
> PaginatedAreaList v1_public_areas_list(code=code, ordering=ordering, page=page, page_size=page_size, type_code=type_code)

A ViewSet for retrieving areas.

### Example


```python
import signals_api_client
from signals_api_client.models.paginated_area_list import PaginatedAreaList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    code = ['code_example'] # List[str] |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    type_code = ['type_code_example'] # List[str] |  (optional)

    try:
        api_response = await api_instance.v1_public_areas_list(code=code, ordering=ordering, page=page, page_size=page_size, type_code=type_code)
        print("The response of V1Api->v1_public_areas_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_public_areas_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | [**List[str]**](str.md)|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **type_code** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**PaginatedAreaList**](PaginatedAreaList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_feedback_forms_partial_update**
> Feedback v1_public_feedback_forms_partial_update(token, patched_feedback=patched_feedback)

View to receive complaint/client feedback.

### Example


```python
import signals_api_client
from signals_api_client.models.feedback import Feedback
from signals_api_client.models.patched_feedback import PatchedFeedback
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    token = 'token_example' # str | A unique value identifying this feedback.
    patched_feedback = signals_api_client.PatchedFeedback() # PatchedFeedback |  (optional)

    try:
        api_response = await api_instance.v1_public_feedback_forms_partial_update(token, patched_feedback=patched_feedback)
        print("The response of V1Api->v1_public_feedback_forms_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_public_feedback_forms_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| A unique value identifying this feedback. | 
 **patched_feedback** | [**PatchedFeedback**](PatchedFeedback.md)|  | [optional] 

### Return type

[**Feedback**](Feedback.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** |  |  -  |
**410** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_feedback_forms_retrieve**
> Feedback v1_public_feedback_forms_retrieve(token)

View to receive complaint/client feedback.

### Example


```python
import signals_api_client
from signals_api_client.models.feedback import Feedback
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    token = 'token_example' # str | A unique value identifying this feedback.

    try:
        api_response = await api_instance.v1_public_feedback_forms_retrieve(token)
        print("The response of V1Api->v1_public_feedback_forms_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_public_feedback_forms_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| A unique value identifying this feedback. | 

### Return type

[**Feedback**](Feedback.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** |  |  -  |
**410** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_feedback_forms_update**
> Feedback v1_public_feedback_forms_update(token, feedback)

View to receive complaint/client feedback.

### Example


```python
import signals_api_client
from signals_api_client.models.feedback import Feedback
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    token = 'token_example' # str | A unique value identifying this feedback.
    feedback = signals_api_client.Feedback() # Feedback | 

    try:
        api_response = await api_instance.v1_public_feedback_forms_update(token, feedback)
        print("The response of V1Api->v1_public_feedback_forms_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_public_feedback_forms_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| A unique value identifying this feedback. | 
 **feedback** | [**Feedback**](Feedback.md)|  | 

### Return type

[**Feedback**](Feedback.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** |  |  -  |
**410** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_feedback_standard_answers_list**
> PaginatedStandardAnswerList v1_public_feedback_standard_answers_list(page=page, page_size=page_size)

View to list all currently visible Standard Answers.

### Example


```python
import signals_api_client
from signals_api_client.models.paginated_standard_answer_list import PaginatedStandardAnswerList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = await api_instance.v1_public_feedback_standard_answers_list(page=page, page_size=page_size)
        print("The response of V1Api->v1_public_feedback_standard_answers_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_public_feedback_standard_answers_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedStandardAnswerList**](PaginatedStandardAnswerList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_questions_list**
> PaginatedPublicQuestionSerializerDetailList v1_public_questions_list(main_slug=main_slug, page=page, page_size=page_size, sub_slug=sub_slug)

### Example


```python
import signals_api_client
from signals_api_client.models.paginated_public_question_serializer_detail_list import PaginatedPublicQuestionSerializerDetailList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    main_slug = 'main_slug_example' # str | Hoofd categorie (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    sub_slug = 'sub_slug_example' # str | Sub categorie (optional)

    try:
        api_response = await api_instance.v1_public_questions_list(main_slug=main_slug, page=page, page_size=page_size, sub_slug=sub_slug)
        print("The response of V1Api->v1_public_questions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_public_questions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **main_slug** | **str**| Hoofd categorie | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **sub_slug** | **str**| Sub categorie | [optional] 

### Return type

[**PaginatedPublicQuestionSerializerDetailList**](PaginatedPublicQuestionSerializerDetailList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_reporter_verify_email_create**
> EmailVerification v1_public_reporter_verify_email_create(email_verification)

Verify the token for reporter email verification.

### Example


```python
import signals_api_client
from signals_api_client.models.email_verification import EmailVerification
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    email_verification = signals_api_client.EmailVerification() # EmailVerification | 

    try:
        api_response = await api_instance.v1_public_reporter_verify_email_create(email_verification)
        print("The response of V1Api->v1_public_reporter_verify_email_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_public_reporter_verify_email_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_verification** | [**EmailVerification**](EmailVerification.md)|  | 

### Return type

[**EmailVerification**](EmailVerification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_signals_create**
> PublicSignalSerializerDetail v1_public_signals_create(public_signal_create)

Create a signal

### Example


```python
import signals_api_client
from signals_api_client.models.public_signal_create import PublicSignalCreate
from signals_api_client.models.public_signal_serializer_detail import PublicSignalSerializerDetail
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    public_signal_create = signals_api_client.PublicSignalCreate() # PublicSignalCreate | 

    try:
        api_response = await api_instance.v1_public_signals_create(public_signal_create)
        print("The response of V1Api->v1_public_signals_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_public_signals_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_signal_create** | [**PublicSignalCreate**](PublicSignalCreate.md)|  | 

### Return type

[**PublicSignalSerializerDetail**](PublicSignalSerializerDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**500** |  |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_signals_geography_retrieve**
> V1PublicSignalsGeographyRetrieve200Response v1_public_signals_geography_retrieve(bbox=bbox, category_slug=category_slug, lat=lat, lon=lon, maincategory_slug=maincategory_slug, ordering=ordering)

GeoJSON of all signals that can be shown on a public map.

### Example


```python
import signals_api_client
from signals_api_client.models.v1_public_signals_geography_retrieve200_response import V1PublicSignalsGeographyRetrieve200Response
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    bbox = 'bbox_example' # str |  (optional)
    category_slug = ['category_slug_example'] # List[str] |  (optional)
    lat = 3.4 # float |  (optional)
    lon = 3.4 # float |  (optional)
    maincategory_slug = ['maincategory_slug_example'] # List[str] |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)

    try:
        api_response = await api_instance.v1_public_signals_geography_retrieve(bbox=bbox, category_slug=category_slug, lat=lat, lon=lon, maincategory_slug=maincategory_slug, ordering=ordering)
        print("The response of V1Api->v1_public_signals_geography_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_public_signals_geography_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bbox** | **str**|  | [optional] 
 **category_slug** | [**List[str]**](str.md)|  | [optional] 
 **lat** | **float**|  | [optional] 
 **lon** | **float**|  | [optional] 
 **maincategory_slug** | [**List[str]**](str.md)|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 

### Return type

[**V1PublicSignalsGeographyRetrieve200Response**](V1PublicSignalsGeographyRetrieve200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_signals_retrieve**
> PublicSignalSerializerDetail v1_public_signals_retrieve(uuid)

Retrieve a public signal

### Example


```python
import signals_api_client
from signals_api_client.models.public_signal_serializer_detail import PublicSignalSerializerDetail
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    uuid = 'uuid_example' # str | 

    try:
        api_response = await api_instance.v1_public_signals_retrieve(uuid)
        print("The response of V1Api->v1_public_signals_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_public_signals_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**PublicSignalSerializerDetail**](PublicSignalSerializerDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_terms_categories_list**
> PaginatedCategoryList v1_public_terms_categories_list(page=page, page_size=page_size)

Add custom serializer for detail view

### Example


```python
import signals_api_client
from signals_api_client.models.paginated_category_list import PaginatedCategoryList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = await api_instance.v1_public_terms_categories_list(page=page, page_size=page_size)
        print("The response of V1Api->v1_public_terms_categories_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_public_terms_categories_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedCategoryList**](PaginatedCategoryList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_terms_categories_retrieve**
> Category v1_public_terms_categories_retrieve(slug)

Add custom serializer for detail view

### Example


```python
import signals_api_client
from signals_api_client.models.category import Category
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = await api_instance.v1_public_terms_categories_retrieve(slug)
        print("The response of V1Api->v1_public_terms_categories_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_public_terms_categories_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**Category**](Category.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_terms_categories_sub_categories_list**
> PaginatedCategoryList v1_public_terms_categories_sub_categories_list(parent_lookup_parent__slug, page=page, page_size=page_size)

Add custom serializer for detail view

### Example


```python
import signals_api_client
from signals_api_client.models.paginated_category_list import PaginatedCategoryList
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    parent_lookup_parent__slug = 'parent_lookup_parent__slug_example' # str | 
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        api_response = await api_instance.v1_public_terms_categories_sub_categories_list(parent_lookup_parent__slug, page=page, page_size=page_size)
        print("The response of V1Api->v1_public_terms_categories_sub_categories_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_public_terms_categories_sub_categories_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_parent__slug** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedCategoryList**](PaginatedCategoryList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_terms_categories_sub_categories_retrieve**
> Category v1_public_terms_categories_sub_categories_retrieve(parent_lookup_parent__slug, slug)

Add custom serializer for detail view

### Example


```python
import signals_api_client
from signals_api_client.models.category import Category
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)
    parent_lookup_parent__slug = 'parent_lookup_parent__slug_example' # str | 
    slug = 'slug_example' # str | 

    try:
        api_response = await api_instance.v1_public_terms_categories_sub_categories_retrieve(parent_lookup_parent__slug, slug)
        print("The response of V1Api->v1_public_terms_categories_sub_categories_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->v1_public_terms_categories_sub_categories_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_lookup_parent__slug** | **str**|  | 
 **slug** | **str**|  | 

### Return type

[**Category**](Category.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_translations_json_retrieve**
> v1_public_translations_json_retrieve()

Retrieve the latest I18Next translation file.

Args:
    request (Request): The incoming request.
    *args (set): Additional positional arguments.
    **kwargs (dict): Additional keyword arguments.

Returns:
    Response | FileResponse: A FileResponse with the file content or Response (404) if the file doesn't exist.

### Example


```python
import signals_api_client
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)

    try:
        await api_instance.v1_public_translations_json_retrieve()
    except Exception as e:
        print("Exception when calling V1Api->v1_public_translations_json_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_relations_retrieve**
> v1_relations_retrieve()

Used for the curies namespace, at this moment it is just a dummy landing page so that we have
a valid URI that resolves

TODO: Implement HAL standard for curies in the future

### Example


```python
import signals_api_client
from signals_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = signals_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with signals_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = signals_api_client.V1Api(api_client)

    try:
        await api_instance.v1_relations_retrieve()
    except Exception as e:
        print("Exception when calling V1Api->v1_relations_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

