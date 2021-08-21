# Import necessary libraries
import streamlit as st
import pandas as pd
import time

# Get the data and process it for each of the players
MJ_data = pd.read_excel("Data\Michael-Jordan.xlsx")
MJ_data = MJ_data.loc[0:18]

LJ_data = pd.read_excel("Data\LeBron-James.xlsx")
LJ_data = LJ_data.loc[0:17]

KAJ_data = pd.read_excel("Data\Kareem-Abdul-Jabbar.xlsx")

SN_data = pd.read_excel("Data\Shaquille-O'Neal.xlsx")
SN_data = SN_data.loc[0:20]

TD_data = pd.read_excel("Data\Tim-Duncan.xlsx")
TD_data = TD_data.loc[0:18]


# Title of the app
st.title("Top 5 Basketball Players Stats Comparison App")

# Sidebar to select the stat to compare
stat_selectbox = st.sidebar.selectbox(
    "Stats",
    ("", "Minutes Played Per Game", "Field Goals", "3 Point Field Goals Per Game", "2 Point Field Goals Per Game",
     "Total Rebounds Per Game", "Assists Per Game", "Steals Per Game", "Blocks Per Game", "Points Per Game")
)

if stat_selectbox == "" :
    st.header("Description")
    st.write("This is a web app that compares various stats of the top 5 basketball players "
             "(according to fox news). On the left is a sidebar that allows you to select the stat that you want to "
             "compare.")

    st.header("Data")
    st.write("The data was retrieved from https://www.basketball-reference.com/. Some of the data is missing "
             "which is why there are gaps in some of the line charts.")
    
    st.header("Graphs")
    st.write("The graphs of the data have 5 lines which represent the 5 players that are being compared. "
             "There is a legend to the right of the graphs which has the player and the color of the line "
             "the players data is.")
    
    st.header("GitHub Link")
    st.write("")

if stat_selectbox == "Minutes Played Per Game":
    st.header("Minutes Played Per Game")

    progress_bar = st.progress(0)
    
    MP_agg = pd.DataFrame([MJ_data.MP, LJ_data.MP, KAJ_data.MP, SN_data.MP, TD_data.MP], 
    index=["Michael Jordan", "LeBron James", "Kareem Abdul-Jabbar", "Shaquille O'Neal", "Tim Duncan"])
    MP_agg = MP_agg.swapaxes("index", "columns")
    st.line_chart(MP_agg)

    for percent_complete in range(100):
        progress_bar.progress(percent_complete + 1)

if stat_selectbox == "Field Goals":
    st.header("Field Goals Per Game")

    progress_bar = st.progress(0)

    FG_agg = pd.DataFrame([MJ_data.FG, LJ_data.FG, KAJ_data.FG, SN_data.FG, TD_data.FG], 
    index=["Michael Jordan", "LeBron James", "Kareem Abdul-Jabbar", "Shaquille O'Neal", "Tim Duncan"])
    FG_agg = FG_agg.swapaxes("index", "columns")    
    st.line_chart(FG_agg)

    for percent_complete in range(100):
        progress_bar.progress(percent_complete + 1)

if stat_selectbox == "3 Point Field Goals Per Game":
    st.header("3 Point Field Goals Per Game")

    progress_bar = st.progress(0)

    FG3P_agg = pd.DataFrame([MJ_data["3P"], LJ_data["3P"], KAJ_data["3P"], SN_data["3P"], TD_data["3P"]], 
    index=["Michael Jordan", "LeBron James", "Kareem Abdul-Jabbar", "Shaquille O'Neal", "Tim Duncan"])
    FG3P_agg = FG3P_agg.swapaxes("index", "columns")    
    st.line_chart(FG3P_agg)

    for percent_complete in range(100):
        progress_bar.progress(percent_complete + 1)

if stat_selectbox == "2 Point Field Goals Per Game":
    st.header("2 Point Field Goals Per Game")

    progress_bar = st.progress(0)

    FG2P_agg = pd.DataFrame([MJ_data["2P"], LJ_data["2P"], KAJ_data["2P"], SN_data["2P"], TD_data["2P"]], 
    index=["Michael Jordan", "LeBron James", "Kareem Abdul-Jabbar", "Shaquille O'Neal", "Tim Duncan"])
    FG2P_agg = FG2P_agg.swapaxes("index", "columns")    
    st.line_chart(FG2P_agg)

    for percent_complete in range(100):
        progress_bar.progress(percent_complete + 1)

if stat_selectbox == "Total Rebounds Per Game":
    st.header("Total Rebounds Per Game")

    progress_bar = st.progress(0)

    TRB_agg = pd.DataFrame([MJ_data["TRB"], LJ_data["TRB"], KAJ_data["TRB"], SN_data["TRB"], TD_data["TRB"]], 
    index=["Michael Jordan", "LeBron James", "Kareem Abdul-Jabbar", "Shaquille O'Neal", "Tim Duncan"])
    TRB_agg = TRB_agg.swapaxes("index", "columns")    
    st.line_chart(TRB_agg)
    
    for percent_complete in range(100):
        progress_bar.progress(percent_complete + 1)

if stat_selectbox == "Assists Per Game":
    st.header("Assists Per Game")

    progress_bar = st.progress(0)

    AST_agg = pd.DataFrame([MJ_data["AST"], LJ_data["AST"], KAJ_data["AST"], SN_data["AST"], TD_data["AST"]], 
    index=["Michael Jordan", "LeBron James", "Kareem Abdul-Jabbar", "Shaquille O'Neal", "Tim Duncan"])
    AST_agg = AST_agg.swapaxes("index", "columns")    
    st.line_chart(AST_agg)

    for percent_complete in range(100):
        progress_bar.progress(percent_complete + 1)

if stat_selectbox == "Steals Per Game":
    st.header("Steals Per Game")

    progress_bar = st.progress(0)

    STL_agg = pd.DataFrame([MJ_data["STL"], LJ_data["STL"], KAJ_data["STL"], SN_data["STL"], TD_data["STL"]], 
    index=["Michael Jordan", "LeBron James", "Kareem Abdul-Jabbar", "Shaquille O'Neal", "Tim Duncan"])
    STL_agg = STL_agg.swapaxes("index", "columns")    
    st.line_chart(STL_agg)

    for percent_complete in range(100):
        progress_bar.progress(percent_complete + 1)

if stat_selectbox == "Blocks Per Game":
    st.header("Blocks Per Game")

    progress_bar = st.progress(0)

    BLK_agg = pd.DataFrame([MJ_data["BLK"], LJ_data["BLK"], KAJ_data["BLK"], SN_data["BLK"], TD_data["BLK"]], 
    index=["Michael Jordan", "LeBron James", "Kareem Abdul-Jabbar", "Shaquille O'Neal", "Tim Duncan"])
    BLK_agg = BLK_agg.swapaxes("index", "columns")    
    st.line_chart(BLK_agg)

    for percent_complete in range(100):
        progress_bar.progress(percent_complete + 1)

if stat_selectbox == "Points Per Game":
    st.header("Points Per Game")

    progress_bar = st.progress(0)

    PTS_agg = pd.DataFrame([MJ_data["PTS"], LJ_data["PTS"], KAJ_data["PTS"], SN_data["PTS"], TD_data["PTS"]], 
    index=["Michael Jordan", "LeBron James", "Kareem Abdul-Jabbar", "Shaquille O'Neal", "Tim Duncan"])
    PTS_agg = PTS_agg.swapaxes("index", "columns")    
    st.line_chart(PTS_agg)

    for percent_complete in range(100):
        progress_bar.progress(percent_complete + 1)