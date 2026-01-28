import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI




def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with streamlit UI.
    This function intialize the UI,Handles users input, configure the LLM model,
    sets up the graph based on the selected use case,and display the output while 
    implementing exceptions handling for robustness.
    """
    
    
    ## load Ui
    
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()
    
    
    if not user_input:
        st.error("Error in loading user inputs from the UI.")
        return
    
    user_message=st.chat_input("Enter your message:")
    
   
    