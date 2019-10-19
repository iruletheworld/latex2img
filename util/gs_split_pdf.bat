@echo off
REM use 64-bit ghosescript to split a pdf

set temp_folder=%1
set outfile=%2
set infile=%3

REM the gswinXXc.exe does not prompt the ghostscript window, the ones without the "c" do prompt

gswin64c -sDEVICE=pdfwrite -dSAFER -dNOPAUSE -dBATCH -sOutputFile=%temp_folder%/%outfile% %infile%
