# coding: utf-8

"""
    Signalen API

    One of the tasks of a municipality is to maintain public spaces. When citizens have complaints about public spaces they can leave these complaints with the municipality. Signalen (SIG) receives these complaints and is used to track progress towards their resolution. SIG provides an API that is used both by the SIG frontend and external systems that integrate with SIG.

    The version of the OpenAPI document: 2.41.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from signals_api_client.api.v1_api import V1Api


class TestV1Api(unittest.IsolatedAsyncioTestCase):
    """V1Api unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = V1Api()

    async def asyncTearDown(self) -> None:
        await self.api.api_client.close()

    async def test_upload_file(self) -> None:
        """Test case for upload_file

        """
        pass

    async def test_v1_my_signals_history_list(self) -> None:
        """Test case for v1_my_signals_history_list

        """
        pass

    async def test_v1_my_signals_list(self) -> None:
        """Test case for v1_my_signals_list

        """
        pass

    async def test_v1_my_signals_me_retrieve(self) -> None:
        """Test case for v1_my_signals_me_retrieve

        """
        pass

    async def test_v1_my_signals_request_auth_token_create(self) -> None:
        """Test case for v1_my_signals_request_auth_token_create

        """
        pass

    async def test_v1_my_signals_retrieve(self) -> None:
        """Test case for v1_my_signals_retrieve

        """
        pass

    async def test_v1_private_areas_geography_retrieve(self) -> None:
        """Test case for v1_private_areas_geography_retrieve

        """
        pass

    async def test_v1_private_areas_list(self) -> None:
        """Test case for v1_private_areas_list

        """
        pass

    async def test_v1_private_autocomplete_usernames_list(self) -> None:
        """Test case for v1_private_autocomplete_usernames_list

        """
        pass

    async def test_v1_private_categories_history_list(self) -> None:
        """Test case for v1_private_categories_history_list

        """
        pass

    async def test_v1_private_categories_icon_destroy(self) -> None:
        """Test case for v1_private_categories_icon_destroy

        """
        pass

    async def test_v1_private_categories_icon_partial_update(self) -> None:
        """Test case for v1_private_categories_icon_partial_update

        """
        pass

    async def test_v1_private_categories_icon_retrieve(self) -> None:
        """Test case for v1_private_categories_icon_retrieve

        """
        pass

    async def test_v1_private_categories_icon_update(self) -> None:
        """Test case for v1_private_categories_icon_update

        """
        pass

    async def test_v1_private_categories_list(self) -> None:
        """Test case for v1_private_categories_list

        """
        pass

    async def test_v1_private_categories_partial_update(self) -> None:
        """Test case for v1_private_categories_partial_update

        """
        pass

    async def test_v1_private_categories_retrieve(self) -> None:
        """Test case for v1_private_categories_retrieve

        """
        pass

    async def test_v1_private_categories_update(self) -> None:
        """Test case for v1_private_categories_update

        """
        pass

    async def test_v1_private_csv_retrieve(self) -> None:
        """Test case for v1_private_csv_retrieve

        """
        pass

    async def test_v1_private_departments_create(self) -> None:
        """Test case for v1_private_departments_create

        """
        pass

    async def test_v1_private_departments_list(self) -> None:
        """Test case for v1_private_departments_list

        """
        pass

    async def test_v1_private_departments_partial_update(self) -> None:
        """Test case for v1_private_departments_partial_update

        """
        pass

    async def test_v1_private_departments_retrieve(self) -> None:
        """Test case for v1_private_departments_retrieve

        """
        pass

    async def test_v1_private_departments_update(self) -> None:
        """Test case for v1_private_departments_update

        """
        pass

    async def test_v1_private_expressions_context_retrieve(self) -> None:
        """Test case for v1_private_expressions_context_retrieve

        """
        pass

    async def test_v1_private_expressions_create(self) -> None:
        """Test case for v1_private_expressions_create

        """
        pass

    async def test_v1_private_expressions_destroy(self) -> None:
        """Test case for v1_private_expressions_destroy

        """
        pass

    async def test_v1_private_expressions_list(self) -> None:
        """Test case for v1_private_expressions_list

        """
        pass

    async def test_v1_private_expressions_partial_update(self) -> None:
        """Test case for v1_private_expressions_partial_update

        """
        pass

    async def test_v1_private_expressions_retrieve(self) -> None:
        """Test case for v1_private_expressions_retrieve

        """
        pass

    async def test_v1_private_expressions_update(self) -> None:
        """Test case for v1_private_expressions_update

        """
        pass

    async def test_v1_private_expressions_validate_retrieve(self) -> None:
        """Test case for v1_private_expressions_validate_retrieve

        """
        pass

    async def test_v1_private_me_filters_create(self) -> None:
        """Test case for v1_private_me_filters_create

        """
        pass

    async def test_v1_private_me_filters_destroy(self) -> None:
        """Test case for v1_private_me_filters_destroy

        """
        pass

    async def test_v1_private_me_filters_list(self) -> None:
        """Test case for v1_private_me_filters_list

        """
        pass

    async def test_v1_private_me_filters_partial_update(self) -> None:
        """Test case for v1_private_me_filters_partial_update

        """
        pass

    async def test_v1_private_me_filters_retrieve(self) -> None:
        """Test case for v1_private_me_filters_retrieve

        """
        pass

    async def test_v1_private_me_filters_update(self) -> None:
        """Test case for v1_private_me_filters_update

        """
        pass

    async def test_v1_private_me_retrieve(self) -> None:
        """Test case for v1_private_me_retrieve

        """
        pass

    async def test_v1_private_permissions_list(self) -> None:
        """Test case for v1_private_permissions_list

        """
        pass

    async def test_v1_private_permissions_retrieve(self) -> None:
        """Test case for v1_private_permissions_retrieve

        """
        pass

    async def test_v1_private_reports_signals_open_list(self) -> None:
        """Test case for v1_private_reports_signals_open_list

        """
        pass

    async def test_v1_private_reports_signals_reopen_requested_list(self) -> None:
        """Test case for v1_private_reports_signals_reopen_requested_list

        """
        pass

    async def test_v1_private_roles_create(self) -> None:
        """Test case for v1_private_roles_create

        """
        pass

    async def test_v1_private_roles_destroy(self) -> None:
        """Test case for v1_private_roles_destroy

        """
        pass

    async def test_v1_private_roles_list(self) -> None:
        """Test case for v1_private_roles_list

        """
        pass

    async def test_v1_private_roles_partial_update(self) -> None:
        """Test case for v1_private_roles_partial_update

        """
        pass

    async def test_v1_private_roles_retrieve(self) -> None:
        """Test case for v1_private_roles_retrieve

        """
        pass

    async def test_v1_private_roles_update(self) -> None:
        """Test case for v1_private_roles_update

        """
        pass

    async def test_v1_private_search_list(self) -> None:
        """Test case for v1_private_search_list

        """
        pass

    async def test_v1_private_signals_attachments_create(self) -> None:
        """Test case for v1_private_signals_attachments_create

        """
        pass

    async def test_v1_private_signals_attachments_destroy(self) -> None:
        """Test case for v1_private_signals_attachments_destroy

        """
        pass

    async def test_v1_private_signals_attachments_list(self) -> None:
        """Test case for v1_private_signals_attachments_list

        """
        pass

    async def test_v1_private_signals_attachments_partial_update(self) -> None:
        """Test case for v1_private_signals_attachments_partial_update

        """
        pass

    async def test_v1_private_signals_attachments_retrieve(self) -> None:
        """Test case for v1_private_signals_attachments_retrieve

        """
        pass

    async def test_v1_private_signals_attachments_update(self) -> None:
        """Test case for v1_private_signals_attachments_update

        """
        pass

    async def test_v1_private_signals_category_removed_list(self) -> None:
        """Test case for v1_private_signals_category_removed_list

        """
        pass

    async def test_v1_private_signals_children_list(self) -> None:
        """Test case for v1_private_signals_children_list

        """
        pass

    async def test_v1_private_signals_context_near_geography_retrieve(self) -> None:
        """Test case for v1_private_signals_context_near_geography_retrieve

        """
        pass

    async def test_v1_private_signals_context_reporter_list(self) -> None:
        """Test case for v1_private_signals_context_reporter_list

        """
        pass

    async def test_v1_private_signals_context_retrieve(self) -> None:
        """Test case for v1_private_signals_context_retrieve

        """
        pass

    async def test_v1_private_signals_create(self) -> None:
        """Test case for v1_private_signals_create

        """
        pass

    async def test_v1_private_signals_email_preview_create(self) -> None:
        """Test case for v1_private_signals_email_preview_create

        """
        pass

    async def test_v1_private_signals_geography_retrieve(self) -> None:
        """Test case for v1_private_signals_geography_retrieve

        """
        pass

    async def test_v1_private_signals_history_list(self) -> None:
        """Test case for v1_private_signals_history_list

        """
        pass

    async def test_v1_private_signals_list(self) -> None:
        """Test case for v1_private_signals_list

        """
        pass

    async def test_v1_private_signals_partial_update(self) -> None:
        """Test case for v1_private_signals_partial_update

        """
        pass

    async def test_v1_private_signals_pdf_retrieve(self) -> None:
        """Test case for v1_private_signals_pdf_retrieve

        """
        pass

    async def test_v1_private_signals_promoted_parent_list(self) -> None:
        """Test case for v1_private_signals_promoted_parent_list

        """
        pass

    async def test_v1_private_signals_reporters_cancel_create(self) -> None:
        """Test case for v1_private_signals_reporters_cancel_create

        """
        pass

    async def test_v1_private_signals_reporters_create(self) -> None:
        """Test case for v1_private_signals_reporters_create

        """
        pass

    async def test_v1_private_signals_reporters_list(self) -> None:
        """Test case for v1_private_signals_reporters_list

        """
        pass

    async def test_v1_private_signals_retrieve(self) -> None:
        """Test case for v1_private_signals_retrieve

        """
        pass

    async def test_v1_private_sources_list(self) -> None:
        """Test case for v1_private_sources_list

        """
        pass

    async def test_v1_private_sources_retrieve(self) -> None:
        """Test case for v1_private_sources_retrieve

        """
        pass

    async def test_v1_private_status_messages_category_create(self) -> None:
        """Test case for v1_private_status_messages_category_create

        """
        pass

    async def test_v1_private_status_messages_create(self) -> None:
        """Test case for v1_private_status_messages_create

        """
        pass

    async def test_v1_private_status_messages_destroy(self) -> None:
        """Test case for v1_private_status_messages_destroy

        """
        pass

    async def test_v1_private_status_messages_list(self) -> None:
        """Test case for v1_private_status_messages_list

        """
        pass

    async def test_v1_private_status_messages_partial_update(self) -> None:
        """Test case for v1_private_status_messages_partial_update

        """
        pass

    async def test_v1_private_status_messages_retrieve(self) -> None:
        """Test case for v1_private_status_messages_retrieve

        """
        pass

    async def test_v1_private_status_messages_search_retrieve(self) -> None:
        """Test case for v1_private_status_messages_search_retrieve

        """
        pass

    async def test_v1_private_status_messages_update(self) -> None:
        """Test case for v1_private_status_messages_update

        """
        pass

    async def test_v1_private_terms_categories_status_message_templates_create(self) -> None:
        """Test case for v1_private_terms_categories_status_message_templates_create

        """
        pass

    async def test_v1_private_terms_categories_status_message_templates_retrieve(self) -> None:
        """Test case for v1_private_terms_categories_status_message_templates_retrieve

        """
        pass

    async def test_v1_private_terms_categories_sub_categories_status_message_templates_create(self) -> None:
        """Test case for v1_private_terms_categories_sub_categories_status_message_templates_create

        """
        pass

    async def test_v1_private_terms_categories_sub_categories_status_message_templates_retrieve(self) -> None:
        """Test case for v1_private_terms_categories_sub_categories_status_message_templates_retrieve

        """
        pass

    async def test_v1_private_translations_create(self) -> None:
        """Test case for v1_private_translations_create

        """
        pass

    async def test_v1_private_users_create(self) -> None:
        """Test case for v1_private_users_create

        """
        pass

    async def test_v1_private_users_history_retrieve(self) -> None:
        """Test case for v1_private_users_history_retrieve

        """
        pass

    async def test_v1_private_users_list(self) -> None:
        """Test case for v1_private_users_list

        """
        pass

    async def test_v1_private_users_partial_update(self) -> None:
        """Test case for v1_private_users_partial_update

        """
        pass

    async def test_v1_private_users_retrieve(self) -> None:
        """Test case for v1_private_users_retrieve

        """
        pass

    async def test_v1_public_areas_geography_retrieve(self) -> None:
        """Test case for v1_public_areas_geography_retrieve

        """
        pass

    async def test_v1_public_areas_list(self) -> None:
        """Test case for v1_public_areas_list

        """
        pass

    async def test_v1_public_feedback_forms_partial_update(self) -> None:
        """Test case for v1_public_feedback_forms_partial_update

        """
        pass

    async def test_v1_public_feedback_forms_retrieve(self) -> None:
        """Test case for v1_public_feedback_forms_retrieve

        """
        pass

    async def test_v1_public_feedback_forms_update(self) -> None:
        """Test case for v1_public_feedback_forms_update

        """
        pass

    async def test_v1_public_feedback_standard_answers_list(self) -> None:
        """Test case for v1_public_feedback_standard_answers_list

        """
        pass

    async def test_v1_public_questions_list(self) -> None:
        """Test case for v1_public_questions_list

        """
        pass

    async def test_v1_public_reporter_verify_email_create(self) -> None:
        """Test case for v1_public_reporter_verify_email_create

        """
        pass

    async def test_v1_public_signals_create(self) -> None:
        """Test case for v1_public_signals_create

        """
        pass

    async def test_v1_public_signals_geography_retrieve(self) -> None:
        """Test case for v1_public_signals_geography_retrieve

        """
        pass

    async def test_v1_public_signals_retrieve(self) -> None:
        """Test case for v1_public_signals_retrieve

        """
        pass

    async def test_v1_public_terms_categories_list(self) -> None:
        """Test case for v1_public_terms_categories_list

        """
        pass

    async def test_v1_public_terms_categories_retrieve(self) -> None:
        """Test case for v1_public_terms_categories_retrieve

        """
        pass

    async def test_v1_public_terms_categories_sub_categories_list(self) -> None:
        """Test case for v1_public_terms_categories_sub_categories_list

        """
        pass

    async def test_v1_public_terms_categories_sub_categories_retrieve(self) -> None:
        """Test case for v1_public_terms_categories_sub_categories_retrieve

        """
        pass

    async def test_v1_public_translations_json_retrieve(self) -> None:
        """Test case for v1_public_translations_json_retrieve

        """
        pass

    async def test_v1_relations_retrieve(self) -> None:
        """Test case for v1_relations_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
