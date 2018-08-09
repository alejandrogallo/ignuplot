from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import HTML


def prompt_info(text):
    print_formatted_text(HTML('<green>{0}</green>').format(text))


def prompt_error(text):
    print_formatted_text(HTML('<red>{0}</red>').format(text))
