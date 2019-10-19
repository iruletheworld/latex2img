Latex :code:`standalone` 包的配置
===================================

本教程是基於由 `Martin Scharrer
<https://bitbucket.org/martin_scharrer/standalone/src/default/>`_
開發的 |standalone| 包（自帶 :code:`standalone` 類），故此於此對此包稍作講解。

.. |standalone| raw:: html

   <em>
   <a href="https://ctan.org/pkg/standalone?lang=en">standalone</a>
   </em>

.. note:: :code:`standalone` (*complex*) [#]_

    :code:`standalone` 是Latex中非常有用的一個包。本教程主要講述怎樣利用此包來進行圖片的轉換，但此包其實還有其它相當多的應用。 `Overleaf
    <https://www.overleaf.com/learn/latex/Multi-file_LaTeX_projects#The_standalone_package>`_ 上有一個非常有用的教程。

:code:`standalone` 的轉換命令配置
----------------------------------

:code:`standalone` 本身的 `說明文檔 <http://mirrors.ibiblio.org/CTAN/macros/latex/contrib/standalone/standalone.pdf>`_ 已經對配置有詳盡的說明，此處重點說一下轉換成圖片需要用到的 :code:`convert` 選項。

配置 :code:`convert` 需要在 :code:`documentclass` 中進行。以下是一個利用 :code:`pdf2svg` 轉換爲SVG的範例配置。

.. code-block:: latex

    \documentclass[tikz, convert, convert={outext=.svg, command=\unexpanded{
        pdf2svg \infile\space \outfile\space all
    }}]{standalone}

其中，

* :code:`tikz`
    此選項告訴 :code:`standalone` Latex文檔中存在 :code:`tikz` 圖片。

* :code:`convert`
    此選項開啓 :code:`standalone` 的轉換功能。

* :code:`convert={}`
    此選項是 :code:`convert` 的詳細配置項。

* :code:`outext=.svg`
    設置輸出文件的後綴名爲".svg"。

    更詳細的說明請參看 :code:`standalone` 本身的 `說明文檔
    <http://mirrors.ibiblio.org/CTAN/macros/latex/contrib/standalone/standalone.pdf>`_ 中的表1。

* :code:`command=\unexpanded{}`
    此項是將要調用系統運行的命令。

* :code:`pdf2svg`
    調用的轉換工具。

    .. note:: :code:`pdf2svg` 的語法

        :code:`pdf2svg` 的語法可以參看 `這裏
        <http://www.cityinthesky.co.uk/opensource/pdf2svg/>`_。

        其中，將一多頁PDF轉換爲分頁的多個SVG的語法爲：

        .. code-block:: bash

            pdf2svg <input_file>.pdf <output_file>%d.svg all

        注意，尖括號中的內容需要替換爲所需的文件名。

* :code:`\infile`
    輸入文件名，包含後綴名。默認後綴名爲".pdf"或".ps"。

   更詳細的說明請參看 :code:`standalone` 本身的 `說明文檔 <http://mirrors.ibiblio.org/CTAN/macros/latex/contrib/standalone/standalone.pdf>`_ 中的表1。

* :code:`\space`
    空格。若不使用此參數，:code:`\infile` 後不會有空格，無論你實際上鍵入了多少個。 :code:`\outfile` 也是這樣。

* :code:`\outfile`
    輸出文件名，包含後綴名。默認後綴名爲".png"。此處已經通過 :code:`outext` 更改爲".svg"。

    更詳細的說明請參看 :code:`standalone` 本身的 `說明文檔
    <http://mirrors.ibiblio.org/CTAN/macros/latex/contrib/standalone/standalone.pdf>`_
    中的表1。

SVG配置範例中之命令將會被翻譯爲如下（可以通過查看LOG文件確認）。其中，
:code:`mew_to_svg` 爲所用的TEX文件的文件名。

.. code-block:: bash

    pdf2svg mwe_to_svg.pdf mwe_to_svg-%01d.svg all

由此可以看出，轉換的重點，是要把 :code:`convert={}` 中的配置正確設置，以令Latex將其翻譯成正確的系統命令來進行圖片的轉換。用戶可以把多個系統命令整合爲一行，以做出豐富多彩的組合來達成不同的目標（在Windows中可以通過"&"或"&&"把多行命令合併爲一行）。在 :doc:`workflow` 中將會詳細敘述各種圖片轉換的流程。

編譯命令
--------

:code:`standalone` 需要在編譯時使用 :code:`-shell-escape` 參數。一個使用 :code:`xelatex` 對 :code:`mew_to_svg.tex` 進行編譯的命令如下（用 :code:`xelatex` 是因爲需要處理中文）。

.. code-block:: bash

    xelatex -synctex=1 -interaction=nonstopmode -shell-escape mwe_to_svg.tex


簡例
-----

以下提供一個轉換爲單頁多個SVG的簡例。詳細的例子會在後文說明。

以下的文件可以在此項目的 :code:`mew` 文件夾中找到。

**主文件：**

.. literalinclude:: ../../mwe/mwe_to_svg.tex
    :linenos:
    :language: latex

**tikz配置文件：**

.. literalinclude:: ../../mwe/configs_tikz.tex
    :linenos:
    :language: latex

**color配置文件：**

.. literalinclude:: ../../mwe/configs_colour.tex
    :linenos:
    :language: latex


.. [#] Ghost In Shell : Standalone Complex