"""イニングごとのストレート平均球速（折れ線グラフ）"""
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# CSVを読み込む（球速はmphからkm/hへ変換）
df = pd.read_csv('2022_Ohtani.csv')
df['speed_km'] = df['release_speed'] * 1.61
Fastball = df[df['pitch_type'] == 'FF']

x = []
y = []
for i in sorted(Fastball['inning'].dropna().unique()):
    inning = Fastball[Fastball['inning'] == i]
    x.append(i)
    y.append(inning['speed_km'].mean())

plt.plot(x, y, marker='o')
plt.title('イニングごとのストレート平均球速')
plt.xlabel('イニング（回）')
plt.ylabel('ストレート平均球速（km/h）')
plt.xticks(x)
plt.show()
