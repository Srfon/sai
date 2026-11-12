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

def create_heatmap(data, title):
    location = [[0,0,0],[0,0,0],[0,0,0]]
    sum = 0

    for height,side in zip(data['plate_z_cm'],data['plate_x_cm']):
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
        sum += 1

    ratio = []
    for lst in location:
        add = []
        for num in lst:
            add.append(num/sum)
        ratio.append(add)

    plt.figure(figsize=(8,8))
    plt.imshow(ratio, cmap='OrRd')

    plt.colorbar()
    plt.clim(0,0.2)
    plt.title(title)
    plt.xticks([0,1,2],['三塁側','真ん中','一塁側'])
    plt.yticks([0,1,2],['高め','真ん中','低め'])
    plt.show()

Fastball_Right = Fastball[Fastball['stand']=='R']
Fastball_Left = Fastball[Fastball['stand']=='L']

create_heatmap(Fastball_Right,'ストレートのコース別投球割合（対右打者）')
create_heatmap(Fastball_Left,'ストレートのコース別投球割合（対左打者）')
