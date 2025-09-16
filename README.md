# User Font Installer (Windows)

A lightweight Python script to install TrueType fonts (`.ttf`) **for the current Windows user** without requiring administrator privileges.

---

## Why Current User Installation?

Installing fonts system-wide (for all users) requires **administrator rights** because it involves copying files to protected system folders (`C:\Windows\Fonts`) and modifying system-wide registry keys (`HKEY_LOCAL_MACHINE`).

This script uses a **per-user installation** approach, which:

* Copies fonts to the current user's font folder (`%LOCALAPPDATA%\Microsoft\Windows\Fonts`).
* Writes registry entries under the current user's registry hive (`HKEY_CURRENT_USER`).
* Loads fonts immediately for the current user session.

This means you can install fonts **without admin permissions** and avoid system security risks.

---

## How It Works

1. The script scans a specified folder for `.ttf` font files.
2. Copies them to the current user’s font folder (creating it if needed).
3. Adds registry entries pointing to these fonts.
4. Calls Windows API to load fonts immediately in the current session.

---

## Usage

1. Modify the `FONT_FOLDER` variable to point to the folder containing your `.ttf` font files.

2. Run the script with Python:

```bash
python install_fonts.py
```

Fonts will be installed for your user account only.

---

## Limitations

* **Windows only** — uses Windows APIs and registry.
* Installs fonts only for the current user, not system-wide.
* Only supports `.ttf` fonts currently.

---

## Future Plans

* Add a graphical user interface (GUI) for easier folder selection and installation control.
* Support `.otf` and other font formats.
* Add logging and uninstall support.

---

## License

MIT License

---
