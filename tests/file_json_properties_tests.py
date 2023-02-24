import unittest

from adjsoned import JsonProperties, FileJsonProperties


class FileJsonPropertiesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.props = FileJsonProperties("properties.json")

    def test_bool(self):
        result = self.props.debug_mode
        self.assertEqual(result, False)

    def test_dict_to_json_props(self):
        settings = self.props.project_settings
        self.assertTrue(isinstance(settings, JsonProperties))

    def test_array_of_dicts(self):
        messages = self.props.messages
        result = messages[0].title
        self.assertEqual(result, "Hello!")

    def test_update_from_same_file(self):
        self.props.update()
        self.assertEqual(self.props.debug_mode, False)

    def test_update_from_other_file(self):
        self.props.update(new_filepath="../examples/some_properties.json")
        self.assertEqual(self.props.debug_mode, True)

    def test_python_in(self):
        result_neg = "this_field_does_not_exist" in self.props
        self.assertFalse(result_neg)

        result_pos = "messages" in self.props and "title" in self.props.messages[0]
        self.assertTrue(result_pos)

        # test if the item's pythonifying works: both pythonified and camel-cased keys should work
        self.assertTrue("debugMode" in self.props and "debug_mode" in self.props)

    def test_subscribtable_get(self):
        result_code = self.props.app_version["code"]
        self.assertEqual(result_code, "4.1.2")

        # test if the item's pythonifying works: both snake- and camel-cased keys should work the same
        result_camel = self.props["projectSettings"]
        result_snake = self.props["project_settings"]

        self.assertEqual(result_camel, result_snake)
        self.assertIsNotNone(result_camel)  # it's sufficient to only check whether one result is not none since
                                            # the equality of the both results gets asserted above

    def test_subscribtable_set(self):
        result_before = self.props["debugMode"]
        self.props["debugMode"] = not result_before
        result_after = self.props["debugMode"]
        self.assertNotEqual(result_before, result_after)
