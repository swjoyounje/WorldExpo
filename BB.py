import numpy as np
import re
import pickle
import urllib.request
import numpy as np
import pandas as pd
from konlpy.tag import Okt
from tqdm import tqdm
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import joblib
from tensorflow import keras

import googleapiclient.discovery
import googleapiclient.errors

okt = Okt()

stopwords = [
    "의",
    "가",
    "이",
    "은",
    "들",
    "는",
    "좀",
    "잘",
    "걍",
    "과",
    "도",
    "를",
    "으로",
    "자",
    "에",
    "와",
    "한",
    "하다",
]

max_len = 30

loaded_model = keras.models.load_model("my_model.h5")

with open("tokenizer.pickle", "rb") as handle:
    tokenizer = pickle.load(handle)

yt_link = "https://www.youtube.com/watch?v=J3VjhnsIT8E"  # <<<<<<<<<<입력받은 유튜브 링크 들어가야 함
remove = "https://www.youtube.com/watch?v="
video_id = yt_link.replace(remove, "")


import googleapiclient.discovery
import googleapiclient.errors

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyBuvDRaZaCTczrhmAatOcIF0FH76-TqYJc"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY
)

request = youtube.commentThreads().list(
    part="snippet", videoId=video_id, maxResults=500
)
response = request.execute()

cmt_str = []

for item in response["items"]:
    cmt_str.append(item["snippet"]["topLevelComment"]["snippet"]["textDisplay"])

cmt_data = pd.DataFrame(cmt_str, columns=["comments"])

emotion = []

for r in cmt_data.iterrows():
    r = str(r[1].values)
    r = re.sub(r"[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "", r)
    r = okt.morphs(r, stem=True)
    r = [word for word in r if not word in stopwords]
    encoded = tokenizer.texts_to_sequences([r])
    pad_new = pad_sequences(encoded, maxlen=max_len)
    score = float(loaded_model.predict(pad_new))
    if score > 0.5:
        emotion.append(1)
    else:
        emotion.append(0)

cmt_data["emotion"] = emotion

print(cmt_data["emotion"].value_counts())
