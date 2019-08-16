# coding: utf-8

"""
    Pick Master Web API Reference

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0-alpha.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Quaternion(object):
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
        'x': 'float',
        'y': 'float',
        'z': 'float',
        'w': 'float',
        'is_identity': 'bool'
    }

    attribute_map = {
        'x': 'x',
        'y': 'y',
        'z': 'z',
        'w': 'w',
        'is_identity': 'isIdentity'
    }

    def __init__(self, x=None, y=None, z=None, w=None, is_identity=None):  # noqa: E501
        """Quaternion - a model defined in Swagger"""  # noqa: E501

        self._x = None
        self._y = None
        self._z = None
        self._w = None
        self._is_identity = None
        self.discriminator = None

        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if z is not None:
            self.z = z
        if w is not None:
            self.w = w
        if is_identity is not None:
            self.is_identity = is_identity

    @property
    def x(self):
        """Gets the x of this Quaternion.  # noqa: E501


        :return: The x of this Quaternion.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this Quaternion.


        :param x: The x of this Quaternion.  # noqa: E501
        :type: float
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this Quaternion.  # noqa: E501


        :return: The y of this Quaternion.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this Quaternion.


        :param y: The y of this Quaternion.  # noqa: E501
        :type: float
        """

        self._y = y

    @property
    def z(self):
        """Gets the z of this Quaternion.  # noqa: E501


        :return: The z of this Quaternion.  # noqa: E501
        :rtype: float
        """
        return self._z

    @z.setter
    def z(self, z):
        """Sets the z of this Quaternion.


        :param z: The z of this Quaternion.  # noqa: E501
        :type: float
        """

        self._z = z

    @property
    def w(self):
        """Gets the w of this Quaternion.  # noqa: E501


        :return: The w of this Quaternion.  # noqa: E501
        :rtype: float
        """
        return self._w

    @w.setter
    def w(self, w):
        """Sets the w of this Quaternion.


        :param w: The w of this Quaternion.  # noqa: E501
        :type: float
        """

        self._w = w

    @property
    def is_identity(self):
        """Gets the is_identity of this Quaternion.  # noqa: E501


        :return: The is_identity of this Quaternion.  # noqa: E501
        :rtype: bool
        """
        return self._is_identity

    @is_identity.setter
    def is_identity(self, is_identity):
        """Sets the is_identity of this Quaternion.


        :param is_identity: The is_identity of this Quaternion.  # noqa: E501
        :type: bool
        """

        self._is_identity = is_identity

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
        if issubclass(Quaternion, dict):
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
        if not isinstance(other, Quaternion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
