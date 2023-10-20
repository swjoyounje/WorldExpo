import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from PIL import Image
import random

st.set_page_config(layout="wide")


# st.markdown(
#     """
#     <style>
#         .big-font {
#             font-size:25px !important;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# st.markdown(
#     '<p class="big-font">2023년 10월 현재로서는, 2030년 부산 월드 엑스포에 대한 구체적인 정보가 제공되지 않았습니다. 그러나 일반적인 월드 엑스포에 대한 설명을 바탕으로 예상해볼 수 있습니다., 2030년 부산 월드 엑스포는 한국의 해양 도시 부산에서 개최될 세계적인 국제 행사입니다. 이 행사는 다양한 나라들이 참가하여 각국의 문화, 기술, 아이디어를 세계에 소개하는 무대로서의 역할을 합니다.</p>',
#     unsafe_allow_html=True,
# )


# Using object notation
matplotlib.rcParams["font.family"] = "Malgun Gothic"  # windows
matplotlib.rcParams["font.size"] = 15
matplotlib.rcParams["axes.unicode_minus"] = False
## 이준서씨가 준 matplotlip데이터 사이즈와 한글 설정




# chart_data = pd.DataFrame(
#     [30, 25, 20, 13, 10, 2],
#     columns=["Energy Costs"],
#     index=["Python", "자바", "Javascript", "C#", "C/C++", "ETC"],
# )

chart_data = pd.read_csv("grapth1.csv")
chart_data.drop("Unnamed: 0", axis=1, inplace=True)

chart_data = chart_data.set_index("labels")

# 그래프 이준서가 준 데이터로 만들기.

btn_text = False
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
    # st.dataframe(chart_data)

    col1, col2, col3 = st.columns([2, 2, 1])

    with col1:
        
        
        pass

    with col2:
        labels = "긍정", "부정"
        sizes = [random.randrange(10, 50), random.randrange(10, 50)]

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct="%1.1f%%", shadow=False, startangle=90)
        ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle
        
        st.divider()
        st.pyplot(fig1)

    with col3:
        pass



