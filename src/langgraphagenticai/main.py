import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit


def load_langgraph_agenticai_app():

    st.set_page_config(layout="wide")

    # Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error in loading user inputs from the UI.")
        return

    user_message = st.chat_input("Enter your message")

    if not user_message:
        return

    try:
        # Configure LLM
        obj_llm_config = GroqLLM(user_controls_input=user_input)
        model = obj_llm_config.get_llm_model()

        if model is None:
            st.error("Error in configuring the LLM model.")
            return

        # Get usecase
        usecase = user_input.get("selected_usecase")

        if usecase is None:
            st.error("No use case selected.")
            return

        # Graph builder
        graph_builder = GraphBuilder(model)

        graph = graph_builder.setup_graph(usecase)

        DisplayResultStreamlit(
            usecase,
            graph,
            user_message
        ).display_result_on_ui()

    except Exception as e:
        st.exception(e)
