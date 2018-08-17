from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory, FileHistory
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

from pygments.lexers.graphics import GnuplotLexer
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic

import os
from ignuplot.utils import prompt_info, prompt_error
import ignuplot.config


def gnuplot(lines):
    import subprocess
    proc = subprocess.Popen(
        [ignuplot.config.GNUPLOT_BINARY, '-p'],
        shell=False,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    for line in lines + ['']:
        proc.stdin.write('{0}\n'.format(line).encode())
    return proc.communicate()


class Shell:

    def __init__(
        self,
        vi_mode=False,
        completer=None,
        multiline=True,
        style=None,
            ):

        self.style = style
        self.multiline = multiline
        self.vi_mode = vi_mode
        self.completer = completer
        self.lines = []
        self.history = FileHistory(
            os.path.join(os.path.expanduser('~'), '.ignuplot-history')
        )

        self.session = PromptSession(
            history=self.history,
            style=self.style,
            enable_history_search=True,
            auto_suggest=AutoSuggestFromHistory()
        )

    def digest(self):
        stdout, stderr = gnuplot(self.lines)
        if stdout:
            prompt_info(stdout.decode())
        if stderr:
            self.lines.pop(-1)
            prompt_error(stderr.decode())

    def run(self):
        while True:
            try:
                text = self.session.prompt(
                    'ignu> ',
                    vi_mode=self.vi_mode,
                    lexer=PygmentsLexer(GnuplotLexer),
                    completer=self.completer,
                    multiline=self.multiline,
                    enable_open_in_editor=True,
                    enable_suspend=True
                )
                self.lines.append(text)
                self.digest()
            except KeyboardInterrupt:
                pass
            except:
                prompt_info('Goodbye and thanks for all the fish!')
                return 0
