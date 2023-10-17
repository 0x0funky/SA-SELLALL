# SA-sellall
 一鍵賣出全部SA KEYS

## 需求

```python 3.10```

## 安裝必要Package
```
pip install web3==5.23.0
```
## 事前設置 (config.ini)
請事先至SA網站設置找到以下資訊並先設定好
```
[DEFAULT]
PRIVATE_KEY = your_private_key_here
BEARER_KEY = your_bearer_key_here
CONTRACT_ADDRESS = 0x563395A2a04a7aE0421d34d62ae67623cAF67D03
REFERRER_ADDRESS = 0xC4E60DeA79C45340a850Fa7E0cCa37C73dB86Fa3
```
* REFERRER是邀請碼地址, 目前Default是設定我的, 當作我做這個腳本的Donate
如果你不願意你可以改成自己的 (等於反傭給自己)
* CONTRACT_ADDRESS目前是看SA審計新的Contract設定的, 最後可能不是這個合約
請關注官方或是等人公布

## PRIVATE_KEY怎麼找?
到 "https://starsarena.com/wallet" 按 "Export Private Key"
![How to find Bearer Key](images/private_keys.png)

## Bearer_Key怎麼找?
到 "https://starsarena.com/shares" 按F12, 選擇Network, 然後重新整理, 找到下面這張圖的地方, 複製Bearer Key到程式碼中
![How to find Bearer Key](images/Bearer_keys.png)

## CONTRACT_ADDRESS怎麼找?
只能等官方公布或是有人提供了 (我會在我的FT ROOM隨時告知)

Produce by 0xFunky
FT: https://friend.tech/0x0funky