# spotify-loginer

利用 Python 和 GithubAction 自动化定时登录 Spotify，解决14天使用限制.

## 环境要求

- Python3+
- Windows10+
- Chrome

## 本地运行

1. 安装 Chrome 及 ChromeDriver 
```powershell
choco install googlechrome -y
choco install chromedriver -y
```

2. 安装 Python3
```powershell
choco install python3 -y
```

3. 安装依赖
```powershell
python -m pip install --upgrade pip
pip install selenium argparse

```
4. 运行
```powershell
python login.py -e <email> -p <password>
```

命令行参数说明：
```bash
  -h, --help            show this help message and exit
  -e EMAIL, -u EMAIL, --email EMAIL
                        Spotify account email
  -p PASSWORD, --password PASSWORD
                        Spotify account password
```

## GithubAction 部署

1. Fork 本仓库
2. 在仓库的 Settings -> Secrets 中添加以下 Secrets:
   - `SPOTIFY_USERNAME`: Spotify 账号邮箱
   - `SPOTIFY_PASSWORD`: Spotify 账号密码
3. 在仓库的 Actions 中启用 GithubAction, 选中 `Run Spotify Loginer`，点击 `Run workflow` 手动运行一次
4. Enjoy it!

