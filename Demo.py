import pandas as pd

# Yahoo 股票網頁需設定網頁編碼為 big-5 避免亂碼
df = pd.read_html('https://jdata.yuanta.com.tw/z/zc/zch/zch_2885.djhtm', encoding='big-5')

# 由於該網頁有多個 table 故會回傳含多個結果的 list，經過觀察發現 index 3 為我們希望的股利資訊
df = pd.DataFrame(df[2])
df.to_csv('revenue.csv',encoding='utf_8_sig',index=False,header=False)

print(df)