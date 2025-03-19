# coding: utf-8

"""
    Signalen API

    One of the tasks of a municipality is to maintain public spaces. When citizens have complaints about public spaces they can leave these complaints with the municipality. Signalen (SIG) receives these complaints and is used to track progress towards their resolution. SIG provides an API that is used both by the SIG frontend and external systems that integrate with SIG.

    The version of the OpenAPI document: 2.41.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from signals_api_client.models.links8_sia_attachments_inner import Links8SiaAttachmentsInner

class TestLinks8SiaAttachmentsInner(unittest.TestCase):
    """Links8SiaAttachmentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Links8SiaAttachmentsInner:
        """Test Links8SiaAttachmentsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Links8SiaAttachmentsInner`
        """
        model = Links8SiaAttachmentsInner()
        if include_optional:
            return Links8SiaAttachmentsInner(
                href = 'https://api.example.com/media/1.png',
                created_by = 'john.doe@example.com',
                created_at = '2023-06-01T00:00Z',
                caption = 'This is a caption'
            )
        else:
            return Links8SiaAttachmentsInner(
        )
        """

    def testLinks8SiaAttachmentsInner(self):
        """Test Links8SiaAttachmentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
