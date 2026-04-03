import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

class OllamaLLM:
    def __init__(self):
        self.model = os.getenv("OLLAMA_MODEL", "qwen2.5:7b")
        self.url = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434/api/generate")

    def generate_streaming_response(self, prompt: str):
        """
        Sends a prompt to the Ollama API and yields the generated text chunks.
        """
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": True
        }

        try:
            response = requests.post(
                self.url,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=90,
                stream=True
            )
            response.raise_for_status()
            
            for line in response.iter_lines():
                if line:
                    data = json.loads(line.decode("utf-8"))
                    chunk = data.get("response", "")
                    if chunk:
                        yield chunk
                    if data.get("done"):
                        break

        except requests.exceptions.RequestException as e:
            error_msg = f"[LLM ERROR] Failed to connect to Ollama: {e}"
            print(f"\n{error_msg}")
            yield error_msg
        except Exception as e:
            error_msg = f"[LLM ERROR] An unexpected error occurred: {e}"
            print(f"\n{error_msg}")
            yield error_msg

    def generate_response(self, prompt: str) -> str:
        """
        Legacy wrapper for non-streaming response.
        """
        full_response = ""
        for chunk in self.generate_streaming_response(prompt):
            if "LLM ERROR" in chunk:
                return chunk
            full_response += chunk
        return full_response

if __name__ == "__main__":
    # Quick test
    llm = OllamaLLM()
    test_prompt = "Say hello!"
    print(f"Test Prompt: {test_prompt}")
    print(f"Response: {llm.generate_response(test_prompt)}")
