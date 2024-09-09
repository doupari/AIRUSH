import streamlit as st # type: ignore
from datetime import datetime, timedelta

today = datetime.today()
    
one_day_ago = today - timedelta(days=1)
two_days_ago = today - timedelta(days=2)
three_days_ago = today - timedelta(days=3)
four_days_ago = today - timedelta(days=4)
five_days_ago = today - timedelta(days=5)
six_days_ago = today - timedelta(days=6)

def archive():

    st.title("날짜별로 확인하기")
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button(one_day_ago.strftime("%Y/%m/%d") + " ★"):
            st.session_state.page = "download"
    with col2:
        st.button(two_days_ago.strftime("%Y/%m/%d") + " (구현예정)")
    with col3:
        st.button(three_days_ago.strftime("%Y/%m/%d") + " (구현예정)")
    
    col4, col5, col6 = st.columns(3)
    with col4:
        st.button(four_days_ago.strftime("%Y/%m/%d") + " (구현예정)")
    with col5:
        st.button(five_days_ago.strftime("%Y/%m/%d") + " (구현예정)")
    with col6:
        st.button(six_days_ago.strftime("%Y/%m/%d") + " (구현예정)")
    
    st.divider()

    st.button("기록 다운로드 (구현예정)")
    st.write("")
    st.write("")
    

    if st.button("뒤로가기"):
        st.session_state.page = "main"
