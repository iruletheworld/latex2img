.. _software :

系統和軟件
===========

此項目會用到如下的系統和軟件，請先保證你已安裝了它們。

* Windows 7或Windows 10
* `texlive（2019年的發佈，免費） <https://www.tug.org/texlive/acquire-netinstall.html>`_
* LaTex的 :code:`standalone` 包（ :code:`texlive` 自帶）
*  :code:`pdftocairo` （ :code:`texlive` 自帶，用於PNG轉換）
* `inksacpe（0.92.4，免費。用於EMF和EPS的轉換） <https://inkscape.org/release/inkscape-0.92.4/>`_
* `pdf2svg（Windows編譯版，免費。用於SVG轉換） <https://github.com/jalios/pdf2svg-windows>`_
* `ghostscript (9.50，免費。用於PDF文件的分頁) <https://github.com/ArtifexSoftware/ghostpdl-downloads/releases>`_


轉換軟件的使用理由
------------------

此項目選擇的轉換軟件主要基於以下理由。

* 此項目堅持所有使用的轉換軟件必須爲免費

* 轉換結果必須是一頁PDF一張圖

* 當把PDF轉換爲矢量圖時，必須爲真正的矢量圖，而不是包裹在矢量格式中的位圖

    * 因此，此項目不使用ImageMagick，因其在轉換矢量圖時經常柵格化

* 當轉爲爲矢量圖時，字體應該嵌入而不是柵格化

* 轉換命令應儘可能簡單

* 使用的軟件儘可能少以降低依賴性

.. note::

    儘管 :code:`inkscape` 也可以進行PNG和SVG的轉換，但 :code:`pdftocairo` 和 :code:`pdf2svg` 自帶了多頁到單頁的功能，使用便利，而且安裝也簡易，故而用此二軟件分別進行PNG和SVG的轉換而不使用 :code:`inkscape` 。若使用 :code:`inkscape` ，則需要先調用 :code:`ghostscript` 對PDF進行分頁，然後再轉換。
