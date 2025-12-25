import streamlit 
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.gropllm import Gropllm 
from src.langgraphagenticai.graph.graph_builder import GraphBuilder


def load_langgraph_agenticai_app():


    # Load UI
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        streamlit.error("Error: Failed to load user input from the UI.")
        return 

    user_message=streamlit.chat_input("Enter your message:")

    if user_message:
        try:
            obj_llm_config=Gropllm(user_controls_input=user_input   )
            model=obj_llm_config.get_llm_model()    

            if not model:
                streamlit.error("Error: Failed to initialize the LLM model.")
                return
            
            usecase=user_input.get("SELECTED_USE_CASE")
            if not usecase:
                streamlit.error("Error: No use case selected.")
                return
            
            graph_builder=GraphBuilder(model=model)

            try:
                graph=graph_builder.setup_graph(usecase=usecase)
            
            except Exception as e:
                streamlit.error(f"Error setting up the graph: {e}")
                return
            
            



        except Exception as e: