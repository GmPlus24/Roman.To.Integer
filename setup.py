from cx_Freeze import setup, Executable
import sys




setup(
    name = "RomanToInteger",
    version = "1.0",
    options = {"build_exe": {"include_files": ["backspace-icon.png", "copy-icon.png", "information-icon.png", "RomanToInteger-icon.png", "qt-icon.png"]}},
    executables = [Executable("RomanToInteger.py", base = "Win32GUI", icon = "RomanToInteger-icon.ico")]
) 


