# 想定環境
- Ubuntu
- zsh

# 目的
- 日単位で予定と進捗を管理するためのGUIを提供する
- スケジュールの変更を後から追えるように，Gitでhtmlのdiffを見れるようにする
- 平日だけの予定表を作成する(強い意志...)

![image](https://github.com/user-attachments/assets/5d4487ae-a88a-4381-9552-855ebc7ce5d9)



# 使い方
- 管理した月のhtmlを生成
```zsh
$ python3 generate_calendar.py -y 2025 -m 5
```
年ごとのディレクトリと`西暦の下二桁-月.html`が作成される．
- ブラウザでhtmlを開く
```zsh
google-chrome 2025/25-05.html
```
- 好きなメモを記入する
- 保存する -> 上書き保存のボタンを押印
  - 保存時は本リポジトリの`西暦の下二桁-月.html`を置き換え保存する(htmlのセキュリティ的に，これ以上のやり方が思いつかなかった)
- スケジュールのアップデートをGitで管理する
  - cronで毎日0時にcommitされるようにする．`crontab -e`で下記の設定を追加(本リポジトリの`auto_commit.sh`のパスを指定してください)
  - commit messageはYY-MM-DDにしてある
```zsh
0 0 * * * /path/schedual/auto_commit.sh
```
