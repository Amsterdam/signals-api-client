# coding: utf-8

"""
    Signalen API

    One of the tasks of a municipality is to maintain public spaces. When citizens have complaints about public spaces they can leave these complaints with the municipality. Signalen (SIG) receives these complaints and is used to track progress towards their resolution. SIG provides an API that is used both by the SIG frontend and external systems that integrate with SIG.

    The version of the OpenAPI document: 2.41.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from signals_api_client.models.paginated_private_signal_attachment_list import PaginatedPrivateSignalAttachmentList

class TestPaginatedPrivateSignalAttachmentList(unittest.TestCase):
    """PaginatedPrivateSignalAttachmentList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedPrivateSignalAttachmentList:
        """Test PaginatedPrivateSignalAttachmentList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedPrivateSignalAttachmentList`
        """
        model = PaginatedPrivateSignalAttachmentList()
        if include_optional:
            return PaginatedPrivateSignalAttachmentList(
                links = signals_api_client.models.paginated_abridged_child_signal_list__links.PaginatedAbridgedChildSignalList__links(
                    self = signals_api_client.models.paginated_abridged_child_signal_list__links_self.PaginatedAbridgedChildSignalList__links_self(
                        href = 'http://api.example.org/endpoint/?page=3', ), 
                    next = signals_api_client.models.paginated_abridged_child_signal_list__links_next.PaginatedAbridgedChildSignalList__links_next(
                        href = 'http://api.example.org/endpoint/?page=4', ), 
                    previous = signals_api_client.models.paginated_abridged_child_signal_list__links_previous.PaginatedAbridgedChildSignalList__links_previous(
                        href = 'http://api.example.org/endpoint/?page=2', ), ),
                count = 123,
                results = [
                    signals_api_client.models.private_signal_attachment.PrivateSignalAttachment(
                        _display = '', 
                        _links = signals_api_client.models._links. links(
                            self = signals_api_client.models._links_5_self._links_5_self(
                                href = 'https://api.example.com/signals/v1/private/signals/1/attachments/1', ), ), 
                        location = '', 
                        is_image = True, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        file = '', 
                        created_by = '', 
                        public = True, 
                        caption = '', )
                    ]
            )
        else:
            return PaginatedPrivateSignalAttachmentList(
        )
        """

    def testPaginatedPrivateSignalAttachmentList(self):
        """Test PaginatedPrivateSignalAttachmentList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
