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

# import os
# import json
# import re
# from openai import OpenAI
# from .models import AnalysisResult
#
# client = OpenAI(
#     api_key=os.getenv('GROQ_API_KEY'),
#     base_url="https://api.groq.com/openai/v1"
# )


# def analyze_answers(user, answers):
#     # Foydalanuvchi javoblarini chiroyli formatda tayyorlash
#     formatted = "\n".join([
#         f"Savol: {a.question.text} | Kategoriya: {a.question.category} | Ball: {a.score}/5"
#         for a in answers
#     ])
#
#     # 12 ta yo'nalish ro'yxati va "insoniy" ko'rsatmalar
#     prompt = f"""
# Siz tajribali IT karyera maslahatchisi va mentorsiz. Quyidagi foydalanuvchining test natijalarini diqqat bilan o'rganib chiqing.
# Uning qiziqishlari, mantiqiy darajasi va texnik moyilligidan kelib chiqib, unga eng mos keladigan 3 ta yo'nalishni tanlang.
#
# Foydalanuvchi javoblari:
# {formatted}
#
# Vazifangiz:
# 1. Eng mos 3 ta yo'nalishni (field) aniqlang.
# 2. Har bir yo'nalish uchun "reason" qismida xuddi mentor kabi samimiy tushuntirish bering.
# 3. Tushuntirishda "AI", "Algoritm" yoki "Sun'iy intellekt" so'zlarini UMUMAN ISHLATMANNG. Go'yoki buni inson yozayotgandek bo'lsin.
#
# Field qiymatlari faqat quyidagilardan biri bo'lishi shart:
# backend, frontend, data_science, ml, flutter, android, ios, devops, cybersecurity, game_dev, ui_ux, qa.
#
# Javobni faqat va faqat JSON formatda qaytaring (markdownsiz):
# {{
#     "results": [
#         {{
#             "field": "backend",
#             "percentage": 95,
#             "reason": "Sizda murakkab tizimlarni tartibga solish va mantiqiy zanjir qurish qobiliyati juda yuqori. Ma'lumotlar bilan ishlashdagi aniqligingiz backend sohasida katta muvaffaqiyatlarga zamin yaratadi."
#         }}
#     ]
# }}
# """
#
#     response = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=[
#             {"role": "system", "content": "Siz professional karyera maslahatchisisiz. Faqat JSON qaytarasiz."},
#             {"role": "user", "content": prompt}
#         ],
#         max_tokens=800,  # Reason uzunroq bo'lishi uchun ko'paytirildi
#         temperature=0.4,  # Javoblar bir xil bo'lib qolmasligi uchun biroz kreativlik berildi
#     )
#
#     raw_content = response.choices[0].message.content.strip()
#
#     # JSONni xavfsiz ajratib olish (Regex yordamida)
#     try:
#         json_match = re.search(r'\{.*\}', raw_content, re.DOTALL)
#         if not json_match:
#             raise ValueError("Natija formatida xatolik")
#
#         data = json.loads(json_match.group())
#     except Exception as e:
#         print(f"Parsing error: {e}")
#         # Xatolik bo'lsa bo'sh ro'yxat qaytarish yoki log qilish mumkin
#         return []
#
#     # Eski natijalarni o'chirib yuborish
#     AnalysisResult.objects.filter(user=user).delete()
#
#     # Yangi natijalarni bazaga saqlash
#     results = []
#     for item in data.get('results', []):
#         result = AnalysisResult.objects.create(
#             user=user,
#             field_name=item['field'],
#             percentage=item['percentage'],
#             reason=item.get('reason', "")  # Mentor tushuntirishi
#         )
#         results.append(result)
#
#     return results
