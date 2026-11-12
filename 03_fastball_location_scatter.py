"""ストレートの投球位置を表す散布図"""
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv('2022_Ohtani.csv')
# Statcastのplate_x/plate_zはフィート単位なのでcmに変換
df['plate_x_cm'] = df['plate_x'] * 30.48
df['plate_z_cm'] = df['plate_z'] * 30.48
Fastball = df[df['pitch_type'] == 'FF']

plt.figure(figsize=(10, 10))
plt.scatter(Fastball['plate_x_cm'], Fastball['plate_z_cm'])
plt.title('ストレートの投球位置（捕手目線）')
plt.xlabel('投球のコース（cm）')
plt.ylabel('投球の高さ（cm）')
plt.xlim(-80, 80)
plt.ylim(0, 150)
# プリントのストライクゾーンの目安
plt.hlines(y=[50, 110], xmin=-30, xmax=30, color='black')
plt.vlines(x=[-30, 30], ymin=50, ymax=110, color='black')
plt.show()
