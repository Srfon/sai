# 【写真2枚目】投球の到達位置を表す散布図
# 写真にない補足: plate_x_cm / plate_z_cm が存在しない場合は作成する。
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

if 'plate_x_cm' not in df.columns:
    df['plate_x_cm'] = df['plate_x'] * 30.48
if 'plate_z_cm' not in df.columns:
    df['plate_z_cm'] = df['plate_z'] * 30.48

Fastball = df[df['pitch_type'] == 'FF']
Cutter = df[df['pitch_type'] == 'FC']
Sweeper = df[df['pitch_type'] == 'ST']
Curve = df[df['pitch_type'] == 'CU']
Splitter = df[df['pitch_type'] == 'FS']

plt.figure(figsize=(10,10))
plt.scatter(Fastball['plate_x_cm'],Fastball['plate_z_cm'])

plt.title('ストレートの投球位置（捕手目線）')
plt.xlabel('投球のコース（cm）')
plt.ylabel('投球の高さ（cm）')
plt.xlim(-80,80)
plt.ylim(0,150)
plt.hlines(y=[50,110],xmin=-30,xmax=30,color='black')
plt.vlines(x=[-30,30],ymin=50,ymax=110,color='black')
plt.show()
