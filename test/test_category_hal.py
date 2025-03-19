# coding: utf-8

"""
    Signalen API

    One of the tasks of a municipality is to maintain public spaces. When citizens have complaints about public spaces they can leave these complaints with the municipality. Signalen (SIG) receives these complaints and is used to track progress towards their resolution. SIG provides an API that is used both by the SIG frontend and external systems that integrate with SIG.

    The version of the OpenAPI document: 2.41.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from signals_api_client.models.category_hal import CategoryHAL

class TestCategoryHAL(unittest.TestCase):
    """CategoryHAL unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CategoryHAL:
        """Test CategoryHAL
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CategoryHAL`
        """
        model = CategoryHAL()
        if include_optional:
            return CategoryHAL(
                links = signals_api_client.models._links. links(
                    curies = signals_api_client.models._links_1_curies._links_1_curies(
                        href = 'https://api.example.com/signals/relations/', ), 
                    self = signals_api_client.models._links_1_self._links_1_self(
                        href = 'https://api.example.com/signals/v1/private/categories/1', ), 
                    archives = signals_api_client.models._links_1_archives._links_1_archives(
                        href = 'https://api.example.com/signals/v1/private/signals/1/history/', ), 
                    sia:questionnaire = signals_api_client.models._links_1_sia_questionnaire._links_1_sia_questionnaire(
                        href = 'https://api.example.com/signals/v1/public/qa/questionnaires/636aacb1-2813-423e-adbe-7ef84d4afc37', ), 
                    sia:icon = signals_api_client.models._links_1_sia_icon._links_1_sia_icon(
                        href = 'https://api.example.com/media/icons/1.png', ), ),
                display = '',
                name = '',
                slug = 'z',
                handling = 'A3DMC',
                departments = '',
                is_active = True,
                description = '',
                handling_message = '',
                questionnaire = '',
                public_name = '',
                is_public_accessible = True
            )
        else:
            return CategoryHAL(
                links = signals_api_client.models._links. links(
                    curies = signals_api_client.models._links_1_curies._links_1_curies(
                        href = 'https://api.example.com/signals/relations/', ), 
                    self = signals_api_client.models._links_1_self._links_1_self(
                        href = 'https://api.example.com/signals/v1/private/categories/1', ), 
                    archives = signals_api_client.models._links_1_archives._links_1_archives(
                        href = 'https://api.example.com/signals/v1/private/signals/1/history/', ), 
                    sia:questionnaire = signals_api_client.models._links_1_sia_questionnaire._links_1_sia_questionnaire(
                        href = 'https://api.example.com/signals/v1/public/qa/questionnaires/636aacb1-2813-423e-adbe-7ef84d4afc37', ), 
                    sia:icon = signals_api_client.models._links_1_sia_icon._links_1_sia_icon(
                        href = 'https://api.example.com/media/icons/1.png', ), ),
                display = '',
                name = '',
                slug = 'z',
                departments = '',
                questionnaire = '',
        )
        """

    def testCategoryHAL(self):
        """Test CategoryHAL"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
