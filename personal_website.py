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
        st.write("""During freelance work as a Data Analyst I am helping to create innovative visualizations and statistics for the Wilkie lab
                at the University of Texas Southwestern. Using programming and science to advance knowledge in health is one of my passions. 
                This project highlights how KCG (Gna15 knockout) mice show less lesion development early on 
                in a mouse's lifecycle. These G-protein knockout mice are research analogs for pancreatic cancer found in human. Gna15 is a G-protein coupled receptor
                that has been proven to 
                play an important role in a distinct mechanism for early pancreatic carcinogenisis.
                There are additional clinical studies occurring in conjunction with these murine studies to help develop better treatments for pancreatic cancer.
                Here are some following examples from the experiments:""")
        st.markdown("""**Innamorati, G., Wilkie, T.M., 
                Malpeli, G. et al. Gα15 in early onset of pancreatic ductal adenocarcinoma. Sci Rep 11, 14922 (2021). https://doi.org/10.1038/s41598-021-94150-3**""")
        image1, image2, dual_image = Image.open('./images/KC_ADM.png'), Image.open('./images/KCG_ADM.png'), Image.open('./images/no_adm_combo.png')
        pie_chart_one, pie_chart_two = Image.open('./images/KCG_Lesion_Pie.png'), Image.open('./images/KC_Lesion_Pie.png')

        st.image(image2, caption='Tumor Lesion Size, Score and Presence of Acinar-to-Ductal Metaplasia')
        st.write("""The above depicts sections of the mouse pancrease for the test cohort showing 
                lesion score as size of the blue dots and presence of ADM with a black ring encompassing the blue dots. 
                The below image shows the difference in total lesion scores between both the test and
                control groups""")
        st.image(dual_image, caption='I changed the color scheme to highlight the different scores and took out the encompassing circles indicating ADM. \n'
                 'This is intended to make the figure align with the colors of the pie charts below.')
        st.markdown("#### Observing the difference between the two groups ")
        image3, image4 = Image.open('./images/KC_pruned_pie.png'), Image.open('./images/KCG_pruned_pie.png')
        st.image(pie_chart_one, caption="These are the total number of fields with lesions of score 0-4 for the knockout group")
        st.image(pie_chart_two, caption="These are the total number of fields with lesions of score 0-4 for the control group")
    
    with tab2_2:
        st.markdown("#### Future of Chicken")
        st.write("""Due to inflation reaching a high of around 7% 
                in 2021 our group thought it would be interesting to predict chicken price changes in the coming year. 
                With data taken from Kaggle on bulk chicken prices, we wanted to see if it will be feasible to include chicken as part of our diet
                in the next year. 
                We were also curious about the seasonality of chicken prices and when the best time to buy chicken may
                be as a consumer. We even took another scope for our project where we assumed we were chicken farmers or investors looking to buy chicken futures 
                and wanted to know the best time to either sell our chicken as farmers or invest in chicken futures.
                
                Reference - https://www.bls.gov/cpi/""")
        image5 = Image.open('./images/prophet_three_changepoints.png')
        image6 = Image.open('./images/seasonality_trends.png')
        st.image(image5, caption="")
        st.write("""Using Facebook's Prophet time-series predicting software we can see how much a pound of 
                chicken could end up being in the next year. We can see it is predicted to steadily increase with variability
                in seasonality. We can also see a noteworthy changepoint where the volitility in chicken price starts to 
                increase.""")
        st.image(image6, caption="")
        st.write("""Using Prophet's trends feature we can investigate how chicken price fluctuates on a monthly bases
                during a yearly period. We were able to find that following February of most years, chicken price increases
                by about 60% from where it was at the start of the year. Its value remains high during the summer months
                and slowly decreases going into the winter months.""")
    with tab2_3:
        st.markdown("#### AWS Robo Advisor - Lexbot")
        st.write("""This project showcases the Lex bot offered through Amazon Web Services with the incorporation of a Lambda function. 
                 I have used Natural Language Processing to handle a simple task of giving investment advice for a given portfolio based
                 on risk chosen by the user. Below is a GIF of how the robo advisor works:""")
        video_file = open("./videos/Lex_Bot_Full.mp4", "rb")
        video_bytes = video_file.read()
        st.video(video_bytes)
        st.write("The reason the text processing goes so fast is due to a time constraint on the recording imposed for this project.")
        st.markdown("##### Backend") 
        image7 = Image.open("./images/full_function.png")
        image8 = Image.open("./images/validation_function.png")
        image9 = Image.open("./images/recommendation_function.png")
        st.write("#### Lambda Functions on AWS for Lexbot")
        st.write("###### Full recommendation function")
        st.image(image7) 
        st.write("""The recommendation function grabs the slots from the Lexbot after the user enters them into the chat.
                 The slots are passed through a verification process to ensure the correct data types have been entered.
                 Finally, a recommendation is retrieved after the algorithm has processed the information entered
                 by the user.""")
        st.write("###### Validation of data function")
        st.image(image8) 
        st.write("""The validation function ensures the proper data types have been entered for the corresponding slots.
                 The bot only gives portfolio recommendations for those between the ages of 21 and 65. Additionally
                 the investment amount needs to be greater than $5000 otherwise the bot will not proceed to a recommendation.
                 Part of natural language processing is handling human errors in text entry. For the risk-level slot
                 the user must enter 'Low', 'Medium', or 'High' with respect to risk otherwise the slot will not get filled.""")
        st.write("###### Recommendation handler function")
        st.image(image9)  
        st.write("""The final function defines the recommendations given to the user after all the information has been processed.
                 You can see that the slots entered by the user are pulled into an f-string that contains the 
                 ultimate recommendation.""")      
    
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
        
        st.write("""The deployer contract sets up the Kasei Coin for use in an Ethereum Virtual Machine.
                 The contract inhereit smart contract standards from Open Zeppelin. The ERC20 Mintable solidity 
                 contract prevents abuse of cryptocurrency technology by implementing SafeMath and includes important
                 smart contract details requiring a coin name, its symbol and the base decimal value of 18 - an
                 ethereum standard.""")
        
        st.write("""The crowdsale contract also inherits standard contracts from OpenZeppelin that allow the 
                 transfer of ownership of the deployed coin contract from above and give the person who earns
                 the crowdsale of the coin the minter role empowering them to transfer coins and perform other 
                 administrative like abilities.""")
        col1, col2, col3= st.columns(3)
        with col1:
            st.header("Crowdsale Contract")
            st.image(image10_1)
            st.write("""In the Remix IDE used to deploy and parameterize the ethereum-based coins the user
                     is able to set up the crowdsale and rate of the Kasei coin.""")
        with col2:
            st.header("ERC20 Coin Constructor")
            st.image(image11)
            st.write("""The user who mints the Kasei coin has many built in standard functions that come along
                     with the inherited contracts. The owner of the contrat can do things like add minters, 
                     renounce minters, set allowance amounts and have veto power over transactions taking place
                     with the Kasei coin.""")
        with col3:
            st.header("Purchase in Metamask")
            st.image(image13)
            st.write("""Metamask is a third-party crypto wallet that is used to verify the coins were 
                     created and verifiably purchased. Here we can see the Kasei coin created was recognized
                     at the address loaded into Metamask.""")
        st.markdown("## Ganache Transaction")
        st.image(image12)
        st.write("""Using Ganache for a test ethereum development environment with preconstructed ether addresses 
                 we can see a transaction has occured where an address was associated with the creation of our Kasei coin.""")
        
        
    
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
                 historical percent change is based on daily percent changes for the last two years and set a 
                 baseline for normal volatility.""")
        st.image(image14)
        st.markdown("### Conditional Logic for Comparison")
        st.image(image15)
        st.markdown("### Twilio API Client")
        st.write("""The user enters their number at the beginning of the CLI application and after
                 they choose coins of interest they can get a rather lengthy text message highlighting 
                 the specific days with significant price swings. Because cryptocurrencies are naturally volatile many dates 
                 show up with alerts that a significant price change had occurred.""")
        col5, col6, col7 = st.columns(3)
        with col5:
            st.image(image16, )
        
        
# tab 1 overview
with tab1:
    st.markdown("## Silvano Ross")
    st.image('./images/me_professional.jpg', caption='Taken at the Arboretum')
    with st.expander(label="About Silvano - CLICK HERE"):
        st.write("""
        His career passion started in science with a desire to help others through research. While he still is a science enthusiast 
        his interests began to migrate into tech after deciding to follow a desire to learn how to program.
        Silvano possesses strong analytical skills through past research, healthcare and clinical diagnostic roles centered around improving
        health outcomes for others.
        
        He prides himself in being an enthusiastic learner and avid coder. At the beginning of his career he was a chef
        and worked in the catering industry. While earning his Bachelor's of Science in biochemistry through the 
        University of Washington (UW) he joined a neuroscience research lab. Here he practiced analysis within the scope of research
        and took on an independent project management role. After he concluded his independent experiments and was part of a team to publish in 
        a high impact scientific journal he decided to explore the world of healthcare. Silvano has a personal tie to health care and wanted
        to be an asset in this community. His mother was cured of stage four melanoma and he wants to give back to the world that allowed her to stay in his life. He joined 
        Bloodworks Northwest initially as a phlebotomist, but quickly found his way back into the laboratory space when a 
        job opened up in the histocompatibility laboratory. 
        
        His current role uses a SQL coded database and practices heavy analysis and review on data for clinical patients in need of solid organs and other specialty diagnostics. 
        The heavy use of data analysis in both the research and clinical settings ultimately sparked an interest in learning how to program and use databases to improve the 
        quality of life for others. Silvano first took introductory courses in programming and 
        relational databases in SQL. Eventually, he enrolled in a certificate program in financial technology to enhance his python programming skills
        and develop foundational knowledge in machine learning. 
        
        Going forward he wants to pursue a career in tech as a Data Scientist and has been accepted into the Data Science certificate program
        offered through UW and the Master's of Science in Information Management program with a specialization in Data Science at UW as well. 
     """)




# tab 3 music

with tab3:
    st.header("Musical History")
    if st.button("Amazon Music"):
        webbrowser.open('https://music.amazon.com/albums/B0BQBHKXQY?marketplaceId=ATVPDKIKX0DER&musicTerritory=US&ref=dm_sh_GkdoO59L4CSyQSX32inw6masV')
    if st.button("SoundCloud"):
         webbrowser.open("https://soundcloud.com/vino-blanco-572551774/sets/terra-firma")
    if st.button("Spotify"):
         webbrowser.open("https://open.spotify.com/album/6dlzSbn1iKovlj8QRvJYvM")
    with st.expander(label="Blurb About Music - CLICK ME"):
        st.write("""Having a creative outlet is incredibly important to me. During my free time I love to learn
                 new hobbies and hone different skills. Having grown up playing in jazz bands music stays close to my heart.
                 With a newfound love for singing I try to perfect this skill while also using programming to craft beats
                 that pay homage to my musical background. I encorporate modern day production techniques with an oldschool feel into my pieces. 
                 Here are a few songs from my album, Terra Firma, out on Itunes and Sound Cloud""")
        
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








