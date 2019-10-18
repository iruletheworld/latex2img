極簡教程
==========

本章意在提供最簡短而必要的步驟，以使用戶快速上手。

在應用本章步驟前，請先保證所有需要的軟件和配置已完成。


轉換爲SVG
--------------

#. 把本教程附帶的“util”文件夾複製到需要轉換的TEX文件所在之目錄下。

#. 對需要轉換的TEX的文件的 :code:`documentclass` 進行如下配置：

    .. literalinclude:: ../../demo_to_svg.tex
        :language: latex
        :lines: 4-11
        :linenos:

#. 使用 :code:`-shell-escape` 參數對TEX文件進行編譯。例如：

    .. code-block:: bash

        xelatex -synctex=1 -interaction=nonstopmode -shell-escape <你TEX文件的文件名>.tex

#. 轉換好的SVG文件將存放在“out_svg”文件夾下。


轉換爲PNG
--------------

#. 把本教程附帶的“util”文件夾複製到需要轉換的TEX文件所在之目錄下。

#. 對需要轉換的TEX的文件的 :code:`documentclass` 進行如下配置：

    .. literalinclude:: ../../demo_to_png.tex
        :language: latex
        :lines: 4-11
        :linenos:


#. 使用 :code:`-shell-escape` 參數對TEX文件進行編譯。例如：

    .. code-block:: bash

        xelatex -synctex=1 -interaction=nonstopmode -shell-escape <你TEX文件的文件名>.tex

#. 轉換好的PNG文件將存放在“out_png”文件夾下。


轉換爲EMF
--------------

#. 把本教程附帶的“util”文件夾複製到需要轉換的TEX文件所在之目錄下。

#. 對需要轉換的TEX的文件的 :code:`documentclass` 進行如下配置：

    .. literalinclude:: ../../demo_to_emf.tex
        :language: latex
        :lines: 4-24
        :linenos:

#. 使用 :code:`-shell-escape` 參數對TEX文件進行編譯。例如：

    .. code-block:: bash

        xelatex -synctex=1 -interaction=nonstopmode -shell-escape <你TEX文件的文件名>.tex

#. 轉換好的EMF文件將存放在“out_emf”文件夾下。


轉換爲EPS
--------------

#. 把本教程附帶的“util”文件夾複製到需要轉換的TEX文件所在之目錄下。

#. 對需要轉換的TEX的文件的 :code:`documentclass` 進行如下配置：

    .. literalinclude:: ../../demo_to_eps.tex
        :language: latex
        :lines: 4-25
        :linenos:

#. 使用 :code:`-shell-escape` 參數對TEX文件進行編譯。例如：

    .. code-block:: bash

        xelatex -synctex=1 -interaction=nonstopmode -shell-escape <你TEX文件的文件名>.tex

#. 轉換好的EPS文件將存放在“out_eps”文件夾下。
