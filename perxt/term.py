import logging

from pyxt.command import command
from pyxt.parser import String, VarArgs
from pyxt.results import error, result
from xdo import Xdo

log = logging.getLogger(__name__)


@command(VarArgs("command_parts", String("command")))
async def term(editor, args):
    command = " ".join(p for p in args.command_parts if p)
    if command:
        command += "\n"
    window_name = r"^Tilix:".encode("utf-8")
    try:
        xdo = Xdo()
        editor_window = xdo.get_active_window()
        windows = xdo.search_windows(window_name, only_visible=True)
        if not windows:
            return error("Tilix window not found")
        term = windows[0]
        xdo.focus_window(term)
        if command:
            xdo.enter_text_window(term, command.encode("utf-8"))
            xdo.focus_window(editor_window)
        else:
            xdo.raise_window(term)
    except Exception:
        log.exception("term error")
        raise
    return result()
