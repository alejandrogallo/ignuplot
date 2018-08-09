from prompt_toolkit.completion import (
    WordCompleter,
    Completer,
    Completion,
)
import os
import re


# These keywords were taken from the vim syntax files for gnuplot
gnuplot_keyword_completer = WordCompleter([
"GNUTERM", "GPVAL_TERM", "GPVAL_TERMOPTIONS", "GPVAL_SPLOT", "GPVAL_OUTPUT",
"GPVAL_ENCODING", "GPVAL_VERSION", "GPVAL_PATCHLEVEL", "GPVAL_COMPILE_OPTIONS",
"GPVAL_MULTIPLOT", "GPVAL_PLOT", "GPVAL_VIEW_ZSCALE", "GPVAL_TERMINALS",
"GPVAL_pi", "GPVAL_NaN", "GPVAL_ERRNO", "GPVAL_ERRMSG", "GPVAL_PWD", "pi",
"NaN", "GPVAL_LAST_PLOT", "GPVAL_TERM_WINDOWID", "GPVAL_X_MIN", "GPVAL_X_MAX",
"GPVAL_X_LOG", "GPVAL_DATA_X_MIN", "GPVAL_DATA_X_MAX", "GPVAL_Y_MIN",
"GPVAL_Y_MAX", "GPVAL_Y_LOG", "GPVAL_DATA_Y_MIN", "GPVAL_DATA_Y_MAX",
"GPVAL_X2_MIN", "GPVAL_X2_MAX", "GPVAL_X2_LOG", "GPVAL_DATA_X2_MIN",
"GPVAL_DATA_X2_MAX", "GPVAL_Y2_MIN", "GPVAL_Y2_MAX", "GPVAL_Y2_LOG",
"GPVAL_DATA_Y2_MIN", "GPVAL_DATA_Y2_MAX", "GPVAL_Z_MIN", "GPVAL_Z_MAX",
"GPVAL_Z_LOG", "GPVAL_DATA_Z_MIN", "GPVAL_DATA_Z_MAX", "GPVAL_CB_MIN",
"GPVAL_CB_MAX", "GPVAL_CB_LOG", "GPVAL_DATA_CB_MIN", "GPVAL_DATA_CB_MAX",
"GPVAL_T_MIN", "GPVAL_T_MAX", "GPVAL_T_LOG", "GPVAL_U_MIN", "GPVAL_U_MAX",
"GPVAL_U_LOG", "GPVAL_V_MIN", "GPVAL_V_MAX", "GPVAL_V_LOG", "GPVAL_R_MIN",
"GPVAL_R_LOG", "GPVAL_TERM_XMIN", "GPVAL_TERM_XMAX", "GPVAL_TERM_YMIN",
"GPVAL_TERM_YMAX", "GPVAL_TERM_XSIZE", "GPVAL_TERM_YSIZE", "GPVAL_VIEW_MAP",
"GPVAL_VIEW_ROT_X", "GPVAL_VIEW_ROT_Z", "GPVAL_VIEW_SCALE", "STATS_records",
"STATS_outofrange", "STATS_invalid", "STATS_blank", "STATS_blocks",
"STATS_columns", "STATS_min", "STATS_max", "STATS_index_min",
"STATS_index_max", "STATS_lo_quartile", "STATS_median", "STATS_up_quartile",
"STATS_mean", "STATS_stddev", "STATS_sum", "STATS_sumsq", "STATS_correlation",
"STATS_slope", "STATS_intercept", "STATS_sumxy", "STATS_pos_min_y",
"STATS_pos_max_y", "STATS_mean", "STATS_stddev", "STATS_mean_x", "STATS_sum_x",
"STATS_stddev_x", "STATS_sumsq_x", "STATS_min_x", "STATS_max_x",
"STATS_median_x", "STATS_lo_quartile_x", "STATS_up_quartile_x",
"STATS_index_min_x", "STATS_index_max_x", "STATS_mean_y", "STATS_stddev_y",
"STATS_sum_y", "STATS_sumsq_y", "STATS_min_y", "STATS_max_y", "STATS_median_y",
"STATS_lo_quartile_y", "STATS_up_quartile_y", "STATS_index_min_y",
"STATS_index_max_y", "STATS_correlation", "STATS_sumxy", "FIT_LIMIT",
"FIT_MAXITER", "FIT_START_LAMBDA", "FIT_LAMBDA_FACTOR", "FIT_LOG",
"FIT_SCRIPT", "ignore", "syn", "case", "match", "abs", "acos", "acosh", "airy",
"arg", "asin", "asinh", "atan", "atan2", "atanh", "EllipticK", "EllipticE",
"EllipticPi", "besj0", "besj1", "besy0", "besy1", "ceil", "cos", "cosh", "erf",
"erfc", "exp", "expint", "floor", "gamma", "ibeta", "inverf", "igamma", "imag",
"invnorm", "int", "lambertw", "lgamma", "log", "log10", "norm", "rand", "real",
"sgn", "sin", "sin", "sinh", "sqrt", "tan", "tanh", "voigt", "gprintf",
"sprintf", "strlen", "strstrt", "substr", "strftime", "strptime", "system",
"word", "words", "column", "columnhead", "columnheader", "defined", "exists",
"hsv2rgb", "stringcolumn", "timecolumn", "tm_hour", "tm_mday", "tm_min",
"tm_mon", "tm_sec", "tm_wday", "tm_yday", "tm_year", "time", "valid", "value",
"x", "y", "t", "u", "v", "z", "s", "if", "else", "do", "for", "while", "via",
"z", "axes", "x1y1", "x1y2", "x2y1", "x2y2", "binary", "matrix", "general",
"array", "record", "format", "endian", "filetype", "avs", "edf", "png", "scan",
"transpose", "dx", "dy", "dz", "flipx", "flipy", "flipz", "origin", "center",
"rotate", "using", "perpendicular", "skip", "every", "binary", "nonuniform",
"matrix", "index", "every", "using", "smooth", "volatile", "noautoscale",
"every", "index", "unique", "frequency", "cumulative", "cnormal", "kdensity",
"csplines", "acsplines", "bezer", "sbezier", "thru", "using", "u",
"xticlabels", "yticlabels", "zticlabels", "x2ticlabels", "y2ticlabels", "xtic",
"ytic", "ztic", "errorbars", "xerrorbars", "yerrorbars", "xyerrorbars",
"errorlines", "xerrorlines", "yerrorlines", "xyerrorlines", "title", "t",
"tit", "notitle", "columnheader", "at", "beginning", "end", "with", "w",
"linestyle", "ls", "linetype", "lt", "linewidth", "lw", "linecolor", "lc",
"pointtype", "pt", "pointsize", "ps", "fill", "fs", "nohidden3d", "nocontours",
"nosurface", "palette", "lines", "l", "points", "p", "linespoints", "lp",
"surface", "dots", "impulses", "labels", "vectors", "steps", "fsteps",
"histeps", "errorbars", "errorlines", "financebars", "xerrorbars",
"xerrorlines", "xyerrorbars", "yerrorbars", "yerrorlines", "boxes",
"boxerrorbars", "boxxyerrorbars", "boxplot", "candlesticks", "circles",
"ellipses", "filledcurves", "histogram", "image", "rgbimage", "rgbalpha",
"pm3d", "variable", "save", "functions", "func", "variables", "all", "var",
"terminal", "term", "set", "angles", "degrees", "deg", "radians", "rad",
"arrow", "from", "to", "rto", "length", "angle", "arrowstyle", "as", "nohead",
"head", "backhead", "heads", "size", "filled", "empty", "nofilled", "front",
"back", "linestyle", "linetype", "linewidth", "autoscale", "x", "y", "z", "cb",
"x2", "y2", "zy", "min", "max", "fixmin", "fixmax", "fix", "keepfix",
"noextend", "bars", "small", "large", "fullwidth", "front", "back", "bind",
"margin", "bmargin", "lmargin", "rmargin", "tmargin", "border", "front",
"back", "boxwidth", "absolute", "relative", "clabel", "clip", "points", "one",
"two", "cntrlabel", "format", "font", "start", "interval", "onecolor",
"cntrparam", "linear", "cubicspline", "bspline", "points", "order", "levels",
"auto", "discrete", "incremental", "colorbox", "vertical", "horizontal",
"default", "user", "origin", "size", "front", "back", "noborder", "bdefault",
"border", "colornames", "contour", "base", "surface", "both", "datafile",
"fortran", "nofpe_trap", "missing", "separator", "whitespace", "tab", "comma",
"commentschars", "binary", "decimalsign", "locale", "dgrid3d", "splines",
"qnorm", "gauss", "cauchy", "exp", "box", "hann", "kdensity", "dummy",
"encoding", "default", "iso_8859_1", "iso_8859_15", "iso_8859_2", "iso_8859_9",
"koi8r", "koi8u", "cp437", "cp850", "cp852", "cp950", "cp1250", "cp1251",
"cp1254", "sjis", "utf8", "fit", "logfile", "default", "quiet", "noquiet",
"results", "brief", "verbose", "errorvariables", "noerrorvariables",
"errorscaling", "noerrorscaling", "prescale", "noprescale", "maxiter", "none",
"limit", "limit_abs", "start-lambda", "script", "lambda-factor", "fontpath",
"format", "functions", "grid", "polar", "layerdefault", "xtics", "ytics",
"ztics", "x2tics", "y2tics", "cbtics", "mxtics", "mytics", "mztics", "mx2tics",
"my2tics", "mcbtics", "xmtics", "ymtics", "zmtics", "x2mtics", "y2mtics",
"cbmtics", "noxtics", "noytics", "noztics", "nox2tics", "noy2tics", "nocbtics",
"nomxtics", "nomytics", "nomztics", "nomx2tics", "nomy2tics", "nomcbtics",
"hidden3d", "offset", "trianglepattern", "undefined", "altdiagonal",
"noaltdiagonal", "bentover", "nobentover", "noundefined", "historysize",
"isosamples", "key", "on", "off", "inside", "outside", "at", "left", "right",
"center", "top", "bottom", "vertical", "horizontal", "Left", "Right", "opaque",
"noopaque", "reverse", "noreverse", "invert", "maxrows", "noinvert", "samplen",
"spacing", "width", "height", "autotitle", "noautotitle", "title", "enhanced",
"noenhanced", "font", "textcolor", "box", "nobox", "linetype", "linewidth",
"maxcols", "label", "left", "center", "right", "rotate", "norotate", "by",
"font", "front", "back", "textcolor", "point", "nopoint", "offset", "boxed",
"hypertext", "linetype", "link", "via", "inverse", "loadpath", "locale",
"logscale", "log", "macros", "mapping", "cartesian", "spherical",
"cylindrical", "mouse", "doubleclick", "nodoubleclick", "zoomcoordinates",
"nozoomcoordinates", "ruler", "noruler", "at", "polardistance",
"nopolardistance", "deg", "tan", "format", "clipboardformat", "mouseformat",
"labels", "nolabels", "zoomjump", "nozoomjump", "verbose", "noverbose",
"multiplot", "title", "font", "layout", "rowsfirst", "downwards", "downwards",
"upwards", "scale", "offset", "object", "behind", "fillcolor", "fc", "fs",
"rectangle", "ellipse", "circle", "polygon", "at", "center", "size", "units",
"xy", "xx", "yy", "to", "from", "offsets", "origin", "output", "parametric",
"plot", "add2history", "hidden3d", "interpolate", "scansautomatic",
"scansforward", "scansbackward", "depthorder", "flush", "begin", "center",
"end", "ftriangles", "noftriangles", "clip1in", "clip4in", "mean", "map",
"corners2color", "geomean", "harmean", "rms", "median", "min", "max", "c1",
"c2", "c3", "c4", "pm3d", "at", "nohidden3d", "implicit", "explicit",
"palette", "gray", "color", "gamma", "rgbformulae", "defined", "file",
"functions", "cubehelix", "start", "cycles", "saturation", "model", "RGB",
"HSV", "CMY", "YIQ", "XYZ", "positive", "negative", "nops_allcF", "ps_allcF",
"maxcolors", "float", "int", "gradient", "fit2rgbformulae", "rgbformulae",
"pointintervalbox", "pointsize", "polar", "print", "append", "psdir", "raxis",
"rrange", "rtics", "samples", "size", "square", "nosquare", "ratio", "noratio",
"style", "arrow", "auto", "back", "border", "boxplot", "candlesticks",
"circle", "clustered", "columnstacked", "data", "default", "ellipse", "empty",
"fill", "financebars", "fraction", "front", "function", "gap", "graph", "head",
"histogram", "increment", "labels", "lc", "line", "linecolor", "linetype",
"linewidth", "lt", "lw", "noborder", "nofilled", "nohead", "nooutliers",
"nowedge", "off", "opaque", "outliers", "palette", "pattern", "pi",
"pointinterval", "pointsize", "pointtype", "ps", "pt", "radius", "range",
"rectangle", "rowstacked", "screen", "separation", "size", "solid", "sorted",
"textbox", "transparent", "units", "unsorted", "userstyles", "wedge", "x",
"x2", "xx", "xy", "yy", "surface", "implicit", "explicit", "table", "terminal",
"term", "push", "pop", "aed512", "aed767", "aifm", "aqua", "be", "cairo",
"cairolatex", "canvas", "cgm", "context", "corel", "debug", "dumb", "dxf",
"dxy800a", "eepic", "emf", "emxvga", "epscairo", "epslatex", "epson_180dpi",
"excl", "fig", "ggi", "gif", "gpic", "hpgl", "grass", "hp2623a", "hp2648",
"hp500c", "hpljii", "hppj", "imagen", "jpeg", "kyo", "latex", "linux", "lua",
"mf", "mif", "mp", "next", "openstep", "pbm", "pdf", "pdfcairo", "pm", "png",
"pngcairo", "postscript", "pslatex", "pstex", "pstricks", "qms", "qt", "regis",
"sun", "svg", "svga", "tek40", "tek410x", "texdraw", "tgif", "tikz",
"tkcanvas", "tpic", "vgagl", "vws", "vx384", "windows", "wx", "wxt", "x11",
"xlib", "color", "monochrome", "dashlength", "dl", "eps", "pdf", "fontscale",
"standalone", "blacktext", "colortext", "colourtext", "header", "noheader",
"mono", "color", "solid", "dashed", "notransparent", "crop", "crop",
"background", "input", "rounded", "butt", "square", "size", "fsize",
"standalone", "name", "jsdir", "defaultsize", "timestamp", "notimestamp",
"colour", "mitered", "beveled", "round", "squared", "palfuncparam",
"blacktext", "nec_cp6", "mppoints", "inlineimages", "externalimages",
"defaultfont", "aspect", "feed", "nofeed", "rotate", "small", "tiny",
"standalone", "oldstyle", "newstyle", "level1", "leveldefault", "level3",
"background", "nobackground", "solid", "clip", "noclip", "colortext",
"colourtext", "epson_60dpi", "epson_lx800", "okidata", "starc", "tandy_60dpi",
"dpu414", "nec_cp6", "draft", "medium", "large", "normal", "landscape",
"portrait", "big", "inches", "pointsmax", "textspecial", "texthidden",
"thickness", "depth", "version", "acceleration", "giant", "delay", "loop",
"optimize", "nooptimize", "pspoints", "FNT9X17", "FNT13X25", "interlace",
"nointerlace", "courier", "originreset", "nooriginreset", "gparrows",
"nogparrows", "picenvironment", "nopicenvironment", "tightboundingbox",
"notightboundingbox", "charsize", "gppoints", "nogppoints", "fontscale",
"textscale", "fulldoc", "nofulldoc", "standalone", "preamble", "header",
"tikzplot", "tikzarrows", "notikzarrows", "cmykimages", "externalimages",
"noexternalimages", "polyline", "vectors", "magnification", "psnfss",
"nopsnfss", "prologues", "a4paper", "amstex", "fname", "fsize", "server",
"persist", "widelines", "interlace", "truecolor", "notruecolor", "defaultplex",
"simplex", "duplex", "nofontfiles", "adobeglyphnames", "noadobeglyphnames",
"nostandalone", "metric", "textrigid", "animate", "nopspoints", "hpdj",
"FNT5X9", "roman", "emtex", "rgbimages", "bitmap", "nobitmap", "providevars",
"nointerlace", "add", "delete", "auxfile", "hacktext", "unit", "raise",
"palfuncparam", "noauxfile", "nohacktext", "nounit", "noraise", "ctrl",
"noctrl", "close", "widget", "fixed", "dynamic", "tek40xx", "vttek",
"bitgraph", "perltk", "interactive", "red", "green", "blue", "interpolate",
"mode", "position", "ctrlq", "replotonresize", "position", "noctrlq",
"noreplotonresize", "termoption", "font", "fontscale", "solid", "dashed",
"tics", "add", "axis", "border", "mirror", "nomirror", "in", "out", "scale",
"rotate", "norotate", "by", "offset", "nooffset", "left", "autojustify",
"format", "font", "textcolor", "right", "center", "ticslevel", "ticscale",
"timestamp", "top", "bottom", "offset", "font", "timefmt", "title", "offset",
"font", "textcolor", "tc", "trange", "urange", "vrange", "variables",
"version", "view", "map", "equal", "noequal", "xy", "xyz", "xdata", "ydata",
"zdata", "x2data", "y2data", "cbdata", "xdtics", "ydtics", "zdtics", "x2dtics",
"y2dtics", "cbdtics", "xzeroaxis", "yzeroaxis", "zzeroaxis", "x2zeroaxis",
"y2zeroaxis", "cbzeroaxis", "time", "geographic", "xlabel", "ylabel", "zlabel",
"x2label", "y2label", "cblabel", "offset", "font", "textcolor", "by",
"parallel", "xrange", "yrange", "zrange", "x2range", "y2range", "cbrange",
"xyplane", "zero", "zeroaxis", "nooutput", "terminal", "palette", "rgb", "rbg",
"grb", "gbr", "brg", "bgr", "contained", "cd", "call", "clear", "evaluate",
"exit", "fit", "help", "history", "load", "lower", "pause", "plot", "p",
"print", "pwd", "quit", "raise", "refresh", "replot", "rep", "reread", "reset",
"save", "set", "show", "shell", "splot", "spstats", "stats", "test",
"undefine", "unset", "update",
], ignore_case=True)


class PathCompleter(Completer):
    """
    Complete for Path variables.

    :param get_paths: Callable which returns a list of directories to look into
                      when the user enters a relative path.
    :param file_filter: Callable which takes a filename and returns whether
                        this file should show up in the completion. ``None``
                        when no filtering has to be done.
    :param min_input_len: Don't do autocompletion when the input string is
    shorter.
    """
    def __init__(
            self, only_directories=False, get_paths=None,
            file_filter=None, min_input_len=0, expanduser=False
            ):
        assert get_paths is None or callable(get_paths)
        assert file_filter is None or callable(file_filter)
        assert isinstance(min_input_len, int)
        assert isinstance(expanduser, bool)

        self.only_directories = only_directories
        self.get_paths = get_paths or (lambda: ['.'])
        self.file_filter = file_filter or (lambda _: True)
        self.min_input_len = min_input_len
        self.expanduser = expanduser

    def get_completions(self, document, complete_event):
        match = re.match(r'^.*[\'"]([^ ]+)$', document.text_before_cursor)
        if match is None:
            return

        text = match.group(1)

        # Complete only when we have at least the minimal input length,
        # otherwise, we can too many results and autocompletion will become too
        # heavy.
        if len(text) < self.min_input_len:
            return

        try:
            # Do tilde expansion.
            if self.expanduser:
                text = os.path.expanduser(text)

            # Directories where to look.
            dirname = os.path.dirname(text)
            if dirname:
                directories = [os.path.dirname(os.path.join(p, text))
                               for p in self.get_paths()]
            else:
                directories = self.get_paths()

            # Start of current file.
            prefix = os.path.basename(text)

            # Get all filenames.
            filenames = []
            for directory in directories:
                # Look for matches in this directory.
                if os.path.isdir(directory):
                    for filename in os.listdir(directory):
                        if filename.startswith(prefix):
                            filenames.append((directory, filename))

            # Sort
            filenames = sorted(filenames, key=lambda k: k[1])

            # Yield them.
            for directory, filename in filenames:
                completion = filename[len(prefix):]
                full_name = os.path.join(directory, filename)

                if os.path.isdir(full_name):
                    # For directories, add a slash to the filename.
                    # (We don't add them to the `completion`. Users can type it
                    # to trigger the autocompletion themselves.)
                    filename += '/'
                elif self.only_directories:
                    continue

                if not self.file_filter(full_name):
                    continue

                yield Completion(completion, 0, display=filename)
        except OSError:
            pass
