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
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image


import googleapiclient.discovery
import googleapiclient.errors


def scrap(url):



    

    okt = Okt()

    graph = [50,50]

    stopwords = [ "하다", "을", "의", "들", "은","는", "다", "니","를", "게", "가", "이", "있는", "하고", "그", "아", "그리고", "또는", "에서", "에게", "이런", "그런",
    "아니라", "하기", "한다", "하지", "없는", "더", "대한", "등", "이러한", "그러한", "데", "대", "차", "에", "도", "것", "되다", "같다", "이다", "하", '자', "이도","등등", "한", "ㅋㅋ", "ㅋ", "ㅋㅋㅋ",
    "ㅋㅋㅋㅋ", "또","않다", "해보다", '나', '진짜', '님','인가', '헐다', '개', '내다',
    "어떤", "언제", "어디", "무엇", "얼마나", "많은", "때문에", "그러나", "때", "또한",
    "및", "으로", "인", "에서는", "이라고", "대해", "만", "그래서", "그대로", "모든",
    "이나", "이라는", "않는", "그러니", "하면", "못", "해도", "같은", "보다", "왜",
    "이에", "갖고", "말", "없이", "만든", "때로", "아니고", "물론", "점", "인데",
    "뭐", "하자", "해야", "그냥", "어때", "그저", "먼저", "가장", "언제나", "몇",
    "모두", "자신", "자기", "저기", "어느", "지금", "누가", "라고", "라면", "라며",
    "이미", "어기", "라기", "만큼", "대로", "도록", "대로", "그만", "과", "때까지",
    "자체", "이자", "이유", "곳", "밖에", "안에", "해야", "해줘", "해주는", "해야지",
    "해주세요", "그게", "이니", "막", "자주", "좀", "직접", "만이", "딱", "거의",
    "예전", "실제로", "당장", "이렇게", "보고", "따라", "오로지", "가운데", "말고",
    "함은", "당연히", "네", "하면서", "단지", "특히", "더욱", "다른", "그중", "일부",
    "만을", "비롯", "단", "다음", "비록", "이제", "그동안", "앞으로", "이후", "대부분",
    "점에서", "바로", "그래도", "이라면", "있을", "듯", "있고", "있다", "아니다", "아니며",
    "아니라고", "아니라는", "아니라면", "아니라며", "아니면", "아니였다", "아니었다",
    "아니었으며", "아니었으나", "아니었다", "아니었다고", "아니었다는", "아니었다면",
    "아니었다며", "아니었다면", "아니었지만", "아니었지만", "않았다", "않았으며",
    "않았으나", "않았다고", "않았다는", "않았다면", "않았다며", "않았다면", "않았지만",
    "않았지만", "없었다", "없었으며", "없었으나", "없었다고", "없었다는", "없었다면",
    "없었다며", "없었다면", "없었지만", "없었지만", "가서", "네요", "라서", "아가", "야",
    "잖아", "예요", "거든", "는데", "에서는", "에게는", "에게서", "로서", "이어서", "하면서",
    "어서", "어서는", "어서도", "어서야", "어야", "어야만", "어야는", "어야도", "어야야",
    "어야지", "어야지만", "어야했다", "어야했다고", "어야했다는", "어야했다면",
    "어야했다며", "어야했다면", "어야했지만", "어야했지만", "어서는", "어서도", "어서야",
    "어야", "어야만", "어야는", "어야도", "어야야", "어야지", "어야지만", "어야했다",
    "어야했다고", "어야했다는", "어야했다면", "어야했다며", "어야했다면", "어야했지만",
    "어야했지만", "로써", "로써는", "로써도", "로써야", "로써지", "로써야지", "로써야만",
    "로써야는", "로써야도", "로써야야", "로써야지", "로써야지만", "로써야했다", "로써야했다고",
    "로써야했다는", "로써야했다면", "로써야했다며", "로써야했다면", "로써야했지만",
    "로써야했지만", "예로써", "예로써는", "예로써도", "예로써야", "예로써지", "예로써야지",
    "예로써야만", "예로써야는", "예로써야도", "예로써야야", "예로써야지", "예로써야지만",
    "예로써야했다", "예로써야했다고", "예로써야했다는", "예로써야했다면", "예로써야했다며",
    "예로써야했다면", "예로써야했지만", "예로써야했지만", "라면서", "라면서는", "라면서도",
    "라면서야", "라면서지", "라면서야지", "라면서야만", "라면서야는", "라면서야도",
    "라면서야야", "라면서야지", "라면서야지만", "라면서야했다", "라면서야했다고",
    "라면서야했다는", "라면서야했다면", "라면서야했다며", "라면서야했다면",
    "라면서야했지만", "라면서야했지만", "라면서로", "라면서로는", "라면서로도", "라면서로야",
    "라면서로지", "라면서로야지", "라면서로야만", "라면서로야는", "라면서로야도",
    "라면서로야야", "라면서로야지", "라면서로야지만", "라면서로야했다", "라면서로야했다고",
    "라면서로야했다는", "라면서로야했다면", "라면서로야했다며", "라면서로야했다면",
    "라면서로야했지만", "라면서로야했지만", "과", "와", "그리고", "더불어", "비롯",
    "외에도", "등", "이나", "또는", "및", "하고", "고", "바랍니다", "많은", "여러분",
    "보세요", "보이", "누가", "무엇", "이라고", "당신", "우리", "함께", "함은", "하면",
    "가서", "네요", "뭐", "지금", "라고", "라며", "라면", "아니라고", "아니라는",
    "아니라면", "아니라며", "아니면", "아니였다", "아니었다", "아니었으며", "아니었으나",
    "아니었다고", "아니었다는", "아니었다면", "아니었다며", "아니었다면", "아니었지만",
    "아니었지만", "않았다", "않았으며", "않았으나", "않았다고", "않았다는", "않았다면",
    "않았다며", "않았다면", "않았지만", "않았지만", "없었다", "없었으며", "없었으나",
    "없었다고", "없었다는", "없었다면", "없었다며", "없었다면", "없었지만", "없었지만",
    "로써", "로써는", "로써도", "로써야", "로써지", "로써야지", "로써야만", "로써야는",
    "로써야도", "로써야야", "로써야지", "로써야지만", "로써야했다", "로써야했다고",
    "로써야했다는", "로써야했다면", "로써야했다며", "로써야했다면", "로써야했지만",
    "로써야했지만", "예로써", "예로써는", "예로써도", "예로써야", "예로써지", "예로써야지",
    "예로써야만", "예로써야는", "예로써야도", "예로써야야", "예로써야지", "예로써야지만",
    "예로써야했다", "예로써야했다고", "예로써야했다는", "예로써야했다면", "예로써야했다며",
    "예로써야했다면", "예로써야했지만", "예로써야했지만", "라면서", "라면서는", "라면서도",
    "라면서야", "라면서지", "라면서야지", "라면서야만", "라면서야는", "라면서야도",
    "라면서야야", "라면서야지", "라면서야지만"]

    max_len = 30

    loaded_model = keras.models.load_model('my_model.h5')

    with open("tokenizer.pickle", "rb") as handle:
        tokenizer = pickle.load(handle)

    yt_link = url  # <<<<<<<<<<입력받은 유튜브 링크 들어가야 함
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
    cloud_str = []

    for r in cmt_data.iterrows():
        r = str(r[1].values)
        r = re.sub(r"[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "", r)
        r = okt.morphs(r, stem=True)
        r = [word for word in r if not word in stopwords]
        cloud_str = cloud_str+r
        encoded = tokenizer.texts_to_sequences([r])
        pad_new = pad_sequences(encoded, maxlen=max_len)
        score = float(loaded_model.predict(pad_new))
        if score > 0.5:
            emotion.append(1)
        else:
            emotion.append(0)

    print(cloud_str)

    

    cmt_data["emotion"] = emotion

    graph = list(cmt_data["emotion"].value_counts())
    print(graph)
    return graph,cloud_str


    

st.set_page_config(layout="wide")

# Using object notation
matplotlib.rcParams["font.family"] = "Malgun Gothic"  # windows
matplotlib.rcParams["font.size"] = 15
matplotlib.rcParams["axes.unicode_minus"] = False
## 이준서씨가 준 matplotlip데이터 사이즈와 한글 설정





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
    st.divider()
    title = st.text_input("유튜브 링크를 입력하세요", "https://www.youtube.com/watch?v=")
    print(title)

    if st.button("댓글 분석하기"):
        btn_Date = True
        btn_text = False


print(title)
if btn_Date:
    

    # st.dataframe(chart_data)

    col1, col2 = st.columns([2, 2])

    with col1:
        labels = "긍정", "부정"
        sizes = scrap(title)[0]

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct="%1.1f%%", shadow=False, startangle=90)
        ax1.axis("equal")  

        
        st.divider()
        st.pyplot(fig1)

    with col2:
        from collections import Counter

        nouns_counter = Counter(scrap(title)[1])
        top_nouns = dict(nouns_counter.most_common(50))

        import matplotlib.pyplot as plt
        from wordcloud import WordCloud
        import numpy as np
        from PIL import Image

       
        wc = WordCloud (max_words=50,
                        width=300,
                        height=200,
                background_color='white',
                font_path= 'C:/Windows/Fonts/HanSantteutDotum-Bold.TTF'
                )
        
        wc.generate_from_frequencies(top_nouns)
        
        fig2=plt.figure(figsize=(4,4))
        plt.imshow(wc)
        plt.axis('off')
        plt.show()
        st.divider()
        st.pyplot(fig2)
        


if btn_text:
    col1, col2, col3 = st.columns([1, 5, 1])
    with col2:
        # st.title("_부산 2030 World Expo_ :blue[응원합니다!] :sunglasses:")
        # st.divider()
        st.markdown(
            """
            <style>
                .big-font {
                    font-size:23px !important;
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
    
        st.title('2030 부산 세계 박람회 유치 홍보를 위한 프로젝트')
        
        
        st.divider()

        st.subheader('2030 부산 월드 엑스포')

        image = Image.open('엑스포.jpg')

        st.image(image)

        col1, col2,  = st.columns([1, 5])
        with col1:
            st.markdown(
                '<p class="big-font">박람회란?</p>',
                unsafe_allow_html=True,
            )
        with col2:

           
            st.markdown(
                '<p class="small-font">인류의 산업, 과학기술 발전 성과를 소개하고 개최국의 역량을 과시하는 장으로 경제∙문화 올림픽이라고도 불립니다.  </p>',
                unsafe_allow_html=True,
            )

            st.markdown(
                '<p class="small-font">BIE는 다음과 같이 엑스포를 규정하고 있습니다.  </p>',
                unsafe_allow_html=True,
            )

            st.markdown(
                '<p class="big-font"> </p>',
                unsafe_allow_html=True,
            )

            st.markdown(
                '<p class="small-font">Expos are global events dedicated to finding solutions to fundamental challenges facing humanity by offering a journey inside a chosen theme through engaging and immersive activities. </p>',
                unsafe_allow_html=True,
            )

        col1, col2,  = st.columns([1, 5])
        with col1:
            st.markdown(
                '<p class="big-font">우리 사이트는?</p>',
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(
                '<p class="small-font">2030부산세계박람회 홍보, 유치   </p>',
                unsafe_allow_html=True,
            )


            #인류의 산업, 과학기술 발전 성과를 소개하고 개최국의 역량을 과시하는 장으로 경제∙문화 올림픽이라고도 불립니다.

           
    st.divider()
    st.markdown(
            '<p class="small-font"></p>',
            unsafe_allow_html=True,
        )

    col1, col2 = st.columns([15, 15])
    with col1:    
        st.subheader('     유튜브 댓글 감정분석')
        image = Image.open('그래프1.png')

        st.image(image)

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

    with col2: 
        st.subheader('유튜브 댓글 워드클라우드')
        image = Image.open('그래프2.png')

        st.image(image)
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
