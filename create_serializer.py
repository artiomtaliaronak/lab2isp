from serializers.json_serializer import JsonSerializer
from serializers.yaml_serializer import YamlSerializer


def language_picker(language):
    if language == "json":
        return JsonSerializer()
    if language == "yaml":
        return YamlSerializer()


def create_serializer(language, input_file="null"):
    if input_file == "null":
        return language_picker(language)
    else:
        if input_file.rpartition(".")[2] == language:
            return language_picker(language)
        else:
            return language_picker(input_file.rpartition(".")[2])
