import sys
import os
import datetime

import pyauto
from keyhac import *

KEY_CODE_LEFT_COMMAND = 235
KEY_CODE_RIGHT_COMMAND = 255
KEY_CODE_LIST_COMMAND = [KEY_CODE_LEFT_COMMAND, KEY_CODE_RIGHT_COMMAND]

def keyhac_default(keymap):
    # --------------------------------------------------------------------
    # Text editer setting for editting config.py file

    # Setting with program file path (Simple usage)
    if 1:
        keymap.editor = "notepad.exe"

    # Setting with callable object (Advanced usage)
    if 0:
        def editor(path):
            shellExecute( None, "notepad.exe", '"%s"'% path, "" )
        keymap.editor = editor

    # --------------------------------------------------------------------
    # Customizing the display

    # Font
    keymap.setFont( "MS Gothic", 12 )

    # Theme
    keymap.setTheme("black")

def fake_mac_configure(keymap):
    keymap_global = keymap.defineWindowKeymap()

    # Switch colon and semicolon because of vim
    keymap_global["Shift-Semicolon"] = "Colon"
    keymap_global["Semicolon"] = "Shift-Semicolon"


    for i in range(len(KEY_CODE_LIST_COMMAND)):
        keymap_global[f"O-({KEY_CODE_LIST_COMMAND[i]})"] = "A-BackQuote"
        keymap.defineModifier(KEY_CODE_LIST_COMMAND[i], f"User{i}")

        # Ctrl + xxx
        keymap_global[f"U{i}-A"] = "C-A"
        keymap_global[f"U{i}-F"] = "C-F"
        keymap_global[f"U{i}-V"] = "C-V"
        keymap_global[f"U{i}-C"] = "C-C"
        keymap_global[f"U{i}-Z"] = "C-Z"
        keymap_global[f"U{i}-X"] = "C-X"
        keymap_global[f"U{i}-W"] = "C-W"


        # Alt + xxx
        keymap_global[f"U{i}-Q"] = "Alt-F4"

        # Windows + xxx
        keymap_global[f"U{i}-D"] = "W-D"
        keymap_global[f"U{i}-E"] = "W-E"
        keymap_global[f"U{i}-M"] = "W-M"
        keymap_global[f"U{i}-T"] = "W-T"
        keymap_global[f"U{i}-Tab"] = "W-Tab"


def configure(keymap):
    # Default settings
    keyhac_default(keymap)

    # Set key bind like MacOS
    fake_mac_configure(keymap)
