# 【写真3枚目 → 4枚目の冒頭】投球の到達位置を表すヒートマップ-1
import pandas as pd
import matplotlib.pyplot as plt
try:
    import japanize_matplotlib
except ImportError:
    print('日本語表示には python -m pip install japanize-matplotlib を実行してください。')

# 1) データの取り込み
df = pd.read_csv('2022_Ohtani.csv')
df['plate_x_cm'] = df['plate_x'] * 30.48
df['plate_z_cm'] = df['plate_z'] * 30.48
df

Fastball = df[df['pitch_type'] == 'FF']
Fastball

# 2) コース別のストレート投球割合を算出・ヒートマップ表示
location = [[0,0,0],[0,0,0],[0,0,0]]
total = 0

for height,side in zip(Fastball['plate_z_cm'],Fastball['plate_x_cm']):
    # 写真にない補足: 座標が欠損している投球は集計しない。
    if pd.isna(height) or pd.isna(side):
        continue
    if height < 50 or 110 < height:
        continue
    if side < -30 or 30 < side:
        continue
    if 90 < height <= 110:
        h = 0
    elif 70 <= height <= 90:
        h = 1
    elif 50 <= height < 70:
        h = 2
    if -30 <= side < -10:
        s = 0
    elif -10 <= side <= 10:
        s = 1
    elif 10 < side <= 30:
        s = 2
    location[h][s] += 1
    total += 1
location

ratio = []
for lst in location:
    # 写真にない補足: 対象が0球なら0で割らない。
    add = [num/total for num in lst] if total else [0,0,0]
    ratio.append(add)
ratio

# ここから写真4枚目の冒頭につながる。
plt.figure(figsize=(8,8))
plt.imshow(ratio, cmap='OrRd')

plt.colorbar()
plt.clim(0,0.2)
plt.title('ストレートのコース別投球割合')
plt.xticks([0,1,2],['三塁側','真ん中','一塁側'])
plt.yticks([0,1,2],['高め','真ん中','低め'])
plt.show()
