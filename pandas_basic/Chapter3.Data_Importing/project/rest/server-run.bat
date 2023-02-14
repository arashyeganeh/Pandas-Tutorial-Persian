@echo off
set "status=Node.js not installed. https://nodejs.org/en/download/"
for %%# in (node.exe) do  if not "%%~f$PATH:#" equ "" set "status=installed"
if "%status%" equ "installed" (
    node %~dp0server.js
) ELSE (
    echo %status%
)