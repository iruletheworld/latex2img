轉換流程
==========

本章將對轉換流程進行講解。鑑於使用到之軟件，轉換成PNG的流程於轉換成SVG之流程相近，而轉換成EPS之流程則於轉換成EMF之流程同理。

本教程中轉換的流程將利用到數份Windows的批處理腳本（在本教程的“util”文件夾中），本教程將在 :doc:`algorithm` 中對它們進行詳細講解。

本章中之方法一律需要使用 :code:`-shell-escape` 參數來進行編譯。一個使用 :code:`xelatex` 對 :code:`mew_to_svg.tex` 進行編譯的命令如下（用 :code:`xelatex` 是因爲需要處理中文）。

.. code-block:: bash

    xelatex -synctex=1 -interaction=nonstopmode -shell-escape mwe_to_svg.tex

請把 :code:`mwe_to_svg` 替換爲你的TEX文件文件名。


轉換爲SVG之流程
-----------------

轉換爲SVG之流程可用如下之流程圖表示：

.. thumbnail:: ../../workflow_pics/workflow_pics/workflow_pics-1.svg
    :group: group1
    :align: center
    :alt: SVG flowchart

如上圖所示，轉換流程將在所在之目錄創建一個名爲 :code:`out_svg` 的文件夾單獨存放生成的SVG文件。之後將會調用 :code:`util` 文件夾中的 :code:`pdf_to_svg` 腳本來實現轉換。

此流程需要用戶對需要轉換之TEX文件的 :code:`documentclass` 進行如下配置：

.. literalinclude:: ../../demo_to_svg.tex
    :language: latex
    :lines: 4-11
    :linenos:

.. note:: 設置 :code:`outext`

    當 :code:`outext` 有設置時， :code:`standalone` 會自動地在輸出文件（即是 :code:`outfile`）的文件名（不含後綴名）後加上計數關鍵字（一般    是 :code:`%d`）。

    這小節的方法正是利用 :code:`standalone` 之此特性，結合 :code:`pdf2svg` 的語法來進行PDF轉換爲分頁的SVG。

.. warning:: 關於 "%" 和 "\\" 符號

    在Latex中，"%" 是一個保留字，用來表示註釋。如果直接使用在 :code:`documentclass` 之中，則會把其後面的同行代碼全部註釋掉。這樣的話，編譯時會出問題。

    然而，若用 "\\" 進行轉義（即 "escape"）的話 :code:`standalone` 是會把 "\\" 符號作爲明文加入到命令中的。這樣一來，命令通常都不對，因爲 "\\" 在Latex中是表示的是後面跟的是參數或者命令。而在Windows命令中 "%" 通常用來指代參數，在Windows中使用for循環時絕對會用到它，無法避免。

    綜上所述，如果在 :code:`documentcalss` 裏面直接把系統命令寫全的話，很難保證其正確性。

    故此，作者選擇把命令封裝到多個批處理腳本中，這樣就可以避免以上提及的符號問題。

本方法用到以下兩份腳本：

#. :code:`mk_folder`
    創建文件夾。

#. :code:`pdf_to_svg`
    將多頁的PDF轉換爲分頁的SVG。

它們的詳細講解在 :doc:`algorithm` 中。


轉換爲PNG之流程
-----------------

轉換爲PNG之流程可用如下之流程圖表示：

.. thumbnail:: ../../workflow_pics/workflow_pics/workflow_pics-2.svg
    :group: group1
    :align: center
    :alt: PNG flowchart

如上圖所示，轉換流程將在所在之目錄創建一個名爲 :code:`out_png` 的文件夾單獨存放生成的PNG文件。之後將會調用 :code:`util` 文件夾中的 :code:`pdf_to_png` 腳本來實現轉換。

此流程需要用戶對需要轉換之TEX文件的 :code:`documentclass` 進行如下配置：

.. literalinclude:: ../../demo_to_png.tex
    :language: latex
    :lines: 4-11
    :linenos:

.. note:: :code:`pdftocairo`

    :code:`pdftocairo` 會自動地把一多頁的PDF自動分割爲多張PNG。故此只需要把輸入文件給它即可（即 :code:`infile`），而不需要設置輸出文件（即 :code:`outfile`）。

本方法用到以下兩份腳本：

#. :code:`mk_folder`
    創建文件夾。

#. :code:`pdf_to_png`
    將多頁的PDF轉換爲分頁的PNG。

它們的詳細講解在 :doc:`algorithm` 中。


轉換爲EMF之流程
-----------------

轉換爲EMF之流程可用如下之流程圖表示：

.. thumbnail:: ../../workflow_pics/workflow_pics/workflow_pics-4.svg
    :group: group1
    :align: center
    :alt: EMF flowchart

如上圖所示，轉換流程將在所在之目錄創建一個名爲 :code:`out_emf` 的文件夾單獨存放生成的EMF文件。之後將會調用 :code:`util` 文件夾中的 :code:`gs_split_pdf` 來對生成的PDF進行分頁，:code:`pdf_to_emf` 腳本來實現轉換。 轉換完畢後會刪除所有單頁之PDF，只保留EMF。

此流程需要用戶對需要轉換之TEX文件的 :code:`documentclass` 進行如下配置：

.. literalinclude:: ../../demo_to_emf.tex
    :language: latex
    :lines: 4-24
    :linenos:

.. note:: :code:`inkscape`

    :code:`inkscape` 在轉換時不會自動對PDF進行分頁。若直接使用 :code:`inkscape` 對多頁PDF進行轉換，只有第一頁會被轉換。

    故此，本方法會先調用 :code:`ghostscript` 對PDF進行分頁，然後在調用 :code:`inkscape` 對所有的單頁PDF進行轉換。

本方法用到以下三份腳本：

#. :code:`mk_folder`
    創建文件夾。

#. :code:`gs_split_pdf`
    將多頁的PDF分割爲單頁的PDF。

#. :code:`pdf_to_emf`
    將PDF轉換爲EMF（僅一頁）。

它們的詳細講解在 :doc:`algorithm` 中。


轉換爲EPS之流程
-----------------

轉換爲EPS之流程可用如下之流程圖表示：

.. thumbnail:: ../../workflow_pics/workflow_pics/workflow_pics-3.svg
    :group: group1
    :align: center
    :alt: EPS flowchart

如上圖所示，轉換流程將在所在之目錄創建一個名爲 :code:`out_eps` 的文件夾單獨存放生成的EMF文件。之後將會調用 :code:`util` 文件夾中的 :code:`gs_split_pdf` 來對生成的PDF進行分頁，:code:`pdf_to_eps` 腳本來實現轉換。 轉換完畢後會刪除所有單頁之PDF，只保留EMF。

此流程需要用戶對需要轉換之TEX文件的 :code:`documentclass` 進行如下配置：

.. literalinclude:: ../../demo_to_eps.tex
    :language: latex
    :lines: 4-25
    :linenos:

本方法之原理於轉換爲EMF的流程完全一樣。都是先對生成的PDF進行分頁，再調用 :code:`inkscape` 進行處理。

本方法用到以下三份腳本：

#. :code:`mk_folder`
    創建文件夾。

#. :code:`gs_split_pdf`
    將多頁的PDF分割爲單頁的PDF。

#. :code:`pdf_to_eps`
    將PDF轉換爲EPS（僅一頁）。


它們的詳細講解在 :doc:`algorithm` 中。
