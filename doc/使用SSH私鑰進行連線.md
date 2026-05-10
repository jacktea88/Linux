# 如何使用 SSH 私鑰進行 ssh 連線 - HackMD

[https://hackmd.io/@MagicJackTing/BywNwqdTD](https://hackmd.io/@MagicJackTing/BywNwqdTD)


你可以在本機端產生金鑰, 然後將公鑰 (public key) 上傳到 server.

或者也可倒著做, 在 server 產生金鑰, 將私鑰 (private key) 下載下來, 並刪掉 server 上的私鑰.

下面是在本機產生金鑰. 在主機產生金鑰請自行腦補.

### 建立金鑰

先在本機端使用 `ssh-keygen` 指令建立金鑰 (`open-ssh` 套件, win10 裡應該有):

請依照指令提示輸入要建立的金鑰檔名 (`ssh-keygen` 會將金鑰建立在當前目前目錄下. 或直接按 Enter 也行, 檔名及位置則如提示)：

```
Generating public/private rsa key pair.
Enter file in which to save the key (C:\Users\user001/.ssh/id_rsa):
```

輸入**保護私鑰**用的密碼, 直接按 Enter 表示私鑰檔不加密.

```
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
```

完成建立出現的訊息:

```
Your identification has been saved in svr_xxx.
Your public key has been saved in svr_xxx.pub.
The key fingerprint is:
SHA256:3UJS9bgwPVqoIsRajmRUTcL6YOWFmapzJvDDR/JAcow user001@myWin10
The key's randomart image is:
+---[RSA 2048]----+
| o.oo*.   ...    |
|E.+.*.o  . o o   |
| +o=+.  . = = .  |
|.oB*o    = * o   |
|.=oBo . S + o    |
|+ * +. .   .     |
| = o             |
|                 |
|                 |
+----[SHA256]-----+
```

此時會產生二個檔案, 一個公鑰 (`"svr_xxx.pub"`) 另一個是私鑰 (`"svr_xxx"`), 如果輸入的檔名是 `svr_xxx`.

可以使用下列指令一氣呵成: 登入 linux 主機, 並將自己的公鑰上傳到主機上的正確位置上. (請將 `svr_xxx.pub`, `host_name` 以及 `user_name` 改成自己的公鑰檔名, linux 主機名稱 (或者是 ip) 及登入的帳號):

```
cat svr_xxx.pub | ssh user_name@host_name "mkdir ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

第一次設定也可以用 `scp` 指令, (上面的作法用於 `authorized_keys` 裡已經有其他內容了, 使用 `scp` 指令會把原有的內容覆蓋掉了)

`scp svr_xxx.pub user_name@host_name:~/.ssh/authorized_keys`
例如root帳號
`scp svr_xxx.pub root@host_name:~/.ssh/authorized_keys`

#### 在linux主機COPY authorized_keys 
在linux主機使用root帳號來copy其他帳號的/.ssh/authorized_keys到root帳號底下的/.ssh/authorized_keys
先到root的/.ssh目錄
`cp ~jack/.ssh/authorized_keys authorized_keys`


修改遠端 linux 主機 sshd 的設定
確認遠端 linux 主機的 sshd 設定:

##### 注意檔名是sshd_config，有一個'd'
$ sudo vi /etc/ssh/sshd_config

    確認設定檔裡有開啟金鑰認證登入

    PubkeyAuthentication yes

    確認裡面有設定可用的公開金鑰檔名及位置:

    AuthorizedKeysFile  .ssh/authorized_keys

    第一次設定請先略過關閉密碼認證登入, 直接重啟 sshd. 等確定可以用私鑰連線之後再進行.
    如果沒有修改 sshd_config 的設定, 就不需要重啟 sshd.

關閉密碼認證登入

我們甚至也可以設定關閉密碼認證登入, 只允許金鑰認證

PasswordAuthentication no
PubkeyAuthentication yes

上面關閉密碼認證登入的動作請在確認可以用私鑰成功登入主機之後再進行.
重啟 sshd

設定修改完成之後, 重啟 sshd.

    RHEL/CentOS 用戶請用以下指令

    $ sudo sysemctl restart sshd

    Ubuntu 用戶

    $ sudo sysemctl restart ssh

ssh 連線時指定私鑰檔.

此時應該可以不必輸入**密碼**就直接連上主機.

連線測試成功之後, 可修改**家目錄**下的 `.ssh/config` 將使用私鑰的設定加到設定裡.

`.ssh/config` 檔裡面是遠端主機的相關設定, 如: ip 地址, 使用哪一個帳號…等等

- `Host`: 輸入的是我們在 `ssh` 指令輸入的**主機代號** (不一定是主機域名, ip 也可以, 甚至同一部主機我們需要以不同的帳號連進去時, 也可以自己取一個代號)
- `User`: 則指定連線這部主機時用什麼用戶帳號
- `Port`: 指定這部主機的 SSH port 號碼.
- `HostName`: 則是輸入 DNS 域名, 或者直接輸入 ip 地址 (如果沒有 DNS 可以幫你 name 轉 ip 時. 例如: 區域網路 (LAN) 中的主機或者自己肚子裡的 VM).
- `IdentityFile`: 指定私鑰檔 (private key) 的位置和檔案名稱.

設定二組**代號**是方便我們用主機名字 (host_name) 或 ip address (192.168.33.10) 都可以自動使用私鑰

使用 `putty` 或者其他軟體 `mobaXterm` 都有類似的設定, 請自行類推.

### Windows系統設定
#### 設定檔路徑
C:\Users\USER\.ssh\config
#### 設定內容
Host vm-linux24-root
  HostName 192.168.85.128
  User root
  IdentityFile ~/.ssh/id_rsa