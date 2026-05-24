在 Linux 中，預設有專門的機制可以記錄指令，但若要連同指令的執行結果一起記錄，則需要透過特定的工具來達成。以下為您整理常見的解決方案：
## 1. 僅記錄歷史指令（預設內建）
Linux 的 Shell（如 Bash）本身會自動記錄所有輸入過的指令。 [1] 

* 指令： 直接輸入 history 即可查看當前帳號執行過的指令清單。
* Log 檔案： 這些指令會被寫入在使用者家目錄下的 .bash_history 檔案中（例如 /home/username/.bash_history）。
* 缺點： 此方法不會記錄指令的執行結果，且如果有多個終端機同時開啟，可能會互相覆蓋。 [1, 2] 

## 2. 同時記錄指令與執行結果（推薦工具）
若要完整記錄敲下的指令以及終端機輸出的所有結果（包含錯誤訊息），推薦使用以下工具：
## A. script 指令（最簡單、免安裝）
這是 Linux 內建的指令，可以將當下終端機的所有輸入與輸出錄製成一個 Log 檔案。 [3] 

* 開始錄製： 輸入 script filename.log。此後該終端機的所有動作都會被寫入 filename.log。
* 結束錄製： 輸入 exit 或按下 Ctrl + D。
* 查看結果： 使用 cat filename.log 即可觀看指令與結果。

## B. scriptreplay（指令視覺化回放）
搭配 script 指令使用，可以像看影片一樣「回放」過去在終端機裡的所有操作過程及結果。
## C. sudosh 或 tlog（進階稽核與集中記錄）
適合伺服器管理員。這類工具可以強制記錄所有使用者的操作（包含 Root 權限切換）與畫面輸出，並將 Log 集中儲存至安全的系統目錄中，無法被一般使用者竄改。
## 3. 系統核心與安全事件追蹤
如果您需要從系統層面嚴格監控特定指令或檔案的存取與執行狀態（例如資安稽核），可以使用系統內建的 auditd（Linux Audit Daemon）機制。 [4] 

* Log 檔案： 通常儲存於 /var/log/audit/audit.log。
* 用途： 可以追蹤哪些使用者在什麼時間點執行了什麼程式、存取了哪些敏感檔案。 [4] 


[1] [https://puremonkey2010.blogspot.com](http://puremonkey2010.blogspot.com/2011/02/linux-history.html)
[2] [https://shazi.info](https://shazi.info/linux-%E6%8A%8A-history-%E7%9A%84-command-log-%E5%AF%AB%E5%88%B0%E6%8C%87%E5%AE%9A%E7%9A%84-log-file/)
[3] [https://eagle.aii.tw](https://eagle.aii.tw/%E5%A5%BD%E7%94%A8%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%A8%8B/%E8%87%AA%E5%8B%95%E5%8C%96%E9%87%8D%E8%A9%A6%E6%8C%81%E7%BA%8C%E8%88%87%E6%97%A5%E8%AA%8C%E8%A8%98%E9%8C%84/)
[4] [https://www.netadmin.com.tw](https://www.netadmin.com.tw/netadmin/zh-tw/technology/87B0B07EEFE849A1A898E6A288C73E9A)


若你想針對 history 中的特定指令進行操作，可以參考以下幾種實用方法：
## 1. 執行特定編號的指令
當你輸入 history 時，每行指令前都有一個編號。

* 快速執行： 輸入 !編號 即可。
* 範例： !105 會直接執行歷史清單中第 105 號的指令。

## 2. 執行「最後一次」開頭為某字串的指令

* 語法： !字串
* 範例： !ssh 會找出最近一次執行的 ssh 指令並直接執行。

## 3. 搜尋含有特定關鍵字的指令（最推薦）
如果你不記得編號，可以使用 Reverse Search（反向搜尋）：

   1. 按下 Ctrl + R。
   2. 開始輸入關鍵字（例如 docker）。
   3. 終端機會自動跳出最近匹配的指令，重複按 Ctrl + R 可切換到更舊的匹配項。
   4. 按下 Enter 執行，或按 右方向鍵 修改該指令。

## 4. 查看特定關鍵字的歷史紀錄
如果你只想「看」而不想馬上執行，可以搭配 grep：

* 指令： history | grep "關鍵字"
* 範例： history | grep "apt install"

## 5. 刪除特定編號的紀錄
如果你不小心輸入了包含密碼的指令，想單獨刪除它：

* 指令： history -d 編號

您是想找回特定的長指令來重新執行，還是想將某個指令的執行過程輸出存成檔案呢？

