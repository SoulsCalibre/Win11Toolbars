@echo off
pyinstaller list_widget.pyw

:wait_for_build
IF NOT EXIST "build" (
  timeout /t 1 >nul
  GOTO wait_for_build
)

rd /s /q build

:wait_for_list_widget
IF NOT EXIST "dist\list_widget" (
  timeout /t 1 >nul
  GOTO wait_for_list_widget
)

move dist\list_widget .

:wait_for_move
IF NOT EXIST "dist" (
  timeout /t 1 >nul
  GOTO wait_for_move
)

IF NOT EXIST "list_widget" (
  timeout /t 1 >nul
  GOTO wait_for_move
)

rd /s /q dist

del list_widget.spec
