# coding: utf-8

"""
    Seldon Deploy API

    API to interact and manage the lifecycle of your machine learning models deployed through Seldon Deploy.  # noqa: E501

    OpenAPI spec version: v1alpha1
    Contact: hello@seldon.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AdvancedConfig(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'horizontal_pod_autoscaler_config': 'HorizontalPodAutoscalerConfig',
        'restore_to_original_replica_count': 'bool'
    }

    attribute_map = {
        'horizontal_pod_autoscaler_config': 'horizontalPodAutoscalerConfig',
        'restore_to_original_replica_count': 'restoreToOriginalReplicaCount'
    }

    def __init__(self, horizontal_pod_autoscaler_config=None, restore_to_original_replica_count=None):  # noqa: E501
        """AdvancedConfig - a model defined in Swagger"""  # noqa: E501

        self._horizontal_pod_autoscaler_config = None
        self._restore_to_original_replica_count = None
        self.discriminator = None

        if horizontal_pod_autoscaler_config is not None:
            self.horizontal_pod_autoscaler_config = horizontal_pod_autoscaler_config
        if restore_to_original_replica_count is not None:
            self.restore_to_original_replica_count = restore_to_original_replica_count

    @property
    def horizontal_pod_autoscaler_config(self):
        """Gets the horizontal_pod_autoscaler_config of this AdvancedConfig.  # noqa: E501


        :return: The horizontal_pod_autoscaler_config of this AdvancedConfig.  # noqa: E501
        :rtype: HorizontalPodAutoscalerConfig
        """
        return self._horizontal_pod_autoscaler_config

    @horizontal_pod_autoscaler_config.setter
    def horizontal_pod_autoscaler_config(self, horizontal_pod_autoscaler_config):
        """Sets the horizontal_pod_autoscaler_config of this AdvancedConfig.


        :param horizontal_pod_autoscaler_config: The horizontal_pod_autoscaler_config of this AdvancedConfig.  # noqa: E501
        :type: HorizontalPodAutoscalerConfig
        """

        self._horizontal_pod_autoscaler_config = horizontal_pod_autoscaler_config

    @property
    def restore_to_original_replica_count(self):
        """Gets the restore_to_original_replica_count of this AdvancedConfig.  # noqa: E501

        +optional  # noqa: E501

        :return: The restore_to_original_replica_count of this AdvancedConfig.  # noqa: E501
        :rtype: bool
        """
        return self._restore_to_original_replica_count

    @restore_to_original_replica_count.setter
    def restore_to_original_replica_count(self, restore_to_original_replica_count):
        """Sets the restore_to_original_replica_count of this AdvancedConfig.

        +optional  # noqa: E501

        :param restore_to_original_replica_count: The restore_to_original_replica_count of this AdvancedConfig.  # noqa: E501
        :type: bool
        """

        self._restore_to_original_replica_count = restore_to_original_replica_count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AdvancedConfig, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AdvancedConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
