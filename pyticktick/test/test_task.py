# coding: utf-8

"""
TickTick API

[TickTick](https://ticktick.com/) TODO task manager.

The version of the OpenAPI document: 0.0.1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from pyticktick.models.task import Task  # noqa: E501


class TestTask(unittest.TestCase):
	"""Task unit test stubs"""

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def make_instance(self, include_optional) -> Task:
		"""Test Task
		include_option is a boolean, when False only required
		params are included, when True both required and
		optional params are included"""
		# uncomment below to create an instance of `Task`
		"""
        model = Task()  # noqa: E501
        if include_optional:
            return Task(
                id = '',
                task_id = '',
                project_id = '',
                title = '',
                completed_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 0,
                is_all_day = True,
                content = '',
                desc = '',
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                items = [
                    pyticktick.models.checklist_item.ChecklistItem(
                        id = '', 
                        title = '', 
                        status = null, 
                        completed_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        is_all_day = True, 
                        sort_order = 234444, 
                        start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_zone = null, )
                    ],
                priority = 0,
                reminders = ["TRIGGER:P0DT9H0M0S","TRIGGER:PT0S"],
                repeat_flag = 'RRULE:FREQ=DAILY;INTERVAL=1',
                sort_order = 12345,
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                time_zone = 'America/Los_Angeles'
            )
        else:
            return Task(
        )
        """

	def testTask(self):
		"""Test Task"""
		# inst_req_only = self.make_instance(include_optional=False)
		# inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
	unittest.main()
