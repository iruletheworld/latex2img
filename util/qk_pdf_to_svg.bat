@echo off

set dst_dir=%1
set inputfile=%2
set outputfile=%3

if not exist %dst_dir%/NUL mkdir %dst_dir%

cd /d %dst_dir%

pdf2svg ../%inputfile% %outputfile% all
