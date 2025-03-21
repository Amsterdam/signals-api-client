# coding: utf-8

"""
    Signalen API

    One of the tasks of a municipality is to maintain public spaces. When citizens have complaints about public spaces they can leave these complaints with the municipality. Signalen (SIG) receives these complaints and is used to track progress towards their resolution. SIG provides an API that is used both by the SIG frontend and external systems that integrate with SIG.

    The version of the OpenAPI document: 2.41.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from signals_api_client.models.nested_category_model import NestedCategoryModel

class TestNestedCategoryModel(unittest.TestCase):
    """NestedCategoryModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NestedCategoryModel:
        """Test NestedCategoryModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NestedCategoryModel`
        """
        model = NestedCategoryModel()
        if include_optional:
            return NestedCategoryModel(
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
                deadline_factor_3 = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return NestedCategoryModel(
                sub = '',
                sub_slug = '',
                main = '',
                main_slug = '',
                departments = '',
                created_by = '',
                deadline = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                deadline_factor_3 = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testNestedCategoryModel(self):
        """Test NestedCategoryModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
