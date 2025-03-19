# coding: utf-8

"""
    Signalen API

    One of the tasks of a municipality is to maintain public spaces. When citizens have complaints about public spaces they can leave these complaints with the municipality. Signalen (SIG) receives these complaints and is used to track progress towards their resolution. SIG provides an API that is used both by the SIG frontend and external systems that integrate with SIG.

    The version of the OpenAPI document: 2.41.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from signals_api_client.models.private_signal_serializer_list import PrivateSignalSerializerList

class TestPrivateSignalSerializerList(unittest.TestCase):
    """PrivateSignalSerializerList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrivateSignalSerializerList:
        """Test PrivateSignalSerializerList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrivateSignalSerializerList`
        """
        model = PrivateSignalSerializerList()
        if include_optional:
            return PrivateSignalSerializerList(
                links = signals_api_client.models._links. links(
                    self = signals_api_client.models._links_self._links_self(
                        href = 'https://api.example.com/signals/v1/private/signals/1', ), ),
                display = '',
                id = 56,
                id_display = '',
                signal_id = '',
                source = '',
                text = '',
                text_extra = '',
                status = signals_api_client.models._nested_status_model._NestedStatusModel(
                    text = '', 
                    user = '', 
                    state = null, 
                    state_display = '', 
                    target_api = null, 
                    extra_properties = null, 
                    send_email = True, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    email_override = '', ),
                location = signals_api_client.models._nested_location_model._NestedLocationModel(
                    id = 56, 
                    stadsdeel = 'A', 
                    buurt_code = '', 
                    area_type_code = '', 
                    area_code = '', 
                    area_name = '', 
                    address = null, 
                    address_text = '', 
                    postcode = '', 
                    geometrie = signals_api_client.models._nested_location_model_geometrie._NestedLocationModel_geometrie(
                        type = 'Point', 
                        coordinates = [12.9721,77.5933], ), 
                    extra_properties = null, 
                    created_by = '', 
                    bag_validated = True, ),
                category = signals_api_client.models._nested_category_model._NestedCategoryModel(
                    sub_category = 'https://api.example.com/signals/v1/public/terms/categories/1/sub_categories/2/', 
                    sub = '', 
                    sub_slug = '', 
                    main = '', 
                    main_slug = '', 
                    category_url = 'https://api.example.com/signals/v1/public/terms/categories/1/sub_categories/2/', 
                    departments = '', 
                    created_by = '', 
                    text = '', 
                    deadline = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    deadline_factor_3 = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                reporter = signals_api_client.models._nested_reporter_model._NestedReporterModel(
                    email = '', 
                    phone = '', 
                    sharing_allowed = True, 
                    allows_contact = True, ),
                priority = signals_api_client.models._nested_priority_model._NestedPriorityModel(
                    created_by = '', ),
                type = signals_api_client.models._nested_type_model._NestedTypeModel(
                    code = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created_by = '', ),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                incident_date_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                incident_date_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                operational_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                has_attachments = '',
                extra_properties = None,
                notes = [
                    signals_api_client.models._nested_note_model._NestedNoteModel(
                        text = '', 
                        created_by = '', )
                    ],
                directing_departments = [
                    signals_api_client.models._nested_department_model._NestedDepartmentModel(
                        id = 56, 
                        code = '', 
                        name = '', 
                        is_intern = True, )
                    ],
                routing_departments = [
                    signals_api_client.models._nested_department_model._NestedDepartmentModel(
                        id = 56, 
                        code = '', 
                        name = '', 
                        is_intern = True, )
                    ],
                attachments = [
                    'https://api.example.com/signals/v1/private/signals/1/attachments/1'
                    ],
                parent = 56,
                has_parent = '',
                has_children = '',
                assigned_user_email = '',
                session = ''
            )
        else:
            return PrivateSignalSerializerList(
                links = signals_api_client.models._links. links(
                    self = signals_api_client.models._links_self._links_self(
                        href = 'https://api.example.com/signals/v1/private/signals/1', ), ),
                display = '',
                id = 56,
                id_display = '',
                signal_id = '',
                text = '',
                location = signals_api_client.models._nested_location_model._NestedLocationModel(
                    id = 56, 
                    stadsdeel = 'A', 
                    buurt_code = '', 
                    area_type_code = '', 
                    area_code = '', 
                    area_name = '', 
                    address = null, 
                    address_text = '', 
                    postcode = '', 
                    geometrie = signals_api_client.models._nested_location_model_geometrie._NestedLocationModel_geometrie(
                        type = 'Point', 
                        coordinates = [12.9721,77.5933], ), 
                    extra_properties = null, 
                    created_by = '', 
                    bag_validated = True, ),
                category = signals_api_client.models._nested_category_model._NestedCategoryModel(
                    sub_category = 'https://api.example.com/signals/v1/public/terms/categories/1/sub_categories/2/', 
                    sub = '', 
                    sub_slug = '', 
                    main = '', 
                    main_slug = '', 
                    category_url = 'https://api.example.com/signals/v1/public/terms/categories/1/sub_categories/2/', 
                    departments = '', 
                    created_by = '', 
                    text = '', 
                    deadline = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    deadline_factor_3 = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                reporter = signals_api_client.models._nested_reporter_model._NestedReporterModel(
                    email = '', 
                    phone = '', 
                    sharing_allowed = True, 
                    allows_contact = True, ),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                incident_date_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                has_attachments = '',
                has_parent = '',
                has_children = '',
        )
        """

    def testPrivateSignalSerializerList(self):
        """Test PrivateSignalSerializerList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
