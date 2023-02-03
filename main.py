from adjsoned import FileJsonProperties


def _main():
    properties = FileJsonProperties(filepath="examples/some_properties.json")

    # We can now access key-value/arrays data stored in our JSON file the following way:
    # (NB: the ROOT element of your JSON file MUST be a DICT!)

    if properties.debug_mode:
        print("We're in debug mode!")
        print("P.S. Properties told me that :)")

    # 'properties' is an instance of FileJsonProperties (as well as JsonProperties — a parent class)
    # 'properties.app_version' is also a JsonProperties instance, so we can access its fields like that:
    print(properties.app_version.code)  # prints '4.1.2'

    # arrays are interpreted as regular Python lists, you can just normally iterate through them:
    for section in properties.project_settings.ignored_sections:
        print("Ignoring section", section)

    # if an array element is a dictionary, it gets interpreted as a JsonProperties object as well:
    print(properties.messages[1].title)  # prints: 'Hello again.'


if __name__ == '__main__':
    _main()
