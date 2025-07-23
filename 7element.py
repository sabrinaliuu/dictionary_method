import pandas as pd
rows = pd.read_csv("./news_split_example.csv")

seven = ['すまい', 'つながり', 'まち', 'こころとからだ','そなえ', '行政とのかかわり', 'くらしむき']
for col in seven:
    rows[col] = 0

keywords = {"1": ["仮設住宅", "半壊", "全壊","住宅被害", "家屋","住まい","再建","住宅","住民","建物", "家は","家で"],
            "2": ["祭り", "まつり", "協力", "ボランティア", "絆","祈願","祈り"],
            "3": ["土砂崩落", "人口", "開通","解体","朝市","交通","インフラ","鉄道"],
            "4": ["不安", "沈む", "絶望", "痛む", "希望", "元気","寂しい","悲しい","うれしい"],
            "5": ["防災","整備","備え"],
            "6": ["アンケート", "公的支援", "政府", "公費","支援","取り組み","行政","予算"],
            "7": ["仮設商店","寄付", "義援金", "奨学金", "輪島塗", "ツアー", "輪島朝市", "住宅ローン", "再開","支援"]} # you can define your own dictionary


for i in range(len(rows)):
    for k in range(1,8):
        keyword = keywords[str(k)] 
        label = any(word in rows.loc[i, 'sentence'] for word in keyword)
        flag = 1 if label == True else 0
        rows.loc[i,seven[k-1]] = flag


print(rows.head())
