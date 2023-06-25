import json
import gzip
import shutil

# 20 JSONデータの読み込み

# 一度に一つのJSONオブジェクトしか処理できない
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
target_json_data = []
with open("./data/jawiki-country.json", "r") as file:
    for line in file:
        article = json.loads(line)
        if "イギリス" in article["title"]:
          target_json_data.append(json.loads(line))

print(target_json_data[0])
# with open('file.txt', 'rb') as f_txt:
#     with gzip.open('file.txt.gz', 'wb') as f_out:
#         shutil.copyfileobj(f_txt, f_out)

