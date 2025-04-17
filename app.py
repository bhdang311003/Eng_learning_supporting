from llm import gen_answer, gen_quiz

import streamlit as st # type: ignore

st.title("Ứng dụng hỗ trợ học tiếng Anh")

tabs = st.tabs(["Kiểm tra ngữ pháp", "Diễn đạt lại", "Dịch thuật", "Tóm tắt", "Hỏi đáp văn bản", "Quiz", "Yêu cầu tự do"])

with tabs[0]:
    st.header("Kiểm tra ngữ pháp")
    input = st.text_area("Nhập văn bản để kiểm tra ngữ pháp:", placeholder="Nhập ở đây...", height = 200)
    prompt = f"Hãy kiểm tra ngữ pháp văn bản sau: {input}"
    if st.button("Bắt đầu", key="grammar"):
        st.write(gen_answer(prompt))

with tabs[1]:
    st.header("Diễn đạt lại")
    input = st.text_area("Nhập văn bản để diễn đạt lại:", placeholder="Nhập ở đây...", height = 200)
    context = st.selectbox("Chọn phong cách văn bản:", ["Trang trọng", "Bình dân", "Học thuật"])
    prompt = f"Hãy viết lại văn bản sau theo phong cách {context}: {input}"
    if st.button("Bắt đầu", key="rewrite"):
        st.write(gen_answer(prompt))

with tabs[2]:
    st.header("Dịch thuật")
    input = st.text_area("Nhập văn bản để dịch:", placeholder="Nhập ở đây...", height = 200)
    if st.button("Dịch sang tiếng Việt", key="translate_to_vi"):
        prompt = f"Hãy dịch văn bản sau sang tiếng Việt: {input}"
        st.write(gen_answer(prompt))
    if st.button("Dịch sang tiếng Anh", key="translate_to_en"):
        prompt = f"Hãy dịch văn bản sau sang tiếng Anh: {input}"
        st.write(gen_answer(prompt))

with tabs[3]:
    st.header("Tóm tắt")
    input = st.text_area("Nhập văn bản để tóm tắt:", placeholder="Nhập ở đây...", height = 200)
    prompt = f"Hãy tóm tắt văn bản sau: {input}"
    if st.button("Bắt đầu", key="summarize"):
        st.write(gen_answer(prompt))


with tabs[4]:
    st.header("Hỏi đáp văn bản")
    text_input = st.text_area("Nhập văn bản:", placeholder="Nhập ở đây...", height = 300)
    question = st.text_area("Nhập câu hỏi:", placeholder="Nhập ở đây...", height = 100)
    prompt = f"""
            Context:
            {text_input}

            Question:
            {question}

            Answer:
            """
    if st.button("Trả lời", key="Q&A"):
        st.write(gen_answer(prompt))

with tabs[5]:
    st.header("English Quiz")

    context = st.selectbox("Chọn chủ đề Quiz:", ["Từ vựng", "Ngữ pháp", "Các thì", "Thành ngữ và cụm từ"])

    match context:
        case "Từ vựng":
            topic = "Vocabulary"
        case "Ngữ pháp":
            topic = "Grammar"
        case "Các thì":
            topic = "Tenses"
        case "Thành ngữ và cụm từ":
            topic = "Idioms and Phrases"

    if "show_quiz" not in st.session_state:
        st.session_state["show_quiz"] = False  

    if "quiz_list" not in st.session_state:
            st.session_state["quiz_list"] = []
        
    if st.button("Bắt đầu quiz", key="quiz"):
        st.session_state["show_quiz"] = True
        st.session_state["quiz_list"] = gen_quiz(topic) 
 
    quiz_list = st.session_state["quiz_list"]

    if st.session_state["show_quiz"]:
        for idx, quiz in enumerate(quiz_list):
            question, answers, correct_answer = quiz.split('|')
            anss = [item.strip() for item in answers.split(', ')]
            st.write(f"{idx + 1}. {question}")
            for ans in anss:
                if st.button(f"{ans}", key = f'check_{idx}_{ans}'):
                    if ans == correct_answer.strip():
                        st.write("Chính xác")
                    else:
                        st.write(f"Chưa chính xác, đáp án là {correct_answer}")

with tabs[6]:
    st.header("Yêu cầu tự do")
    input = st.text_area("Bạn muốn yêu cầu điều gì?", placeholder="Nhập ở đây...", height = 200)
    prompt = f"{input}"
    if st.button("Bắt đầu", key="request"):
        st.write(gen_answer(prompt))



