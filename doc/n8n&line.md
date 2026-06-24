以下為您完整整理在 Render 部署 n8n 以及 建立 LINE Bot + Google 試算表儲存 所需的終極完整步驟指南。
------------------------------
## 🌐 第一階段：Render 雲端部署 n8n (512MB RAM 生存配置)## 1. 建立 Web Service

* 前往 [Render Dashboard](https://dashboard.render.com/)，點擊 New + ➡️ Web Service。
* 選擇 Deploy an existing image。
* Image URL 填入官方鏡像：docker.io/n8nio/n8n:latest
* Instance Type 選擇 Free（完全免費）。

## 2. 複製公網網址 (重要)

* 建立專案後，在 Render 控制台左上角複製分配給您的專屬網址。
* 格式範例：https://onrender.com

## 3. 設定 10 組防爆環境變數 (Environment Variables)
進入專案的 Environment 頁面，務必全數補齊以下 10 組金牌防爆設定，否則 512MB 記憶體會直接卡死崩溃：

| Key (名稱) | Value (數值) | 作用說明 |
|---|---|---|
| DB_PING_TIMEOUT_SECONDS | 30 | 延後資料庫超時，防止 SQLite 初始化卡死 |
| DB_PING_INTERVAL_SECONDS | 10 | 降低檢查頻率，減輕免費硬碟 I/O 負擔 |
| N8N_DISABLE_TASK_RUNNERS | true | 關閉新版運行器，徹底解決 5679 連線報錯 |
| N8N_BLOCK_ENV_ACCESS_IN_NODE | true | 禁用運行器後的安全性輔助補強 |
| N8N_FEATURE_FLAG_MCP | false | 關閉官方 AI MCP 聯網，避免 6000ms 超時 |
| N8N_NATIVE_PYTHON_RUNNER | false | 關閉 Python 模組，避免缺少環境引發的崩潰 |
| NODE_OPTIONS | --max-old-space-size=300 | 嚴格限制 Node.js 記憶體在 300MB 以內 |
| N8N_DEFAULT_BINARY_DATA_MODE | filesystem | 強制資料寫入硬碟暫存，釋放寶貴的 RAM |
| N8N_ENCRYPTION_KEY | （自訂英文亂碼） | n8n 憑證加密金鑰（必填） |
| WEBHOOK_URL | https://onrender.com | 您剛剛複製的 Render 正式網址（結尾一定要加 /） |


* 設定完成後點擊 Save Changes，Render 會自動重啟，直到左上角亮起 🟢 Live 燈號即可用新分頁開啟 n8n。

------------------------------
## 🔑 第二階段：LINE Developers 後台與憑證設定## 1. 取得 LINE 兩把鑰匙

* 登入 [LINE Developers 控制台](https://developers.line.biz/)。
* Channel Secret：在 Basic settings 頁籤中複製。
* Channel Access Token：在 Messaging API 頁籤最下方點擊 Issue 發行並完整複製。

## 2. 在 n8n 控制台建立 LINE 憑證

* 進入 n8n ➡️ Credentials ➡️ Add Credential ➡️ 搜尋並選擇 Header Auth。
* Name (Header 名稱)：填入 Authorization
* Value (Header 數值)：填入 Bearer 加上您的 Token (⚠️ 注意：Bearer 後面必須有一個空格)。

------------------------------
## 📊 第三階段：Google 試算表外接設定 (Service Account)## 1. 申請 Google 服務帳戶金鑰

* 前往 [Google Cloud Console](https://console.cloud.google.com/) 建立免費專案，並在 API 庫中啟用 Google Sheets API。
* 在 IAM 和管理 ➡️ 服務帳戶 中建立一個服務帳戶，並進入該帳戶的「管理金鑰」下載 JSON 格式金鑰檔案。
* 複製該帳戶長的像 Email 的地址（如 n8n-bot@://gserviceaccount.com）。

## 2. 打開試算表權限

* 新建一個 Google 試算表（第一列寫好標頭：時間、使用者ID、訊息內容）。
* 點擊右上角 「共用」，將剛剛複製的服務帳戶 Email 加進來，並設定權限為 「編輯者」。

## 3. 在 n8n 綁定 Google 憑證

* 進入 n8n ➡️ Credentials ➡️ Add Credential ➡️ 選擇 Google Sheets Service Account。
* 將下載的 .json 檔案文字全部複製，完整貼進 Service Account Key 大框框中並儲存。
* 或是手動輸入：
Service Account Email：申請的服務帳戶 Email
Private Key：.json 檔案的Private Key但不含引號

------------------------------
## 🚀 第四階段：n8n 畫布工作流設定與正式上線## 1. 關鍵字分流與回覆 (HTTP Request)

* Webhook 節點：Method 設為 POST，Path 設為 line-webhook。
* Switch 節點：檢查字串，條件左側變數路徑一律使用帶有陣列的格式：
* 文字內容路徑：{{ $json.body.events.message.text }}
* HTTP Request 節點 (Reply)：Authentication 選擇建好的 Header Auth 憑證，Method 為 POST，URL 填入 https://line.me。
* JSON Body 正確格式（一字不能錯）：
   
{
  "replyToken": "{{ $json.body.events[0].replyToken }}",
  "messages": 
  [
    {
      "type": "text",
      "text": "回覆內容"
    }
  ]
}

   
   
## 2. 儲存至 Google 試算表 (具名導向語法)
為了防止分流導致資料迷路，在 Google Sheets 節點（Operation 設為 Append Row）的 Map Each Column Below 區塊中，必須使用「強制具名導向」語法隔空抓取最左邊 Webhook 的資料：

* 時間 欄位：{{ $now.setZone('Asia/Taipei').format('yyyy-MM-dd HH:mm:ss') }}

* 使用者ID 欄位：{{ $('Webhook 節點的真實名稱').item.json.body.events[0].source.userId }}

* LINE訊息 欄位：{{ $('Webhook 節點的真實名稱').item.json.body.events[0].message.text }}

* （💡 註：節點真實名稱可點開 Webhook 節點看左上角確認，例如 Webhook 或 Webhook (LINE)）

## 3. 正式對接與保持清醒

* 點開 n8n 的 Webhook 節點，切換到 Production URL 標籤頁，複製那串正式網址。
* 貼回 LINE Developers 後台的 Webhook URL 中，開啟 Use webhook 開關，並點擊 Verify 通過驗證。
* 啟用工作流：點擊 n8n 右上角開關，切換成綠色的 Active。
* 防止已讀不回：前往 UptimeRobot 設定一個免費的 HTTP 監控，每 10 分鐘對您的 Render 網址（不含 webhook 的根網址）發送一次請求，確保免費伺服器 24 小時不進入休眠。



