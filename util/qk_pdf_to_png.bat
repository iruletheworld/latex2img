@echo off

set dst_dir=%1
set dpi=%2
set intputfile=%3

if not exist %dst_dir%/NUL mkdir %dst_dir%

cd /d %dst_dir%

pdftocairo -r  %dpi% -png ../%intputfile%
