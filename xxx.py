import requests
import streamlit as st
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="saabiqmasoodi",page_icon=":alien monster:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
    


lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

with st.container():
    st.subheader("Hi i am saabiq :wave:")
    st.title("a student in Paul George Global School")
    st.write("a passionate game dev looking for ideas")
    st.write("[see my channel>](https://www.youtube.com/@saabiqmasoodi)")



with st.container():
    st.write
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What i do")
        st.write("##")
        st.write(
            """
      I’m Saabiq Masoodi, a creative developer and designer who loves building
      premium-quality games, projects, and interactive experiences. Passionate
      about blending technology with creativity, I focus on turning ideas into
      polished work that inspires and connects people.
"""
)
with right_column:
    st_lottie(lottie_coding, height=300, key="coding")


    with st.container():
        st.write("###")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            with text_column:
                st.subheader("Buy my book")
                st.write(
                """
 buy unknown origons for only 400₹ a book for children to start reading
 """
                )
            st.markdown("[Purchase...](https://www.bribooks.com/bookstore/unknown-origins)")
