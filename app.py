from operator import ge
from pickle import TRUE
from ssl import HAS_TLSv1_1
from tkinter import CENTER
import streamlit as st
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

# components.html(
    
# )

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Generate csv'], 
        icons=['house', 'cloud-upload'], menu_icon="cast", default_index=1)
    selected

# 2. horizontal menu
# selected2 = option_menu(None, ["Home", "Csv", "Quotes", 'Links'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     menu_icon="cast", default_index=0, orientation="horizontal")
# selected2

# # 3. CSS style definitions
# selected3 = option_menu(None, ["Home", "Upload",  "Tasks", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     menu_icon="cast", default_index=0, orientation="horizontal",
#     styles={
#         "container": {"padding": "0!important", "background-color": "#fafafa"},
#         "icon": {"color": "orange", "font-size": "25px"}, 
#         "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#         "nav-link-selected": {"background-color": "green"},
#     }
# )

# st.title('Quotes Scrapper')
# st.image(logo_url, width=100)
st.markdown("<h1 style='text-align: center; color: white;'>QUOTES SCRAPPER 💬</h1>", unsafe_allow_html=True)
st.markdown("---")
# st.markdown("<h1 style='text-align:center;'>Quotes Scrapper</h1>", unsafe_allow_html=TRUE)
# lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



# lottie animation 

lottie_coding = load_lottiefile("read.json")  # replace link to local lottie file
# lottie_hello = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_0c8439m5.json")
lottie_hello=load_lottiefile("read.json")

st_lottie(
    lottie_hello,
    speed=1.5,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    # renderer="svg", # canvas
    height=None,
    # height=400,
    width=None,
    key=None,
)

# main content

# col1, col2= st.columns([4,1])
# with col1:
st.markdown("<h3 style='text-align: center; color: white;'>Choose A Topic</h3>", unsafe_allow_html=True)
tag=st.selectbox(' ',['love','humor','inspiration','life','books'])

# with col2:
generate=st.button('Generate Csv')


url=f"https://quotes.toscrape.com/tag/{tag}/"
# st.write(url)
res=requests.get(url)
# st.write(res)
content=BeautifulSoup(res.content,'html.parser')
# st.code(content)
quotes=content.find_all('div', class_='quote')

file=[]
for quote in quotes:
    text=quote.find('span',class_='text').text
    author=quote.find('small',class_='author').text
    link=quote.find('a')
    st.success(text)
    # st.write(author)
    st.markdown(f"<h5 ><a href=https://quotes.toscrape.com{link['href']}>{author}</a></h5>", unsafe_allow_html=True)
    st.code(f"https://quotes.toscrape.com{link['href']}")
    file.append([text,author,link['href']])
if generate:
    try:
        df=pd.DataFrame(file)
        df.to_csv('quotes.csv', index=False, header=['Quote', 'Author', 'Link'],encoding='cp1252')

    

    except:
        st.write('Loading ...')
