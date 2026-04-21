import streamlit as st
from generator.blog import generate_blog

st.set_page_config(page_title="AI Blog Generator", layout="wide")

st.title("🤖 AI Blog Generator")

# 输入
topic = st.text_input("请输入博客主题：")
tone = st.selectbox("选择风格：", ["专业", "轻松", "营销"])

if st.button("生成博客"):
    if not topic:
        st.warning("请输入主题")
    else:
        with st.spinner("生成中..."):
            blog = generate_blog(topic, tone)

        st.markdown(blog)

        st.download_button("下载 Markdown", blog, "blog.md")