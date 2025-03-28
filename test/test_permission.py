# coding: utf-8

"""
    Signalen API

    One of the tasks of a municipality is to maintain public spaces. When citizens have complaints about public spaces they can leave these complaints with the municipality. Signalen (SIG) receives these complaints and is used to track progress towards their resolution. SIG provides an API that is used both by the SIG frontend and external systems that integrate with SIG.

    The version of the OpenAPI document: 2.41.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from signals_api_client.models.permission import Permission

class TestPermission(unittest.TestCase):
    """Permission unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Permission:
        """Test Permission
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Permission`
        """
        model = Permission()
        if include_optional:
            return Permission(
                links = signals_api_client.models._links. links(
                    self = signals_api_client.models._links_3_self._links_3_self(
                        href = 'http://api.example.org/endpoint/1', ), ),
                display = '',
                id = 56,
                name = '',
                codename = ''
            )
        else:
            return Permission(
                links = signals_api_client.models._links. links(
                    self = signals_api_client.models._links_3_self._links_3_self(
                        href = 'http://api.example.org/endpoint/1', ), ),
                display = '',
                id = 56,
                name = '',
                codename = '',
        )
        """

    def testPermission(self):
        """Test Permission"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
