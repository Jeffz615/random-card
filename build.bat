@echo off
pyinstaller main.spec
move /y dist\\main.exe .\\main.exe
rd /s /q dist
rd /s /q build