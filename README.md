# 大谷翔平2022年投球データ：プリントのグラフ

4枚の写真を**送信順**に読み、ページをまたぐコードをつないだ独立したPythonスクリプトです。

| ファイル | 写真の位置 | グラフ |
|---|---|---|
| `01_inning_mean_speed.py` | 1枚目上部（前のページから続く） | イニングごとのストレート平均球速 |
| `02_pitch_speed_histogram.py` | 1枚目下部 | 球種ごとの球速分布 |
| `03_fastball_location_scatter.py` | 2枚目前半 | ストレートの投球位置 |
| `04_swinging_vs_called_strikes.py` | 2枚目後半（3) で 2) を書き直す） | 空振りと見逃しストライクの投球位置 |
| `05_fastball_heatmap.py` | 3枚目 → 4枚目冒頭 | ストレートのコース別投球割合 |
| `06_heatmap_by_batter_stand.py` | 4枚目後半 | 対右打者・対左打者のヒートマップ |

## 実行方法

1. リポジトリをダウンロードまたはクローンします。
2. **実際の `2022_Ohtani.csv` をPythonファイルと同じフォルダーに配置**します。このCSVはリポジトリには含まれていません。
3. ターミナルで下記を実行します。

```bash
python -m pip install -r requirements.txt
python 03_fastball_location_scatter.py
python 04_swinging_vs_called_strikes.py
python 05_fastball_heatmap.py
python 06_heatmap_by_batter_stand.py
```

プリントの `! pip install` はNotebook用なので、Pythonファイルにはそのまま書かず、上記のpipコマンドでインストールします。

## 写真から追加した最低限の修正

- **03・04**: 2枚目の写真には `plate_x_cm` と `plate_z_cm` を作る行がないため、列がない場合だけ3枚目の `plate_x * 30.48`, `plate_z * 30.48` を追加します（`KeyError`対策）。
- **04**: 写真の「3)」は「2)」の散布図を**書き直す**指示なので、色分けした散布図のみを作ります。
- **05**: 写真3枚目の `ratio` 計算から写真4枚目上部の `plt.imshow(ratio, ...)` までを結合しました。
- **06**: 4枚目の「変わらない部分は省略」は、3枚目の3×3コース判定のロジックを補いました。
- **05・06**: 座標欠損（NaN）の行を飛ばし、該当球が0球でも0除算しないようにしました。コース境界・計算方法・グラフ設定は元のプリントに準じます。
- **全ファイル**: `japanize_matplotlib` がなくてもグラフ処理自体は動きますが、日本語を表示するには `pip install japanize-matplotlib` が必要です。

データの列: `inning`, `pitch_type`, `release_speed`, `plate_x`, `plate_z`, `description`, `stand`

**検証**: 架空のテストCSVで6種類とも実行成功、欠損値・集計対象0件も確認済み。実際のCSVは提供されていないため未検証です。
