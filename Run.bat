@echo off 
if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit
"%cd%\system\python\python.exe" "%cd%\PDF-Parser\main.py"
exit