# WSL 教學指南（Windows Subsystem for Linux）

> 適用版本：WSL 2 / Windows 10・11

---

## 目錄

1. [WSL 簡介](#1-wsl-簡介)
2. [安裝與設定](#2-安裝與設定)
3. [基本操作指令](#3-基本操作指令)
4. [檔案系統操作](#4-檔案系統操作)
5. [網路相關](#5-網路相關)
6. [套件管理（apt）](#6-套件管理apt)
7. [WSL 與 Windows 互通](#7-wsl-與-windows-互通)
8. [程序管理](#8-程序管理)
9. [實用技巧與進階設定](#9-實用技巧與進階設定)
10. [常見問題排除](#10-常見問題排除)

---

## 1. WSL 簡介

WSL（Windows Subsystem for Linux）是 Microsoft 提供的功能，讓你在 Windows 上執行 Linux 指令列環境，無需虛擬機器或雙重開機。

**WSL 1 vs WSL 2**

| 特性 | WSL 1 | WSL 2 |
|------|-------|-------|
| 核心 | 轉譯層 | 真實 Linux 核心 |
| 檔案效能 | 跨系統較快 | Linux 本機較快 |
| 相容性 | 部分 | 完整 |
| Docker 支援 | 有限 | 完整 |

---

## 2. 安裝與設定

### 安裝 WSL（PowerShell 以系統管理員執行）

```powershell
# 一鍵安裝 WSL + 預設 Ubuntu
wsl --install

# 安裝指定發行版
wsl --install -d Ubuntu-22.04
wsl --install -d Debian
```

### 查看可用發行版

```powershell
# 列出線上可安裝的發行版
wsl --list --online

# 列出已安裝的發行版
wsl --list --verbose
```

### 設定預設版本

```powershell
# 設定 WSL 2 為預設
wsl --set-default-version 2

# 將特定發行版升級至 WSL 2
wsl --set-version Ubuntu 2

# 設定預設啟動的發行版
wsl --set-default Ubuntu-22.04
```

### 啟動與關閉

```powershell
# 啟動預設發行版
wsl

# 啟動指定發行版
wsl -d Ubuntu-22.04

# 關閉所有 WSL 執行個體
wsl --shutdown

# 關閉特定發行版
wsl --terminate Ubuntu-22.04

# show現在開啟的發行版名稱(已開啟linux時)
echo $WSL_DISTRO_NAME
```



---

## 3. 基本操作指令

### 目錄操作

```bash
# 顯示目前所在路徑
pwd

# 切換目錄
cd /home/user          # 切換到絕對路徑
cd Documents           # 切換到相對路徑
cd ~                   # 切換到家目錄
cd ..                  # 上一層目錄
cd -                   # 切換到上一次的目錄

# 列出目錄內容
ls                     # 基本列表
ls -l                  # 詳細資訊（長格式）
ls -la                 # 包含隱藏檔案
ls -lh                 # 人類可讀的檔案大小

# 建立目錄
mkdir my_folder
mkdir -p path/to/nested/folder    # 建立多層目錄
```

### 檔案操作

```bash
# 建立空檔案
touch file.txt

# 複製檔案
cp source.txt destination.txt
cp -r source_dir/ destination_dir/    # 複製目錄

# 移動 / 重新命名
mv old_name.txt new_name.txt
mv file.txt /home/user/Documents/

# 刪除
rm file.txt                  # 刪除檔案
rm -r my_folder/             # 刪除目錄（遞迴）
rm -rf my_folder/            # 強制刪除（小心使用！）

# 查看檔案內容
cat file.txt                 # 全部輸出
less file.txt                # 分頁瀏覽（q 離開）
head -n 20 file.txt          # 查看前 20 行
tail -n 20 file.txt          # 查看後 20 行
tail -f log.txt              # 即時追蹤檔案更新（Ctrl+C 離開）
```

### 搜尋

```bash
# 搜尋檔案
find /home -name "*.txt"              # 找出所有 .txt 檔案
find . -name "config" -type f         # 只找檔案
find . -name "logs" -type d           # 只找目錄
find . -mtime -7                      # 7 天內修改的檔案

# 搜尋檔案內容
grep "keyword" file.txt               # 搜尋關鍵字
grep -r "keyword" ./                  # 遞迴搜尋整個目錄
grep -i "keyword" file.txt            # 忽略大小寫
grep -n "keyword" file.txt            # 顯示行號
grep -v "keyword" file.txt            # 反向（排除含關鍵字的行）
```

---

## 4. 檔案系統操作

### 權限管理

```bash
# 查看權限
ls -l file.txt
# 輸出範例：-rw-r--r-- 1 user group 1024 Mar 24 10:00 file.txt

# 修改權限（chmod）
chmod 755 script.sh             # rwxr-xr-x
chmod 644 file.txt              # rw-r--r--
chmod +x script.sh              # 加入執行權限
chmod -x script.sh              # 移除執行權限
chmod -R 755 my_folder/         # 遞迴修改目錄

# 修改擁有者（chown）
chown user:group file.txt
sudo chown -R user:group folder/
```

**權限數字對照：**

| 數字 | 權限 | 說明 |
|------|------|------|
| 7 | rwx | 讀 + 寫 + 執行 |
| 6 | rw- | 讀 + 寫 |
| 5 | r-x | 讀 + 執行 |
| 4 | r-- | 唯讀 |
| 0 | --- | 無權限 |

### 磁碟空間

```bash
# 查看磁碟使用量
df -h                           # 各掛載點空間
df -h /                         # 根目錄空間

# 查看目錄大小
du -sh /home/user/              # 目錄總大小
du -sh *                        # 當前目錄各子項目大小
du -sh * | sort -h              # 排序顯示
```

### 壓縮與解壓縮

```bash
# tar 打包
tar -cvf archive.tar folder/        # 打包（不壓縮）
tar -czvf archive.tar.gz folder/    # 打包並 gzip 壓縮
tar -cjvf archive.tar.bz2 folder/   # 打包並 bzip2 壓縮

# tar 解壓縮
tar -xvf archive.tar                # 解包
tar -xzvf archive.tar.gz            # 解 gzip 壓縮包
tar -xvf archive.tar.gz -C /目標路徑/  # 解壓到指定目錄

# zip / unzip
zip -r archive.zip folder/
unzip archive.zip
unzip archive.zip -d /目標路徑/
```

---

## 5. 網路相關

```bash
# 查看 IP 位址
ip addr show
hostname -I

# 測試連線
ping google.com
ping -c 4 google.com        # 只 ping 4 次

# 查看開放的連接埠
ss -tuln
netstat -tuln               # 需安裝 net-tools

# 下載檔案
wget https://example.com/file.zip
curl -O https://example.com/file.zip
curl -o myfile.zip https://example.com/file.zip

# 傳送 HTTP 請求（測試 API）
curl https://api.example.com/data
curl -X POST -H "Content-Type: application/json" \
     -d '{"key":"value"}' \
     https://api.example.com/endpoint
```

---

## 6. 套件管理（apt）

```bash
# 更新套件列表
sudo apt update

# 升級所有已安裝套件
sudo apt upgrade
sudo apt full-upgrade           # 含依賴關係升級

# 安裝套件
sudo apt install git
sudo apt install git curl wget  # 一次安裝多個

# 移除套件
sudo apt remove package-name
sudo apt autoremove             # 移除不需要的依賴

# 搜尋套件
apt search keyword
apt show package-name           # 查看套件詳細資訊

# 列出已安裝套件
apt list --installed
dpkg -l | grep package-name
```

---

## 7. WSL 與 Windows 互通

### 存取 Windows 檔案

```bash
# Windows 磁碟機掛載在 /mnt/
ls /mnt/c/                      # C 槽
ls /mnt/d/Users/YourName/       # D 槽使用者目錄

# 切換到 Windows 桌面
cd /mnt/c/Users/YourName/Desktop

# 複製 Windows 檔案到 Linux 家目錄
cp /mnt/c/Users/YourName/file.txt ~/
```

### 在 WSL 中執行 Windows 程式

```bash
# 用 Windows 記事本開啟檔案
notepad.exe file.txt

# 用 Windows 檔案總管開啟當前目錄（注意有個點）
explorer.exe .

# 執行任意 Windows 執行檔
/mnt/c/Program\ Files/app/app.exe

# 開啟 VS Code（需安裝 WSL 擴充套件）
code .
```

### 在 PowerShell 中執行 Linux 指令

```powershell
# 執行單一指令
wsl ls -la

# 執行指令並取得輸出
wsl cat /etc/os-release

# 透過管線傳遞（Windows → Linux）
Get-Content file.txt | wsl grep "keyword"
```

### 環境變數互通

```bash
# 在 WSL 中存取 Windows 環境變數
echo $USERPROFILE           # 通常是 /mnt/c/Users/YourName
echo $PATH                  # 包含 Windows PATH

# 將 WSL 路徑轉換為 Windows 路徑
wslpath -w /home/user/file.txt
# 輸出：\\wsl$\Ubuntu\home\user\file.txt

# 將 Windows 路徑轉換為 WSL 路徑
wslpath "C:\\Users\\YourName\\file.txt"
# 輸出：/mnt/c/Users/YourName/file.txt
```

---

## 8. 程序管理

```bash
# 查看執行中的程序
ps aux                          # 所有程序
ps aux | grep python            # 篩選特定程序
top                             # 即時監控（q 離開）
htop                            # 進階版（需安裝：sudo apt install htop）

# 結束程序
kill PID                        # 送出 SIGTERM（正常結束）
kill -9 PID                     # 送出 SIGKILL（強制結束）
pkill process-name              # 依名稱結束程序
killall process-name            # 結束所有同名程序

# 背景執行
command &                       # 背景執行
nohup command &                 # 關閉終端後繼續執行
jobs                            # 查看背景工作
fg %1                           # 將背景工作帶回前景
bg %1                           # 繼續在背景執行
```

---

## 9. 實用技巧與進階設定

### Shell 快捷鍵

| 快捷鍵 | 功能 |
|--------|------|
| `Ctrl + C` | 中斷目前指令 |
| `Ctrl + Z` | 暫停目前程序（可用 fg 恢復） |
| `Ctrl + D` | 離開目前 Shell |
| `Ctrl + L` | 清除螢幕（同 clear） |
| `Ctrl + A` | 移到行首 |
| `Ctrl + E` | 移到行尾 |
| `Ctrl + R` | 搜尋指令歷史 |
| `↑ / ↓` | 瀏覽指令歷史 |
| `Tab` | 自動補全指令或路徑 |

### .bashrc 常用設定

```bash
# 編輯 .bashrc
nano ~/.bashrc

# 常用別名範例（加入 .bashrc）
alias ll='ls -la'
alias gs='git status'
alias update='sudo apt update && sudo apt upgrade -y'
alias myip='hostname -I'

# 自訂 PATH
export PATH="$HOME/.local/bin:$PATH"

# 套用修改
source ~/.bashrc
```

### wsl.conf 設定（Linux 側）

```bash
# 建立或編輯 /etc/wsl.conf
sudo nano /etc/wsl.conf
```

```ini
[boot]
systemd=true          # 啟用 systemd（WSL 2 支援）

[automount]
enabled = true
root = /mnt/
options = "metadata,umask=22,fmask=11"

[network]
hostname = my-wsl      # 自訂主機名稱
generateHosts = true

[interop]
enabled = true
appendWindowsPath = true    # 是否將 Windows PATH 加入 WSL PATH
```

### .wslconfig 設定（Windows 側）

在 `C:\Users\YourName\.wslconfig` 建立此檔案：

```ini
[wsl2]
memory=4GB            # 限制記憶體用量
processors=2          # 限制 CPU 核心數
swap=2GB              # 虛擬記憶體大小
localhostForwarding=true
```

### 備份與還原 WSL 發行版

```powershell
# 匯出（備份）
wsl --export Ubuntu backup-ubuntu.tar

# 匯入（還原）版本名稱 目的地路徑    備份還原檔路徑及檔名
wsl --import Ubuntu C:\WSL\Ubuntu backup-ubuntu.tar --version 2

# 登錄並刪除發行版（危險！）
wsl --unregister Ubuntu
```

---

## 10. 常見問題排除

### WSL 無法啟動

```powershell
# 重設 WSL 網路
wsl --shutdown
netsh winsock reset

# 重新安裝 WSL 核心元件
wsl --update
```

### 忘記 Linux 密碼

```powershell
# 以 root 登入
wsl -u root

# 重設密碼
passwd your-username
```

### 檔案權限問題（Windows 掛載的檔案）

```bash
# 在 /etc/wsl.conf 加入 metadata 選項
sudo nano /etc/wsl.conf
```

```ini
[automount]
options = "metadata"
```

### 提升效能：將專案放在 Linux 檔案系統

```bash
# ✅ 建議：在 Linux 家目錄工作
cd ~/projects
git clone https://github.com/example/repo.git

# ❌ 避免：在 /mnt/c/ 下操作（速度較慢）
```

---

## 快速參考卡

```
安裝/管理   wsl --install / --list / --shutdown / --export
目錄操作    cd / ls / mkdir / rm / cp / mv
檔案查看    cat / less / head / tail / grep / find
權限        chmod / chown
套件        sudo apt update && apt install
網路        ping / curl / wget / ss
程序        ps / top / kill / jobs
互通        explorer.exe . / code . / wslpath
```

---

*最後更新：2026 年 3 月 | 適用 WSL 2 + Ubuntu 22.04*
