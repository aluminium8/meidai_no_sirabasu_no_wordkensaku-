# meidai_no_sirabasu_no_wordkensaku

名大**工学部・工学研究科**で文字一致検索できるスクリプトです．

※動作の完全な保証はしません，ご了承ください

また，全ページを一度開いて確認するという方法をとっておりますので，
サーバのことを考えて
ある程度のスリープタイムを設けましょう．


動作環境は以下の通り

・chromeがインストールされているPC,

・次のリンクを参考にselenium, chrome driver をインストール https://qiita.com/memakura/items/20a02161fa7e18d8a693


## つかいかた

seleniumが使える環境にて，
検索したいものなどを設定(後述)した状態で
main.pyを起動すると
標準出力にその文字列を含む講義の開講専攻，講義名がでます

(    $ python main.py > test.txt 

(ドル文字以降を実行)などとすることで，出力結果をファイルに出せる
)

## 設定
nendo_select.select_by_visible_text("２０２１年度")
の部分を，自分の入学年度に設定

target_str_num=driver.page_source.count('制御')
の部分に検索対象文字列を入力

daigakuin=driver.find_elements_by_name('k')[1] 
の数字を，工学部なら0, 工学研究科なら1に設定

また，  kamokutachi=driver.find_elements_by_partial_link_text("論")
を設定すると検索対象しぼりこみができます

~~seleniumについて勉強するとよりカスタマイズできるよ！~~
