import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from PIL import Image

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

labels = "긍정", "부정"
sizes = [15, 30]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct="%1.1f%%", shadow=False, startangle=90)
ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.


# chart_data = pd.DataFrame(
#     [30, 25, 20, 13, 10, 2],
#     columns=["Energy Costs"],
#     index=["Python", "자바", "Javascript", "C#", "C/C++", "ETC"],
# )

chart_data = pd.read_csv("grapth1.csv")
chart_data.drop("Unnamed: 0", axis=1, inplace=True)

chart_data = chart_data.set_index("labels")

# 그래프 이준서가 준 데이터로 만들기.

btn_circle = False
btn_bar = False
btn_text = True
# 변수?


# Using "with" notation
with st.sidebar:
    st.image(
        "https://i.namu.wiki/i/tvGyhYywWMsAcu6DB_LNqDgXsPeaXzDt4Su8mc8pckqINu1ceRlXh6mqVaquCFE9vCBk9Pduf9xkzWr0gcC_Ng.svg",
        caption="This is an image from the web.",
    )  # 이미지 불러오기(웹으로)
    if st.button("Home", type="primary"):
        btn_text = True
        btn_circle = False
        btn_bar = False

    if st.button("댓글 분석하기"):
        btn_bar = True
        btn_circle = True
        btn_text = False

    # title = st.text_input("유튜브 링크", "Life of Brian")

    # if st.button("원그래프", key=2):
    #     btn_circle = True
    #     btn_bar = False
    #     btn_text = False

    # if st.button("막대그래프", key=1):
    #     btn_bar = True
    #     btn_circle = False
    #     btn_text = False


# print(btn_bar, btn_circle)


# if st.button("막대그래프"):
#     st.dataframe(chart_data)
#     st.bar_chart(data=chart_data)

if btn_bar:
    # st.dataframe(chart_data)

    col1, col2, col3 = st.columns([3, 1, 1])

    with col1:
        st.title("_부산 2030 World Expo_ :blue[응원합니다!] :sunglasses:")
        st.divider()
        st.bar_chart(data=chart_data)

    with col2:
        pass

    with col3:
        pass


# if st.button("원그래프"):
#     st.pyplot(fig1)  # Streamlit에 그래프 표시``

if btn_circle:
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        pass

    with col2:
        st.title("_부산 2030 World Expo_ :blue[응원합니다!] :sunglasses:")
        st.divider()
        st.pyplot(fig1)

    with col3:
        pass

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
        # st.markdown(
        #   '<p class="big-font">부산 2030 World Expo에 대하여</p>',
        #  unsafe_allow_html=True,
        # )
        # st.markdown(
        #    '<p class="small-font">부산 2030 World Expo는 어쩌고 저쩌고 이러쿵 저러쿵 </p>',
        #   unsafe_allow_html=True,
        # )
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
            '<p class="small-font">사용법은 웹 사이트 좌측의 사이드바에 있는 유튜브 링크 입력창에 시각화할  </p>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<p class="small-font">유튜브 영상의 링크를 입력한 후 나타낼 그래프의 종류를 선택하면   </p>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<p class="small-font">실시간으로 그 유튜브 영상의 댓글에 나타난 긍정적 여론과 부정적 여론의    </p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="small-font">비율을 선택한 종류의 그래프로 나타냅니다.    </p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="small-font">*예시 사진 추가*  </p>',
            unsafe_allow_html=True,
        )

    with col2:
        pass


# https://www.expo2030busan.kr/index.do#page1
