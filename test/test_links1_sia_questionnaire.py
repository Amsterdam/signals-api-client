# coding: utf-8

"""
    Signalen API

    One of the tasks of a municipality is to maintain public spaces. When citizens have complaints about public spaces they can leave these complaints with the municipality. Signalen (SIG) receives these complaints and is used to track progress towards their resolution. SIG provides an API that is used both by the SIG frontend and external systems that integrate with SIG.

    The version of the OpenAPI document: 2.41.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from signals_api_client.models.links1_sia_questionnaire import Links1SiaQuestionnaire

class TestLinks1SiaQuestionnaire(unittest.TestCase):
    """Links1SiaQuestionnaire unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Links1SiaQuestionnaire:
        """Test Links1SiaQuestionnaire
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Links1SiaQuestionnaire`
        """
        model = Links1SiaQuestionnaire()
        if include_optional:
            return Links1SiaQuestionnaire(
                href = 'https://api.example.com/signals/v1/public/qa/questionnaires/636aacb1-2813-423e-adbe-7ef84d4afc37'
            )
        else:
            return Links1SiaQuestionnaire(
        )
        """

    def testLinks1SiaQuestionnaire(self):
        """Test Links1SiaQuestionnaire"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
