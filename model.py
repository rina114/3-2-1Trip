from gensim.models import word2vec
import csv
import pandas as pd
import re

# CSVファイル読み込み
csv_input = pd.read_csv(filepath_or_buffer="scrape_data.csv", encoding="ms932", sep=",")
url_csv_input = pd.read_csv(filepath_or_buffer="url_data.csv", encoding="ms932", sep=",")

# モデルのロード
model = word2vec.Word2Vec.load("word2vec_model.model")

def word_get(word_1, word_2, word_3, num, point, popularity):
  # 受け取った3つの単語を足しあわせて1つの単語にする
  if word_1 in model.wv and word_2 in model.wv and word_3 in model.wv:
    s_word = model.wv.most_similar(positive=[word_1, word_2, word_3])
  else:
    s_word = model.predict_output_word([word_1, word_2, word_3],topn=1)

  spot_id = 0
  max_cnt = 0

  for i in range(951):
    # (num, point, popularity) = (0, 0, 0)のとき
    if num == 0 and point == 0 and popularity == 0:
      if int(csv_input.loc[i, "good_cnt"]) > 400:
        if int(csv_input.loc[i,"review"].count('家族')) + int(csv_input.loc[i,"review"].count('友達')) + int(csv_input.loc[i,"review"].count('グループ')) < 3:
          if int(csv_input.loc[i,"review"].count('景色')) + int(csv_input.loc[i,"review"].count('絶景')) + int(csv_input.loc[i,"review"].count('きれい')) + int(csv_input.loc[i,"review"].count('綺麗')) >= 10:
            word_cnt = csv_input.loc[i,"review"].count(s_word[0][0])
            if word_cnt > max_cnt:
              max_cnt = word_cnt
              spot_id = i

    # (num, point, popularity) = (0, 0, 1)のとき
    if num == 0 and point == 0 and popularity == 1:
      if int(csv_input.loc[i, "good_cnt"]) <= 400:
        if int(csv_input.loc[i,"review"].count('家族')) + int(csv_input.loc[i,"review"].count('友達')) + int(csv_input.loc[i,"review"].count('グループ')) < 3:
          if int(csv_input.loc[i,"review"].count('景色')) + int(csv_input.loc[i,"review"].count('絶景')) + int(csv_input.loc[i,"review"].count('きれい')) + int(csv_input.loc[i,"review"].count('綺麗')) >= 10:
            word_cnt = csv_input.loc[i,"review"].count(s_word[0][0])
            if word_cnt > max_cnt:
              max_cnt = word_cnt
              spot_id = i

    # (num, point, popularity) = (0, 1, 0)のとき
    if num == 0 and point == 1 and popularity == 0:
      if int(csv_input.loc[i, "good_cnt"]) > 400:
        if int(csv_input.loc[i,"review"].count('家族')) + int(csv_input.loc[i,"review"].count('友達')) + int(csv_input.loc[i,"review"].count('グループ')) < 3:
          if int(csv_input.loc[i,"review"].count('ごはん')) + int(csv_input.loc[i,"review"].count('ご飯')) + int(csv_input.loc[i,"review"].count('昼食')) + int(csv_input.loc[i,"review"].count('夕食')) + int(csv_input.loc[i,"review"].count('美味しい')) + int(csv_input.loc[i,"review"].count('おいしい')) +int(csv_input.loc[i,"review"].count('絶品')) >= 3:
            word_cnt = csv_input.loc[i,"review"].count(s_word[0][0])
            if word_cnt > max_cnt:
              max_cnt = word_cnt
              spot_id = i

    # (num, point, popularity) = (0, 1, 1)のとき
    if num == 0 and point == 1 and popularity == 1:
      if int(csv_input.loc[i, "good_cnt"]) <= 400:
        if int(csv_input.loc[i,"review"].count('家族')) + int(csv_input.loc[i,"review"].count('友達')) + int(csv_input.loc[i,"review"].count('グループ')) < 3:
          if int(csv_input.loc[i,"review"].count('ごはん')) + int(csv_input.loc[i,"review"].count('ご飯')) + int(csv_input.loc[i,"review"].count('昼食')) + int(csv_input.loc[i,"review"].count('夕食')) + int(csv_input.loc[i,"review"].count('美味しい')) + int(csv_input.loc[i,"review"].count('おいしい')) +int(csv_input.loc[i,"review"].count('絶品')) >= 3:
            word_cnt = csv_input.loc[i,"review"].count(s_word[0][0])
            if word_cnt > max_cnt:
              max_cnt = word_cnt
              spot_id = i

    # (num, point, popularity) = (1, 0, 0)のとき
    if num == 1 and point == 0 and popularity == 0:
      if int(csv_input.loc[i, "good_cnt"]) > 400:
        if int(csv_input.loc[i,"review"].count('家族')) + int(csv_input.loc[i,"review"].count('友達')) + int(csv_input.loc[i,"review"].count('グループ')) >= 3:
          if int(csv_input.loc[i,"review"].count('景色')) + int(csv_input.loc[i,"review"].count('絶景')) + int(csv_input.loc[i,"review"].count('きれい')) + int(csv_input.loc[i,"review"].count('綺麗')) >= 10:
            word_cnt = csv_input.loc[i,"review"].count(s_word[0][0])
            if word_cnt > max_cnt:
              max_cnt = word_cnt
              spot_id = i

    # (num, point, popularity) = (1, 0, 1)のとき
    if num == 1 and point == 0 and popularity == 1:
      if int(csv_input.loc[i, "good_cnt"]) <= 400:
        if int(csv_input.loc[i,"review"].count('家族')) + int(csv_input.loc[i,"review"].count('友達')) + int(csv_input.loc[i,"review"].count('グループ')) >= 3:
          if int(csv_input.loc[i,"review"].count('景色')) + int(csv_input.loc[i,"review"].count('絶景')) + int(csv_input.loc[i,"review"].count('きれい')) + int(csv_input.loc[i,"review"].count('綺麗')) >= 10:
            word_cnt = csv_input.loc[i,"review"].count(s_word[0][0])
            if word_cnt > max_cnt:
              max_cnt = word_cnt
              spot_id = i

    # (num, point, popularity) = (1, 1, 0)のとき
    if num == 1 and point == 1 and popularity == 0:
      if int(csv_input.loc[i, "good_cnt"]) > 400:
        if int(csv_input.loc[i,"review"].count('家族')) + int(csv_input.loc[i,"review"].count('友達')) + int(csv_input.loc[i,"review"].count('グループ')) >= 3:
          if int(csv_input.loc[i,"review"].count('ごはん')) + int(csv_input.loc[i,"review"].count('ご飯')) + int(csv_input.loc[i,"review"].count('昼食')) + int(csv_input.loc[i,"review"].count('夕食')) + int(csv_input.loc[i,"review"].count('美味しい')) + int(csv_input.loc[i,"review"].count('おいしい')) +int(csv_input.loc[i,"review"].count('絶品')) >= 3:
            word_cnt = csv_input.loc[i,"review"].count(s_word[0][0])
            if word_cnt > max_cnt:
              max_cnt = word_cnt
              spot_id = i

    # (num, point, popularity) = (1, 1, 1)のとき
    if num == 1 and point == 1 and popularity == 1:
      if int(csv_input.loc[i, "good_cnt"]) <= 400:
        if int(csv_input.loc[i,"review"].count('家族')) + int(csv_input.loc[i,"review"].count('友達')) + int(csv_input.loc[i,"review"].count('グループ')) >= 3:
          if int(csv_input.loc[i,"review"].count('ごはん')) + int(csv_input.loc[i,"review"].count('ご飯')) + int(csv_input.loc[i,"review"].count('昼食')) + int(csv_input.loc[i,"review"].count('夕食')) + int(csv_input.loc[i,"review"].count('美味しい')) + int(csv_input.loc[i,"review"].count('おいしい')) +int(csv_input.loc[i,"review"].count('絶品')) >= 3:
            word_cnt = csv_input.loc[i,"review"].count(s_word[0][0])
            if word_cnt > max_cnt:
              max_cnt = word_cnt
              spot_id = i
  
  r_address = csv_input.loc[spot_id, 'address'].replace('?','ー')

  return csv_input.loc[spot_id, 'url'], csv_input.loc[spot_id, 'spot_name'], csv_input.loc[spot_id, 'caption'], r_address, csv_input.loc[spot_id, 'img_url'], url_csv_input.loc[spot_id, 'around_url']