from google import genai
client = genai.Client(api_key="AIzaSyDYTpG4klIwlcGocy0ljEl3Dtibp4PIIV8")

print("Checking available models...")
for model in client.models.list():
    # We changed 'supported_methods' to 'supported_actions'
    print(f"Name: {model.name} | Actions: {model.supported_actions}")