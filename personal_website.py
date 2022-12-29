# imports
import streamlit as st
import os
import webbrowser
from pathlib import Path
from PIL import Image
import webbrowser
import urllib.request


# Create Header for Website
st.markdown("# Welcome to Silvano Ross's Portfolio")

# Create tabs
tab2, tab1, tab3 = st.tabs(["Examples","Overview", "Music"])

# tab 2 examples
with tab2:
    tab2_names = ["Pathogenisis of Pancreatic Cancer in Mice", "Future of Chicken", "AWS Robo Advisor", "Kasei Coin", "Crypto Notifier"]
    tab2_1, tab2_2, tab2_3, tab2_4, tab2_5 = st.tabs(tab2_names)
   
    st.write("-------------------------------------------------------------------------------------------------------")
    with tab2_1:
        st.markdown("#### Pathogenesis of Pancreatic Cancer in Mice")
        st.write("""During freelance work as a Data Analyst I started creating visualizations and statistics for a lab
                at the University of Texas Southwestern. Using programming to advance health and humanity is one of the many 
                passions that I hold. Here are some following examples:""")
        image1, image2 = Image.open('./images/KC_ADM.png'), Image.open('./images/KCG_ADM.png')

        st.image(image2, caption='Tumor Lesion Size, Score and Presence of Acinar-to-Ductal Metaplasia')
        st.write("""The above depicts what the sections of pancrease in the test cohort look like in terms of 
                lesion score and presence of ADM. 
                The below shows the difference in total lesion 
                scores between both the test and
                control groups""")
        image3, image4 = Image.open('./images/KC_pruned_pie.png'), Image.open('./images/KCG_pruned_pie.png')
        st.image(image3, caption="")
        st.image(image4, caption="")
    
    with tab2_2:
        st.markdown("#### Future of Chicken")
        st.write("""Due to inflation for the last 12 months for food at a high of roughly 10% 
                we thought it would be interesting to try and predict how prices will rise in the coming year 
                with respect to chicken. The group I was a part of are all meat eaters and we want to see if 
                it will be feasible to include this part of our diet in our budgets to come. 
                We were also curious about the seasonality of chicken prices and when the best time to buy chicken may
                be. Assuming we were chicken farmers or investors looking to buy chicken futures when would be the best 
                time to invest.
                
                Reference - https://www.bls.gov/cpi/""")
        image5 = Image.open('./images/prophet_three_changepoints.png')
        image6 = Image.open('./images/seasonality_trends.png')
        st.image(image5, caption="")
        st.write("""Using Facebook's Prophet time-series predicting software we can see how much a pound of 
                chicken could end up being in the next. We can see it is predicted to steadily increase with variability
                in seasonality. We can also see a noteworthy changepoint where the volitility in chicken price starts to 
                increase.""")
        st.image(image6, caption="")
        st.write("""Using Propeht's trends feature we can investigate how chicken price fluctuates on a monthly bases
                during a yearly period. We were able to find that following February of most years chicken price increases
                by about 60% from where it was at the start of the year. Its value remains high during the summer months
                and slowly decreases going into the winter months.""")
    with tab2_3:
        st.markdown("#### AWS Robo Advisor")
        st.write("""This project showcases the Lex bot offered through Amazon Web Services. I have used Natural 
                 Language Processing to handle a simple task of giving investment advice for a given portfolio based
                 on risk chosen by the user. Below is a GIF of how the robo advisor works:""")
        video_file = open("./videos/Lex_Bot_Full.mp4", "rb")
        video_bytes = video_file.read()
        st.video(video_bytes)
        st.markdown("##### Backend") 
        image7 = Image.open("./images/full_function.png")
        image8 = Image.open("./images/validation_function.png")
        image9 = Image.open("./images/recommendation_function.png")
        st.write("Full recommendation function")
        st.image(image7) 
        st.write("Validation of data function")
        st.image(image8) 
        st.write("Recommendation handler function")
        st.image(image9)        
    
    with tab2_4:
        st.markdown("#### Kasei Coin")
        st.write("""This project creates smart contracts on an ethereum virtual
                 network using ERC20 protocols. The smart contracts are coded in Solidity and test accounts
                 are taken from the Ganache app and connected to the ethereum virtual machine through Metamask. 
                 New coins are minted through transactions by non contract owners. 
                 The balances are shown before and after the contracts are used and the newly minted coin shows up 
                 in Metamask.""")
        image10 = Image.open("./images/deployer_compile.png")
        image10_1 = Image.open("./images/connected_crowdsale.png")
        image11 = Image.open("./images/connected_KaseiCoin.png")
        image12 = Image.open("./images/significant_buy_ganache.png")
        image13 = Image.open("./images/significant_buy_metamask.png")
        st.markdown("## Deployer Contract")
        st.image(image10)
        col1, col2, col3= st.columns(3)
        with col1:
            st.header("Crowdsale Contract")
            st.image(image10_1)
        with col2:
            st.header("ERC20 Coin Constructor")
            st.image(image11)
        with col3:
            st.header("Purchase in Metamask")
            st.image(image13)
        st.markdown("## Ganache Transaction")
        st.image(image12)
    
    with tab2_5:
        st.markdown("#### Crypto Notifier App")
        st.write("""A Twilio, CoinGecko API, and pandas showcase. A user chooses a cryptocurrency from a premade list.
                 Cryptocurrency data for the coins of interest are taken from the CoinGecko API 
                 and passed into a pandas dataframe. A threshold for noteworthy changes has been created by taking three
                 years of past price changes and finding the absolute average for the coins listed. If in the past two
                 weeks any of these coins have been more volatile than what they have historically been known to be the
                 user gets a text message with the date and coin for when the volatility occurred.""")
        image14 = Image.open("./images/2_week_pct_change.png")
        image15 = Image.open("./images/conditional_logic.png")
        image16 = Image.open("./images/text_message.png")
        st.markdown("### Coin Gecko API Pull")
        st.write("""After pulling two weeks worth of recent prices, we compare each day's 
                 percent change to a historical absolute average daily percent change for each token. Our
                 historical percent change is based on daily percent changes for the last two years""")
        st.image(image14)
        st.markdown("### Conditional Logic for Comparison")
        st.image(image15)
        st.markdown("### Twilio API Client")
        st.write("""The user enters their number at the beginning of the CLI application and after
                 they choose the coins they want a report on they get a rather lengthy text message highlighting 
                 which days has significant price swings. Because cryptocurrencies are naturally volatile many dates 
                 show up with alerts that a significant price change had occurred.""")
        col5, col6, col7 = st.columns(3)
        with col5:
            st.image(image16, )
        
        
# tab 1 overview
with tab1:
    st.markdown("## Silvano Ross")
    st.image('./images/avatar_1.jpg', caption='Avatar created using Lensi AI')
    with st.expander(label="About Silvano - CLICK HERE"):
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




# tab 3 music

with tab3:
    st.header("Musical History")
    with st.expander(label="Blurb About Music - CLICK ME"):
        st.write("""Having a creative outlet is incredibly important to Silvano. During his free time he loves to learn
                 new hobbies and hone different skills. Having grown up playing in jazz bands music stays close to his heart
                 with a newfound love for singing he tries to perfect this skill while also using programming to craft beats
                 that pay homage to his background in jazz while also using modern day production techniques. Here are a few songs from 
                 his album, Terra Firma, out on Itunes and Sound Cloud""")
    image = Image.open('./images/album_artwork.png')
    st.image(image, caption='TERRA FIRMA Album 2022')
    st.write("GIVE ME YOUR DREAMS")
    audio_file = open('./audio/give me your dreams.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    
    st.write("YEARN")
    audio_file = open('./audio/yearn.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    
    st.write("HOLD ME IN")
    audio_file = open('./audio/hold me in.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    
    column1, column2, column3 = st.columns(3)
    
    # with column2:
    #     if st.button("Sound Cloud"):
    #         url = "https://soundcloud.com/vino-blanco-572551774"
    #         webbrowser.open(url)
    
    
    


# create repository of projects
projects = {
    "Full GitHub Link": 'https://github.com/silvanoross', 
    "Blockchain Ledger": 'https://github.com/silvanoross/Block_Chain_Ledger',
    "Future of Chicken": 'https://github.com/silvanoross/Meat_Predictor',
    "AWS Robo Advisor": 'https://github.com/silvanoross/AWS_Robo_Adviser',
    "Predicting Success": 'https://github.com/silvanoross/Predicting_Success',
    "Crypto Notifier": 'https://github.com/silvanoross/Crypto_Notifier',
    "Kasei Coin": 'https://github.com/silvanoross/KaseiCoin'
     
}

project_list = []
for key, value in projects.items():
    project_list.append(key)

# Markdown sidebar
st.sidebar.markdown("# GitHub Links")
# create sidebar to make selection
project = st.sidebar.selectbox(
    "Select project to view",
    project_list
)

# go to link associated with project
if st.sidebar.button("Go to Project"):
    webbrowser.open(projects[project])








