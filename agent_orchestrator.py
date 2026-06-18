import datetime
import json
import os

class DataAgent:
    def execute(self, task_input: str) -> dict:
        print(" -> [DataAgent]: Processing metrics/dataset payload...")
        return {
            "processed_by": "data_worker_v1",
            "result": f"Extracted operational metrics from: '{task_input}'"
        }

class CodeAgent:
    def execute(self, task_input: str) -> dict:
        print(" -> [CodeAgent]: Executing logic synthesis...")
        return {
            "processed_by": "code_worker_v1",
            "result": f"Generated logic structures for: '{task_input}'"
        }

class AgentOrchestrator:
    def __init__(self, memory_file="session_memory.json"):
        self.data_sub_agent = DataAgent()
        self.code_sub_agent = CodeAgent()
        self.memory_file = memory_file
        
        # Heuristic routing matrices
        self.data_matrix = ["analyze", "data", "metrics", "parse", "format", "dataset", "trends", "numbers"]
        self.code_matrix = ["code", "script", "function", "build", "algorithm", "implementation", "binary", "tree"]
        
        # Initialize persistent storage file if it doesn't exist
        if not os.path.exists(self.memory_file):
            with open(self.memory_file, 'w') as f:
                json.dump([], f)

    def _load_memory(self) -> list:
        """Reads the historical session log from the local disk."""
        with open(self.memory_file, 'r') as f:
            return json.load(f)

    def _write_memory(self, log_entry: dict):
        """Appends the latest execution lifecycle data to the persistent store."""
        history = self._load_memory()
        history.append(log_entry)
        with open(self.memory_file, 'w') as f:
            json.dump(history, f, indent=4)

    def _classify_intent(self, user_input: str) -> str:
        """Evaluates request vectors using a local score matrix."""
        normalized_input = user_input.lower()
        data_score = sum(1 for token in self.data_matrix if token in normalized_input)
        code_score = sum(1 for token in self.code_matrix if token in normalized_input)
        
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
            execution_payload = {"processed_by": "core_fallback", "result": "Default routine."}

        # Construct the historical tracking log
        runtime_log = {
            "timestamp": str(datetime.datetime.now()),
            "user_prompt": user_input,
            "resolved_route": intent,
            "worker_response": execution_payload["result"]
        }
        
        # Commit log to persistent disk memory
        self._write_memory(runtime_log)
        print(f" -> [System]: Execution state successfully archived to {self.memory_file}")

        return execution_payload

if __name__ == "__main__":
    engine = AgentOrchestrator()
    
    # Executing the live test routines
    engine.route_and_execute("Build a function that outputs binary trees.")
    engine.route_and_execute("Parse the financial metrics dataset.")