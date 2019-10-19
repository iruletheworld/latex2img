@echo off

set dst_dir=%1
set outputfile=%2
set intputfile=%3

if not exist %dst_dir%/NUL mkdir %dst_dir%

gswin64c -sDEVICE=pdfwrite -dSAFER -dNOPAUSE -dBATCH -sOutputFile=%dst_dir%/%outputfile% %intputfile%

cd /d %dst_dir%

for /r %%i in (*.pdf) do inkscape %%i -M %%~pni.emf

del /F *.pdf
