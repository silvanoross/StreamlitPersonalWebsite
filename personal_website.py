# imports
import streamlit as st
import os
import webbrowser

# Create tabs

tab1, tab2, tab3 = st.tabs(["Overview", "Examples", "Music"])

# tab 1 overview
with tab1:
    st.markdown("# Portfolio - Silvano Ross")
    st.image('./images/avatar_1.jpg', caption='Avatar created using Lensi AI')
    with st.expander(label="Blurb: "):
        st.write("""
        He started in science and began to migrate into tech after deciding to follow a spark of an interest.
        Silvano possesses strong analytical skills through research, healthcare and clinical diagnostic experience.
        He prides himself in being an enthusiastic learner and avid coder. At the beginning of his career he was a chef
        and worked in the catering industry. While earning his Bachelor's of Science in biochemistry through the 
        University of Washington he joined a neuroscience research lab. Here he practiced analysis within the scope of research
        and took on an independent project management role. After he concluded his experiments and was part of a team to publish in 
        a high impact scientific journal he decided to explore the world of healthcare. Silvano has a personal tie to health care and wanted
        to be an asset in this community as his mother was cured of stage four melanoma while he was growing up. He joined 
        Bloodworks Northwest initially as a phlebotomist, but quickly found his way back into the laboratory space when a 
        job opened up in the histocompatibility laboratory. 
        
        His current role uses a SQL coded database and practices heavy analysis and review on data for clinical patients. This ultimately sparked
        an interest in learning how to program and use databases in more depth. Silvano first took introductory courses in programming and 
        relational databases in SQL. Eventually, he enrolled in a certificate program in financial technology to enhance his python programming skills
        and develop expertise in machine learning and blockchain technology. 
        
        Going forward he wants to pursue a career in tech and will be applying to the Master's of Science in Information Management through the
        University of Washington with a specialty in Data Science. 
     """)


# tab 2 examples

# tab 3 music

with tab3:
    st.header("Musical History")
    st.write("give me your dreams")
    audio_file = open('./audio/give me your dreams.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    
    st.write("yearn")
    audio_file = open('./audio/yearn.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    
    
    


# create repository of projects
projects = {
    "Blockchain Ledger": 'https://github.com/silvanoross/Block_Chain_Ledger',
    "Chicken Futures": 'https://github.com/silvanoross/Meat_Predictor',
    "AWS Robo Advisor": 'https://github.com/silvanoross/AWS_Robo_Adviser',
    "Predicting Success": 'https://github.com/silvanoross/Predicting_Success',
    "Crypto Notifier": 'https://github.com/silvanoross/Crypto_Notifier',   
}

project_list = []
for key, value in projects.items():
    project_list.append(key)

# Markdown sidebar
st.sidebar.markdown("# Past Projects")
# create sidebar to make selection
project = st.sidebar.selectbox(
    "Select project to view",
    project_list
)

# go to link associated with project
if st.sidebar.button("Go to Project"):
    webbrowser.open(projects[project])

