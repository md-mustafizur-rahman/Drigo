import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.llm import OllamaLLM

def test_ollama():
    print("--- Ollama Integration Test ---")
    llm = OllamaLLM()
    
    prompt = "Translate 'Hello, how can I help you today?' into Bengali."
    print(f"[*] Prompt: {prompt}")
    
    try:
        print("[*] Thinking...", end="", flush=True)
        response = llm.generate_response(prompt)
        # Clear "Thinking..." line
        print("\r" + " " * 30 + "\r", end="", flush=True)
        
        print("\n" + "="*50)
        print("🤖 DRIGO AI RESPONSE".center(50))
        print("="*50)
        print(f"{response}")
        print("="*50 + "\n")
        
        if "LLM ERROR" in response:
            print("\n[!] Test FAILED: Check if Ollama is running and the model is pulled.")
        else:
            print("\n[V] Test PASSED: Ollama is responding correctly.")
            
    except Exception as e:
        print(f"\n[!] Test CRASHED: {e}")

if __name__ == "__main__":
    test_ollama()
