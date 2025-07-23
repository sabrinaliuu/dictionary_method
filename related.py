import pandas as pd
rows = pd.read_csv("./news_split_example.csv")
rows['related'] = 0

keyword = ["能登", "復興"]
    
for i in range(len(rows)):
    label = any(word in rows.loc[i, 'sentence'] for word in keyword)
    flag = 1 if label == True else 0
    rows.loc[i,'related'] = flag

print(rows.head())

