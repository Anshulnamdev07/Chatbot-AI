from src.langgraphagenticai.state.state import State


class BasicChatbotNode:
    """
    Basic Chatbot Login Implementation
    """
    def __init__(self, model):
        self.llm = model
        
    def process(self,state:State) -> dict:
        """
        Process the input state and generate a chatbot response using the LLM model.
        
        """
        return {"messages":self.llm.invoke(state["messages"])}
         