# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class DrgAttachment(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'drg_id': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'drg_id': 'drgId',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'vcn_id': 'vcnId'
        }

        self._compartment_id = None
        self._display_name = None
        self._drg_id = None
        self._id = None
        self._lifecycle_state = None
        self._time_created = None
        self._vcn_id = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this DrgAttachment.
        The OCID of the compartment containing the DRG attachment.


        :return: The compartment_id of this DrgAttachment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DrgAttachment.
        The OCID of the compartment containing the DRG attachment.


        :param compartment_id: The compartment_id of this DrgAttachment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this DrgAttachment.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this DrgAttachment.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DrgAttachment.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this DrgAttachment.
        :type: str
        """
        self._display_name = display_name

    @property
    def drg_id(self):
        """
        Gets the drg_id of this DrgAttachment.
        The OCID of the DRG.


        :return: The drg_id of this DrgAttachment.
        :rtype: str
        """
        return self._drg_id

    @drg_id.setter
    def drg_id(self, drg_id):
        """
        Sets the drg_id of this DrgAttachment.
        The OCID of the DRG.


        :param drg_id: The drg_id of this DrgAttachment.
        :type: str
        """
        self._drg_id = drg_id

    @property
    def id(self):
        """
        Gets the id of this DrgAttachment.
        The DRG attachment's Oracle ID (OCID).


        :return: The id of this DrgAttachment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DrgAttachment.
        The DRG attachment's Oracle ID (OCID).


        :param id: The id of this DrgAttachment.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DrgAttachment.
        The DRG attachment's current state.


        :return: The lifecycle_state of this DrgAttachment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DrgAttachment.
        The DRG attachment's current state.


        :param lifecycle_state: The lifecycle_state of this DrgAttachment.
        :type: str
        """
        allowed_values = ["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]
        if lifecycle_state not in allowed_values:
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this DrgAttachment.
        The date and time the DRG attachment was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this DrgAttachment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DrgAttachment.
        The date and time the DRG attachment was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this DrgAttachment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this DrgAttachment.
        The OCID of the VCN.


        :return: The vcn_id of this DrgAttachment.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this DrgAttachment.
        The OCID of the VCN.


        :param vcn_id: The vcn_id of this DrgAttachment.
        :type: str
        """
        self._vcn_id = vcn_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
