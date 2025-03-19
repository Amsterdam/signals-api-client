# coding: utf-8

# flake8: noqa

"""
    Signalen API

    One of the tasks of a municipality is to maintain public spaces. When citizens have complaints about public spaces they can leave these complaints with the municipality. Signalen (SIG) receives these complaints and is used to track progress towards their resolution. SIG provides an API that is used both by the SIG frontend and external systems that integrate with SIG.

    The version of the OpenAPI document: 2.41.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from signals_api_client.api.v1_api import V1Api

# import ApiClient
from signals_api_client.api_response import ApiResponse
from signals_api_client.api_client import ApiClient
from signals_api_client.configuration import Configuration
from signals_api_client.exceptions import OpenApiException
from signals_api_client.exceptions import ApiTypeError
from signals_api_client.exceptions import ApiValueError
from signals_api_client.exceptions import ApiKeyError
from signals_api_client.exceptions import ApiAttributeError
from signals_api_client.exceptions import ApiException

# import models into sdk package
from signals_api_client.models.abridged_child_signal import AbridgedChildSignal
from signals_api_client.models.active_terms_facet import ActiveTermsFacet
from signals_api_client.models.area import Area
from signals_api_client.models.area_create import AreaCreate
from signals_api_client.models.area_create_geometry import AreaCreateGeometry
from signals_api_client.models.area_geo import AreaGeo
from signals_api_client.models.area_geo_properties import AreaGeoProperties
from signals_api_client.models.area_type import AreaType
from signals_api_client.models.blank_enum import BlankEnum
from signals_api_client.models.cancel_signal_reporter import CancelSignalReporter
from signals_api_client.models.category import Category
from signals_api_client.models.category_department import CategoryDepartment
from signals_api_client.models.category_hal import CategoryHAL
from signals_api_client.models.email_preview import EmailPreview
from signals_api_client.models.email_preview_post import EmailPreviewPost
from signals_api_client.models.email_verification import EmailVerification
from signals_api_client.models.expression import Expression
from signals_api_client.models.feedback import Feedback
from signals_api_client.models.field_type_enum import FieldTypeEnum
from signals_api_client.models.generic_error import GenericError
from signals_api_client.models.gis_feature_enum import GisFeatureEnum
from signals_api_client.models.handling_enum import HandlingEnum
from signals_api_client.models.highlight import Highlight
from signals_api_client.models.history_log_hal import HistoryLogHal
from signals_api_client.models.links import Links
from signals_api_client.models.links1 import Links1
from signals_api_client.models.links1_archives import Links1Archives
from signals_api_client.models.links1_curies import Links1Curies
from signals_api_client.models.links1_self import Links1Self
from signals_api_client.models.links1_sia_icon import Links1SiaIcon
from signals_api_client.models.links1_sia_questionnaire import Links1SiaQuestionnaire
from signals_api_client.models.links2 import Links2
from signals_api_client.models.links2_sia_status_message_templates import Links2SiaStatusMessageTemplates
from signals_api_client.models.links3 import Links3
from signals_api_client.models.links3_self import Links3Self
from signals_api_client.models.links4 import Links4
from signals_api_client.models.links4_self import Links4Self
from signals_api_client.models.links5 import Links5
from signals_api_client.models.links5_self import Links5Self
from signals_api_client.models.links6 import Links6
from signals_api_client.models.links6_archives import Links6Archives
from signals_api_client.models.links6_self import Links6Self
from signals_api_client.models.links6_sia_attachments import Links6SiaAttachments
from signals_api_client.models.links6_sia_children_inner import Links6SiaChildrenInner
from signals_api_client.models.links6_sia_context import Links6SiaContext
from signals_api_client.models.links6_sia_pdf import Links6SiaPdf
from signals_api_client.models.links7 import Links7
from signals_api_client.models.links7_sia_context_geography_detail import Links7SiaContextGeographyDetail
from signals_api_client.models.links7_sia_context_reporter_detail import Links7SiaContextReporterDetail
from signals_api_client.models.links8 import Links8
from signals_api_client.models.links8_archives import Links8Archives
from signals_api_client.models.links8_self import Links8Self
from signals_api_client.models.links8_sia_attachments_inner import Links8SiaAttachmentsInner
from signals_api_client.models.links9 import Links9
from signals_api_client.models.links_self import LinksSelf
from signals_api_client.models.meta import Meta
from signals_api_client.models.my_signals_logged_in_reporter import MySignalsLoggedInReporter
from signals_api_client.models.my_signals_token import MySignalsToken
from signals_api_client.models.nested_category_model import NestedCategoryModel
from signals_api_client.models.nested_department_model import NestedDepartmentModel
from signals_api_client.models.nested_location_model import NestedLocationModel
from signals_api_client.models.nested_location_model_geometrie import NestedLocationModelGeometrie
from signals_api_client.models.nested_my_signal_location import NestedMySignalLocation
from signals_api_client.models.nested_my_signal_location_geometrie import NestedMySignalLocationGeometrie
from signals_api_client.models.nested_my_signal_status import NestedMySignalStatus
from signals_api_client.models.nested_note_model import NestedNoteModel
from signals_api_client.models.nested_priority_model import NestedPriorityModel
from signals_api_client.models.nested_private_category_department import NestedPrivateCategoryDepartment
from signals_api_client.models.nested_public_department import NestedPublicDepartment
from signals_api_client.models.nested_public_status_model import NestedPublicStatusModel
from signals_api_client.models.nested_reporter_model import NestedReporterModel
from signals_api_client.models.nested_status_model import NestedStatusModel
from signals_api_client.models.nested_status_model_state import NestedStatusModelState
from signals_api_client.models.nested_status_model_target_api import NestedStatusModelTargetApi
from signals_api_client.models.nested_type_model import NestedTypeModel
from signals_api_client.models.paginated_abridged_child_signal_list import PaginatedAbridgedChildSignalList
from signals_api_client.models.paginated_abridged_child_signal_list_links import PaginatedAbridgedChildSignalListLinks
from signals_api_client.models.paginated_abridged_child_signal_list_links_next import PaginatedAbridgedChildSignalListLinksNext
from signals_api_client.models.paginated_abridged_child_signal_list_links_previous import PaginatedAbridgedChildSignalListLinksPrevious
from signals_api_client.models.paginated_abridged_child_signal_list_links_self import PaginatedAbridgedChildSignalListLinksSelf
from signals_api_client.models.paginated_area_list import PaginatedAreaList
from signals_api_client.models.paginated_area_type_list import PaginatedAreaTypeList
from signals_api_client.models.paginated_category_list import PaginatedCategoryList
from signals_api_client.models.paginated_expression_list import PaginatedExpressionList
from signals_api_client.models.paginated_permission_list import PaginatedPermissionList
from signals_api_client.models.paginated_private_category_list import PaginatedPrivateCategoryList
from signals_api_client.models.paginated_private_department_serializer_list_list import PaginatedPrivateDepartmentSerializerListList
from signals_api_client.models.paginated_private_signal_attachment_list import PaginatedPrivateSignalAttachmentList
from signals_api_client.models.paginated_private_signal_serializer_list_list import PaginatedPrivateSignalSerializerListList
from signals_api_client.models.paginated_public_question_serializer_detail_list import PaginatedPublicQuestionSerializerDetailList
from signals_api_client.models.paginated_role_list import PaginatedRoleList
from signals_api_client.models.paginated_signal_context_reporter_list import PaginatedSignalContextReporterList
from signals_api_client.models.paginated_signal_id_list_list import PaginatedSignalIdListList
from signals_api_client.models.paginated_signal_list_list import PaginatedSignalListList
from signals_api_client.models.paginated_signal_reporter_list import PaginatedSignalReporterList
from signals_api_client.models.paginated_source_list import PaginatedSourceList
from signals_api_client.models.paginated_standard_answer_list import PaginatedStandardAnswerList
from signals_api_client.models.paginated_status_message_list import PaginatedStatusMessageList
from signals_api_client.models.paginated_stored_signal_filter_list import PaginatedStoredSignalFilterList
from signals_api_client.models.paginated_user_list_hal_list import PaginatedUserListHALList
from signals_api_client.models.paginated_user_name_list_list import PaginatedUserNameListList
from signals_api_client.models.parent_category_hal import ParentCategoryHAL
from signals_api_client.models.patched_expression import PatchedExpression
from signals_api_client.models.patched_feedback import PatchedFeedback
from signals_api_client.models.patched_private_category import PatchedPrivateCategory
from signals_api_client.models.patched_private_department_serializer_list import PatchedPrivateDepartmentSerializerList
from signals_api_client.models.patched_private_signal_attachment_update import PatchedPrivateSignalAttachmentUpdate
from signals_api_client.models.patched_private_signal_serializer_list import PatchedPrivateSignalSerializerList
from signals_api_client.models.patched_role import PatchedRole
from signals_api_client.models.patched_status_message import PatchedStatusMessage
from signals_api_client.models.patched_stored_signal_filter import PatchedStoredSignalFilter
from signals_api_client.models.patched_user_detail_hal import PatchedUserDetailHAL
from signals_api_client.models.permission import Permission
from signals_api_client.models.priority_enum import PriorityEnum
from signals_api_client.models.private_category import PrivateCategory
from signals_api_client.models.private_category_history_hal import PrivateCategoryHistoryHal
from signals_api_client.models.private_category_icon import PrivateCategoryIcon
from signals_api_client.models.private_category_sla import PrivateCategorySLA
from signals_api_client.models.private_department_serializer_detail import PrivateDepartmentSerializerDetail
from signals_api_client.models.private_department_serializer_list import PrivateDepartmentSerializerList
from signals_api_client.models.private_signal_attachment import PrivateSignalAttachment
from signals_api_client.models.private_signal_attachment_update import PrivateSignalAttachmentUpdate
from signals_api_client.models.private_signal_serializer_detail import PrivateSignalSerializerDetail
from signals_api_client.models.private_signal_serializer_list import PrivateSignalSerializerList
from signals_api_client.models.private_user_history_hal import PrivateUserHistoryHal
from signals_api_client.models.profile_detail import ProfileDetail
from signals_api_client.models.profile_list import ProfileList
from signals_api_client.models.public_question_serializer_detail import PublicQuestionSerializerDetail
from signals_api_client.models.public_signal_attachment import PublicSignalAttachment
from signals_api_client.models.public_signal_create import PublicSignalCreate
from signals_api_client.models.public_signal_serializer_detail import PublicSignalSerializerDetail
from signals_api_client.models.report_signals_per_category import ReportSignalsPerCategory
from signals_api_client.models.role import Role
from signals_api_client.models.routing_expression import RoutingExpression
from signals_api_client.models.signal_context import SignalContext
from signals_api_client.models.signal_context_near import SignalContextNear
from signals_api_client.models.signal_context_reporter import SignalContextReporter
from signals_api_client.models.signal_context_reporter_category import SignalContextReporterCategory
from signals_api_client.models.signal_context_reporter_feedback import SignalContextReporterFeedback
from signals_api_client.models.signal_context_reporter_status import SignalContextReporterStatus
from signals_api_client.models.signal_detail import SignalDetail
from signals_api_client.models.signal_id_list import SignalIdList
from signals_api_client.models.signal_list import SignalList
from signals_api_client.models.signal_reporter import SignalReporter
from signals_api_client.models.signals_per_category_count import SignalsPerCategoryCount
from signals_api_client.models.simple_category import SimpleCategory
from signals_api_client.models.source import Source
from signals_api_client.models.stadsdeel_enum import StadsdeelEnum
from signals_api_client.models.standard_answer import StandardAnswer
from signals_api_client.models.state_a07_enum import StateA07Enum
from signals_api_client.models.state_status_message_template import StateStatusMessageTemplate
from signals_api_client.models.state_status_message_template_state_enum import StateStatusMessageTemplateStateEnum
from signals_api_client.models.state_terms_facet import StateTermsFacet
from signals_api_client.models.status_enum import StatusEnum
from signals_api_client.models.status_message import StatusMessage
from signals_api_client.models.status_message_category_position import StatusMessageCategoryPosition
from signals_api_client.models.status_message_facet import StatusMessageFacet
from signals_api_client.models.status_message_list import StatusMessageList
from signals_api_client.models.status_message_search_result import StatusMessageSearchResult
from signals_api_client.models.stored_signal_filter import StoredSignalFilter
from signals_api_client.models.target_api_enum import TargetApiEnum
from signals_api_client.models.temporary_category_hal import TemporaryCategoryHAL
from signals_api_client.models.temporary_parent_category_hal import TemporaryParentCategoryHAL
from signals_api_client.models.tmp_category import TmpCategory
from signals_api_client.models.user_detail_hal import UserDetailHAL
from signals_api_client.models.user_list_hal import UserListHAL
from signals_api_client.models.user_name_list import UserNameList
from signals_api_client.models.v1_private_signals_context_near_geography_retrieve200_response import V1PrivateSignalsContextNearGeographyRetrieve200Response
from signals_api_client.models.v1_private_signals_context_near_geography_retrieve200_response_features_inner import V1PrivateSignalsContextNearGeographyRetrieve200ResponseFeaturesInner
from signals_api_client.models.v1_private_signals_context_near_geography_retrieve200_response_features_inner_geometry import V1PrivateSignalsContextNearGeographyRetrieve200ResponseFeaturesInnerGeometry
from signals_api_client.models.v1_private_signals_context_near_geography_retrieve200_response_features_inner_properties import V1PrivateSignalsContextNearGeographyRetrieve200ResponseFeaturesInnerProperties
from signals_api_client.models.v1_private_signals_geography_retrieve200_response import V1PrivateSignalsGeographyRetrieve200Response
from signals_api_client.models.v1_private_signals_geography_retrieve200_response_features_inner import V1PrivateSignalsGeographyRetrieve200ResponseFeaturesInner
from signals_api_client.models.v1_private_signals_geography_retrieve200_response_features_inner_properties import V1PrivateSignalsGeographyRetrieve200ResponseFeaturesInnerProperties
from signals_api_client.models.v1_public_signals_geography_retrieve200_response import V1PublicSignalsGeographyRetrieve200Response
from signals_api_client.models.v1_public_signals_geography_retrieve200_response_features_inner import V1PublicSignalsGeographyRetrieve200ResponseFeaturesInner
from signals_api_client.models.v1_public_signals_geography_retrieve200_response_features_inner_properties import V1PublicSignalsGeographyRetrieve200ResponseFeaturesInnerProperties
from signals_api_client.models.v1_public_signals_geography_retrieve200_response_features_inner_properties_category import V1PublicSignalsGeographyRetrieve200ResponseFeaturesInnerPropertiesCategory
from signals_api_client.models.v1_public_signals_geography_retrieve200_response_features_inner_properties_category_parent import V1PublicSignalsGeographyRetrieve200ResponseFeaturesInnerPropertiesCategoryParent
from signals_api_client.models.validation_error import ValidationError
