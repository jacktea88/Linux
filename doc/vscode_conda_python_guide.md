# VS Code + Conda + Python 開發環境完整教學

## 一、安裝必要工具
1. 安裝 Anaconda 或 Miniconda  
2. 安裝 VS Code  
3. 安裝 VS Code 擴充套件：
   - Python (Microsoft)

---

## 二、初始化 Conda

開啟終端機輸入：

```
conda init
```

重新啟動 VS Code

---

## 三、建立 Conda 環境

```
conda create -n myenv python=3.10
```

啟動環境：

```
conda activate myenv
```

---

## 四、VS Code 綁定 Python 環境

1. 按 Ctrl + Shift + P  
2. 輸入：Python: Select Interpreter  
3. 選擇 myenv  

---

## 五、終端機自動啟動環境

建立 `.vscode/settings.json`

```
{
  "python.defaultInterpreterPath": "C:\\Users\\你的帳號\\anaconda3\\envs\\myenv\\python.exe"
}
```
default env: base
```
{
  "python.defaultInterpreterPath": "C:\\Users\\你的帳號\\anaconda3\\envs\\base\\python.exe"
}
```


### 終端機選擇
python.terminal.activateEnvironment

### PS設定檔
C:\Users\USER\anaconda3\shell\condabin\conda-hook.ps1

---

## 六、常見問題

### 1. conda 無法使用
```
conda init
```

### 2. PowerShell 問題
```
conda init powershell
```

### 3. 找不到環境
```
conda info --envs
```

---

## 七、驗證環境

```
python --version
which python   # Linux/Mac
where python   # Windows
```

---

## 八、開發建議

- 一個專案一個 env  
- 不要用 base 做開發  
- 使用 requirements.txt 或 environment.yml 管理套件  

---

## 九、進階：匯出環境

```
conda env export > environment.yml
```

還原：

```
conda env create -f environment.yml
```

---


