import streamlit as st # type: ignore
from datetime import datetime, timedelta

today = datetime.today()
one_day_ago = today - timedelta(days=1)

def download():

    st.title(one_day_ago.strftime("%Y/%m/%d"))
    st.divider()

    st.write("""
날짜 : """, one_day_ago.strftime("%Y/%m/%d") , """ \n\n
내용 : 남자친구는 나에게서 오늘 30만원을 가져갔다. 월세 낼 돈이 없는데도 계속 협박하면서 사랑하는 사람에게는 뭐든지 할 수 있는게 아니나며 결국 돈을 가져갔다. 나는 이에 좌절감과 무력감을 느꼈다.

증거 : 사진 1장, 녹음본 1건
""")

    audio_file = open("evidence.m4a", "rb").read()
    
    st.divider()
    if st.button("사진1"):
        st.image("pic1.jpg")

    if st.button("음성1"):
        st.audio(audio_file)


    if st.button("뒤로가기"):
        st.session_state.page = "main"
