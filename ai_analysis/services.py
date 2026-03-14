import os
import json
from openai import OpenAI
from .models import AnalysisResult

client = OpenAI(
    api_key=os.getenv('GROQ_API_KEY'),
    base_url="https://api.groq.com/openai/v1"
)


def analyze_answers(user, answers):
    formatted = "\n".join([
        f"Savol: {a.question.text} | Kategoriya: {a.question.category} | Ball: {a.score}/5"
        for a in answers
    ])

    prompt = f"""
Quyidagi foydalanuvchi javoblarini tahlil qil va IT yo'nalishlarini aniqlа.

Javoblar:
{formatted}

Faqat JSON formatda javob ber, boshqa hech narsa yozma, markdown ham yozma:
{{
    "results": [
        {{"field": "backend", "percentage": 87}},
        {{"field": "data_science", "percentage": 95}},
        {{"field": "ml", "percentage": 90}}
    ]
}}

Eng mos 3 ta yo'nalishni chiqar.
field qiymatlari faqat shu bo'lsin:
backend, frontend, data_science, ml, ai_engineering,
flutter, android, ios, devops, cybersecurity,
blockchain, game_dev, ui_ux, cloud, qa
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "Sen IT career advisor san. Faqat JSON qaytarasan, markdown ishlatma."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.3,
    )

    raw = response.choices[0].message.content.strip()
    raw = raw.replace('```json', '').replace('```', '').strip()

    data = json.loads(raw)

    # Eski natijalarni o'chir
    AnalysisResult.objects.filter(user=user).delete()

    # Yangilarini saqlа
    results = []
    for item in data['results']:
        result = AnalysisResult.objects.create(
            user=user,
            field_name=item['field'],
            percentage=item['percentage']
        )
        results.append(result)

    return results
