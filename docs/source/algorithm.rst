腳本詳解
==========

本章將對本教程中所用到之腳本進行講解。

本項目所使用到的腳本存放在 :code:`util` 文件夾之中，它們爲：

* :code:`mk_folder.bat`
    用於創建文件夾。

    .. note:: 腳本命名問題

        在Windows當中，如果把批處理腳本命名爲所要調用的系統命令名，很可能會導致死循環。 故此命名此腳本為 :code:`mk_folder.bat` 而不是 :code:`mkdir.bat`

* :code:`gs_split_pdf.bat`
    調用 :code:`ghostscript` 把PDF分割爲單頁。

* :code:`pdf_to_svg.bat`
    把多頁PDF轉換爲分頁的SVG。

* :code:`pdf_to_png.bat`
    把多頁PDF轉換爲分頁的PNG。

* :code:`pdf_to_emf.bat`
    把PDF轉換爲EMF（僅一頁）。

* :code:`pdf_to_eps.bat`
    把PDF轉換爲的EPS（僅一頁）。


:code:`mk_folder.bat` 詳解
----------------------------

:code:`mk_folder.bat` 的內容如下：

.. literalinclude:: ../../util/mk_folder.bat
    :language: windows
    :linenos:

此腳本用於在CMD當前所在之目錄爲根來創建文件夾。如果該文件夾已存在，則不創建而退出。

此腳本接受一個參數。此參數爲將要創建的文件夾路徑。

此腳本之使用方法如下：

.. code-block:: windows

    mk_folder <要創建之文件夾路徑>

此腳本的語法和 :code:`mkdir` 命令的語法一致。此處給出一個例子，假設要在目前的目錄下創建一個名爲 :code:`a` 的文件夾，其下有一個子目錄，名爲 :code:`b`，而 :code:`b` 之下又有一個子目錄，名爲 :code:`c` 。

.. code-block:: windows

    mk_folder a\b\c

若文件夾路徑中有空格，則需要把路徑放在兩個雙引號之中，如：

.. code-block:: windows

    mk_folder "a b\c d"


:code:`gs_split_pdf.bat` 詳解
-------------------------------

:code:`gs_split_pdf.bat` 的內容如下：

.. literalinclude:: ../../util/gs_split_pdf.bat
    :language: windows
    :linenos:

此腳本用於把輸入的PDF分割爲單頁的PDF。

此腳本接受三個參數。它們如下（按順序）：

#. 輸出的單頁PDF的文件夾的路徑

#. 輸出的單頁PDF文件的共用文件名加上 "%d"

#. 需要分頁的PDF的路徑

此腳本調用的是64位的 :code:`ghostscript` ，若你安裝的是32位的版本則需要把此腳本中的 :code:`gswin64c` 更改爲 :code:`gswin32c` 。

此處給出一個例子，輸出的文件夾爲 :code:`output` （已存在），共用文件名爲 :code:`common`，需要分頁的PDF爲 :code:`pdf_in` 。

.. code-block:: windows

    gs_split_pdf output common%d.pdf pdf_in.pdf

.. note:: "%d"

    如果不在共用文件名後加上 "%d"，:code:`ghostscript` 則不會對PDF進行分頁。


:code:`pdf_to_svg.bat` 詳解
----------------------------

:code:`pdf_to_svg.bat` 的內容如下：

.. literalinclude:: ../../util/pdf_to_svg.bat
    :language: windows
    :linenos:

此腳本用於把PDF轉換爲SVG。

此腳本接受兩個參數。它們如下（按順序）：

#. 需要轉換的PDF文件路徑

#. 輸出的單頁PDF文件的共用文件名加上 "%d"

此腳本調用 :code:`pdf2svg` 來進行文件的轉換。此處給出一個例子，需要轉換的PDF名爲 :code:`pdf_in`，輸出的單頁PDF的共用文件名爲 :code:`pdf_out` ，輸出的文件夾爲 :code:`out_svg` （已存在）。

.. code-block:: windows

    pdf_to_svg pdf_in.pdf .\out_svg\pdf_out%d.svg

.. note:: "%d"

    如果不在共用文件名後加上 "%d"，則只會轉換PDF的第一頁。


:code:`pdf_to_png.bat` 詳解
----------------------------

:code:`pdf_to_png.bat` 的內容如下：

.. literalinclude:: ../../util/pdf_to_png.bat
    :language: windows
    :linenos:

此腳本用於把PDF轉換爲PNG。此腳本會在CMD當前所在之目錄創建PNG文件。

此腳本接受兩個參數。它們如下（按順序）：

#. 轉換的PNG的DPI，一般爲300或600。過高的DPI會令轉換過程冗長。

#. 需要轉換的PDF的路徑

此腳本調用 :code:`pdftocairo` 來進行文件的轉換。此處給出一個例子，轉換的DPI爲600像素，需要轉換的PDF名爲 :code:`pdf_in` 。

.. code-block:: windows

    pdf_to_png 300 pdf_in.pdf

.. note:: :code:`pdftocairo`

    :code:`pdftocairo` 會自動把多頁PDF轉換爲單頁的PNG，非常方便。
