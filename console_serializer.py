import argparse
import converter


def main():
    try:
        parser = argparse.ArgumentParser(
            description="Serializer", fromfile_prefix_chars="@"
        )

        parser.add_argument(
            "input_path",
            metavar="input_path",
            type=str
        )

        parser.add_argument(
            "-il",
            metavar="input_language",
            choices=["json", "yaml"],
            default="json",
            type=str
        )

        parser.add_argument(
            "-ol",
            metavar="output_language",
            choices=["json", "yaml"],
            default="json",
            type=str
        )

        parser.add_argument(
            "output_path",
            metavar="output_path",
            type=str
        )

        args = parser.parse_args()
        converter.convert_file(**vars(args))

    except (Exception,) as e:
        print(e.message)
