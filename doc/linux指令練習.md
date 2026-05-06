
### **第一部分：基本指令與檔案操作**

**練習題：**
1.  如何一次建立多層目錄 `~/test/level1/level2`？
2.  如何檢視 `/etc/passwd` 檔案內容並顯示行號（排除空白行）？
3.  如何將 `/etc/passwd` 複製到 `/tmp` 目錄下，並確保檔案屬性（如時間戳記）被保留？
4.  如何將目錄 `~/test` 及其內容強制刪除且不彈出確認視窗？
5.  在不進入編輯器的情況下，如何快速建立一個名為 `empty.txt` 的空檔案？

**解答：**
1.  使用 `mkdir -p ~/test/level1/level2`。
2.  執行 `cat -b /etc/passwd` 或 `nl /etc/passwd`。
3.  使用 `cp -p /etc/passwd /tmp/` 或 `cp -a /etc/passwd /tmp/`。
4.  執行 `rm -rf ~/test`。
5.  執行 `touch empty.txt`。

---

### **第二部分：帳號管理與權限設定**

**練習題：**
1.  建立一個新使用者 `student1`，要求自動建立家目錄且預設 Shell 為 `/bin/bash`。
2.  如何將檔案 `report.txt` 的權限設定為：擁有者具備讀寫執行權限，群組具備讀與執行權限，其他人僅能讀取（請用數字模式表示）？
3.  如何將目錄 `/data` 及其下所有檔案的擁有者更改為 `tony`，擁有群組更改為 `users`？
4.  如何將使用者 `u3` 加入到 `student` 這個次要群組中？
5.  如何設定一個目錄具有 **Sticky Bit (SBIT)** 權限，讓使用者只能刪除自己建立的檔案？

**解答：**
1.  執行 `sudo useradd -m -s /bin/bash student1`。
2.  執行 `chmod 754 report.txt` (7=rwx, 5=rx, 4=r)。
3.  執行 `sudo chown -R tony:users /data`。
4.  執行 `sudo usermod -G student u3`。
5.  執行 `chmod 1777 目錄名稱` 或 `chmod o+t 目錄名稱`。

---

### **第三部分：資料流重導向與管線命令**

**練習題：**
1.  如何將 `ls -l` 的執行結果輸出並 **附加 (append)** 到 `file_list.txt` 檔案末端？
2.  如何執行 `cat` 指令讀取一個不存在的檔案，並將錯誤訊息導向至 `/dev/null`（使其不顯示在螢幕上）？
3.  如何找出 `/etc/passwd` 檔案中包含 "root" 字串的行？
4.  如何將 `ls -l /etc` 的前 10 行結果顯示出來？
5.  如何同時將指令執行結果輸出到螢幕並存入 `output.log` 檔案？

**解答：**
1.  執行 `ls -l >> file_list.txt`。
2.  執行 `cat nofile 2> /dev/null`。
3.  執行 `grep 'root' /etc/passwd`。
4.  執行 `ls -l /etc | head -n 10`。
5.  使用管線搭配 `tee` 指令：`command | tee output.log`。

---

### **第四部分：系統管理與自動化**

**練習題：**
1.  如何以容易閱讀的單位（如 GB, MB）檢視目前系統磁碟空間的使用現況？
2.  如何強行中止 PID 為 `1234` 的程序？
3.  將 `/home` 目錄下的所有內容打包並壓縮為 `/backup/home_bck.tar.gz`。
4.  如何撰寫一個簡單的 Shell Script 段落，判斷變數 `n1` 是否大於 `n2`？
5.  如何在 `vi` 編輯器中顯示行號？

**解答：**
1.  執行 `df -h` 或 `df -Th`。
2.  執行 `kill -9 1234`。
3.  執行 `tar -zcvf /backup/home_bck.tar.gz /home`。
4.  腳本內容如下：
    ```bash
    if [ $n1 -gt $n2 ]; then
        echo "$n1 is bigger"
    else
        echo "$n2 is bigger"
    fi
    ```
5.  在指令列模式輸入 `:set nu`。