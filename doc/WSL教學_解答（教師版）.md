# WSL 練習題解答 — 教師版

> ⚠️ 本文件僅供教師參考，請勿在課前發放給學生。  
> 部分題目有多種正確答案，以下提供最常見的參考解法。

---

## 第 1 堂解答：認識環境

---

**Q1｜基本資訊查詢**

每位學生答案不同（依其系統環境），格式參考：
```
whoami   → student（依帳號名稱）
hostname → DESKTOP-XXXXXX（依電腦名稱）
uname -r → 5.15.90.1-microsoft-standard-WSL2（版本因人而異）
$SHELL   → /bin/bash
```

---

**Q2｜查看家目錄隱藏檔案**

```bash
ls -la ~
```

常見的隱藏檔案（以 `.` 開頭）：
```
.bashrc      ← bash 設定
.bash_history ← 指令歷史
.profile     ← 登入設定
.bash_logout ← 登出設定
.config/     ← 應用程式設定目錄
```

---

**Q3｜使用說明查詢**

```bash
ls --help | grep "\-t"
ls --help | grep "\-S"
```

- `-t`：依修改時間排序（最新的在前）
- `-S`：依檔案大小排序（最大的在前）

---

**Q4｜挑戰題**

```bash
ls -laht ~
```

說明：
- `-l`：長格式
- `-a`：含隱藏檔
- `-h`：人類可讀大小（KB/MB）
- `-t`：依時間排序

---

## 第 2 堂解答：目錄與檔案操作

---

**Q1｜建立目錄結構**

```bash
mkdir -p ~/practice/week1 ~/practice/week2 ~/practice/week3/notes
```

或：
```bash
mkdir -p ~/practice/{week1,week2,week3/notes}
```

驗證：
```bash
ls -R ~/practice/
```

---

**Q2｜檔案建立與內容寫入**

```bash
cd ~/practice/week1/
touch myinfo.txt                      # 1. 建立檔案
echo "王小明" > myinfo.txt             # 2. 寫入名字（覆蓋）
echo "2026-03-24" >> myinfo.txt        # 3. 附加日期
cat myinfo.txt                         # 4. 確認內容
```

> 📌 注意：`>` 覆蓋，`>>` 附加，是最常混淆的地方。

---

**Q3｜複製與移動**

```bash
cp myinfo.txt ~/practice/week2/myinfo_copy.txt
mv ~/practice/week2/myinfo_copy.txt ~/practice/week3/notes/
ls ~/practice/week2/          # 確認 week2 為空
ls ~/practice/week3/notes/    # 確認 notes 有檔案
```

---

**Q4｜挑戰題**

```bash
# 建立 5 個檔案
touch ~/practice/week1/{a,b,c,d,e}.txt

# 刪除 b.txt 和 d.txt（一行）
rm ~/practice/week1/b.txt ~/practice/week1/d.txt
```

或：
```bash
rm ~/practice/week1/{b,d}.txt
```

---

## 第 3 堂解答：文字處理與搜尋

---

**Q1｜grep 搜尋**

```bash
# 1. 列出 Engineer
grep "Engineer" employees.txt

# 2. Taipei 員工（含行號）
grep -n "Taipei" employees.txt

# 3. 不是 Engineer
grep -v "Engineer" employees.txt

# 4. Manager 數量
grep -c "Manager" employees.txt
# 答：2 個
```

---

**Q2｜find 搜尋**

```bash
# 1. 所有 .txt
find ~/practice/ -name "*.txt"

# 2. 所有目錄
find ~/practice/ -type d
```

---

**Q3｜管線（pipe）組合**

```bash
# 1. /usr/bin 含 zip 的指令
ls /usr/bin | grep "zip"

# 2. 行數統計
cat employees.txt | wc -l
# 或：wc -l employees.txt

# 3. 存到新檔案
grep "Taipei" employees.txt > taipei_staff.txt
```

---

**Q4｜挑戰題**

```bash
grep "Engineer" employees.txt | grep "Taipei" | sort
```

結果：
```
Alice Engineer Taipei 85000
Eve Engineer Taipei 92000
```

---

## 第 4 堂解答：權限管理

---

**Q1｜讀懂權限**

```
-rw-r--r-- 1 root root 2847 ...
```

| 角色 | 權限字元 | 數字 |
|------|---------|------|
| 擁有者 | rw- | 6 |
| 群組 | r-- | 4 |
| 其他人 | r-- | 4 |

- 一般使用者能執行嗎？**不能**（沒有 x 權限）

---

**Q2｜chmod 練習**

```bash
# 1. 直接執行（失敗）
~/practice/week1/test.sh
# 錯誤：-bash: /home/user/practice/week1/test.sh: Permission denied

# 2. 加上執行權限
chmod +x ~/practice/week1/test.sh
~/practice/week1/test.sh

# 3. ls -l 確認
ls -l ~/practice/week1/test.sh
# 輸出：-rwxr-xr-x 1 user group 41 Mar 24 10:00 test.sh
```

---

**Q3｜sudo 練習**

```bash
# 1. 一般使用者（失敗）
touch /opt/test.txt
# 錯誤：touch: cannot touch '/opt/test.txt': Permission denied

# 2. 使用 sudo（成功）
sudo touch /opt/test.txt

# 3. 刪除測試檔案
sudo rm /opt/test.txt
```

---

**Q4｜挑戰題**

```bash
touch ~/secret.txt
chmod 640 ~/secret.txt
ls -l ~/secret.txt
```

輸出：
```
-rw-r----- 1 user group 0 Mar 24 10:00 secret.txt
```

| 角色 | 數字 | 說明 |
|------|------|------|
| owner | 6 | rw- |
| group | 4 | r-- |
| other | 0 | --- |

---

## 第 5 堂解答：套件管理

---

**Q1｜安裝與確認**

```bash
sudo apt update
sudo apt install tree curl git -y

tree --version   # tree v2.x.x
curl --version   # curl 7.x.x ...
git --version    # git version 2.x.x
```

---

**Q2｜套件查詢**

```bash
# 1. 搜尋 python3 相關（只取前 5 行）
apt search python3 | head -5

# 2. git 詳細資訊
apt show git
# Description: fast, scalable, distributed revision control system

# 3. which git
which git
# /usr/bin/git
```

---

**Q3｜Python 虛擬環境**

```bash
cd ~/practice/
python3 -m venv myenv              # 建立
source myenv/bin/activate          # 啟動
pip install requests               # 安裝
pip list | grep requests           # 確認
deactivate                         # 離開
```

---

**Q4｜挑戰題**

```bash
cd ~/practice/
python3 -m venv myenv && source myenv/bin/activate
pip install httpx

cat > test_http.py << 'EOF'
import httpx
print(httpx.__version__)
EOF

python3 test_http.py
```

---

## 第 6 堂解答：整合實戰

---

**Step 1｜目錄初始化**

```bash
mkdir -p ~/memo_system/{notes,archive,scripts}
```

---

**Step 2｜建立腳本**

```bash
cat > ~/memo_system/scripts/add_note.sh << 'EOF'
#!/bin/bash
echo "$(date '+%Y-%m-%d %H:%M:%S'): $1" >> ~/memo_system/notes/notes.txt
echo "備忘已儲存！"
EOF

chmod +x ~/memo_system/scripts/add_note.sh
```

---

**Step 3｜測試腳本**

```bash
~/memo_system/scripts/add_note.sh "記得繳作業"
~/memo_system/scripts/add_note.sh "買晚餐"
~/memo_system/scripts/add_note.sh "複習 WSL 指令"

cat ~/memo_system/notes/notes.txt
```

預期輸出：
```
2026-03-24 10:15:30: 記得繳作業
2026-03-24 10:15:32: 買晚餐
2026-03-24 10:15:34: 複習 WSL 指令
```

---

**Step 4｜搜尋備忘**

```bash
grep "作業" ~/memo_system/notes/notes.txt > ~/memo_system/archive/search_result.txt
cat ~/memo_system/archive/search_result.txt
```

---

**Step 5｜Windows 檔案總管**

```bash
explorer.exe ~/memo_system/
```

或使用 Windows 路徑：
```bash
explorer.exe .    # 若已在 ~/memo_system/ 目錄下
```

---

## 📊 評分建議

| 堂次 | 滿分 | 關鍵評分點 |
|------|------|-----------|
| 第 1 堂 | 20 | Q4 能組合選項即得滿分 |
| 第 2 堂 | 20 | `>` 與 `>>` 使用正確 |
| 第 3 堂 | 20 | 管線與 grep 搭配使用 |
| 第 4 堂 | 20 | 數字權限與 chmod 正確 |
| 第 5 堂 | 20 | 虛擬環境完整流程 |
| 第 6 堂 | 20 | 腳本能成功執行 |

---

## 🔍 常見錯誤提醒

| 錯誤 | 原因 | 正確做法 |
|------|------|---------|
| `>` 把重要檔案覆蓋了 | 混淆 `>` 和 `>>` | 附加用 `>>` |
| `rm -rf` 刪錯目錄 | 路徑不對 | 先 `ls` 確認再刪 |
| chmod 沒生效 | 路徑錯誤 | 用絕對路徑確認 |
| apt install 失敗 | 忘記 `sudo apt update` | 先更新再安裝 |
| venv 啟動後無變化 | 忘記 `source` | `source venv/bin/activate` |
