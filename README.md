# Personal PyXT commands

Intended to be forked and customized.

The `term` command uses
[xdotool](https://manpages.ubuntu.com/manpages/focal/man1/xdotool.1.html)
([library docs](https://rshk.github.io/python-libxdo/library.html)) to
send commands to [Tilix](https://gnunn1.github.io/tilix-web/).

The `def` command extends PyXT's `ag` built in command to make it easier to find
the definition of a function, class or variable by its name. Currently it
supports Python (.py) and JavaScript (.js). By default it searches the file
type of the current file, but `--py` or `--js` may be passed as an option to
force it to search a specific file type. It is a candidate to be moved into
PyXT-proper once it has an extensible framework for adding new languages.

Sample shortcut mappings:

- Hotkey to send a command to the Tilix running beside VS Code.
  ```json
  {
      "key": "ctrl+r",
      "command": "pyxt.command",
      "args": {"text": "term "}
  }
  ```
- Hotkey to immediately run the most recent `term` command (usually something
  like `nosetests -x`).
  ```json
  {
      "key": "f6",
      "command": "pyxt.command",
      "args": {"text": "history redo term", "exec": true}
  }
  ```

Installation:

```sh
git clone https://github.com/millerdev/perxt.git
cd perxt
pyenv activate pyxt  # or however you ativate your pyxt virtualenv
pip install -r requires.txt
pip install .  # --editable can be handy here if you plan to customize the code
```

Open VS Code settings and set "PyXT: User Script" value to "perxt", then reload
VS Code.

See also https://github.com/millerdev/pyxt#adding-your-own-custom-commands
