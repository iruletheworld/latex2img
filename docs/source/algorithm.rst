腳本詳解
==========

本章將對轉換流程進行講解。鑑於使用到之軟件，轉換成PNG的流程於轉換成SVG之
流程相近，而轉換成EPS之流程則於轉換成EMF之流程同理。


轉換爲SVG之流程
-----------------

轉換爲SVG之流程可用如下之流程圖表示：

.. thumbnail:: ../../workflow_pics/workflow_pics/workflow_pics-1.svg
    :group: group1
    :align: center
    :alt: SVG flowchart

如上圖所示，轉換流程將創建在所在之目錄創建一個名爲 :code:`out_svg` 的文
件夾單獨存放生成的SVG文件。之後將會調用 :code:`util` 文件夾中的
:code:`pdf_to_svg` 腳本來實現轉換。

此流程需要用戶對需要轉換之TEX文件的 :code:`documentclass` 進行如下配置：

.. code-block:: latex
    :linenos:

        \documentclass[tikz, convert, convert={outext=.svg, command=\unexpanded{
        % 'out_svg'是用来存放SVG的文件夹
        % 'out_svg'是用來存放SVG的文件夾
        % 'out_svg' is destination folder for SVG files
        call ./util/mk_folder out_svg
        && cd /d out_svg
        && call ../util/pdf_to_svg ../\infile\space \outfile\space
        }}]{standalone}

.. note:: 設置 :code:`outext`

    當 :code:`outext` 有設置時， :code:`standalone` 會自動地在輸出文件
    （即是 :code:`outfile`）的文件名（不含後綴名）後加上計數關鍵字（一般
    是 :code:`%d`）。

    這小節的方法正是利用 :code:`standalone` 之此特性，結合
    :code:`pdf2svg` 的語法來進行PDF轉換爲分頁的SVG。



轉換爲PNG之流程
-----------------

轉換爲PNG之流程可用如下之流程圖表示：

.. thumbnail:: ../../workflow_pics/workflow_pics/workflow_pics-2.svg
    :group: group1
    :align: center
    :alt: PNG flowchart


轉換爲EMF之流程
-----------------

轉換爲EMF之流程可用如下之流程圖表示：

.. thumbnail:: ../../workflow_pics/workflow_pics/workflow_pics-2.svg
    :group: group1
    :align: center
    :alt: EMF flowchart


轉換爲EPS之流程
-----------------

轉換爲EPS之流程可用如下之流程圖表示：

.. thumbnail:: ../../workflow_pics/workflow_pics/workflow_pics-2.svg
    :group: group1
    :align: center
    :alt: EPS flowchart
