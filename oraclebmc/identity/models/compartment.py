# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class Compartment(object):

    def __init__(self):

        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'inactive_status': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'inactive_status': 'inactiveStatus'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._description = None
        self._time_created = None
        self._lifecycle_state = None
        self._inactive_status = None

    @property
    def id(self):
        """
        Gets the id of this Compartment.
        The OCID of the compartment.


        :return: The id of this Compartment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Compartment.
        The OCID of the compartment.


        :param id: The id of this Compartment.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Compartment.
        The OCID of the tenancy containing the compartment.


        :return: The compartment_id of this Compartment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Compartment.
        The OCID of the tenancy containing the compartment.


        :param compartment_id: The compartment_id of this Compartment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        Gets the name of this Compartment.
        The name you assign to the compartment during creation. The name must be unique across all
        compartments in the tenancy and cannot be changed.


        :return: The name of this Compartment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Compartment.
        The name you assign to the compartment during creation. The name must be unique across all
        compartments in the tenancy and cannot be changed.


        :param name: The name of this Compartment.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Compartment.
        The description you assign to the compartment. Does not have to be unique, and it's changeable.


        :return: The description of this Compartment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Compartment.
        The description you assign to the compartment. Does not have to be unique, and it's changeable.


        :param description: The description of this Compartment.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this Compartment.
        Date and time the compartment was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this Compartment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Compartment.
        Date and time the compartment was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this Compartment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Compartment.
        The compartment's current state. After creating a compartment, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.


        :return: The lifecycle_state of this Compartment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Compartment.
        The compartment's current state. After creating a compartment, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.


        :param lifecycle_state: The lifecycle_state of this Compartment.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]
        if lifecycle_state not in allowed_values:
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def inactive_status(self):
        """
        Gets the inactive_status of this Compartment.
        The detailed status of INACTIVE lifecycleState.


        :return: The inactive_status of this Compartment.
        :rtype: int
        """
        return self._inactive_status

    @inactive_status.setter
    def inactive_status(self, inactive_status):
        """
        Sets the inactive_status of this Compartment.
        The detailed status of INACTIVE lifecycleState.


        :param inactive_status: The inactive_status of this Compartment.
        :type: int
        """
        self._inactive_status = inactive_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
