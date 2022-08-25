# HowtoUseJanomeUsingMultiprocessing


# 並列処理で[Janome](https://mocobeta.github.io/janome/)ライブラリを高速化する書き方.

```Shell
python paraJa.py < text.txt  > result.txt
```


- 例えば1行140文字のテキストが100万行あるようなデータがあり、CPUコアが16個使えるような場合、このような並列処理を行うとスループットが良くなる。


- 並列処理にはオーバーヘッドが伴うので、入力データが小さく、かつ並列数が大きい場合はスループットが悪い。


Hironobu Suzuki <suzuki.hironobu@gmail.com>
