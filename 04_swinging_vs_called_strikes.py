# ! pip install japanize_matplotlib
import japanize_matplotlib
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('2022_Ohtani.csv')
df

df['speed_km']=df['release_speed']*1.61
df
Fastball = df[df['pitch_type']=='FF']
Cutter = df[df['pitch_type']=='FC']
Sweeper = df[df['pitch_type']=='ST']
Curve = df[df['pitch_type']=='CU']
Splitter = df[df['pitch_type']=='FS']

Swinging=Fastball[Fastball['description'].isin(['swinging_strike','swinging_strike_blocked'])]
Called = Fastball[Fastball['description']=='called_strike']

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
