REM use ghost script (32-bit) to split a pdf into individual pages
gswin32 -sDEVICE=pdfwrite -dSAFER -o .\pdf_split\demo_to_png_%%d.pdf demo_to_png.pdf