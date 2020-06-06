### 編碼說明：

1.「冎」<br />
根據沈紅蓮女士的回信，「咼的上部」可以當作輔助字形，故「冎」取碼為「月月」。

2.被強制Big-5化的漢字<br />
官方倉頡三代所依據取碼的字形曾經有過變更。在較晚出版的《零壹中文電腦叢書之九 倉頡第三代中文輸入法》（下簡稱增訂版三代手冊）一書之附錄三提到：「…本書收集字數以國科會、教育部、中央標準局及主計處公佈的『通用漢字交換碼』一書為主，共計13053個字…相信標準字對統一中文電腦字形會有很大的幫助。所以，這次我們儘量依標準字形來取碼，故中文字的輸入碼及輸出字都因應標準字而作了若干修正。…」。該附錄又提到：「…交換碼以揑為標準字。…」。由此，手冊中有「揑」而無「捏」。然而，Big-5中實際上以「捏」而非「揑」為標準字。結果，官方錯誤地將「揑」對應到了「捏」所在的Big-5碼位。本碼表將取消這些錯誤的對應，而將這些被強制Big-5化的漢字恢復其本應有的取碼，現將這些漢字列舉如下：
|UCS碼位|漢字|官方取形所據漢字|強制Big-5化時的編碼|本碼表編碼|
|-|-|-|-|-|
|4E1F|丟|丢|竹土戈|一土戈|
|541E|吞|呑|竹大.口|一大.口|
|5F65|彥|彦|卜竹.竹.竹竹|卜大.一.竹竹|
|634F|捏|揑|手.竹難.一|手.日.土|
|6490|撐|撑|手.火月.手|手.火月.竹|
|7522|產|産|卜竹.竹手一|卜大.一.竹一|
|7F8B|羋|芈|中一卜手|廿中.手|
|87A4|螤|斔|卜戈.竹難人|卜戈.中田人|

3.「軣」等字的取碼<br />
目前許多碼表將「軣」取為「十十.戈一.人」，但漢文庫典的取碼為「十十.金.金」。根據沈紅蓮女士的回信，「軣」取「十十.金.金」較符合完整原則，本碼表從之。將包含「軣」下部的字部分羅列如下：
|UCS碼位|漢字|取碼|
|-|-|-|
|43EE|䏮|月.大尸.金|
|5841|塁|田.金.金土|
|6442|摂|手.尸十.金|
|6E0B|渋|水.卜一.金|
|7582|疂|田.金.金一|
|8EE3|軣|十十.金.金|
|2B753|𫝓|十.大尸.金|
|2D0F2|𭃲|水金.中.弓|
|2DD11|𭴑|火.金.金|
|2DF89|𭾉|中田.金.金廿|
|2E42A|𮐪|廿.口.金木|
|2E4FC|𮓼|中戈.金.金|
|2E6CE|𮛎|口人.金.金|

4.疊字之取碼<br />
許多常見的碼表，在取碼時不依從「一次分離」原則，而是將疊字的成字部件作為字首、次字首劃分出來。例如許多碼表將「鱻」取碼為「弓火.弓火.火」。但無論是1984年出版的原三代手冊或是後來的增訂版三代手冊，都未有提到對疊字的特殊取碼規則。而在六代中，明確規定了「毳(HUHUU)、龘(YPYPP)等二、三或四同形字組成者」，將整塊同形字劃為字首，而〇三五代中，取碼則不甚統一，例「譶」字在〇三五代中被取為「卜口.卜口.口」，而「鱻」卻取「弓田.火.弓火」，推測可能是官方本想在〇三五代中亦應用疊字規則，但漏改之故。<br />
本碼表依「一次分離」原則對疊字進行取碼，但由於疊字對於許多人而言可能容易劃分錯誤，所以本碼表也有「疊字規則」的容錯編碼。現不完全列舉例字如下：
|UCS碼位|漢字|一次分離取碼|容錯碼|
|-|-|-|-|
|4A3A|䨺|一月.一.一戈|一戈.一戈.戈|
|569E|嚞|土.口.土口|土口.土口.口|
|8B76|譶|卜.一.一口|卜口.卜口.口|
|9750|靐|一月.田.一田|一田.一田.田|
|9C7B|鱻|弓田.火.弓火|弓火.弓火.火|
|21B0F|𡬏|十.一土.土|十土.十土.土|
|25A4C|𥩌|十金.一.十一|十一.十一.一|
|29EB0|𩺰|弓田.火.弓火|弓火.弓火|

5.「韲」上方部件取碼<br />
許多常見的碼表將「韲」上方的部件分拆開，故「韲」取「卜.尸人.一」。
本碼表依從漢文庫典中的官方取碼，將「韲」的上方定為難字，故全字取「卜難.中一一」。現不完全列舉一些包含同樣部件的漢字如下：
|UCS碼位|漢字|取碼|
|-|-|-|
|4421|䐡|卜難.人月人|
|20188|𠆈|卜難.月.女|
|20197|𠆗|卜難.人.一口|
|21141|𡅁|口.卜難.木|
|2405C|𤁜|水.卜難.手|
|2698F|𦦏|卜難.竹難|
|2A5CE|𪗎|卜難.竹弓.金|
|2A5D0|𪗐|卜難.田.金日|

6.「鹿形字」取碼<br />
有一些罕用字，如「𢉖」，包含了「鹿」上方的部件。漢文庫典對這些字的取碼並不統一，例「⿸[鹿-比]⿱且又」字取碼為「戈難水」，而「𢉖」被取碼為「戈難戈戈」。根據沈紅蓮女士的回信，可將「鹿-广-比」視作「X」的輔助字形。本碼表採用該方式。而原手冊中訂的難字，如「鹿」、「慶」、「廌」等字予以保留。

7.「龜」形字的取碼<br />
有一些字，結構類似於「龜」，取碼甚為困難。去信官方詢問，沈紅蓮女士回答：「中間類龜的均可取X，取頭尾作分辨。」。本碼表從之。現將這些字部分列舉如下：
|UCS碼位|漢字|取碼|
|-|-|-|
|258E8|𥣨|竹一.中難山|
|2A6A6|𪚦|一難山|

但是「𪚾」、「𪚿」等字，由於中間為一豎而非兩豎，故不取難字，仍按普通規則取碼。

8.「靑」的取碼<br />
漢文庫典中，「靑」字被取碼為「手一月」，與「青」重碼，即是將「円」設置為「月」之輔助字形。本碼表從之。

9.「㐃」的取碼<br />
漢文庫典中，「㐃」字被取碼為「戈中」，即是將「△」設置為「戈」之輔助字形。本碼表從之。

10.「𠥓」系列字的取碼<br />
含「𠥓」的一系列漢字，取碼較為困難。之前，流行的碼表均將其取為「尸中尸中」，似不甚合理。去信官方詢問，沈紅蓮女士建議可「在尸中加不包含內框的輔助字形」，即將「𠥓去掉里面的匚」字形設為「尸」的輔助字形。故「𠥓」取碼為「尸尸」。「𧀍」亦比照此法取碼。另有一結構較為相似的字「𠚜」，則依從漢文庫典，將「凹」設置為「山」的輔助字形。現將涉及的漢字不完全列舉如下：
|UCS碼位|漢字|取碼|
|-|-|-|
|2069C|𠚜|山.月.竹難|
|20953|𠥓|尸尸|
|20967|𠥧|尸尸.一火.口|
|20969|𠥩|尸尸.廿一金|
|2096A|𠥪|尸尸.月.竹難|
|2096B|𠥫|尸尸.竹山.尸|
|2096C|𠥬|尸尸.廿.人難|
|2700D|𧀍|山山.山山.土|

但是「兕」等字並不將「凹」視作「山」的輔助字形，區分的方法如下：若「凹」上部的「凵」內有部件存在，就可以應用「山」的輔助字形，否則仍應拆解為「尸尸山」。

11.新增複合字首「门」<br />
當繁體的「門」位於左側時，根据倉頡輸入法之規則，會將「門」視為一個整體從而將其劃分為字首。但簡體的「门」字，並無相關規定，又因其結構較為特殊，取碼時有一定困難。與官方通信後，決定將簡體的「门」設置為複合字首。現將涉及的漢字不完全列舉如下：
|UCS碼位|漢字|取碼|
|-|-|-|
|21B5C|𡭜|中尸.火|
|2CB98|𬮘|中尸.人|

12.複合字首「亥」<br />
增訂版三代手冊中有如下規則：「戊、戈、𢦏、㦰、产、麻、䧹、厭、厤、鴈、辰、厥、羽、府、鹿、亥、老、包、君..等字，雖不能作上下或左右一次分離，然為了取碼方便，一律定義之為字首。」。然而，按照倉頡之規則，「羽」顯然是可以左右一次分離的。而「亥」若無法上下一次分離，則結構相同的「玄」字也必然無法上下分離，則「畜」之取碼會變為「卜戈.田」。在漢文庫典中，「賌」取碼被修改為「卜.女人.金」，而五代手冊中亦無「亥」的特殊規則。故結合三代手冊上下文，本碼表將「亥」視為倉頡三代定義的複合字首，因此「賌」取碼跟從三代手冊，為「卜人.月山金」。

13.「丸」的取碼<br />
「丸」在原三代手冊中取「大弓戈」，是使用了「九」與「丶」不相交的字形。對於「九」與「丶」相交的字形，漢文庫典取「大弓大」。因此，對於傳統漢字，本碼表在遇到「丸」形時，一律兼容「大弓大」與「大弓戈」之字形。對於簡體字，本碼表一律取「大弓大」，容錯「大弓戈」之取碼，避免用戶的困擾。

14.「吂」之取碼<br />
許多流行的三代碼表將「吂」取碼為「卜女口」。增訂版三代手冊的附錄中雖無「吂」字，但其在「複合字」章節中明确將「吂」定義為複合字，取碼「卜口」。故本碼表將「吂」取碼為「卜口」。

15.「癶」之取碼<br />
倉頡二代手冊之附錄、漢文庫典等均將「癶」取碼為「弓戈卜人」。84版三代手冊和增訂版三代手冊之附錄中雖沒有「癶」字，但增訂版三代手冊之附錄二：常用字首、字身、字典部首取碼中亦明確將「癶」取碼為「弓戈卜人」。去信詢問官方，沈紅蓮女士亦肯認「兩短撇」為「卜」之輔助字形。故本碼表將「癶」取碼為「弓戈卜人」，將「兩短撇」歸入「卜」之輔助字形。唯注意「形」之右側為長撇，不適用於該輔助字形。

16.鏡像字的取碼<br />
有一些漢字包含了水平鏡像部件，或是垂直镜像部件，取碼相當困難。去信詢問官方，沈紅蓮女士稱六代以「Z」表示翻轉的功能，例如「𠄏」取「NNZ」，不必直接拆分，建議我們使用該方案。本碼表從之，在鏡像部件後補一「Z」（片）代表水平鏡像或垂直鏡像。現將涉及到的字不完全列舉如下：
|Unicode|漢字|取碼|
|-|-|-|
|2010F|𠄏|弓弓片|
|20114|𠄔|弓戈弓片|
|20432|𠐲|人.戈一.片|
|221B4|𢆴|女戈.弓弓片|
|22A0B|𢨋|戈一.戈口片|
|23028|𣀨|戈片.卜水|
|23952|𣥒|卜片.卜中一|
|24489|𤒉|戈一.戈片.火|
|24493|𤒓|戈一.戈片.火|
|27951|𧥑|戈一.戈片.月|
|27E42|𧹂|卜片.月山金|
|28668|𨙨|口.日山片|
|286DC|𨛜|口片.口.日山|
|287A0|𨞠|口片.廿金.山|
|287B0|𨞰|口片.竹心.片|
|2BE2A|𫸪|弓.弓片|
|2C886|𬢆|卜片.月山山|
|2E5D9|𮗙|月山.竹山片|
|304A5|𰒥|戈片.戈|
|30A07|𰨇|人片.一.一火|
|30C9E|𰲞|卜弓.戈片/卜山.戈片|

17.「醯」的取碼<br />
原三代碼表將「醯」取為「一田.卜山.廿」，視「曲川」之形上連。但是有觀點認為該取法不符倉頡規則，且漢文庫典中已將其取碼修改為「一田.卜戈.廿」。<br />
本碼表依從漢文庫典，將「醯」改碼為「一田.卜戈.廿」。其他含「⿱㐬皿」部件的漢字例如「橀」亦比照此取碼辦法。

18.「芈」的取碼<br />
就本「編碼說明」條目之第2點說明，「芈」被倉頡官方強制Big-5化對應到了「羋」所在碼位，亦即「芈」在增訂版三代手冊之附錄中的取碼實為「中一卜手」。這是因為，無論是增訂版或84版三代手冊中，「⻀」均不是「廿」之輔助字形，故要分拆開來取「中一卜」，與漢文庫典中的做法不同。於是，「芈」字作為連體字便取「中一卜手」。但如果按此方法，台灣標準字形的「敬」便要取碼「中口.人大」，「歡」字也要取碼「中土.弓人」，將會造成使用者的不便，也會增加重碼。本碼表將「卝」視為「廿」之輔助字形，故「芈」字改碼「廿手」，「羋」如上所述取「廿中手」。

19.彎曲封閉字形的取碼<br />
一些漢字，如「𡦹」包含了形若「♉」的彎曲筆畫。本碼表將此類封閉彎曲、末端交叉的字形一律取為「大」。因此「𡦹」取碼為「戈弓.大大」。

20.特殊字<br />
84版三代手冊和增訂版三代手冊在特殊字部分雖未言明「戈」、「七」的特殊字地位，但在實際取碼時卻有用到。例如「彧」在增訂版三代手冊附錄中取碼「戈大.口.一」，「屯」在增訂版三代手冊中取「心山」，等等。故本碼表取碼時將「戈」、「七」視作特殊字。

21.「八」的形狀與上連<br />
漢文庫典的取碼顯示「八」的形狀可能會影響其是否有上連功能。例：在漢文庫典中，「𦦡」取「竹金.一中」，但「𦦑」卻取「竹月.金.尸竹」。再如「𡩥」字在漢文庫典取「十.金.戈一」，而非「十金.戈.尸一」。再例如「𦉵」在漢文庫典中取碼「田中.金」，而非「田中中金」。更強的證據是「兗」字，在漢文庫典由不同的字形而分別取碼為「卜金.口竹山」、「卜.金.口山」。<br />
亦即，若「八」呈「舊字形的八」之形，則它便不會上連，而若其呈「/L」或「新字形的八」之形，則其有上連功能。<br />
本碼表依從漢文庫典的做法，視「八」的字形不同而決定其是否有上連。

### 字形兼容
注：
1.對於大陸簡體字，通常不類推字形兼容，僅以大陸字形取碼。但若該簡體字在Unicode Chart中有多個字形，則將兼容不同的字形。例如「残」（U+6B8B)同時對應着⿰歹戋和⿰歹㦮兩個源的字形，本碼表便取「一弓.戈十」和「一弓.戈手」。<br />
2.同一字的不同字形若被Unicode分開編碼，並不設字形兼容碼。例如本碼表不會給「黃」這一字本身設置「廿中田金」的字形兼容，因為「黃」與「黄」的單字被分開編碼了，但本碼表中「潢」等字有「水廿一金」和「水廿中金」的兩個編碼，因為「潢」字的三個字形被統合到了U+6F62的碼位之中。
|部件|取碼|備注|
|-|-|-|
|刃|尸戈/尸竹/尸大|對應「⿹刀丿」、「⿹刀丶」、「⿻刀丶」和「⿹𠃌㐅」等字形。「尸大」僅限於部分漢字。|
|卂|弓十/弓大||
|丸|大弓戈/大弓大||
|贏|卜口月月弓/卜口月月大||
|急|弓尸心/弓一心|取「弓尸.心」之字形的「一」未突出「コ」。取「弓一.心」之字形的「一」突出「コ」。|
|黃/黄|廿一田金/廿一中金/廿中田金/廿田金|「黃」字在單獨取碼時兼容「廿一田金/廿一中金」。「黄」單獨取碼時兼容「廿中田金/廿田金」。「廿田金」之字形不類推至全部漢字，而前三者類推。|
|爭/争|月尸木/弓尸木|傳統字形為「爭」，大陸字形為「争」。|
|尨|戈山竹竹竹/戈大山竹|三撇與「尤」不相交者為分體字取「戈山.竹竹竹」，相交者取「戈大山竹」。|
|吳/吴/呉|口女弓大/口一大/口女弓金|「呉」字形僅用於部分漢字，不類推。|
|反|竹水/一水|「⿸厂又」字形取「一水」，「⿸𠂆又」字形取「竹水」。|
|壬|竹土/一土|大陸標準首筆為撇，台灣標準首筆為橫。|
|呈|口竹土/口一土|大陸標準將「呈」中的「𡈼」寫作「王」。|
|四|田金/田竹山|區分「金」與「竹山」的重點不在於其在漢字中的相對位置，而是看尾形是否有鉤。沒有鉤取「金」，反之取「竹山」。因此陸標「四」取「田竹山」。「田竹山」僅在Unicode文檔有該字形時類推。|
|匹|尸金/尸竹山|同「四」。|
|屬|尸卜卜戈/尸水田戈|「屬」有兩種常見字形，一种中間寫「二丨二」，對於此種字形，三代取「尸卜卜戈」，而五代因增添了「二丨二」的輔助字形在「水」上，故可取「尸.水.田戈」。另一種字形中間寫「氺」，對於此種字形，無論是三代還是五代均可取「尸.水.田戈」。|
|犀|尸卜卜手/尸水竹手|同「屬」。|
|⺶|廿手/廿竹|大陸標準為六筆，傳統字形為七筆。|
|麥|十人弓戈/木人弓戈/木人竹水/十人竹水|「木人.弓戈」不用於字首，僅在字身類推|
|為|戈大弓火/月竹弓火||
|聚|尸水人人人/尸水心竹人/尸水人竹人/尸水竹竹人||
|衆|竹廿人竹人/竹廿竹竹人||
|周|月手口|香港標準字形為「⺆キ口」，而台灣標準和大陸標準為「⺆土口」。依字源，前者為篆形寫法。|
|憲|十手一心/十手十心|台灣標準字形取「十.手一.心」，而大陸標準取「十.手十.心」。|
|令|人一尸中/人戈弓戈|傳統字形下作「⿱𠃌丨」，為人跪坐之形，取「人.一.尸中」。|
|鼎|月山女一中/月山女一弓|香港標準和三代手冊所依字形為「月山.女一.中」，大陸標準與台灣標準取「月山.女一.弓」。|
|戶|竹尸/一尸/戈尸|「一.尸」僅在Unicode文檔有該字形時|
|灰|大火/一火|「一.火」僅在Unicode文檔有該字時|
|巽|口山廿金/口女廿金||
|羌|廿土竹山/廿手山|大陸標準為七筆，傳統字形為八筆。|
|幾|女戈竹戈/女戈大|大陸標準中「丿丶」與上方複合字相交呈「大」形。|
|飠/𩙿|人戈日戈/人一日卜/人戈日卜||
|查|木月一/木日一|傳統字形與日本標準字形中下方作「且」。|
|臭|竹山戈大/竹山大|日本標準下方作「大」，不類推。|
|突|十金戈大/十金大|下方作「大」之字形取「十金大」，不類推。|
|器|口口戈大口/口口大口口|中間作「大」者取「口口大口口」，不類推。|
|礻|戈火/一火|傳統字形左側作「示」形。|
|舌|一十口/竹十口|若有「一十口」字形可類推「竹十口」字形，而是否兼容「一十口」視Unicode文檔有無或倉頡官方是否兼容而定|
|臿|一十難/竹十難|大陸字形首筆為撇。|
|州|竹中戈中/戈中戈中/一中一中|大陸字形首筆為短撇，台灣字形首筆為點。|
|并|廿廿/卜十卜十||
|开|一廿/一大一十/一十一十||
|𤰇|廿竹月手/廿一月手||
|俞|人一月弓/人一月女|取「人.一.月女」之字形右下角作「巜」。|
|次|一一弓人/戈一弓人|取「一一.弓人」字形左側為「二」。|
|每|人田卜戈/人田十|「人.田十」僅在Unicode文檔有該字形時|
|毋|田十/田十竹|據漢文庫典及沈女士之回信，「毋」字之撇不出頭之字形取「田十」。|
|養|廿人戈日女/廿人一日女/廿金戈日女/廿金一日女||
|潛|大山/一山||
|流|水卜戈山/水卜戈女|台灣字形下方作「女」。|
|冬|竹水卜/竹水戈一|取「竹水.戈一」之字形下方作「冫」，較合字源。|
|兼|竹竹廿金/廿難金/金一難金|「金.一難金」僅在Unicode文檔有該字形時|
|酋|金.一金田一/廿金田一|傳統字形上方作「八」。|
|真|十月一金/心月山金/十山一金|「十山.一金」僅在Unicode文檔有該字形時|
|既|日戈一女山/竹卜一女山/竹心一女山||
|即|日戈尸中/竹心尸中/竹卜尸中||
|益|廿金月廿/金一金廿|取「金.一.金廿」之字形上方作「八」形。|
|良|戈戈/戈女||
|电|中田山/中田女|部分漢字|
|並|廿廿一/廿廿金||
|蔑|廿田中戈/廿田中一|「廿.田中.一」僅在Unicode文檔有該字形時|
|覃|一田日十/一月日十|「一月.日十」僅在Unicode文檔有該字形時|
|負|尸竹月山金/竹尸月山金/弓月山金|「竹尸.月山金」僅在Unicode文檔有該字形時|
|兔|弓山戈/尸竹日山戈|某些字形上方作「刀」。|
|免|弓日竹山/尸竹日竹山|同「兔」。|
|色|弓日山/尸竹日山|「尸竹.日山」僅有部分漢字|
|鼻|竹山田一中/竹山田廿|「竹山.田.廿」不用於字首，僅在字身類推|
|嘆之右側|廿中手人/廿日手人|「廿.日手人」僅在Unicode文檔有該字形時|
|戋|戈十/戈手|「戈手」僅在Unicode文檔有該字形時|
|堇|廿日手一/廿中手一|「廿.日手一」僅在Unicode文檔有該字形時|
|包|心口山/心尸山||
|臽|竹尸難/弓竹難/尸竹難||
|㒸|廿心竹人/金一尸人|「金.一尸人」之取碼字形上方作「八」，較合字源。|
|弱|弓一弓戈一/弓竹弓竹竹||
|䪞|一大中一一/竹大中一一||
|䨿|一大中一卜/竹大中一卜||
|秃|竹木竹弓/竹木竹山|視Unicode文檔情況而定|
|瓊之右側|弓月月山水/弓月月山大||
|界|田人中中/田金中中|台灣字形「田」下為「八」。|
|戎|戈十/戈大|「戈.大」可類推至簡體字。|
|关|廿大/金一大|部分漢字|
|主|卜土/手一|僅數個漢字|
|具|月一一金/月山一金|「月山.一金」僅在Unicode文檔有該字形時|
|郎|戈戈弓中/戈女弓中||
|朗|戈戈月/戈女月||
|尃|戈月木戈/戈中木戈/戈田木戈|「戈中.木戈」為部分漢字、「戈田.木戈」僅有數個漢字|
|叟|竹難中水/竹難水|取「竹難.水」之字形為香港標準，也是84版三代手冊取碼所據字形|
|曾|金田日/金田火日|取「金.田火.日」之字形上方作「八」。|

## 重碼字排序調整
|原排序|新排序|
|-|-|
|皿冊|冊皿|
|臓臟|臟臓|
|枟橱|橱枟|
|栘杼|杼栘|
|濑漱|漱濑|
|濯洭渥|渥濯洭|
|籹娄|娄籹|
|汨沓汩|沓汨汩|
|摮|摯摮摰|
|翺翱翶|翱翺翶|
|籩舮|舴籩舮|
|覝覔𧢄|視覔覝𧢄|
|戍庅|戍廆庅|
|弒|弒弑|
|弑弒|弒弑|
|剎|剎刹|
|瘶癞|癞瘶|
|猉|猉獚|
|蜞|蜞蟥|
|忝憨懕|憨忝恐懕|
|砅泵|泵砅|
|珼|贋珼|
|魲|鮓魲|
|欠久飞|久欠飞|
|个仲|仲个|
|旬旨|旨旬|
|掀抓|抓掀|
|拻熬|热熬拻|
|跖唔|唔跖|
|茱|孽茱蘖糵|
|靰莞|莞靰|
|蔈蘸|蘸蔈|
|苗曲|曲苗|
|妒幻|幻妒|
|嬬绷|绷嬬|
|纩戕|戕纩|
|筘吿|吿筘|
|衱版|版衱|
|呅哒|哒呅|
|剙刱|刱剙|
|刱剏剙|刱剙剏|
|观沉|沉观|
|郗郁郩|郁郗郩|
|噭唳|唳噭|
|坈壳|壳坈|
|蜑蚀|蚀蜑|
|洮溃|溃洮|
|忝懲|懲忝|
|苋藐|藐苋|
|鋶銃|銃鋶|
|锍铳|铳锍|
|愗憨|憨愗|
|蘘藹|藹蘘|
|洫盪|盪洫|
|擨攒|攒擨|
|抆挞|挞抆|