import streamlit as st # type: ignore

# 페이지 상태를 초기화
if 'page' not in st.session_state:
    st.session_state.page = "main"

# 페이지 라우팅
if st.session_state.page == "main":
    from main import main
    main()
elif st.session_state.page == "chat":
    from chat import chat
    chat()
elif st.session_state.page == "archive":
    from archive import archive
    archive()
elif st.session_state.page == "guide":
    from guide import guide
    guide()
elif st.session_state.page == "download":
    from download import download
    download()