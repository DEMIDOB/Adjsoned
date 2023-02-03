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
