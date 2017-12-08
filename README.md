# Cangjie5

[简化字版说明](https://github.com/Jackchows/Cangjie5/blob/master/README-hans.md)

相關項目：[Arthurmcarthur/Cangjie3-Plus](https://github.com/Arthurmcarthur/Cangjie3-Plus)

原碼表為[「倉頡平台 2012」](http://www.chinesecj.com/forum/viewthread.php?tid=2596)的「五倉世紀」碼表。

本項目參考官方資料對碼表進行修改，但無意完善倉頡輸入法理論，亦無意追求客觀。<br />
本項目以1999版倉頡五代為基礎，採納部份2003版倉頡五代的修改。

本項目主要參考以下資料：<br />
1. 《第五代倉頡輸入法手冊》正文中對規則的描述（簡稱「手冊」）<br />
本項目認為「手冊」闡述了倉頡輸入法的基本理念和規則，但描述並不詳盡。<br />
《第五代倉頡輸入法手冊》有兩個版本，分別由文化傳信和博碩文化出版，兩個版本僅在列舉字例上有細微差異。<br />
「手冊」屬於1999版倉頡五代。<br />
2. 《第五代倉頡輸入法手冊》附錄碼表（簡稱「附表」）<br />
本項目認為，與編寫《手冊》相比，官方在實際編寫碼表時對規則的考慮更為周全，因此「附表」較「手冊」有更高可信度。<br />
3. [「漢文庫典」](http://hanculture.com/dic/index.php)網站（簡稱「漢文庫典」）<br />
本項目認為「漢文庫典」對於大字庫的考慮比「手冊」和「附表」周全，但「漢文庫典」存在受倉頡六代影響而出現錯誤的情況。<br />
《漢文庫典》屬於2003版倉頡五代。<br />
4. 《第二代倉頡輸入法手冊》、《第三代倉頡輸入法手冊》、朱邦復工作室《內碼對照表》的六代編碼<br />
本項目認為這些資料雖不屬於倉頡五代的範圍，但可體現官方的設計理念。<br />

修改編碼時，將遵循以下原則：<br />
1. 某字收錄於「附表」，則依「附表」取碼。<br />
2. 「附表」和「手冊」發生矛盾，依「附表」取碼，適當設兼容碼。<br />
3. 採納「漢文庫典」針對「難字」取碼的修改，採納「漢文庫典」針對大字庫集的修改。<br />
4. 「附表」和「漢文庫典」發生矛盾，適當設兼容碼，屬於原則③的情況除外。<br />
5. 「手冊」和「漢文庫典」發生矛盾，而該字未見於「附表」，適當設兼容碼。但若該字屬於常用字，則盡量避免設兼容碼。<br />
6. 取碼發生爭議，將參考各方觀點，凴個人理解確定編碼，並在[說明](https://github.com/Jackchows/Cangjie5/blob/master/change_summary.md#主要改碼說明及爭議取碼)中列明理由。<br />

## 反饋錯誤

若發現錯誤，可在此處[反饋](https://github.com/Jackchows/Cangjie5/issues/new)。
另外，也會收集在下方「友情連接」各處反饋的錯誤。
多謝！

## 友情連接
- [「倉頡之友·馬來西亞」論壇](http://www.chinesecj.com/forum/forum.php)
- [「天蒼人頡」論壇](http://ejsoon.win/phpbb/)
- 「倉頡輸入法」QQ 群組 [30476878](https://jq.qq.com/?_wv=1027&k=5W3qETZ)
- 「倉頡輸入法」Freenode IRC 頻道 [#CJDFH](https://webchat.freenode.net/?channels=%23CJDFH)
- 「倉頡輸入法」Telegram 群組 [@changjei](https://t.me/changjei)