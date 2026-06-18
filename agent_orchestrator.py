import datetime

class DataAgent:
    """Specialized agent for parsing and structuring raw data payloads."""
    def execute(self, task_input: str) -> dict:
        print(" -> [DataAgent Active]: Extracting entities and structures...")
        return {
            "processed_by": "Data_Analysis_Module_v1",
            "timestamp": str(datetime.datetime.now()),
            "result": f"Extracted metrics from tracking payload: '{task_input}'"
        }

class CodeAgent:
    """Specialized agent for syntax construction and architectural logic."""
    def execute(self, task_input: str) -> dict:
        print(" -> [CodeAgent Active]: Generating syntax blocks...")
        return {
            "processed_by": "Syntax_Generation_Module_v1",
            "timestamp": str(datetime.datetime.now()),
            "result": f"Generated structural logic template for: '{task_input}'"
        }

class AgentOrchestrator:
    """Master controller that classifies intent and routes tasks to specialized assets."""
    def __init__(self):
        # Initialize the specialized workforce
        self.data_sub_agent = DataAgent()
        self.code_sub_agent = CodeAgent()

    def _classify_intent(self, user_input: str) -> str:
        """Internal routing classifier (Heuristic Intent Engine)."""
        input_lower = user_input.lower()
        
        # Logic vectors to evaluate intent
        if any(keyword in input_lower for keyword in ["analyze", "data", "metrics", "parse", "format"]):
            return "DATA_TASK"
        if any(keyword in input_lower for keyword in ["code", "script", "function", "build", "algorithm"]):
            return "CODE_TASK"
        
        return "GENERAL_TASK"

    def route_and_execute(self, user_input: str) -> dict:
        print(f"\n[Orchestrator]: Intercepted prompt: '{user_input}'")
        intent = self._classify_intent(user_input)
        print(f"[Orchestrator]: Classified intent as -> {intent}")

        # Routing matrix
        if intent == "DATA_TASK":
            execution_payload = self.data_sub_agent.execute(user_input)
        elif intent == "CODE_TASK":
            execution_payload = self.code_sub_agent.execute(user_input)
        else:
            execution_payload = {
                "processed_by": "Default_Core",
                "result": "Prompt fell outside specialized domain parameters. Handled by fallback model."
            }

        return {
            "status": "Execution_Complete",
            "detected_intent": intent,
            "payload": execution_payload
        }

if __name__ == "__main__":
    # Initialize the engine
    master_orchestrator = AgentOrchestrator()
    
    # Test Case 1: Trigger Data Routing
    response_one = master_orchestrator.route_and_execute("Analyze the user growth metrics dataset.")
    print(f"System Response: {response_one}\n")
    
    # Test Case 2: Trigger Code Routing
    response_two = master_orchestrator.route_and_execute("Build a quick python function for sorting.")
    print(f"System Response: {response_two}\n")