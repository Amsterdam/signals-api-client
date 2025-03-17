# coding: utf-8

"""
    Signalen API

    One of the tasks of a municipality is to maintain public spaces. When citizens have complaints about public spaces they can leave these complaints with the municipality. Signalen (SIG) receives these complaints and is used to track progress towards their resolution. SIG provides an API that is used both by the SIG frontend and external systems that integrate with SIG.

    The version of the OpenAPI document: 2.41.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from signals_api_client.models.links7 import Links7

class TestLinks7(unittest.TestCase):
    """Links7 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Links7:
        """Test Links7
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Links7`
        """
        model = Links7()
        if include_optional:
            return Links7(
                curies = signals_api_client.models._links_1_curies._links_1_curies(
                    href = 'https://api.example.com/signals/relations/', ),
                var_self = signals_api_client.models._links_self._links_self(
                    href = 'https://api.example.com/signals/v1/private/signals/1', ),
                sia_context_reporter_detail = signals_api_client.models._links_7_sia_context_reporter_detail._links_7_sia_context_reporter_detail(
                    href = 'https://api.example.com/signals/v1/private/signals/1/context/reporter/', ),
                sia_context_geography_detail = signals_api_client.models._links_7_sia_context_geography_detail._links_7_sia_context_geography_detail(
                    href = 'https://api.example.com/signals/v1/private/signals/1/context/near/geography/', )
            )
        else:
            return Links7(
        )
        """

    def testLinks7(self):
        """Test Links7"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
