# RIME 倉頡輸入法方案集成

本專案搜集及整理多個不同用途的倉頡編碼表，讓需要的人能便利地組合出適當的 RIME 倉頡輸入法方案。

授權條款除特別聲明外皆為 [MIT License](LICENSE)。（注意：`resources/` 目錄之內容是引用其他專案，授權方式以原專案之聲明為憑）

## 使用方法

* 在系統上安裝 [RIME 輸入法引擎](https://rime.im/)，將本方案主目錄下的檔案（`cangjie*`）複製到 RIME 的使用者目錄下，即可新增輸入法方案使用。
* `cangjie.schema.yaml` 為輸入法方案配置檔，`cangjie.dict.yaml` 為整合詞典檔案。可自行建立 `cangjie.custom.yaml` 調整方案配置，或建立 `cangjie.dict.custom.yaml` 調整詞典設定。
* 輸入法方案的具體客製方法詳見 [RIME 文檔](https://rime.im/docs)。

## 資料來源及修訂資訊

本專案主要修訂三代及五代倉頡輸入法。原始編碼表來自[倉頡平台2012](http://www.chinesecj.com/forum/forum.php?mod=viewthread&tid=2596)的「五倉世紀」及「三倉世紀」編碼表（各收錄繁簡漢字七萬餘字），並參考官方資料（《第二代倉頡輸入法手冊》、《第三代倉頡輸入法手冊》、《第五代倉頡輸入法手冊》、朱邦復工作室提供的蒼頡檢字法編碼表、[漢文庫典](http://hanculture.com/dic/index.php)）、權威機構（[中文全字庫](https://www.cns11643.gov.tw/searchQ.jsp?ID=1) 、[Unihan 資料庫](https://unicode.org/charts/unihan.html)）及資深網友的討論結果修訂。

修訂內容大致如下：
1. 擴充漢字編碼，支援 Unicode 中日韓統一表意文字及其擴展區 A~F 共九萬餘字。
2. 修正錯誤或版本錯亂的編碼，使之盡可能符合各代倉頡輸入法之原意。
3. 倉頡系統根據 Unicode 未收錄字形取碼，或取碼規則有模糊或爭議等情況，適當設兼容碼以方便使用。
4. 調整重碼字的排序。

具體修訂原則與細節請參見[倉頡編碼修訂原則](doc/rules.md)。

## 如何參與？

您可以[提出新議題](https://github.com/Arthurmcarthur/Cangjie3-Plus/issues/new)向我們回報錯誤或回饋想法。

如果您熟悉 Git，也可以直接複刻（fork）此專案、修訂資料再向我們提出拉收請求（pull request）。

本專案主分支為 **master**。**devel** 為開發中分支，可能不定期 rebase 重整歷史，階段性任務完成後會整併入 master 分支。
