# 【写真2枚目】空振り・見逃しストライクを色分けした散布図
# 2枚目「3）」は「2）」の散布図を置き換える続きなので、必要な部分を統合している。
import pandas as pd
import matplotlib.pyplot as plt
try:
    import japanize_matplotlib
except ImportError:
    print('日本語表示には python -m pip install japanize-matplotlib を実行してください。')

df = pd.read_csv('2022_Ohtani.csv')
df

df['speed_km'] = df['release_speed'] * 1.61
df

# 写真にない補足: CSVが元のStatcast列のみの場合は座標をcmに変換。
if 'plate_x_cm' not in df.columns:
    df['plate_x_cm'] = df['plate_x'] * 30.48
if 'plate_z_cm' not in df.columns:
    df['plate_z_cm'] = df['plate_z'] * 30.48

Fastball = df[df['pitch_type'] == 'FF']
Cutter = df[df['pitch_type'] == 'FC']
Sweeper = df[df['pitch_type'] == 'ST']
Curve = df[df['pitch_type'] == 'CU']
Splitter = df[df['pitch_type'] == 'FS']

# 3) 空振りストライク・見逃しストライクを抽出
Swinging = Fastball[Fastball['description'].isin(['swinging_strike','swinging_strike_blocked'])]
Called = Fastball[Fastball['description'] == 'called_strike']

# 2) の散布図部分を書き直す
plt.figure(figsize=(10,10))
plt.scatter(Swinging['plate_x_cm'],Swinging['plate_z_cm'],color='red',label='空振り')
plt.scatter(Called['plate_x_cm'],Called['plate_z_cm'],color='blue',label='見逃し')

plt.title('ストレートの投球位置（捕手目線）')
plt.xlabel('投球のコース（cm）')
plt.ylabel('投球の高さ（cm）')
plt.xlim(-80,80)
plt.ylim(0,150)
plt.hlines(y=[50,110],xmin=-30,xmax=30,color='black')
plt.vlines(x=[-30,30],ymin=50,ymax=110,color='black')
plt.show()
