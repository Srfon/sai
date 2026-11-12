# 大谷翔平 2022年投球データ：グラフ作成コード

授業プリントのグラフ6種類を再現する独立したPythonスクリプトです。

## 準備

```bash
python -m pip install pandas matplotlib japanize-matplotlib
```

`2022_Ohtani.csv` をPythonファイルと同じフォルダに置いて実行します。

```bash
python 02_pitch_speed_histogram.py
```

## ファイル

- `01_inning_mean_speed.py` — イニングごとのストレート平均球速
- `02_pitch_speed_histogram.py` — 球種ごとの球速分布
- `03_fastball_location_scatter.py` — ストレートの投球位置
- `04_swinging_vs_called_strikes.py` — 空振り・見逃しストライクの投球位置
- `05_fastball_heatmap.py` — ストレートのコース別投球割合
- `06_heatmap_by_batter_stand.py` — 対右打者・対左打者のコース別投球割合

### 注意

- `2022_Ohtani.csv` はこのリポジトリには含まれていません。データファイルを別途配置してください。
- イニング別グラフはプリントの冒頭が切れているため、データに存在するイニングから作成しています。
- ストライクゾーンはプリント記載の概算（左右±30cm、高さ50～110cm）です。
- ヒートマップの割合の分母は、上記の範囲内に入ったストレートの投球数です。
