# MachineLearning_report

流れ
1. scraping.pyにて該当するワードによる画像のスクレイピング

2. 得られた画像たちに対して、get_cut_face.pyにて顔部分だけを切り出す(このとき、https://github.com/nagadomi/lbpcascade_animeface によるcascadeが必要)

3. 顔画像たちを分類したいファイルにひたすら分類(自力)

4. CNN.ipynbに該当するデータセットを学習させる

5. 未知のデータに適用可
