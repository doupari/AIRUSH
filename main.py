import streamlit as st # type: ignore

from datetime import datetime


def main():
    st.write("교제폭력 증거수집 AI 다이어리")
    st.subheader("AIME")

    st.write("")
    st.write("")

    st.write("당신과 함께 새로운 기록을 작성할,")
    st.subheader(datetime.today().strftime("%Y/%m/%d"))

    st.write("")

    if st.button("AIME와 *오늘의 기록* 작성하기 "):
        st.session_state.page = "chat"
    if st.button("다이어리에서 *지난 기록* 열람하기"):
        st.session_state.page = "archive"

    st.write("")
    st.write("")
    st.write("")


    col3, col4 = st.columns(2)
    with col3:
        if st.button("AIME 사용 가이드"):
            st.session_state.page = "guide"
    with col4:
        st.button("네이버로 간편 로그인 (구현예정)")



