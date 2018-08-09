from prompt_toolkit.styles import Style, merge_styles, style_from_pygments_cls

from pygments.style import Style as PygmentStyle
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic


class MyGpStyle(PygmentStyle):
    default_style = ""
    styles = {
        Comment:                'italic #888',
        Keyword:                'bold #ff0000',
        Name:                   '#00aaff',
        Name.Function:          '#0f0',
        Name.Class:             'bold #0f0',
        String:                 '#ffaa00'
    }


gnuplot_style = style_from_pygments_cls(MyGpStyle)
completion_style = Style.from_dict({
    'completion-menu.completion': 'bg:#008888 #ffffff',
    'completion-menu.completion.current': 'bg:#00aaaa #000000',
    'scrollbar.background': 'bg:#88aaaa',
    'scrollbar.button': 'bg:#222222',
})
ignuplot_style = merge_styles([gnuplot_style, completion_style])
