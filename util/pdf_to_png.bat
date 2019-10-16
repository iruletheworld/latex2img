@echo off
REM use pdftocairo to convert a pdf into multiple pngs

set dpi=%1
set inputfile=%2

pdftocairo -r %dpi% -png %inputfile%
