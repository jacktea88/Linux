# WSL 教學範例 — 老師示範手冊

> 共 6 堂課，每堂約 50 分鐘。老師依序示範，學生跟著操作。

---

## 第 1 堂：認識 WSL 與基本環境

### 🎯 教學目標
- 了解 WSL 是什麼、為什麼要用它
- 成功啟動並登入 WSL
- 熟悉 Shell 提示字元結構

### 📋 老師示範步驟

**Step 1：確認 WSL 已安裝**
```powershell
# 在 Windows PowerShell 執行
wsl --list --verbose
```
預期輸出：
```
  NAME      STATE           VERSION
* Ubuntu    Running         2
```

**Step 2：啟動並觀察提示字元**
```bash
wsl
# 提示字元說明：
# user@hostname:~$
# │    │         │└─ $ = 一般使用者，# = root
# │    │         └── ~ = 目前在家目錄
# │    └──────────── 電腦名稱
# └───────────────── 使用者名稱
```

**Step 3：認識基本環境資訊**
```bash
whoami              # 目前登入的使用者
hostname            # 電腦名稱
uname -a            # Linux 核心版本資訊
cat /etc/os-release # 發行版詳細資訊
echo $SHELL         # 目前使用的 Shell
```

**Step 4：示範 help 與 man**
```bash
ls --help           # 查看指令說明
man ls              # 查看完整手冊（q 離開）
```

### 💡 課堂重點提示
- 大小寫有區別：`ls` ≠ `LS`
- 路徑分隔符是 `/`，不是 `\`
- `~` 代表家目錄，等於 `/home/你的帳號`

---

## 第 2 堂：目錄與檔案操作

### 🎯 教學目標
- 熟練目錄切換與檔案管理
- 理解絕對路徑與相對路徑

### 📋 老師示範步驟

**Step 1：建立練習環境**
```bash
# 進入家目錄，建立課程目錄
cd ~
mkdir -p wsl_class/lesson2/{docs,images,scripts}
ls -R wsl_class/
```

**Step 2：路徑概念示範**
```bash
pwd                        # 顯示絕對路徑
cd wsl_class/lesson2       # 相對路徑切換
cd /home/$USER/wsl_class   # 絕對路徑切換
cd ..                      # 上一層
cd -                       # 切回上一次的目錄
```

**Step 3：檔案建立與查看**
```bash
cd ~/wsl_class/lesson2/docs

# 建立測試檔案
touch note.txt
echo "Hello WSL!" > hello.txt
echo "第一行" >> hello.txt     # >> 是附加，不覆蓋
echo "第二行" >> hello.txt

# 查看內容
cat hello.txt
wc -l hello.txt               # 計算行數
```

**Step 4：複製、移動、刪除**
```bash
cp hello.txt hello_backup.txt            # 複製
mv hello_backup.txt ../                  # 移動到上層目錄
ls ../ 
cp -r docs/ docs_backup/                 # 複製整個目錄
rm docs_backup/hello.txt                 # 刪除檔案
rm -r docs_backup/                       # 刪除目錄
```

**Step 5：ls 進階用法**
```bash
ls -l                  # 詳細列表
ls -la                 # 含隱藏檔
ls -lh                 # 人類可讀大小
ls -lt                 # 依時間排序
ls -lS                 # 依大小排序
```

### 💡 課堂重點提示
- `>` 覆蓋；`>>` 附加，不要搞混
- `rm -rf` 無法還原，操作前請確認路徑

---

## 第 3 堂：文字處理與搜尋

### 🎯 教學目標
- 使用 grep / find 搜尋資料
- 了解管線（pipe）的用法

### 📋 老師示範步驟

**Step 1：準備練習資料**
```bash
cd ~/wsl_class
mkdir lesson3 && cd lesson3

# 建立模擬的學生名單
cat > students.txt << 'EOF'
Alice 90 Math
Bob 75 English
Carol 88 Math
David 62 Science
Eve 95 Math
Frank 80 English
EOF
```

**Step 2：grep 搜尋示範**
```bash
grep "Math" students.txt             # 搜尋含 Math 的行
grep -i "math" students.txt          # 忽略大小寫
grep -n "Math" students.txt          # 顯示行號
grep -v "Math" students.txt          # 排除 Math（反向）
grep -c "Math" students.txt          # 計算符合行數
```

**Step 3：find 搜尋示範**
```bash
# 回到上層查看目錄結構
cd ~/wsl_class

find . -name "*.txt"                 # 找所有 txt 檔案
find . -type d                       # 只找目錄
find . -type f -size +0c             # 找非空檔案
find . -name "*.txt" -mtime -1       # 24 小時內修改的 txt
```

**Step 4：管線（pipe）示範**
```bash
cd lesson3

# | 把前一個指令的輸出，送給下一個指令當輸入
cat students.txt | grep "Math"
cat students.txt | wc -l
ls /usr/bin | grep "zip"
cat students.txt | sort
cat students.txt | sort | uniq

# 組合使用：找 Math 學生並排序
grep "Math" students.txt | sort
```

**Step 5：重新導向**
```bash
grep "Math" students.txt > math_students.txt    # 輸出到檔案
grep "English" students.txt >> math_students.txt # 附加
cat math_students.txt
ls non_exist 2> error.log                        # 錯誤訊息導向
```

### 💡 課堂重點提示
- `|` 是管線，讓指令「串起來」
- `>` 是輸出導向，會覆蓋檔案
- grep 的強大在於可以搭配正規表達式

---

## 第 4 堂：權限與使用者管理

### 🎯 教學目標
- 理解 Linux 權限模型（rwx）
- 熟悉 chmod / chown / sudo

### 📋 老師示範步驟

**Step 1：讀懂權限欄位**
```bash
ls -l ~/wsl_class/lesson2/docs/hello.txt
# 輸出：-rw-r--r-- 1 user group 25 Mar 24 10:00 hello.txt
#        │││││││││
#        │└┤└┤└┤└── other: r--  = 4
#        │ │ └──── group: r--  = 4
#        │ └────── owner: rw-  = 6
#        └──────── 檔案類型（- 是檔案，d 是目錄）
```

**Step 2：chmod 示範**
```bash
cd ~/wsl_class/lesson2/scripts

# 建立一個腳本
echo '#!/bin/bash' > hello.sh
echo 'echo "Hello from script!"' >> hello.sh

ls -l hello.sh             # 查看目前權限
./hello.sh                 # 執行（會失敗，沒有執行權限）

chmod +x hello.sh          # 加上執行權限
ls -l hello.sh             # 再查看
./hello.sh                 # 成功執行

chmod 644 hello.sh         # 改為 rw-r--r--
chmod 755 hello.sh         # 改為 rwxr-xr-x（腳本常用）
```

**Step 3：sudo 示範**
```bash
# 一般使用者無法安裝軟體
apt install tree           # 會失敗

# 使用 sudo 取得臨時 root 權限
sudo apt update
sudo apt install tree -y
tree ~/wsl_class/          # 樹狀顯示目錄結構
```

**Step 4：查看使用者資訊**
```bash
id                          # 顯示 uid / gid / groups
whoami                      # 目前使用者
cat /etc/passwd | grep $USER  # 使用者帳號資訊
groups                      # 所屬群組
```

### 💡 課堂重點提示
- 755 = 擁有者可執行，其他人只能讀
- 644 = 擁有者可讀寫，其他人只能讀
- 永遠不要在不了解的情況下 `sudo rm -rf`

---

## 第 5 堂：套件管理與環境建置

### 🎯 教學目標
- 熟悉 apt 套件管理
- 能夠安裝開發工具並驗證

### 📋 老師示範步驟

**Step 1：apt 基本操作**
```bash
sudo apt update                     # 更新套件列表（必須先做）
sudo apt list --upgradable          # 查看可升級的套件

sudo apt install curl -y            # 安裝 curl
sudo apt install git python3 -y     # 一次安裝多個

apt show git                        # 查看套件資訊
which git                           # 確認安裝位置
git --version                       # 確認版本
```

**Step 2：搜尋與移除**
```bash
apt search "text editor"            # 搜尋套件
sudo apt remove nano -y             # 移除（保留設定）
sudo apt purge nano -y              # 移除（含設定）
sudo apt autoremove -y              # 清除無用依賴
```

**Step 3：安裝 Python 開發環境（實際範例）**
```bash
sudo apt install python3 python3-pip python3-venv -y

python3 --version
pip3 --version

# 建立虛擬環境
mkdir ~/wsl_class/python_demo && cd ~/wsl_class/python_demo
python3 -m venv venv
source venv/bin/activate            # 啟動虛擬環境
# 提示字元變為 (venv) user@host:~$

pip install requests                # 在虛擬環境中安裝
pip list
deactivate                          # 離開虛擬環境
```

**Step 4：安裝 Node.js（nvm 方式）**
```bash
# 使用 nvm 管理 Node.js 版本
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc

nvm install --lts           # 安裝最新 LTS 版
nvm list
node --version
npm --version
```

### 💡 課堂重點提示
- 安裝前必須 `sudo apt update`，否則可能找不到套件
- 虛擬環境讓每個專案有獨立的 Python 套件
- 推薦使用 nvm 管理 Node.js，避免版本衝突

---

## 第 6 堂：WSL 與 Windows 整合 + 實戰演練

### 🎯 教學目標
- 熟悉 WSL 與 Windows 互通機制
- 完成一個完整的小型開發流程

### 📋 老師示範步驟

**Step 1：存取 Windows 檔案**
```bash
ls /mnt/c/                             # C 槽
ls /mnt/c/Users/                       # 所有 Windows 使用者

# 將 Windows 桌面的檔案複製進來
cp /mnt/c/Users/$USER/Desktop/test.txt ~/   # (若桌面有 test.txt)

# 路徑轉換
wslpath -w ~/wsl_class                 # Linux 路徑轉 Windows 路徑
wslpath "C:\\Users"                    # Windows 路徑轉 Linux 路徑
```

**Step 2：從 WSL 開啟 Windows 程式**
```bash
explorer.exe .            # 用檔案總管開啟當前目錄
notepad.exe ~/.bashrc     # 用記事本編輯 .bashrc
code .                    # 用 VS Code 開啟（需安裝 WSL 擴充）
```

**Step 3：.bashrc 客製化**
```bash
nano ~/.bashrc

# 在檔案末尾加入：
# alias ll='ls -la'
# alias gs='git status'
# alias ..='cd ..'
# alias ...='cd ../..'

# 儲存後套用
source ~/.bashrc
ll              # 測試別名是否生效
```

**Step 4：完整開發流程示範**
```bash
# 建立一個小型 Python 專案
mkdir ~/wsl_class/myproject && cd ~/wsl_class/myproject
python3 -m venv venv && source venv/bin/activate

# 建立程式
cat > main.py << 'EOF'
def greet(name):
    return f"Hello, {name}! Welcome to WSL."

if __name__ == "__main__":
    print(greet("Student"))
EOF

# 執行
python3 main.py

# 用 VS Code 開啟專案
code .

# 完成後用檔案總管查看成果
explorer.exe .
```

### 💡 課堂重點提示
- `/mnt/c/` 效能比 `~/` 慢，專案請放在家目錄
- VS Code 的 WSL 擴充可讓你在 Windows UI 編輯 Linux 的檔案
- `source ~/.bashrc` 讓修改立即生效，不需重啟
