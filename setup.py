import sys
from cx_Freeze import setup, Executable

setup(
	name = "SSSS",
	version = "2.0.0.0",
	description = "Soccer Spirits Stone Simulator",
	author = "Kinos",
	executables = [Executable("SSSS.py", base = "Win32GUI", icon = "SSSS.ico")],
	options = {
		"build.exe": {
		"create_shared_zip": False,
		"append_script_to_exe": True,
		}
	})