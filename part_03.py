import json
import gzip
import shutil
import re

# 20 JSONデータの読み込み

# 一度に一つのJSONオブジェクトしか処理できない
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
target_json_data = []
target_json_category = []
# with open("./data/jawiki-country.json", "r") as file:
#     for line in file:
#         article = json.loads(line)
#         if "イギリス" in article["Category"]:
#           target_json_data.append(json.loads(line))

# print(target_json_data[0])
# with open('file.txt', 'rb') as f_txt:
#     with gzip.open('file.txt.gz', 'wb') as f_out:
#         shutil.copyfileobj(f_txt, f_out)

# 21 カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．
target_json_data = []
pattern = r"\[\[Category:.*?\]\]"
with open("./data/jawiki-country.json", "r") as file:
    for line in file:
        category_line = re.findall(pattern,line)
        target_json_data.append(category_line)
# print(target_json_data[0])

# 22 カテゴリ名を抽出
# 記事中でカテゴリ名を抽出せよ．
target_json_data = []
pattern = r"\[\[Category:(.*?)(?:\|.*)?\]\]"
with open("./data/jawiki-country.json", "r") as file:
    for line in file:
        is_match = re.search(pattern, line)
        if is_match:
          category_name = is_match.group(1)
          target_json_data.append(category_name)
# print(target_json_data)

# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．
target_json_data = []
# pattern = r"\[\[Category:(.*?)(?:\|.*)?\]\]"
pattern = r"(==+)(.*?)(==+)"
with open("./data/jawiki-country.json", "r") as file:
    for line in file:
        matches = re.findall(pattern, line)
        for match in matches:
          section_name = match[1].strip()
          section_level = len(match[0]) - 1
          target_json_data.append(f"Section Name: {section_name}, Level: {section_level}")

# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．
target_json_data = []
# pattern = r"\[\[Category:(.*?)(?:\|.*)?\]\]"
pattern = r"\[\[(File|ファイル):(.*?)\]\]"
with open("./data/jawiki-country.json", "r") as file:
    for line in file:
        matches = re.findall(pattern, line)
        for match in matches:
          section_name = match[1].strip()
          target_json_data.append(section_name)

# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
target_json_data = []
pattern = re.compile(r"\{\{基礎情報 国\n(.*?)\n\}\}", re.DOTALL)
pattern_for_field = re.compile(r"^\|(\s*.*?\s*)=(\s*.*?\s*)$", re.MULTILINE)

with open("./data/jawiki-country.json", "r") as file:
    for line in file:
        data = json.loads(line)
        if 'text' in data.keys():
            text = data['text']
            match = re.search(pattern, text)
            if match:
                template = match.group(1)
                fields = re.findall(pattern_for_field,template)
                info = {field.strip(): value.strip() for field, value in fields}
                print(info)
