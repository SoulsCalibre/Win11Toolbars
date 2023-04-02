@echo off
pyinstaller list_widget.pyw
timeout 1
rd /s /q build
move dist\caller .
rd /s /q dist
del caller.spec