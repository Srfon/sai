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
