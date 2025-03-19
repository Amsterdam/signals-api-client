# coding: utf-8

"""
    Signalen API

    One of the tasks of a municipality is to maintain public spaces. When citizens have complaints about public spaces they can leave these complaints with the municipality. Signalen (SIG) receives these complaints and is used to track progress towards their resolution. SIG provides an API that is used both by the SIG frontend and external systems that integrate with SIG.

    The version of the OpenAPI document: 2.41.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from signals_api_client.models.links6_archives import Links6Archives

class TestLinks6Archives(unittest.TestCase):
    """Links6Archives unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Links6Archives:
        """Test Links6Archives
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Links6Archives`
        """
        model = Links6Archives()
        if include_optional:
            return Links6Archives(
                href = 'https://api.example.com/signals/v1/private/signals/2/history/'
            )
        else:
            return Links6Archives(
        )
        """

    def testLinks6Archives(self):
        """Test Links6Archives"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
