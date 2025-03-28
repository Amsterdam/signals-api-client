# coding: utf-8

"""
    Signalen API

    One of the tasks of a municipality is to maintain public spaces. When citizens have complaints about public spaces they can leave these complaints with the municipality. Signalen (SIG) receives these complaints and is used to track progress towards their resolution. SIG provides an API that is used both by the SIG frontend and external systems that integrate with SIG.

    The version of the OpenAPI document: 2.41.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from signals_api_client.models.links6 import Links6

class TestLinks6(unittest.TestCase):
    """Links6 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Links6:
        """Test Links6
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Links6`
        """
        model = Links6()
        if include_optional:
            return Links6(
                curies = signals_api_client.models._links_1_curies._links_1_curies(
                    href = 'https://api.example.com/signals/relations/', ),
                var_self = signals_api_client.models._links_6_self._links_6_self(
                    href = 'https://api.example.com/signals/v1/private/signals/2', ),
                archives = signals_api_client.models._links_6_archives._links_6_archives(
                    href = 'https://api.example.com/signals/v1/private/signals/2/history/', ),
                sia_attachments = signals_api_client.models._links_6_sia_attachments._links_6_sia_attachments(
                    href = 'https://api.example.com/signals/v1/private/signals/2/attachments/', ),
                sia_pdf = signals_api_client.models._links_6_sia_pdf._links_6_sia_pdf(
                    href = 'https://api.example.com/signals/v1/private/signals/2/pdf/', ),
                sia_context = signals_api_client.models._links_6_sia_context._links_6_sia_context(
                    href = 'https://api.example.com/signals/v1/private/signals/2/context/', ),
                sia_parent = signals_api_client.models._links_self._links_self(
                    href = 'https://api.example.com/signals/v1/private/signals/1', ),
                sia_children = [
                    signals_api_client.models._links_6_sia_children_inner._links_6_sia_children_inner(
                        href = 'https://api.example.com/signals/v1/private/signals/3', )
                    ]
            )
        else:
            return Links6(
        )
        """

    def testLinks6(self):
        """Test Links6"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
