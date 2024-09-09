import streamlit as st # type: ignore

def guide():
    st.header("에이미(AIME) 사용 가이드")
    st.write("에이미는 당신의 피해사실을 기록하고, 증거자료를 체계적으로 수집할 수 있도록 도움을 제공합니다.")
    st.write("")
    st.divider()
    st.info("[일기작성] \n\n AI 어시스턴트인 에이미의 질문에 따라 답변을 남기거나 증거자료를 업로드하면, 에이미는 응답을 기반으로 일기를 구조화해서 제공합니다.")
    st.info("[공감지지] \n\n 에이미와 대화하며 마음의 위로를 건네받고, [상담센터연계]를 통해 도움을 받을 수 있는 상담센터를 안내합니다.")
    st.write("")
    st.info("[증거자료수집 및 관리] \n 1) 작성된 일기 \n 2) 업로드한 증거자료 \n 3) 채팅 내용 \n\n 은 MyBox에 저장되며, 추후 필요시 (법률상담, 피해자지원센터, 112 신고 등) 저장된 기록을 다운받아 이용할 수 있습니다.")

    st.divider()
    
    st.write("")    
    st.write("그림과 함께 이해하기") 

    st.image("main.png", width = 200)
    st.success("""앱을 클릭한 당신은 홈 화면을 마주합니다. 
                    날짜 아래에 '오늘의 기록'과 '과거의 기록'이라는 두개의 버튼이 눈에 들어옵니다. """)
    
    st.write("")
    st.image("chat.png", width = 200)
    st.success("""[오늘의 기록] 버튼을 클릭한 당신은 아래와 같은 채팅창을 마주합니다. 
                    채팅을 시작하자 AI 챗봇 AIME가 질문을 건네옵니다. """)
    
    st.write("")
    st.image("download.png", width = 200)
    st.success("""[과거의 기록] 버튼은 클릭한 당신은 당신은 오늘 작성한 일기가 제대로 저장되었는지 확인할 수 있습니다. 
                    최근의 기록/날짜별/키워드별로 일기, 증거자료, 대화내용을 열람하고, 필요시 다운받아 저장할 수 있습니다.""")
    st.divider()
    st.write("사용 가이드를 다 숙지했습니다:) 에이미는 당신에게 최대한 도움이 될 수 있도록 노력하겠습니다")
    if st.button("뒤로가기"):
        st.session_state.page = "main"