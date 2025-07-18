# coding: utf-8

"""
TickTick API

[TickTick](https://ticktick.com/) TODO task manager.

The version of the OpenAPI document: 0.0.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from pyticktick.models.oauth_token_post_request import OauthTokenPostRequest  # noqa: E501


class TestOauthTokenPostRequest(unittest.TestCase):
	"""OauthTokenPostRequest unit test stubs"""

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def make_instance(self, include_optional) -> OauthTokenPostRequest:
		"""Test OauthTokenPostRequest
		include_option is a boolean, when False only required
		params are included, when True both required and
		optional params are included"""
		# uncomment below to create an instance of `OauthTokenPostRequest`
		"""
        model = OauthTokenPostRequest()  # noqa: E501
        if include_optional:
            return OauthTokenPostRequest(
                code = None,
                grant_type = None,
                scope = None,
                redirect_uri = None
            )
        else:
            return OauthTokenPostRequest(
        )
        """

	def testOauthTokenPostRequest(self):
		"""Test OauthTokenPostRequest"""
		# inst_req_only = self.make_instance(include_optional=False)
		# inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
	unittest.main()
