from os.path import splitext

from pyxt.command import command
from pyxt.cmd.ag import ag, get_selection_regex, project_dirname
from pyxt.parser import File, Regex, RegexPattern, VarArgs, String
from pyxt.results import error, input_required


RULES = {
    "py": {
        "ag_filetype_options": ["--py"],
        "delimiters": [
            (r"(?<=\bclass[ \t])[ \t]*", r"(?=[ \t]*[(:])"),
            (r"(?<=\bdef[ \t])[ \t]*", r"(?=[ \t]*\()"),
            (r"\b", r"(?=[ \t]*=[^=])"),
        ],
    },
    "js": {
        "ag_filetype_options": ["--js"],
        "delimiters": [
            (r"(?<=\bfunction[ \t])[ \t]*", r"(?=[ \t]*[(:])"),
            (r"\b", r"(?=[ \t]*=[^=])"),
        ],
    },
}


@command(
    Regex("pattern", default=get_selection_regex, delimiters="'\""),
    File("path", default=project_dirname, directory=True),
    VarArgs("options", String("options")),
    name="def",
)
async def find_definition(editor, args):
    """Find definition

    Search in files for definitions matching the specified pattern based
    on an option passed on the command line (`--py` or `--js`) or on the
    current file's syntax rules.

    Currently only two languages are supported: Python and JavaScript.
    """
    if not args.pattern:
        return input_required("pattern is required", args)
    def_pattern = args.pattern
    lang = get_lang_option(args.options) or get_lang(await editor.file_path)
    rules = RULES.get(lang)
    if rules is None:
        return error(f"delimiters for {lang} not found")
    delims = rules["delimiters"]
    args.pattern = RegexPattern(
        "|".join(start + def_pattern + end for start, end in delims),
        def_pattern.flags,
    )
    args.options.extend(rules.get("ag_filetype_options", []))
    return await ag(editor, args)


def get_lang(file_path):
    return splitext(file_path)[1].lstrip(".")


def get_lang_option(options):
    for lang, data in RULES.items():
        if any(opt in options for opt in data["ag_filetype_options"]):
            return lang
    return None
