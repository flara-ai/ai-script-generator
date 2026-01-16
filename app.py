# app.py - Simple AI Script Generator
import openai

# OpenAI API açarını burada əlavə et
openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_script(prompt):
    """
    Verilən prompt-a əsasən ssenari yaradır
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text.strip()

def main():
    print("AI Script Generator-a xoş gəldiniz!")
    user_prompt = input("Ssenari üçün mövzu daxil edin: ")
    script = generate_script(user_prompt)
    print("\n=== Yaradılmış Ssenari ===\n")
    print(script)

if __name__ == "__main__":
    main()
