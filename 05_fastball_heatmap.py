# ! pip install japanize_matplotlib
import japanize_matplotlib
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('2022_Ohtani.csv')
df['plate_x_cm']=df['plate_x']*30.48
df['plate_z_cm']=df['plate_z']*30.48
df

Fastball =df[df['pitch_type']=='FF']
Fastball

location = [[0,0,0],[0,0,0],[0,0,0]]
total=0

for height,side in zip(Fastball['plate_z_cm'],Fastball['plate_x_cm']):
    if height<50 or 110<height:
        continue
    if side<-30 or 30<side:
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

ratio =[]
for lst in location:
    add = [num/total for num in lst]
    ratio.append(add)
ratio

plt.figure(figsize=(8,8))
plt.imshow(ratio, cmap='OrRd')

plt.colorbar()
plt.clim(0,0.2)
plt.title('ストレートのコース別投球割合')
plt.xticks([0,1,2],['三塁側','真ん中','一塁側'])
plt.yticks([0,1,2],['高め','真ん中','低め'])
plt.show()
