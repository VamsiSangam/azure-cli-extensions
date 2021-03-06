# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse

from .. import models


class WorkspaceAclOperations(object):
    """WorkspaceAclOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The Synapse client API Version. Constant value: "2019-11-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config
        self.api_version = "2019-11-01-preview"

    def get_access_control_info(
            self, workspace_name, resource, custom_headers=None, raw=False, **operation_config):
        """Get access control info.

        :param workspace_name: The name of the workspace to execute operations
         on.
        :type workspace_name: str
        :param resource: The resource to get the access control info for.
        :type resource: ~azure.synapse.models.GetAccessControlInfoRequest
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: WorkspaceAccessControlResponse or ClientRawResponse if
         raw=true
        :rtype: ~azure.synapse.models.WorkspaceAccessControlResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.synapse.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get_access_control_info.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self.config.synapse_dns_suffix", self.config.synapse_dns_suffix, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(resource, 'GetAccessControlInfoRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('WorkspaceAccessControlResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_access_control_info.metadata = {'url': '/getAccessControl'}

    def set_workspace_administrators(
            self, workspace_name, administrators=None, custom_headers=None, raw=False, **operation_config):
        """Replace Admins of the Workspace.

        :param workspace_name: The name of the workspace to execute operations
         on.
        :type workspace_name: str
        :param administrators:
        :type administrators: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: WorkspaceAccessControlResponse or ClientRawResponse if
         raw=true
        :rtype: ~azure.synapse.models.WorkspaceAccessControlResponse or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.synapse.models.ErrorResponseException>`
        """
        request = models.SetWorkspaceAdministratorsRequest(administrators=administrators)

        # Construct URL
        url = self.set_workspace_administrators.metadata['url']
        path_format_arguments = {
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str', skip_quote=True),
            'SynapseDnsSuffix': self._serialize.url("self.config.synapse_dns_suffix", self.config.synapse_dns_suffix, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(request, 'SetWorkspaceAdministratorsRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('WorkspaceAccessControlResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    set_workspace_administrators.metadata = {'url': '/setWorkspaceAdmins'}
