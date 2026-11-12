"""空振りストライクと見逃しストライクを色分けした散布図"""
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv('2022_Ohtani.csv')
df['plate_x_cm'] = df['plate_x'] * 30.48
df['plate_z_cm'] = df['plate_z'] * 30.48
Fastball = df[df['pitch_type'] == 'FF']

Swinging = Fastball[Fastball['description'].isin([
    'swinging_strike', 'swinging_strike_blocked'
])]
Called = Fastball[Fastball['description'] == 'called_strike']

plt.figure(figsize=(10, 10))
plt.scatter(Swinging['plate_x_cm'], Swinging['plate_z_cm'], color='red', label='空振り')
plt.scatter(Called['plate_x_cm'], Called['plate_z_cm'], color='blue', label='見逃し')
plt.title('ストレートの投球位置（捕手目線）')
plt.xlabel('投球のコース（cm）')
plt.ylabel('投球の高さ（cm）')
plt.xlim(-80, 80)
plt.ylim(0, 150)
plt.hlines(y=[50, 110], xmin=-30, xmax=30, color='black')
plt.vlines(x=[-30, 30], ymin=50, ymax=110, color='black')
plt.legend()
plt.show()
