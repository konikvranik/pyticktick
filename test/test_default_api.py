# coding: utf-8

"""
    TickTick API

    [TickTick](https://ticktick.com/) TODO task manager.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pyticktick.openapi_client.api.default_api import DefaultApi  # noqa: E501


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_oauth_token_post(self) -> None:
        """Test case for oauth_token_post

        Get token  # noqa: E501
        """
        pass

    def test_open_v1_project_get(self) -> None:
        """Test case for open_v1_project_get

        Get User Project.  # noqa: E501
        """
        pass

    def test_open_v1_project_post(self) -> None:
        """Test case for open_v1_project_post

        Create Project  # noqa: E501
        """
        pass

    def test_open_v1_project_project_id_data_get(self) -> None:
        """Test case for open_v1_project_project_id_data_get

        """
        pass

    def test_open_v1_project_project_id_delete(self) -> None:
        """Test case for open_v1_project_project_id_delete

        """
        pass

    def test_open_v1_project_project_id_get(self) -> None:
        """Test case for open_v1_project_project_id_get

        """
        pass

    def test_open_v1_project_project_id_post(self) -> None:
        """Test case for open_v1_project_project_id_post

        Update Project  # noqa: E501
        """
        pass

    def test_open_v1_project_project_id_task_task_id_complete_post(self) -> None:
        """Test case for open_v1_project_project_id_task_task_id_complete_post

        Update Task  # noqa: E501
        """
        pass

    def test_open_v1_project_project_id_task_task_id_delete(self) -> None:
        """Test case for open_v1_project_project_id_task_task_id_delete

        Delete task.  # noqa: E501
        """
        pass

    def test_open_v1_project_project_id_task_task_id_get(self) -> None:
        """Test case for open_v1_project_project_id_task_task_id_get

        Get Task By Project ID And Task ID.  # noqa: E501
        """
        pass

    def test_open_v1_task_post(self) -> None:
        """Test case for open_v1_task_post

        Create Task  # noqa: E501
        """
        pass

    def test_open_v1_task_task_id_post(self) -> None:
        """Test case for open_v1_task_task_id_post

        Update Task  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
