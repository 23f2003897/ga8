from google import genai
import hashlib
import json

# 1. Setup - Use the NEW client
client = genai.Client(api_key="AI")



# 2. Your Puzzle
puzzle = "Start with 2, multiply by 3, subtract 2, then divide by 2"
prompt = f"Solve this math puzzle step by step: {puzzle}. Return ONLY a JSON object with 'answer' (integer) and 'steps' (list of strings)."

try:
    # 3. Use the high-capacity stable model
    response = client.models.generate_content(
        model="gemini-flash-latest", 
        contents=prompt
    )

    # 4. Parse
    clean_text = response.text.strip().replace('```json', '').replace('```', '')
    data = json.loads(clean_text)
    
    answer = data["answer"]
    steps_count = len(data["steps"])

    # 5. Generate Hash
    email = "23f2003897@ds.study.iitm.ac.in"
    verify_input = f"{email}:{answer}:{steps_count}"
    verify_hash = hashlib.sha256(verify_input.encode()).hexdigest()[:14]

    print(f"\n--- SUBMISSION DATA ---")
    print(f"{answer},{steps_count},{verify_hash}")

except Exception as e:
    print(f"Error: {e}")