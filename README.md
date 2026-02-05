# 🧮 Calcus - Modern CustomTkinter Calculator

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A modern, responsive, and customizable calculator application built using **Python** and **CustomTkinter**. Designed for Windows with a sleek dark/light mode UI.

---

## 📥 Download App

Get the standalone installer for Windows. No Python installation required.

> **Current Version:** v1.0 | **File:** `Calcus Setup.exe`

[![Download Calcus](https://img.shields.io/badge/Download_Installer-.exe-blue?style=for-the-badge&logo=windows)](https://github.com/salmansync/CustomTkinter_Calculator_All/blob/main/Output/Calcus%20Setup.exe)

_Click the button above to download._

---

## 📸 Screenshots

|                                          Light Mode                                          |                                         Dark Mode                                          |
| :------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------: |
| ![Light Mode](https://github.com/salmansync/CustomTkinter_Calculator_All/raw/main/Light.png) | ![Dark Mode](https://github.com/salmansync/CustomTkinter_Calculator_All/raw/main/Dark.png) |

> _Tip: Upload screenshots to your repo and replace the links above to show off your UI!_

---

## 🚀 Features

- 🌓 **Theme Toggle:** Switch instantly between Light and Dark modes.
- 🧠 **Smart History:** View past calculations and clear history with one click.
- 📱 **Responsive UI:** Auto-scaling font sizes and window layout (`350x650 px`).
- ➗ **Advanced Math:** Includes Square Root (`√`), Power (`^`), and Percentage (`%`) logic.
- 🔁 **ANS Memory:** Recall your last calculated answer automatically.
- 🚫 **Safety First:** Robust error handling for invalid inputs and division by zero.

---

## ⌨️ Keyboard Shortcuts

| Key                   | Action                    |
| :-------------------- | :------------------------ |
| `0-9` `+` `-` `*` `/` | Standard Input            |
| `Enter`               | Evaluate Result (=)       |
| `Backspace`           | Delete last character     |
| `Esc`                 | Clear All (AC)            |
| `r`                   | Square Root (√)           |
| `^`                   | Power / Exponent (\*\*)   |
| `%`                   | Percentage                |
| `t`                   | Toggle Theme (Light/Dark) |

---

## 🛠️ For Developers: Installation & Setup

If you want to run the source code or contribute:

### 1. Requirements

- Python 3.x
- `customtkinter` library

### 2. Install Dependencies

```bash
pip install customtkinter
3. Run the App
Bash

python Calculator7.py
Make sure calcu.ico is in the project folder for the icon to load.

🏗️ Build it Yourself (.exe)
To compile the application from source code into a standalone .exe:

1. Install PyInstaller
Bash

pip install pyinstaller
2. Build Command
Bash

pyinstaller --noconsole --onefile --icon=calcu.ico Calculator7.py
Output: The file will appear in the dist/ folder.

🛠️ Tech Stack
Language: Python 3.12+

UI Framework: CustomTkinter (Modern wrapper for Tkinter)

Core GUI: Tkinter

Packaging: PyInstaller / Inno Setup

👤 Author
Salman Farsi
```
