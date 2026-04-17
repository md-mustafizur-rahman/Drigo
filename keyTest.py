from google import genai

client = genai.Client(api_key="AQ.Ab8RN6KlTidK604xXtZhDtFp1krLUxBn9Bf5rciUxZfCWWYJnA")

# for m in client.models.list():
#     print(m.name)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello, test response"
)

print(response.text)