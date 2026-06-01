import streamlit as st
import requests

backend_url = st.secrets["backend_url"]

st.set_page_config(
    page_title = "AI Content Generator",
    layout="wide"
)

st.title("🚀 AI Content Generator")

st.write("Generate Blogs", "LinkedIn posts", "Captions", "Email and more")

topic = st.text_input("Enter Topic")

technology = st.selectbox("Select Technology",[
        "Python",
        "React",
        "MERN",
        "NodeJS",
        "FastAPI",
        "AI",
        "GenAI"])

content_type = st.selectbox("Content Type", [
    "LinkedIn Post",
        "Blog",
        "Instagram Caption",
        "Twitter Post",
        "Email",
        "YouTube Description"

])

tone = st.selectbox("Tone",[
    "Professional",
        "Technical",
        "Friendly",
        "Casual",
        "Marketing"
])

Generate = st.button("Generate Content")

if Generate:
    if topic == "":
        st.warning("Invalid Credincials")
    else:
        with st.spinner("Generate Content....."):
            response = requests.post(f"{backend_url}/generate", params={
                "topic":topic,
                "technology":technology,
                "content_type":content_type,
                "tone":tone
            })

            st.write("Status_code: ", response.status_code)
            if response.status_code == 200:

                st.write("Response Text:", response.json()["content"])

                st.success("Content Generated Successfully")

                st.subheader("Generated Content Below")
