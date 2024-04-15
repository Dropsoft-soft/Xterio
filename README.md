# Xterio 

## 🔗 Links
[![Telegram channel](https://img.shields.io/endpoint?url=https://runkit.io/damiankrawczyk/telegram-badge/branches/master?url=https://t.me/drop_software)](https://t.me/drop_software)

🔔 CHANNEL: https://t.me/drop_software

💰 DONATION EVM ADDRESS: 0x9dBA8Ba2E1F00442b53775FCe236818BC73b1D48

## 🤖 Features :

🟢 Support for mobile and regular proxies

🟢 Infinite loop (you can specify how often the script is run)

🟢 Referral code

🟢 Register new accounts

🟢 Daily quests

🟢 Bridge from BNB to Xterio

🟢 Eggs and Utility Clues

🟢 Voting

## 🚀 Installation
```
git clone https://github.com/Dropsoft-soft/Xterio.git

cd Xterio

pip install -r requirements.txt

# Before you start, configure the required modules in config.ini and /data files

python main.py
```

### Config

`referral_code` = referral code

`attempts` = maximum number of attempts to complete the task

`LAUNCH_TIME` = how often to run the script in hours

`mobile_proxy` = mobile proxies (yes or no)

`change_ip_pause` = pause after changing the IP of mobile proxies


### Data
The data is in the data folder:

`accounts.txt`          Contains accounts (private key or mnemo phrase)

`proxies.txt`           Contains proxies in the format user:pass@ip:port

`ip_change_links.txt`   Contains links to change mobile proxy IPs

