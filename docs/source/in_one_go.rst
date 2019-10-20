一步到位
==========

本章在 :doc:`algorithm` 的基礎上，講解怎樣把命令合併到一個腳本中從而簡化 :code:`documentclass` 的配置。

從 :doc:`algorithm` 中可以看出，本教程爲了方便排錯，而把命令分到多個腳本之中，逐個擊破，但其實完全是可以把命令全部寫入單個腳本之中，而實現簡化 :code:`documentclass` 的設置的。

本章將會提供這麼做的範例。


一步轉換成SVG
--------------

本小結將使用 :code:`util` 文件夾中之 :code:`qk_pdf_to_svg.bat` 腳本，以 :code:`mwe` 文件夾中的 :code:`qk_to_svg.tex` 爲例，展示如何一步轉換到SVG。

:code:`qk_to_svg.tex` 中的 :code:`documentclass` 的配置如下：

.. literalinclude:: ../../mwe/qk_to_svg.tex
    :language: latex
    :lines: 1-6
    :linenos:

其中， :code:`out_svg` 是存放SVG的文件夾。

:code:`qk_pdf_svg.bat` 腳本的內容如下：

.. literalinclude:: ../../util/qk_pdf_to_svg.bat
    :language: windows
    :linenos:

:code:`qk_pdf_to_svg.bat` 中的命令，是把 :code:`demo_to_svg.tex` 中的 :code:`documentclass` 中的命令整合爲一，以達到簡化 :code:`documentclass` 的配置的目的。


一步轉換成PNG
--------------

本小結將使用 :code:`util` 文件夾中之 :code:`qk_pdf_to_png.bat` 腳本，以 :code:`mwe` 文件夾中的 :code:`qk_to_png.tex` 爲例，展示如何一步轉換到PNG 。

:code:`qk_to_png.tex` 中的 :code:`documentclass` 的配置如下：

.. literalinclude:: ../../mwe/qk_to_png.tex
    :language: latex
    :lines: 1-6
    :linenos:

其中， :code:`out_png` 是存放PNG的文件夾。

:code:`qk_pdf_to_png.bat` 腳本的內容如下：

.. literalinclude:: ../../util/qk_pdf_to_png.bat
    :language: windows
    :linenos:

:code:`qk_pdf_to_png.bat` 中的命令，是把 :code:`demo_to_png.tex` 中的 :code:`documentclass` 中的命令整合爲一，以達到簡化 :code:`documentclass` 的配置的目的。


一步轉換成EMF
--------------

本小結將使用 :code:`util` 文件夾中之 :code:`qk_pdf_to_emf.bat` 腳本，以 :code:`mwe` 文件夾中的 :code:`qk_to_emf.tex` 爲例，展示如何一步轉換到EMF。

:code:`qk_to_emf.tex` 中的 :code:`documentclass` 的配置如下：

.. literalinclude:: ../../mwe/qk_to_emf.tex
    :language: latex
    :lines: 1-7
    :linenos:

其中， :code:`out_emf` 是存放EMF的文件夾。

:code:`qk_pdf_to_emf.bat` 腳本的內容如下：

.. literalinclude:: ../../util/qk_pdf_to_emf.bat
    :language: windows
    :linenos:

:code:`qk_pdf_to_emf.bat` 中的命令，是把 :code:`demo_to_emf.tex` 中的 :code:`documentclass` 中的命令整合爲一，以達到簡化 :code:`documentclass` 的配置的目的。


一步轉換成EPS
--------------

本小結將使用 :code:`util` 文件夾中之 :code:`qk_pdf_to_eps.bat` 腳本，以 :code:`mwe` 文件夾中的 :code:`qk_to_eps.tex` 爲例，展示如何一步轉換到EPS。

:code:`qk_to_eps.tex` 中的 :code:`documentclass` 的配置如下：

.. literalinclude:: ../../mwe/qk_to_eps.tex
    :language: latex
    :lines: 1-7
    :linenos:

其中， :code:`out_eps` 是存放EPS的文件夾。

:code:`qk_pdf_to_eps.bat` 腳本的內容如下：

.. literalinclude:: ../../util/qk_pdf_to_eps.bat
    :language: windows
    :linenos:

:code:`qk_pdf_to_eps.bat` 中的命令，是把 :code:`demo_to_eps.tex` 中的 :code:`documentclass` 中的命令整合爲一，以達到簡化 :code:`documentclass` 的配置的目的。
