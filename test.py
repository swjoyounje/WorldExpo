import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from PIL import Image
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

import googleapiclient.discovery
import googleapiclient.errors
def scrap():



    okt = Okt()

    graph = [50,50]

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

    loaded_model = keras.models.load_model('my_model.h5')

    with open("tokenizer.pickle", "rb") as handle:
        tokenizer = pickle.load(handle)

    yt_link = "https://www.youtube.com/watch?v=c6EA_Fi44Ik"  # <<<<<<<<<<입력받은 유튜브 링크 들어가야 함
    remove = "https://www.youtube.com/watch?v="
    video_id = yt_link.replace(remove, "")



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

    graph = list(cmt_data["emotion"].value_counts())
    return graph

st.set_page_config(layout="wide")

# Using object notation
matplotlib.rcParams["font.family"] = "Malgun Gothic"  # windows
matplotlib.rcParams["font.size"] = 15
matplotlib.rcParams["axes.unicode_minus"] = False
## 이준서씨가 준 matplotlip데이터 사이즈와 한글 설정

labels = "긍정", "부정"
sizes = scrap()

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct="%1.1f%%", shadow=False, startangle=90)
ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.


# chart_data = pd.read_csv("grapth1.csv")
# chart_data.drop("Unnamed: 0", axis=1, inplace=True)

# chart_data = chart_data.set_index("labels")

# 그래프 이준서가 준 데이터로 만들기.

btn_text = True
btn_Date = False
# 변수?


# Using "with" notation
with st.sidebar:
    st.image(
        "https://i.namu.wiki/i/tvGyhYywWMsAcu6DB_LNqDgXsPeaXzDt4Su8mc8pckqINu1ceRlXh6mqVaquCFE9vCBk9Pduf9xkzWr0gcC_Ng.svg",
        caption="This is an image from the web.",
    )  # 이미지 불러오기(웹으로)
    if st.button("Home", type="primary"):
        btn_text = True
        btn_Date = False

    if st.button("댓글 분석하기"):
        btn_Date = True
        btn_text = False

    



if btn_Date:
    st.divider()
    title = st.text_input("유튜브 링크를 입력하세요", "https://www.youtube.com/watch?v=")

    # st.dataframe(chart_data)

    col1, col2 = st.columns([2, 2])

    with col1:
        if st.button("Date"):
            st.divider()
            st.pyplot(fig1)
       
    with col2:
        st.divider()
        # st.bar_chart(data=chart_data)


if btn_text:
    col1, col2 = st.columns([30, 14])
    with col1:
        # st.title("_부산 2030 World Expo_ :blue[응원합니다!] :sunglasses:")
        # st.divider()
        st.markdown(
            """
            <style>
                .big-font {
                    font-size:50px !important;
                }
            </style>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <style>
                .small-font {
                    font-size:18px !important;
                    font-family:Black Han Sans;
                }
            </style>
        """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <style>
                .msmall-font {
                    font-size:15px !important;
                
                }
            </style>
        """,
            unsafe_allow_html=True,
        )
    
        st.markdown(
            '<p class="big-font">웹 사이트 소개 </p>',
            unsafe_allow_html=True,
        )
        # st.markdown(
        # '<p class="msmall-font">목적•기능•사용법</p>',
        # unsafe_allow_html=True,
        #  )
        st.divider()

        st.markdown(
            '<p class="small-font">이 웹의 목적은 수집한 데이터를 시각화 하여 나타내는 것입니다.</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="small-font">여러 정책, 미디어, 사건에 대한 선호도 및 여론 또는 현재의 이슈나 트렌드의   </p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="small-font">정보를 실시간으로 크롤링하여 수집한 데이터들을 리스트화 합니다.  </p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="small-font">그 수집한 데이터를 리스트화 하여 정리하고 그래프로 나타내어 줍니다.</p>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<p class="small-font">*이 부분에 그래프 사진*</p>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<p class="small-font">현재는 단적인 예시로 유튜브 영상의 댓글에 적용시킨 상태입니다. </p>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<p class="small-font">사용법은 웹 사이트 좌측의 사이드바에 댓글 분석하기 버튼을 누르면  </p>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<p class="small-font">우측의 메인 사이트에 유튜브 링크 입력란이 나옵니다.  </p>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<p class="small-font">그 입력란에 본인이 원하는 링크를 입력하고 몇분간 기다리면   </p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="small-font">  실시간으로 그 유튜브의 댓글을 크롤링 하여 그 유튜브의 댓글에서  </p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="small-font">나타난 시청자들의 선호도를 자료화 하고 그래프로 나타냅니다.</p>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<p class="small-font">*예시 사진 추가*  </p>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<p class="small-font">이를 통하여 사용자는 한 눈에 영상의 선호도를 파악하여 </p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="small-font">어떤 영상이 사람들에게 선호도가 높은지 낮은지를 확인할 수 있습니다. </p>',
            unsafe_allow_html=True,
        )
       
        st.markdown(
            '<p class="small-font">현재는 크롤링 하는 모델의 한계로 긍정, 부정의 비율만 나타내지만 </p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="small-font">추후에 지속적인 개발을 통하여 여러 기능을 추가할 예정입니다.   </p>',
            unsafe_allow_html=True,
        )
      



    with col2:
        pass



# https://www.expo2030busan.kr/index.do#page1
