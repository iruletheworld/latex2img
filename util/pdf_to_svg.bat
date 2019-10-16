@each off
REM use pdf2svg (https://github.com/jalios/pdf2svg-windows) to convert a pdf to individual svgs

set inputfile=%1
set outputfile=%2

pdf2svg %inputfile% %outputfile% all
