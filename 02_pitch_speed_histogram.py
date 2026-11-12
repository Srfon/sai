"""球種ごとの球速分布（ヒストグラム）"""
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv('2022_Ohtani.csv')
df['speed_km'] = df['release_speed'] * 1.61

Fastball = df[df['pitch_type'] == 'FF']
Cutter = df[df['pitch_type'] == 'FC']
Sweeper = df[df['pitch_type'] == 'ST']
Curve = df[df['pitch_type'] == 'CU']
Splitter = df[df['pitch_type'] == 'FS']

border = [110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165]
plt.hist(Fastball['speed_km'], alpha=0.7, hatch='/', label='Fastball', bins=border)
plt.hist(Cutter['speed_km'], alpha=0.7, hatch='o', label='Cutter', bins=border)
plt.hist(Sweeper['speed_km'], alpha=0.7, hatch='.', label='Sweeper', bins=border)
plt.hist(Curve['speed_km'], alpha=0.7, hatch='-', label='Curve', bins=border)
plt.hist(Splitter['speed_km'], alpha=0.7, hatch='*', label='Splitter', bins=border)

plt.title('球種ごとの球速分布')
plt.xlabel('球速（km/h）')
plt.ylabel('投球数')
plt.legend(loc='upper left')
plt.show()
