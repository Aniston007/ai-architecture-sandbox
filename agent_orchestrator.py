import datetime

class DataAgent:
    """Handles parsing, entity extraction, and formatting for raw data inputs."""
    def execute(self, task_input: str) -> dict:
        print(" -> [DataAgent]: Processing metrics/dataset payload...")
        return {
            "processed_by": "data_worker_v1",
            "timestamp": str(datetime.datetime.now()),
            "result": f"Extracted operational metrics from: '{task_input}'"
        }

class CodeAgent:
    """Handles logic generation, algorithm construction, and code formatting."""
    def execute(self, task_input: str) -> dict:
        print(" -> [CodeAgent]: Executing logic synthesis...")
        return {
            "processed_by": "code_worker_v1",
            "timestamp": str(datetime.datetime.now()),
            "result": f"Generated logic structures for: '{task_input}'"
        }

class AgentOrchestrator:
    """Master controller handling runtime classification and sub-agent task routing."""
    def __init__(self):
        self.data_sub_agent = DataAgent()
        self.code_sub_agent = CodeAgent()
        
        # Pre-compiled high-impact matrix categories for strict intent isolation
        self.data_matrix = ["analyze", "data", "metrics", "parse", "format", "dataset", "trends", "numbers"]
        self.code_matrix = ["code", "script", "function", "build", "algorithm", "implementation", "binary", "tree"]

    def _classify_intent(self, user_input: str) -> str:
        """Evaluates request vectors using a local score matrix to determine target path."""
        print(" -> [Orchestrator]: Analyzing text vector matching...")
        
        normalized_input = user_input.lower()
        
        # Calculate matrix intersection scores
        data_score = sum(1 for token in self.data_matrix if token in normalized_input)
        code_score = sum(1 for token in self.code_matrix if token in normalized_input)
        
        # Route execution based on highest vector alignment
        if data_score > code_score and data_score > 0:
            return "DATA_TASK"
        elif code_score > data_score and code_score > 0:
            return "CODE_TASK"
        
        return "GENERAL_TASK"

    def route_and_execute(self, user_input: str) -> dict:
        print(f"\n[Orchestrator]: Intercepted runtime prompt: '{user_input}'")
        intent = self._classify_intent(user_input)
        print(f"[Orchestrator]: Route resolved -> {intent}")

        if intent == "DATA_TASK":
            execution_payload = self.data_sub_agent.execute(user_input)
        elif intent == "CODE_TASK":
            execution_payload = self.code_sub_agent.execute(user_input)
        else:
            execution_payload = {
                "processed_by": "core_fallback_routine",
                "result": f"Handled by default routing profile. Reason: Ambiguous text structure."
            }

        return {
            "status": "success",
            "resolved_route": intent,
            "output": execution_payload
        }

if __name__ == "__main__":
    # Internal test matrix execution
    engine = AgentOrchestrator()
    
    # Target Route: DATA_TASK
    dataset_test = engine.route_and_execute("Can you look over these quarterly projection numbers and break down the core trends?")
    print(f"Payload Return: {dataset_test}\n")
    
    # Target Route: CODE_TASK
    algorithm_test = engine.route_and_execute("Give me an implementation of a binary search tree layer.")
    print(f"Payload Return: {algorithm_test}\n")