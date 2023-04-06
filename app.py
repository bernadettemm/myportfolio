from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


# find more emojis here: hhtps://webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Portfolio", page_icon=":tada:", layout="wide")

# ---Function to access the json fine of lottie ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#--- LOAD ASSETS ---
lottie_girl = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_toupngka.json")
#img_contact_form = Image.open("images/cloth3.jpg")
project1 = Image.open("images/covid.webp")
project2 = Image.open("images/exdashboard.webp")
project3 = Image.open("images/afya.webp")


#----HEADER SECTION ------
with st.container():
    st.subheader("Hi, I am Bernadette :wave:")
    st.title("I am a Data Scientist with extended interest towards Cybersecurity")
    

# Define the HTML code for the social media icons
social_icons = '''
<a href="https://www.linkedin.com/in/bernadette-massawe-5a99361b5/" target="_blank"><img src="https://img.icons8.com/color/48/000000/linkedin.png"/></a>&nbsp;&nbsp;
<a href="https://github.com/bernadettemm" target="_blank"><img src="https://img.icons8.com/color/48/000000/github--v1.png"/></a>&nbsp;&nbsp;
<a href="https://twitter.com/amb_bernadette" target="_blank"><img src="https://img.icons8.com/color/48/000000/twitter.png"/></a>&nbsp;&nbsp;
'''

# Display the social media icons
st.markdown(social_icons, unsafe_allow_html=True)

#---- WHAT I DO -------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Welcome to my portfolio page! I am a data scientist with a passion for analyzing complex 
            data sets to uncover insights and drive business decisions. In addition to my data science skills, 
            I also have a keen interest in Cybersecurity and enjoy staying up-to-date with the latest trends and techniques in the field. 
            With a strong background in statistics, machine learning, and data visualization, I'm able to tackle a wide range of analytical 
            problems and present my findings in a clear and compelling way. 
            Take a look at my projects and feel free to contact me if you'd like to learn more about my work!
              
            """
        )
        st.write("[LinkedIn Profile >](https://www.linkedin.com/in/bernadette-massawe-5a99361b5/)")
    with right_column:
        st_lottie(lottie_girl, height=300, key="girl")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    image_column, text_column = st.columns((1, 2))
    with image_column:
         st.image(project1) 
    with text_column:
         st.subheader("COVID-19 Data Exploration")
         st.write(
             """
             Used SQL Server to explore and analyse covid-19 Data from the open source global data on 
              COVID-19 as 29/03/2023. 
             
             """
         )
         st.markdown("[View Project...](https://github.com/bernadettemm/data-analysis-projects/blob/main/COVID19%20SQL%20Data%20Exploration.sql)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
         st.image(project2) 
    with text_column:
         st.subheader("Excel Dasboard for Bike Sales")
         st.write(
             """
             Leeveraged various features in excel such as charts, pivot tables and conditional formatting to create an interactive
             dashboard for bike sales through the available open source data. 
             
             """
         )
         st.markdown("[View Project...](https://github.com/bernadettemm/data-analysis-projects/blob/main/Excel%20Dashboard.xlsx)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
         st.image(project3) 
    with text_column:
         st.subheader("Web Development")
         st.write(
             """
             Designed and developed the website for Afya Intelligence, a healthcare technology company. The website showcases the 
             company's services and success stories in a modern and user-friendly format, and is optimized for search engines. Deployed 
             google analytics for traffic monitoring.
             
             """
         )
         st.markdown("[View Project...](https://github.com/bernadettemm/data-analysis-projects/blob/main/Excel%20Dashboard.xlsx)")

# --- CONTACT ---
with st.container():
    st.write("---")
    st.header("Contact me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/helloberna22@gmail.com" method="POST">
     <input type= "hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Message" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()





