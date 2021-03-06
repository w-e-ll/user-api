# coding: utf-8

"""
    Python Users API

    This is a simple Users API. It provides basic logic, CRUD operations of users.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: valentin.sheboldaev@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UserApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_user_by_uuid_post(self, user_uuid, **kwargs):  # noqa: E501
        """Delete a single user record  # noqa: E501

        Delete a user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_by_uuid_post(user_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_uuid: UUID of the user to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_user_by_uuid_post_with_http_info(user_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_user_by_uuid_post_with_http_info(user_uuid, **kwargs)  # noqa: E501
            return data

    def delete_user_by_uuid_post_with_http_info(self, user_uuid, **kwargs):  # noqa: E501
        """Delete a single user record  # noqa: E501

        Delete a user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_user_by_uuid_post_with_http_info(user_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_uuid: UUID of the user to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user_by_uuid_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_uuid' is set
        if ('user_uuid' not in params or
                params['user_uuid'] is None):
            raise ValueError("Missing the required parameter `user_uuid` when calling `delete_user_by_uuid_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_uuid' in params:
            path_params['user_uuid'] = params['user_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/delete_user/<user_uuid>', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_total_users_get(self, **kwargs):  # noqa: E501
        """Get all system users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_total_users_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_total_users_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_total_users_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_total_users_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all system users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_total_users_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_total_users_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/get_total_users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_by_email_get(self, user_email, **kwargs):  # noqa: E501
        """Get's a single user record  # noqa: E501

        Get single user record by given user_email  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_by_email_get(user_email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_email: Email of the user to get (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_by_email_get_with_http_info(user_email, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_by_email_get_with_http_info(user_email, **kwargs)  # noqa: E501
            return data

    def get_user_by_email_get_with_http_info(self, user_email, **kwargs):  # noqa: E501
        """Get's a single user record  # noqa: E501

        Get single user record by given user_email  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_by_email_get_with_http_info(user_email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_email: Email of the user to get (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_email']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_by_email_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_email' is set
        if ('user_email' not in params or
                params['user_email'] is None):
            raise ValueError("Missing the required parameter `user_email` when calling `get_user_by_email_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_email' in params:
            path_params['user_email'] = params['user_email']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/get_user_by_email/<user_email>', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_by_uuid_get(self, user_uuid, **kwargs):  # noqa: E501
        """Get's a single user record  # noqa: E501

        Get single user record by given user_uuid  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_by_uuid_get(user_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_uuid: UUID of the user to get (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_by_uuid_get_with_http_info(user_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_by_uuid_get_with_http_info(user_uuid, **kwargs)  # noqa: E501
            return data

    def get_user_by_uuid_get_with_http_info(self, user_uuid, **kwargs):  # noqa: E501
        """Get's a single user record  # noqa: E501

        Get single user record by given user_uuid  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_by_uuid_get_with_http_info(user_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_uuid: UUID of the user to get (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_by_uuid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_uuid' is set
        if ('user_uuid' not in params or
                params['user_uuid'] is None):
            raise ValueError("Missing the required parameter `user_uuid` when calling `get_user_by_uuid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_uuid' in params:
            path_params['user_uuid'] = params['user_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/get_user_by_uuid/<user_uuid>', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_user_post(self, body, **kwargs):  # noqa: E501
        """Adds a single user record  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_user_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param User body: User object (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_user_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_user_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def post_user_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Adds a single user record  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_user_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param User body: User object (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_user_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_user_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/post_user', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_users_post(self, body, **kwargs):  # noqa: E501
        """Adds users to User db. Upload as many as you want.  # noqa: E501

        Add as many users to User db, as want.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_users_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Users body: List of users to post (required)
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_users_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_users_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def post_users_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Adds users to User db. Upload as many as you want.  # noqa: E501

        Add as many users to User db, as want.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_users_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Users body: List of users to post (required)
        :return: Users
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_users_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_users_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/post_users', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Users',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_user_by_uuid_put(self, user_uuid, body, **kwargs):  # noqa: E501
        """Updates an existing user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_by_uuid_put(user_uuid, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_uuid: UUID of user to update (required)
        :param User body: User object to update (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_user_by_uuid_put_with_http_info(user_uuid, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_user_by_uuid_put_with_http_info(user_uuid, body, **kwargs)  # noqa: E501
            return data

    def update_user_by_uuid_put_with_http_info(self, user_uuid, body, **kwargs):  # noqa: E501
        """Updates an existing user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_user_by_uuid_put_with_http_info(user_uuid, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_uuid: UUID of user to update (required)
        :param User body: User object to update (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_uuid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_user_by_uuid_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_uuid' is set
        if ('user_uuid' not in params or
                params['user_uuid'] is None):
            raise ValueError("Missing the required parameter `user_uuid` when calling `update_user_by_uuid_put`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_user_by_uuid_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_uuid' in params:
            path_params['user_uuid'] = params['user_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/update_user/<user_uuid>', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
