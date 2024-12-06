import logging
import time

from pyxt.command import command
from pyxt.parser import UnlimitedString
from pyxt.results import error, result
from xdo import Xdo

log = logging.getLogger(__name__)


@command(UnlimitedString("command"))
async def term(editor, args):
    command = args.command
    if command:
        command += "\n"
    classname = "^(ptyxis|tilix)$"
    xdo = Xdo()
    editor_window = xdo.get_active_window()
    windows = xdo.search_windows(
        winclassname=classname.encode("utf-8"), only_visible=True)
    if not windows:
        return error(f"Terminal window not found: {classname}")
    term = windows[0]
    xdo.focus_window(term)
    if command:
        xdo.enter_text_window(term, command.encode("utf-8"), 10)
        time.sleep(0.00001 * len(command) + 0.1)
        xdo.focus_window(editor_window)
    else:
        xdo.activate_window(term)
    return result()
