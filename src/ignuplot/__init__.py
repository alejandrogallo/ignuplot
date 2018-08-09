
import logging

import click

import ignuplot.repl
import ignuplot.style
from ignuplot.completion import PathCompleter, gnuplot_keyword_completer
from prompt_toolkit.completion import merge_completers

__version__ = '0.1.0'


@click.command()
@click.help_option('--help', '-h')
@click.version_option(version=__version__)
@click.option(
    '--multiline/--no-multiline',
    default=True,
    help='Enable multiline editing'
)
@click.option(
    '--vi/--no-vi',
    default=False,
    help='Enable vi editing mode'
)
@click.option(
    '--debug',
    is_flag=True,
    help='enable debug logging'
)
def main(debug, vi, multiline):
    """A gnuplot shell
    """

    logging.basicConfig(level=logging.WARNING)
    logger = logging.getLogger(__name__)
    if debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Enabled debug output")

    print('''
    If you press Control-x Control-e, the prompt will open in $EDITOR.
    Auto-suggestion accept pressing right arrow.
    Auto completion using TAB
    Exit by pressing Control-d
    ''')

    pathcompleter = PathCompleter(expanduser=True)
    completer = merge_completers(
        [pathcompleter, gnuplot_keyword_completer]
    )
    style = ignuplot.style.ignuplot_style

    repl = ignuplot.repl.Shell(
        vi_mode=vi,
        multiline=multiline,
        style=style,
        completer=completer
    )
    return repl.run()
