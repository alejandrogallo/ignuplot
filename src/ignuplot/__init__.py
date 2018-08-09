
import logging

import click
import os

import ignuplot.repl
import ignuplot.style
from ignuplot.completion import PathCompleter, gnuplot_keyword_completer
from prompt_toolkit.completion import merge_completers

__version__ = '0.1.0'


@click.command()
@click.help_option('--help', '-h')
@click.argument(
    'script',
    default=None,
    nargs=1,
    required=False,
    type=click.Path()
)
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
    '--record', '-r',
    is_flag=True,
    help='Append the commands typed to the input gnuplot script'
)
@click.option(
    '--debug',
    is_flag=True,
    help='enable debug logging'
)
def main(script, debug, vi, multiline, record):
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

    if script is not None and os.path.exists(script):
        with open(script) as fd:
            text = fd.read()
            repl.lines = [text]
            repl.history.append_string(text)
            repl.digest()

    returncode = repl.run()
    if record:
        with open(script, 'a+') as fd:
            for line in repl.lines:
                fd.write('{0}\n'.format(line))

    return returncode
