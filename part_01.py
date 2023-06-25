# 言語処理100本ノック 第１章
# https://nlp100.github.io/ja/ch01.html


# 0: 文字列の逆順
# 文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
targetStr = "stressed"[::-1]
# print(targetStr)
# [(開始位置) : (終わり位置) : (間隔)]
# ex "stressed"[0:4:1] => stres
# ex "stressed"[0:4:2] => re

# 1: パタトクカシーー
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
targetStr = "パタトクカシーー"[0::2]
# print(targetStr)

# 3 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
targetStr = ""
for i_str, j_str in zip("パトカー", "タクシー"):
    targetStr += i_str + j_str
# print(targetStr)

# 4 円周率
# “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
# 文字列を定義
sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# カンマとピリオドを除去
sentence = sentence.replace(",", "").replace(".", "")
# 文字列をスペースで分割して単語のリストを作成
words = sentence.split()
# 各単語の文字数をリストに格納(リスト内包表記)
word_lengths = [len(word) for word in words]
# print(word_lengths)

# 5 元素記号
# “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ.

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".replace(".", "")
sentence_list = sentence.split()
targetDic = {}
countNum = 0
for element in sentence_list:
  countNum = countNum + 1
  if countNum == 1:
    keyStr = element[0:1:1]
    targetDic = {**targetDic, keyStr: countNum }
    continue
  if countNum == 5:
    keyStr = element[0:1:1]
    targetDic = {**targetDic, keyStr: countNum }
    continue
  if countNum == 6:
    keyStr = element[0:1:1]
    targetDic = {**targetDic, keyStr: countNum }
    continue
  keyStr = element[0:2:1]
  targetDic = {**targetDic, keyStr: countNum }
# 模範解答
# 文字列をスペースで分割して単語のリストを作成
words = sentence.split()

# 先頭の1文字を取り出す単語の位置
one_char_positions = [1, 5, 6, 7, 8, 9, 15, 16, 19]

# 単語の位置から文字列への連想配列を作成
word_map = {}
for i, word in enumerate(words, start=1):
    if i in one_char_positions:
        key = word[0]
    else:
        key = word[:2]
    word_map[key] = i


# 06 集合
# “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．

def n_gram(sequence, n):
    return [sequence[i:i+n] for i in range(len(sequence) - n + 1)]

# 文字bi-gramの集合を作成
X = set(n_gram("paraparaparadise", 2))
Y = set(n_gram("paragraph", 2))

# 和集合
union = X | Y
# print("Union:", union)

# 積集合
intersection = X & Y
# print("Intersection:", intersection)

# 差集合
difference = X - Y
# print("Difference:", difference)

# # 'se'がXおよびYに含まれるかどうか
# print("'se' in X:", 'se' in X)
# print("'se' in Y:", 'se' in Y)

# 7 テンプレートによる文生成
# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．
def get_sentence (x, y, z):
  return f"{x}時の{y}は{z}"
# print(get_sentence(12, "気温", 22.4))


