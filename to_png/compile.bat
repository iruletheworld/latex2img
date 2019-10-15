REM uses xelatex for CJK

cmd /K xelatex -synctex=1 -interaction=nonstopmode -shell-escape demo_to_png.tex
REM cmd /K pdflatex -synctex=1 -interaction=nonstopmode -shell-escape demo_to_png.tex