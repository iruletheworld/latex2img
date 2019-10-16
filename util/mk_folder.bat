@echo off
REM this file is not call "mkdir" to avoid run errors

set dst_dir=%1

if not exist %dst_dir%/NUL mkdir %dst_dir%