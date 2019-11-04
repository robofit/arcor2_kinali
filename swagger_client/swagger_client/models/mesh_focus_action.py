# coding: utf-8

"""
    Pick Master Web API Reference

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0-alpha.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.vector3 import Vector3  # noqa: F401,E501


class MeshFocusAction(object):
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
        'mesh_focus_points': 'list[Vector3]',
        'robot_space_points': 'list[Vector3]'
    }

    attribute_map = {
        'mesh_focus_points': 'meshFocusPoints',
        'robot_space_points': 'robotSpacePoints'
    }

    def __init__(self, mesh_focus_points=None, robot_space_points=None):  # noqa: E501
        """MeshFocusAction - a model defined in Swagger"""  # noqa: E501

        self._mesh_focus_points = None
        self._robot_space_points = None
        self.discriminator = None

        if mesh_focus_points is not None:
            self.mesh_focus_points = mesh_focus_points
        if robot_space_points is not None:
            self.robot_space_points = robot_space_points

    @property
    def mesh_focus_points(self):
        """Gets the mesh_focus_points of this MeshFocusAction.  # noqa: E501

        Gets or sets mesh object focus points.  # noqa: E501

        :return: The mesh_focus_points of this MeshFocusAction.  # noqa: E501
        :rtype: list[Vector3]
        """
        return self._mesh_focus_points

    @mesh_focus_points.setter
    def mesh_focus_points(self, mesh_focus_points):
        """Sets the mesh_focus_points of this MeshFocusAction.

        Gets or sets mesh object focus points.  # noqa: E501

        :param mesh_focus_points: The mesh_focus_points of this MeshFocusAction.  # noqa: E501
        :type: list[Vector3]
        """

        self._mesh_focus_points = mesh_focus_points

    @property
    def robot_space_points(self):
        """Gets the robot_space_points of this MeshFocusAction.  # noqa: E501

        Gets or sets mesh focus points reached in robot space.  # noqa: E501

        :return: The robot_space_points of this MeshFocusAction.  # noqa: E501
        :rtype: list[Vector3]
        """
        return self._robot_space_points

    @robot_space_points.setter
    def robot_space_points(self, robot_space_points):
        """Sets the robot_space_points of this MeshFocusAction.

        Gets or sets mesh focus points reached in robot space.  # noqa: E501

        :param robot_space_points: The robot_space_points of this MeshFocusAction.  # noqa: E501
        :type: list[Vector3]
        """

        self._robot_space_points = robot_space_points

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
        if issubclass(MeshFocusAction, dict):
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
        if not isinstance(other, MeshFocusAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other