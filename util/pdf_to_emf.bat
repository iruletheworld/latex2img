REM loop through recursively and convert all pdf to emf

for /r %%i in (*.pdf) do inkscape %%i -M %%~pni.emf