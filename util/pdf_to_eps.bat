REM loop through recursively and convert all pdf to eps

for /r %%i in (*.pdf) do inkscape %%i -E %%~pni.eps