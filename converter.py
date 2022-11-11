from create_serializer import create_serializer


def convert_string(string, input_language, output_language):
    if input_language == output_language:
        return string
    return create_serializer(output_language).dumps(create_serializer(input_language).loads(string))


def convert_file(input_path, output_path, input_language, output_language):
    if (input_language == output_language) and (input_path == output_path):
        return
    with open(input_path, "r") as file_path:
        cache = create_serializer(input_language, input_path).load(file_path)

    with open(output_path, "w") as file_path:
        create_serializer(output_language, output_path).dumps(cache, file_path)
