# signals-api-client
One of the tasks of a municipality is to maintain public spaces. When citizens have complaints about public spaces they can leave these complaints with the municipality. Signalen (SIG) receives these complaints and is used to track progress towards their resolution. SIG provides an API that is used both by the SIG frontend and external systems that integrate with SIG.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.41.0
- Package version: 1.0.0
- Generator version: 7.12.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/Amsterdam/signals-api-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Amsterdam/signals-api-client.git`)

Then import the package:
```python
import signals_api_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import signals_api_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    except ApiException as e:
        print("Exception when calling V1Api->upload_file: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*V1Api* | [**upload_file**](docs/V1Api.md#upload_file) | **POST** /signals/v1/public/signals/{uuid}/attachments/ | 
*V1Api* | [**v1_my_signals_history_list**](docs/V1Api.md#v1_my_signals_history_list) | **GET** /signals/v1/my/signals/{uuid}/history/ | 
*V1Api* | [**v1_my_signals_list**](docs/V1Api.md#v1_my_signals_list) | **GET** /signals/v1/my/signals/ | 
*V1Api* | [**v1_my_signals_me_retrieve**](docs/V1Api.md#v1_my_signals_me_retrieve) | **GET** /signals/v1/my/signals/me | 
*V1Api* | [**v1_my_signals_request_auth_token_create**](docs/V1Api.md#v1_my_signals_request_auth_token_create) | **POST** /signals/v1/my/signals/request-auth-token | 
*V1Api* | [**v1_my_signals_retrieve**](docs/V1Api.md#v1_my_signals_retrieve) | **GET** /signals/v1/my/signals/{uuid}/ | 
*V1Api* | [**v1_private_areas_geography_retrieve**](docs/V1Api.md#v1_private_areas_geography_retrieve) | **GET** /signals/v1/private/areas/geography/ | 
*V1Api* | [**v1_private_areas_list**](docs/V1Api.md#v1_private_areas_list) | **GET** /signals/v1/private/areas/ | 
*V1Api* | [**v1_private_autocomplete_usernames_list**](docs/V1Api.md#v1_private_autocomplete_usernames_list) | **GET** /signals/v1/private/autocomplete/usernames/ | 
*V1Api* | [**v1_private_categories_history_list**](docs/V1Api.md#v1_private_categories_history_list) | **GET** /signals/v1/private/categories/{id}/history/ | 
*V1Api* | [**v1_private_categories_icon_destroy**](docs/V1Api.md#v1_private_categories_icon_destroy) | **DELETE** /signals/v1/private/categories/{category_id}/icon | 
*V1Api* | [**v1_private_categories_icon_partial_update**](docs/V1Api.md#v1_private_categories_icon_partial_update) | **PATCH** /signals/v1/private/categories/{category_id}/icon | 
*V1Api* | [**v1_private_categories_icon_retrieve**](docs/V1Api.md#v1_private_categories_icon_retrieve) | **GET** /signals/v1/private/categories/{category_id}/icon | 
*V1Api* | [**v1_private_categories_icon_update**](docs/V1Api.md#v1_private_categories_icon_update) | **PUT** /signals/v1/private/categories/{category_id}/icon | 
*V1Api* | [**v1_private_categories_list**](docs/V1Api.md#v1_private_categories_list) | **GET** /signals/v1/private/categories/ | 
*V1Api* | [**v1_private_categories_partial_update**](docs/V1Api.md#v1_private_categories_partial_update) | **PATCH** /signals/v1/private/categories/{id}/ | 
*V1Api* | [**v1_private_categories_retrieve**](docs/V1Api.md#v1_private_categories_retrieve) | **GET** /signals/v1/private/categories/{id}/ | 
*V1Api* | [**v1_private_categories_update**](docs/V1Api.md#v1_private_categories_update) | **PUT** /signals/v1/private/categories/{id}/ | 
*V1Api* | [**v1_private_csv_retrieve**](docs/V1Api.md#v1_private_csv_retrieve) | **GET** /signals/v1/private/csv/ | 
*V1Api* | [**v1_private_departments_create**](docs/V1Api.md#v1_private_departments_create) | **POST** /signals/v1/private/departments/ | 
*V1Api* | [**v1_private_departments_list**](docs/V1Api.md#v1_private_departments_list) | **GET** /signals/v1/private/departments/ | 
*V1Api* | [**v1_private_departments_partial_update**](docs/V1Api.md#v1_private_departments_partial_update) | **PATCH** /signals/v1/private/departments/{id}/ | 
*V1Api* | [**v1_private_departments_retrieve**](docs/V1Api.md#v1_private_departments_retrieve) | **GET** /signals/v1/private/departments/{id}/ | 
*V1Api* | [**v1_private_departments_update**](docs/V1Api.md#v1_private_departments_update) | **PUT** /signals/v1/private/departments/{id}/ | 
*V1Api* | [**v1_private_expressions_context_retrieve**](docs/V1Api.md#v1_private_expressions_context_retrieve) | **GET** /signals/v1/private/expressions/context/ | 
*V1Api* | [**v1_private_expressions_create**](docs/V1Api.md#v1_private_expressions_create) | **POST** /signals/v1/private/expressions/ | 
*V1Api* | [**v1_private_expressions_destroy**](docs/V1Api.md#v1_private_expressions_destroy) | **DELETE** /signals/v1/private/expressions/{id}/ | 
*V1Api* | [**v1_private_expressions_list**](docs/V1Api.md#v1_private_expressions_list) | **GET** /signals/v1/private/expressions/ | 
*V1Api* | [**v1_private_expressions_partial_update**](docs/V1Api.md#v1_private_expressions_partial_update) | **PATCH** /signals/v1/private/expressions/{id}/ | 
*V1Api* | [**v1_private_expressions_retrieve**](docs/V1Api.md#v1_private_expressions_retrieve) | **GET** /signals/v1/private/expressions/{id}/ | 
*V1Api* | [**v1_private_expressions_update**](docs/V1Api.md#v1_private_expressions_update) | **PUT** /signals/v1/private/expressions/{id}/ | 
*V1Api* | [**v1_private_expressions_validate_retrieve**](docs/V1Api.md#v1_private_expressions_validate_retrieve) | **GET** /signals/v1/private/expressions/validate/ | 
*V1Api* | [**v1_private_me_filters_create**](docs/V1Api.md#v1_private_me_filters_create) | **POST** /signals/v1/private/me/filters/ | 
*V1Api* | [**v1_private_me_filters_destroy**](docs/V1Api.md#v1_private_me_filters_destroy) | **DELETE** /signals/v1/private/me/filters/{id}/ | 
*V1Api* | [**v1_private_me_filters_list**](docs/V1Api.md#v1_private_me_filters_list) | **GET** /signals/v1/private/me/filters/ | 
*V1Api* | [**v1_private_me_filters_partial_update**](docs/V1Api.md#v1_private_me_filters_partial_update) | **PATCH** /signals/v1/private/me/filters/{id}/ | 
*V1Api* | [**v1_private_me_filters_retrieve**](docs/V1Api.md#v1_private_me_filters_retrieve) | **GET** /signals/v1/private/me/filters/{id}/ | 
*V1Api* | [**v1_private_me_filters_update**](docs/V1Api.md#v1_private_me_filters_update) | **PUT** /signals/v1/private/me/filters/{id}/ | 
*V1Api* | [**v1_private_me_retrieve**](docs/V1Api.md#v1_private_me_retrieve) | **GET** /signals/v1/private/me/ | 
*V1Api* | [**v1_private_permissions_list**](docs/V1Api.md#v1_private_permissions_list) | **GET** /signals/v1/private/permissions/ | 
*V1Api* | [**v1_private_permissions_retrieve**](docs/V1Api.md#v1_private_permissions_retrieve) | **GET** /signals/v1/private/permissions/{id}/ | 
*V1Api* | [**v1_private_reports_signals_open_list**](docs/V1Api.md#v1_private_reports_signals_open_list) | **GET** /signals/v1/private/reports/signals/open/ | 
*V1Api* | [**v1_private_reports_signals_reopen_requested_list**](docs/V1Api.md#v1_private_reports_signals_reopen_requested_list) | **GET** /signals/v1/private/reports/signals/reopen-requested/ | 
*V1Api* | [**v1_private_roles_create**](docs/V1Api.md#v1_private_roles_create) | **POST** /signals/v1/private/roles/ | 
*V1Api* | [**v1_private_roles_destroy**](docs/V1Api.md#v1_private_roles_destroy) | **DELETE** /signals/v1/private/roles/{id}/ | 
*V1Api* | [**v1_private_roles_list**](docs/V1Api.md#v1_private_roles_list) | **GET** /signals/v1/private/roles/ | 
*V1Api* | [**v1_private_roles_partial_update**](docs/V1Api.md#v1_private_roles_partial_update) | **PATCH** /signals/v1/private/roles/{id}/ | 
*V1Api* | [**v1_private_roles_retrieve**](docs/V1Api.md#v1_private_roles_retrieve) | **GET** /signals/v1/private/roles/{id}/ | 
*V1Api* | [**v1_private_roles_update**](docs/V1Api.md#v1_private_roles_update) | **PUT** /signals/v1/private/roles/{id}/ | 
*V1Api* | [**v1_private_search_list**](docs/V1Api.md#v1_private_search_list) | **GET** /signals/v1/private/search/ | 
*V1Api* | [**v1_private_signals_attachments_create**](docs/V1Api.md#v1_private_signals_attachments_create) | **POST** /signals/v1/private/signals/{parent_lookup__signal__pk}/attachments/ | 
*V1Api* | [**v1_private_signals_attachments_destroy**](docs/V1Api.md#v1_private_signals_attachments_destroy) | **DELETE** /signals/v1/private/signals/{parent_lookup__signal__pk}/attachments/{id}/ | 
*V1Api* | [**v1_private_signals_attachments_list**](docs/V1Api.md#v1_private_signals_attachments_list) | **GET** /signals/v1/private/signals/{parent_lookup__signal__pk}/attachments/ | 
*V1Api* | [**v1_private_signals_attachments_partial_update**](docs/V1Api.md#v1_private_signals_attachments_partial_update) | **PATCH** /signals/v1/private/signals/{parent_lookup__signal__pk}/attachments/{id}/ | 
*V1Api* | [**v1_private_signals_attachments_retrieve**](docs/V1Api.md#v1_private_signals_attachments_retrieve) | **GET** /signals/v1/private/signals/{parent_lookup__signal__pk}/attachments/{id}/ | 
*V1Api* | [**v1_private_signals_attachments_update**](docs/V1Api.md#v1_private_signals_attachments_update) | **PUT** /signals/v1/private/signals/{parent_lookup__signal__pk}/attachments/{id}/ | 
*V1Api* | [**v1_private_signals_category_removed_list**](docs/V1Api.md#v1_private_signals_category_removed_list) | **GET** /signals/v1/private/signals/category/removed/ | 
*V1Api* | [**v1_private_signals_children_list**](docs/V1Api.md#v1_private_signals_children_list) | **GET** /signals/v1/private/signals/{id}/children/ | 
*V1Api* | [**v1_private_signals_context_near_geography_retrieve**](docs/V1Api.md#v1_private_signals_context_near_geography_retrieve) | **GET** /signals/v1/private/signals/{id}/context/near/geography/ | 
*V1Api* | [**v1_private_signals_context_reporter_list**](docs/V1Api.md#v1_private_signals_context_reporter_list) | **GET** /signals/v1/private/signals/{id}/context/reporter/ | 
*V1Api* | [**v1_private_signals_context_retrieve**](docs/V1Api.md#v1_private_signals_context_retrieve) | **GET** /signals/v1/private/signals/{id}/context/ | 
*V1Api* | [**v1_private_signals_create**](docs/V1Api.md#v1_private_signals_create) | **POST** /signals/v1/private/signals/ | 
*V1Api* | [**v1_private_signals_email_preview_create**](docs/V1Api.md#v1_private_signals_email_preview_create) | **POST** /signals/v1/private/signals/{id}/email/preview/ | 
*V1Api* | [**v1_private_signals_geography_retrieve**](docs/V1Api.md#v1_private_signals_geography_retrieve) | **GET** /signals/v1/private/signals/geography/ | 
*V1Api* | [**v1_private_signals_history_list**](docs/V1Api.md#v1_private_signals_history_list) | **GET** /signals/v1/private/signals/{id}/history/ | 
*V1Api* | [**v1_private_signals_list**](docs/V1Api.md#v1_private_signals_list) | **GET** /signals/v1/private/signals/ | 
*V1Api* | [**v1_private_signals_partial_update**](docs/V1Api.md#v1_private_signals_partial_update) | **PATCH** /signals/v1/private/signals/{id}/ | 
*V1Api* | [**v1_private_signals_pdf_retrieve**](docs/V1Api.md#v1_private_signals_pdf_retrieve) | **GET** /signals/v1/private/signals/{id}/pdf/ | 
*V1Api* | [**v1_private_signals_promoted_parent_list**](docs/V1Api.md#v1_private_signals_promoted_parent_list) | **GET** /signals/v1/private/signals/promoted/parent/ | 
*V1Api* | [**v1_private_signals_reporters_cancel_create**](docs/V1Api.md#v1_private_signals_reporters_cancel_create) | **POST** /signals/v1/private/signals/{parent_lookup__signal_id}/reporters/{id}/cancel/ | 
*V1Api* | [**v1_private_signals_reporters_create**](docs/V1Api.md#v1_private_signals_reporters_create) | **POST** /signals/v1/private/signals/{parent_lookup__signal_id}/reporters/ | 
*V1Api* | [**v1_private_signals_reporters_list**](docs/V1Api.md#v1_private_signals_reporters_list) | **GET** /signals/v1/private/signals/{parent_lookup__signal_id}/reporters/ | 
*V1Api* | [**v1_private_signals_retrieve**](docs/V1Api.md#v1_private_signals_retrieve) | **GET** /signals/v1/private/signals/{id}/ | 
*V1Api* | [**v1_private_sources_list**](docs/V1Api.md#v1_private_sources_list) | **GET** /signals/v1/private/sources/ | 
*V1Api* | [**v1_private_sources_retrieve**](docs/V1Api.md#v1_private_sources_retrieve) | **GET** /signals/v1/private/sources/{id}/ | 
*V1Api* | [**v1_private_status_messages_category_create**](docs/V1Api.md#v1_private_status_messages_category_create) | **POST** /signals/v1/private/status-messages/category/{category_id}/ | 
*V1Api* | [**v1_private_status_messages_create**](docs/V1Api.md#v1_private_status_messages_create) | **POST** /signals/v1/private/status-messages/ | 
*V1Api* | [**v1_private_status_messages_destroy**](docs/V1Api.md#v1_private_status_messages_destroy) | **DELETE** /signals/v1/private/status-messages/{id}/ | 
*V1Api* | [**v1_private_status_messages_list**](docs/V1Api.md#v1_private_status_messages_list) | **GET** /signals/v1/private/status-messages/ | 
*V1Api* | [**v1_private_status_messages_partial_update**](docs/V1Api.md#v1_private_status_messages_partial_update) | **PATCH** /signals/v1/private/status-messages/{id}/ | 
*V1Api* | [**v1_private_status_messages_retrieve**](docs/V1Api.md#v1_private_status_messages_retrieve) | **GET** /signals/v1/private/status-messages/{id}/ | 
*V1Api* | [**v1_private_status_messages_search_retrieve**](docs/V1Api.md#v1_private_status_messages_search_retrieve) | **GET** /signals/v1/private/status-messages/search/ | 
*V1Api* | [**v1_private_status_messages_update**](docs/V1Api.md#v1_private_status_messages_update) | **PUT** /signals/v1/private/status-messages/{id}/ | 
*V1Api* | [**v1_private_terms_categories_status_message_templates_create**](docs/V1Api.md#v1_private_terms_categories_status_message_templates_create) | **POST** /signals/v1/private/terms/categories/{slug}/status-message-templates/ | 
*V1Api* | [**v1_private_terms_categories_status_message_templates_retrieve**](docs/V1Api.md#v1_private_terms_categories_status_message_templates_retrieve) | **GET** /signals/v1/private/terms/categories/{slug}/status-message-templates/ | 
*V1Api* | [**v1_private_terms_categories_sub_categories_status_message_templates_create**](docs/V1Api.md#v1_private_terms_categories_sub_categories_status_message_templates_create) | **POST** /signals/v1/private/terms/categories/{slug}/sub_categories/{sub_slug}/status-message-templates/ | 
*V1Api* | [**v1_private_terms_categories_sub_categories_status_message_templates_retrieve**](docs/V1Api.md#v1_private_terms_categories_sub_categories_status_message_templates_retrieve) | **GET** /signals/v1/private/terms/categories/{slug}/sub_categories/{sub_slug}/status-message-templates/ | 
*V1Api* | [**v1_private_translations_create**](docs/V1Api.md#v1_private_translations_create) | **POST** /signals/v1/private/translations/ | 
*V1Api* | [**v1_private_users_create**](docs/V1Api.md#v1_private_users_create) | **POST** /signals/v1/private/users/ | 
*V1Api* | [**v1_private_users_history_retrieve**](docs/V1Api.md#v1_private_users_history_retrieve) | **GET** /signals/v1/private/users/{id}/history/ | 
*V1Api* | [**v1_private_users_list**](docs/V1Api.md#v1_private_users_list) | **GET** /signals/v1/private/users/ | 
*V1Api* | [**v1_private_users_partial_update**](docs/V1Api.md#v1_private_users_partial_update) | **PATCH** /signals/v1/private/users/{id}/ | 
*V1Api* | [**v1_private_users_retrieve**](docs/V1Api.md#v1_private_users_retrieve) | **GET** /signals/v1/private/users/{id}/ | 
*V1Api* | [**v1_public_areas_geography_retrieve**](docs/V1Api.md#v1_public_areas_geography_retrieve) | **GET** /signals/v1/public/areas/geography/ | 
*V1Api* | [**v1_public_areas_list**](docs/V1Api.md#v1_public_areas_list) | **GET** /signals/v1/public/areas/ | 
*V1Api* | [**v1_public_feedback_forms_partial_update**](docs/V1Api.md#v1_public_feedback_forms_partial_update) | **PATCH** /signals/v1/public/feedback/forms/{token}/ | 
*V1Api* | [**v1_public_feedback_forms_retrieve**](docs/V1Api.md#v1_public_feedback_forms_retrieve) | **GET** /signals/v1/public/feedback/forms/{token}/ | 
*V1Api* | [**v1_public_feedback_forms_update**](docs/V1Api.md#v1_public_feedback_forms_update) | **PUT** /signals/v1/public/feedback/forms/{token}/ | 
*V1Api* | [**v1_public_feedback_standard_answers_list**](docs/V1Api.md#v1_public_feedback_standard_answers_list) | **GET** /signals/v1/public/feedback/standard_answers/ | 
*V1Api* | [**v1_public_questions_list**](docs/V1Api.md#v1_public_questions_list) | **GET** /signals/v1/public/questions/ | 
*V1Api* | [**v1_public_reporter_verify_email_create**](docs/V1Api.md#v1_public_reporter_verify_email_create) | **POST** /signals/v1/public/reporter/verify-email | 
*V1Api* | [**v1_public_signals_create**](docs/V1Api.md#v1_public_signals_create) | **POST** /signals/v1/public/signals/ | 
*V1Api* | [**v1_public_signals_geography_retrieve**](docs/V1Api.md#v1_public_signals_geography_retrieve) | **GET** /signals/v1/public/signals/geography/ | 
*V1Api* | [**v1_public_signals_retrieve**](docs/V1Api.md#v1_public_signals_retrieve) | **GET** /signals/v1/public/signals/{uuid}/ | 
*V1Api* | [**v1_public_terms_categories_list**](docs/V1Api.md#v1_public_terms_categories_list) | **GET** /signals/v1/public/terms/categories/ | 
*V1Api* | [**v1_public_terms_categories_retrieve**](docs/V1Api.md#v1_public_terms_categories_retrieve) | **GET** /signals/v1/public/terms/categories/{slug}/ | 
*V1Api* | [**v1_public_terms_categories_sub_categories_list**](docs/V1Api.md#v1_public_terms_categories_sub_categories_list) | **GET** /signals/v1/public/terms/categories/{parent_lookup_parent__slug}/sub_categories/ | 
*V1Api* | [**v1_public_terms_categories_sub_categories_retrieve**](docs/V1Api.md#v1_public_terms_categories_sub_categories_retrieve) | **GET** /signals/v1/public/terms/categories/{parent_lookup_parent__slug}/sub_categories/{slug}/ | 
*V1Api* | [**v1_public_translations_json_retrieve**](docs/V1Api.md#v1_public_translations_json_retrieve) | **GET** /signals/v1/public/translations.json | 
*V1Api* | [**v1_relations_retrieve**](docs/V1Api.md#v1_relations_retrieve) | **GET** /signals/v1/relations/ | 


## Documentation For Models

 - [AbridgedChildSignal](docs/AbridgedChildSignal.md)
 - [ActiveTermsFacet](docs/ActiveTermsFacet.md)
 - [Area](docs/Area.md)
 - [AreaGeo](docs/AreaGeo.md)
 - [AreaGeoGeometry](docs/AreaGeoGeometry.md)
 - [AreaGeoProperties](docs/AreaGeoProperties.md)
 - [AreaType](docs/AreaType.md)
 - [BlankEnum](docs/BlankEnum.md)
 - [CancelSignalReporter](docs/CancelSignalReporter.md)
 - [Category](docs/Category.md)
 - [CategoryDepartment](docs/CategoryDepartment.md)
 - [CategoryHAL](docs/CategoryHAL.md)
 - [EmailPreview](docs/EmailPreview.md)
 - [EmailPreviewPost](docs/EmailPreviewPost.md)
 - [EmailVerification](docs/EmailVerification.md)
 - [Expression](docs/Expression.md)
 - [Feedback](docs/Feedback.md)
 - [FieldTypeEnum](docs/FieldTypeEnum.md)
 - [GenericError](docs/GenericError.md)
 - [GisFeatureEnum](docs/GisFeatureEnum.md)
 - [HandlingEnum](docs/HandlingEnum.md)
 - [Highlight](docs/Highlight.md)
 - [HistoryLogHal](docs/HistoryLogHal.md)
 - [Links](docs/Links.md)
 - [Links1](docs/Links1.md)
 - [Links1Archives](docs/Links1Archives.md)
 - [Links1Curies](docs/Links1Curies.md)
 - [Links1Self](docs/Links1Self.md)
 - [Links1SiaIcon](docs/Links1SiaIcon.md)
 - [Links1SiaQuestionnaire](docs/Links1SiaQuestionnaire.md)
 - [Links2](docs/Links2.md)
 - [Links2SiaStatusMessageTemplates](docs/Links2SiaStatusMessageTemplates.md)
 - [Links3](docs/Links3.md)
 - [Links3Self](docs/Links3Self.md)
 - [Links4](docs/Links4.md)
 - [Links4Self](docs/Links4Self.md)
 - [Links5](docs/Links5.md)
 - [Links5Self](docs/Links5Self.md)
 - [Links6](docs/Links6.md)
 - [Links6Archives](docs/Links6Archives.md)
 - [Links6Self](docs/Links6Self.md)
 - [Links6SiaAttachments](docs/Links6SiaAttachments.md)
 - [Links6SiaChildrenInner](docs/Links6SiaChildrenInner.md)
 - [Links6SiaContext](docs/Links6SiaContext.md)
 - [Links6SiaPdf](docs/Links6SiaPdf.md)
 - [Links7](docs/Links7.md)
 - [Links7SiaContextGeographyDetail](docs/Links7SiaContextGeographyDetail.md)
 - [Links7SiaContextReporterDetail](docs/Links7SiaContextReporterDetail.md)
 - [Links8](docs/Links8.md)
 - [Links8Archives](docs/Links8Archives.md)
 - [Links8Self](docs/Links8Self.md)
 - [Links8SiaAttachmentsInner](docs/Links8SiaAttachmentsInner.md)
 - [Links9](docs/Links9.md)
 - [LinksSelf](docs/LinksSelf.md)
 - [Meta](docs/Meta.md)
 - [MySignalsLoggedInReporter](docs/MySignalsLoggedInReporter.md)
 - [MySignalsToken](docs/MySignalsToken.md)
 - [NestedCategoryModel](docs/NestedCategoryModel.md)
 - [NestedDepartmentModel](docs/NestedDepartmentModel.md)
 - [NestedLocationModel](docs/NestedLocationModel.md)
 - [NestedLocationModelGeometrie](docs/NestedLocationModelGeometrie.md)
 - [NestedMySignalLocation](docs/NestedMySignalLocation.md)
 - [NestedMySignalLocationGeometrie](docs/NestedMySignalLocationGeometrie.md)
 - [NestedMySignalStatus](docs/NestedMySignalStatus.md)
 - [NestedNoteModel](docs/NestedNoteModel.md)
 - [NestedPriorityModel](docs/NestedPriorityModel.md)
 - [NestedPrivateCategoryDepartment](docs/NestedPrivateCategoryDepartment.md)
 - [NestedPublicDepartment](docs/NestedPublicDepartment.md)
 - [NestedPublicStatusModel](docs/NestedPublicStatusModel.md)
 - [NestedReporterModel](docs/NestedReporterModel.md)
 - [NestedStatusModel](docs/NestedStatusModel.md)
 - [NestedStatusModelState](docs/NestedStatusModelState.md)
 - [NestedStatusModelTargetApi](docs/NestedStatusModelTargetApi.md)
 - [NestedTypeModel](docs/NestedTypeModel.md)
 - [PaginatedAbridgedChildSignalList](docs/PaginatedAbridgedChildSignalList.md)
 - [PaginatedAbridgedChildSignalListLinks](docs/PaginatedAbridgedChildSignalListLinks.md)
 - [PaginatedAbridgedChildSignalListLinksNext](docs/PaginatedAbridgedChildSignalListLinksNext.md)
 - [PaginatedAbridgedChildSignalListLinksPrevious](docs/PaginatedAbridgedChildSignalListLinksPrevious.md)
 - [PaginatedAbridgedChildSignalListLinksSelf](docs/PaginatedAbridgedChildSignalListLinksSelf.md)
 - [PaginatedAreaList](docs/PaginatedAreaList.md)
 - [PaginatedCategoryList](docs/PaginatedCategoryList.md)
 - [PaginatedExpressionList](docs/PaginatedExpressionList.md)
 - [PaginatedPermissionList](docs/PaginatedPermissionList.md)
 - [PaginatedPrivateCategoryList](docs/PaginatedPrivateCategoryList.md)
 - [PaginatedPrivateDepartmentSerializerListList](docs/PaginatedPrivateDepartmentSerializerListList.md)
 - [PaginatedPrivateSignalAttachmentList](docs/PaginatedPrivateSignalAttachmentList.md)
 - [PaginatedPrivateSignalSerializerListList](docs/PaginatedPrivateSignalSerializerListList.md)
 - [PaginatedPublicQuestionSerializerDetailList](docs/PaginatedPublicQuestionSerializerDetailList.md)
 - [PaginatedRoleList](docs/PaginatedRoleList.md)
 - [PaginatedSignalContextReporterList](docs/PaginatedSignalContextReporterList.md)
 - [PaginatedSignalIdListList](docs/PaginatedSignalIdListList.md)
 - [PaginatedSignalListList](docs/PaginatedSignalListList.md)
 - [PaginatedSignalReporterList](docs/PaginatedSignalReporterList.md)
 - [PaginatedSourceList](docs/PaginatedSourceList.md)
 - [PaginatedStandardAnswerList](docs/PaginatedStandardAnswerList.md)
 - [PaginatedStatusMessageList](docs/PaginatedStatusMessageList.md)
 - [PaginatedStoredSignalFilterList](docs/PaginatedStoredSignalFilterList.md)
 - [PaginatedUserListHALList](docs/PaginatedUserListHALList.md)
 - [PaginatedUserNameListList](docs/PaginatedUserNameListList.md)
 - [ParentCategoryHAL](docs/ParentCategoryHAL.md)
 - [PatchedExpression](docs/PatchedExpression.md)
 - [PatchedFeedback](docs/PatchedFeedback.md)
 - [PatchedPrivateCategory](docs/PatchedPrivateCategory.md)
 - [PatchedPrivateDepartmentSerializerList](docs/PatchedPrivateDepartmentSerializerList.md)
 - [PatchedPrivateSignalAttachmentUpdate](docs/PatchedPrivateSignalAttachmentUpdate.md)
 - [PatchedPrivateSignalSerializerList](docs/PatchedPrivateSignalSerializerList.md)
 - [PatchedRole](docs/PatchedRole.md)
 - [PatchedStatusMessage](docs/PatchedStatusMessage.md)
 - [PatchedStoredSignalFilter](docs/PatchedStoredSignalFilter.md)
 - [PatchedUserDetailHAL](docs/PatchedUserDetailHAL.md)
 - [Permission](docs/Permission.md)
 - [PriorityEnum](docs/PriorityEnum.md)
 - [PrivateCategory](docs/PrivateCategory.md)
 - [PrivateCategoryHistoryHal](docs/PrivateCategoryHistoryHal.md)
 - [PrivateCategoryIcon](docs/PrivateCategoryIcon.md)
 - [PrivateCategorySLA](docs/PrivateCategorySLA.md)
 - [PrivateDepartmentSerializerDetail](docs/PrivateDepartmentSerializerDetail.md)
 - [PrivateDepartmentSerializerList](docs/PrivateDepartmentSerializerList.md)
 - [PrivateSignalAttachment](docs/PrivateSignalAttachment.md)
 - [PrivateSignalAttachmentUpdate](docs/PrivateSignalAttachmentUpdate.md)
 - [PrivateSignalSerializerDetail](docs/PrivateSignalSerializerDetail.md)
 - [PrivateSignalSerializerList](docs/PrivateSignalSerializerList.md)
 - [PrivateUserHistoryHal](docs/PrivateUserHistoryHal.md)
 - [ProfileDetail](docs/ProfileDetail.md)
 - [ProfileList](docs/ProfileList.md)
 - [PublicQuestionSerializerDetail](docs/PublicQuestionSerializerDetail.md)
 - [PublicSignalAttachment](docs/PublicSignalAttachment.md)
 - [PublicSignalCreate](docs/PublicSignalCreate.md)
 - [PublicSignalSerializerDetail](docs/PublicSignalSerializerDetail.md)
 - [ReportSignalsPerCategory](docs/ReportSignalsPerCategory.md)
 - [Role](docs/Role.md)
 - [RoutingExpression](docs/RoutingExpression.md)
 - [SignalContext](docs/SignalContext.md)
 - [SignalContextNear](docs/SignalContextNear.md)
 - [SignalContextReporter](docs/SignalContextReporter.md)
 - [SignalContextReporterCategory](docs/SignalContextReporterCategory.md)
 - [SignalContextReporterFeedback](docs/SignalContextReporterFeedback.md)
 - [SignalContextReporterStatus](docs/SignalContextReporterStatus.md)
 - [SignalDetail](docs/SignalDetail.md)
 - [SignalIdList](docs/SignalIdList.md)
 - [SignalList](docs/SignalList.md)
 - [SignalReporter](docs/SignalReporter.md)
 - [SignalsPerCategoryCount](docs/SignalsPerCategoryCount.md)
 - [SimpleCategory](docs/SimpleCategory.md)
 - [Source](docs/Source.md)
 - [StadsdeelEnum](docs/StadsdeelEnum.md)
 - [StandardAnswer](docs/StandardAnswer.md)
 - [StateA07Enum](docs/StateA07Enum.md)
 - [StateStatusMessageTemplate](docs/StateStatusMessageTemplate.md)
 - [StateStatusMessageTemplateStateEnum](docs/StateStatusMessageTemplateStateEnum.md)
 - [StateTermsFacet](docs/StateTermsFacet.md)
 - [StatusEnum](docs/StatusEnum.md)
 - [StatusMessage](docs/StatusMessage.md)
 - [StatusMessageCategoryPosition](docs/StatusMessageCategoryPosition.md)
 - [StatusMessageFacet](docs/StatusMessageFacet.md)
 - [StatusMessageList](docs/StatusMessageList.md)
 - [StatusMessageSearchResult](docs/StatusMessageSearchResult.md)
 - [StoredSignalFilter](docs/StoredSignalFilter.md)
 - [TargetApiEnum](docs/TargetApiEnum.md)
 - [TemporaryCategoryHAL](docs/TemporaryCategoryHAL.md)
 - [TemporaryParentCategoryHAL](docs/TemporaryParentCategoryHAL.md)
 - [TmpCategory](docs/TmpCategory.md)
 - [UserDetailHAL](docs/UserDetailHAL.md)
 - [UserListHAL](docs/UserListHAL.md)
 - [UserNameList](docs/UserNameList.md)
 - [V1PrivateSignalsContextNearGeographyRetrieve200Response](docs/V1PrivateSignalsContextNearGeographyRetrieve200Response.md)
 - [V1PrivateSignalsContextNearGeographyRetrieve200ResponseFeaturesInner](docs/V1PrivateSignalsContextNearGeographyRetrieve200ResponseFeaturesInner.md)
 - [V1PrivateSignalsContextNearGeographyRetrieve200ResponseFeaturesInnerGeometry](docs/V1PrivateSignalsContextNearGeographyRetrieve200ResponseFeaturesInnerGeometry.md)
 - [V1PrivateSignalsContextNearGeographyRetrieve200ResponseFeaturesInnerProperties](docs/V1PrivateSignalsContextNearGeographyRetrieve200ResponseFeaturesInnerProperties.md)
 - [V1PrivateSignalsGeographyRetrieve200Response](docs/V1PrivateSignalsGeographyRetrieve200Response.md)
 - [V1PrivateSignalsGeographyRetrieve200ResponseFeaturesInner](docs/V1PrivateSignalsGeographyRetrieve200ResponseFeaturesInner.md)
 - [V1PrivateSignalsGeographyRetrieve200ResponseFeaturesInnerProperties](docs/V1PrivateSignalsGeographyRetrieve200ResponseFeaturesInnerProperties.md)
 - [V1PublicSignalsGeographyRetrieve200Response](docs/V1PublicSignalsGeographyRetrieve200Response.md)
 - [V1PublicSignalsGeographyRetrieve200ResponseFeaturesInner](docs/V1PublicSignalsGeographyRetrieve200ResponseFeaturesInner.md)
 - [V1PublicSignalsGeographyRetrieve200ResponseFeaturesInnerProperties](docs/V1PublicSignalsGeographyRetrieve200ResponseFeaturesInnerProperties.md)
 - [V1PublicSignalsGeographyRetrieve200ResponseFeaturesInnerPropertiesCategory](docs/V1PublicSignalsGeographyRetrieve200ResponseFeaturesInnerPropertiesCategory.md)
 - [V1PublicSignalsGeographyRetrieve200ResponseFeaturesInnerPropertiesCategoryParent](docs/V1PublicSignalsGeographyRetrieve200ResponseFeaturesInnerPropertiesCategoryParent.md)
 - [ValidationError](docs/ValidationError.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="JWTAuthBackend"></a>
### JWTAuthBackend

- **Type**: Bearer authentication (JWT)

<a id="tokenAuth"></a>
### tokenAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




