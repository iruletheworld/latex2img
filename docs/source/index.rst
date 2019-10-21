.. LaTex (tikz)转换为图像/LaTex (tikz)轉換爲圖像/LaTex (tikz) to Images documentation master file, created by
   sphinx-quickstart on Thu Oct 17 09:48:07 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

======================
LaTex (tikz)轉換爲圖像
======================

.. raw:: latex

    \vspace*{1cm}

此項目是一個關於把LaTex文檔直接轉換爲各種圖像的教程（在編譯TEX文件時，同時生成單獨的圖片）。此教程主要關注如何把tikz生成的，內嵌於LaTex生成的PDF文件中的圖像轉換爲各種格式的單獨圖片。

此項目會討論到的圖片格式如下

* SVG （矢量圖）
* PNG（位圖）
* EMF （Windows系統上的矢量圖）
* EPS （印刷常用格式）

此項目的在於提供基於Windows系統的教程和例子。作者相信Linux用戶有能力獨自解決這個問題。

此教程會提供軟件安裝和配置指南，並會結合例子進行講解。

此教程認爲用戶已經對LaTex有一定的理解，因而不會對LaTex中之各種進行詳解。

本教程將會詳盡講解流程。若只想快速使用而不在乎原理，可先閱讀 :doc:`/installation_and_configuration` 然後按照 :doc:`/accelerated_guide` 中之步驟執行即可。

.. toctree::
    :maxdepth: 3
    :numbered:
    :caption: 目錄

    system_and_software
    installation_and_configuration
    accelerated_guide
    config_standalone
    workflow
    algorithm
    in_one_go
    conclusion
