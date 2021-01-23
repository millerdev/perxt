# Personal PyXT commands

Intended to be forked and customized.

The `term` command uses
[xdotool](https://manpages.ubuntu.com/manpages/focal/man1/xdotool.1.html) to
send commands to [Tilix](https://gnunn1.github.io/tilix-web/).

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
