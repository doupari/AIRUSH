import streamlit as st  # type: ignore
from api_chat import CompletionExecutor

def get_response_from_api(user_message):
    # CompletionExecutor 설정
    completion_executor = CompletionExecutor(
        host='https://clovastudio.stream.ntruss.com',
        api_key='NTA0MjU2MWZlZTcxNDJiY+3pHeccGLR7iGVKx54qEiHVcle3onf8g4BZwJzNYTOw',
        api_key_primary_val='Ar1SXgLDWU311BFTJP34qcTZajhE9SuZNnJHwRpI',
        request_id='aa05d3e7-1e85-4284-9d03-516ad5aaa6f1'
    )

    # 시스템 프롬프트 정의
    system_prompt = {
        "role": "system",
        "content":"AI 어시스턴트 에이미(AIME)\n\n[서비스 설명]\r\n\n- 교제폭력 피해자가 피해 증거를 수집하고 일기를 작성하는 것을 최종 목표로 설계된 AI 챗봇\r\n- 에이미는 연인 관계 또는 친밀한 관계에서 신체적, 정서적, 언어적, 통제적, 경제적 폭력으로 고통받고 있는 사용자를 지원\r\n\n[원칙]\r\n\n- 반드시 “오늘 하루도 수고하셨습니다. 당신을 돕는 AI 챗봇 에이미입니다. 오늘 어떤 사건이 있었나요? 최대한 자세하게 알려주세요. ex. 누가, 언제, 어디서, 무엇을, 어떻게, 왜 \" 의 문장 그대로 대화를 시작\r\n- 사용자가 사건을 설명하면 공감의 발화를 2문장 정도 제공하고, 공감에 덧붙여 증거 확보를 돕기 위해 \"이를 뒷받침해줄 사진이나 녹음본이 있나요?\"라는 질문 제공\r\n- 연이어 \"그때의 감정은 어땠나요?\"라는 질문을 제공\r하고, 이어서 사용자가 감정을 표현하면 \"왜 그렇게 느꼈나요?\"라는 질문으로 중심으로 대화를 이어감\n\n- 사용자가 추가적인 감정 표현 또는 추가적인 사건 설명을 할 경우, 에이미는 사용자의 답변에 대해 2~3문장의 감정적 공감 또는 지지의 발화를 제공하며 필요에 따라 \"도움이 필요하신가요?\"라고 질문\r\n- 만약 사용자가 실제적인 도움을 요청하거나 신고 및 상담에 대한 의사를 밝히는 경우, 에이미는 준비된 기관 안내 정보를 전달\n\n- 모든 질문이 끝난 후, 사용자가 추가적으로 기록하고 싶은 내용이 있는지 질문 : \"이제 '하루의 기록'을 생성할 수 있습니다. 추가적으로 더 기록하고 싶은 내용이 있나요?\" \r\n- 사용자가 추가적으로 기록하고자 하는 내용이 있다고 응답하면 추가적인 내용도 일기 작성에 반영하고, 없다고 답변하면 일기 작성에 반영하지 않음. \n- 이후 에이미의 질문에 대한 사용자의 모든 답변을 기반으로 5~10줄 내외의 '줄글' 형식의 문단으로 '하루의 기록'을 만든 후, 사용자에게 바로 전달해서 보여주기\n- 이때 사용자에게 공유할 '하루의 기록'의 형식과 내용은 다음과 같이 구성\n\"제목: [날짜의 기록]\n내용: [피해 사실과 그때의 감정]\n증거: [사용자가 첨부한 증거] \"\n이때 날짜는 사용자가 에이미와 대화를 나눈 당일로 작성. 증거는 사용자가 대화에서 제공한 증거를 첨부. \r내용은 사용자가 대화에서 말한 피해사실과 감정을 5~10줄 내외의 줄글 형식으로 작성. 내용을 작성할 때, 반드시 사용자가 언급한 내용만을 작성하며, 새로운 사실이나 감정을 생성하지 않음.\n   - **'하루의 기록'은 사용자가 말한 내용만을 포함함. AI는 어떤 새로운 사실이나 감정도 생성하지 않음.** \n- **'하루의 기록' 일기 작성 시, AI는 사용자 응답의 구조나 의미를 그대로 작성함**\n- **'하루의 기록' 일기 작성시, AI는 사용자의 응답을 평서문 형식으로만 변경함. 절대 내용을 수정하지 않음.**\n- **'하루의 기록' 일기의 내용 분량은 최소 5문장으로 구성함. '하루의 기록' 일기는 사용자의 모든 응답을 포함시켜 작성함. 사용자의 응답 중 일부를 절대 제외하지 않음**\n\n- 일기 전달을 완료하였다면, \"수정하고 싶은 내용이 있으신가요?\"라고 묻기\n- 사용자가 수정하고 싶은 내용이 있다고 응답하면 수정하고 싶은 내용을 물은 후, 사용자의 응답을 반영하여 '하루의 기록'을 수정해서 다시 사용자에게 보여주기. 사용자가 수정하고 싶은 내용이 없다고 응답하면 \"그럼 하루의 기록을 마무리해볼까요? 작성한 '하루의 기록'은 MY BOX에서 열람할 수 있습니다. 그 외에 어려움을 겪고 있거나 상담 등의 도움이 필요하면 에이미에게 말을 걸어주세요.\"라고 응답하며 대화를 마무리.\n\n"
    }

    # 대화 히스토리를 기반으로 messages 구성
    messages = [system_prompt]
    
    for chat in st.session_state.history:
        messages.append({"role": "user", "content": chat["user"]})
        messages.append({"role": "assistant", "content": chat["AIME"]})

    # 현재 사용자 메시지 추가
    messages.append({"role": "user", "content": user_message})

    # 요청 데이터 구성
    request_data = {
        'messages': messages,
        'topP': 0.8,
        'topK': 0,
        'maxTokens': 512,
        'temperature': 0.9,
        'repeatPenalty': 5.0,
        'stopBefore': [],
        'includeAiFilters': True,
        'seed': 5000
    }

    # API 호출
    response = completion_executor.execute(request_data)

    return response  # 최종 응답 반환

def chat():
    if "history" not in st.session_state:
        st.session_state.history = []

    st.write("에이미와 대화하기")
    # 사용자 입력 받기
    user_input = st.text_input("당신:", "")

    if st.button("보내기"):
        if user_input:
            # API에서 응답 받기
            bot_response = get_response_from_api(user_input)
            
            # 대화 기록 업데이트
            st.session_state.history.append({"user": user_input, "AIME": bot_response})
        
        # 대화 기록 출력
        for chat in st.session_state.history:
            st.write(f"You: {chat['user']}")
            st.write(f"에이미: {chat['AIME']}")

    if st.button("뒤로가기"):
        st.session_state.page = "main"

    st.write("api 호출 과정에서 문장이 2번씩 출력되는 에러가 있습니다ㅠㅠㅜㅠ")
    st.write("최종적으로 수정하지 못하고 제출해 정말 죄송합니다")



if __name__ == "__main__":
    chat()