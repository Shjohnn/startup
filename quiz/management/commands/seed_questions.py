from django.core.management.base import BaseCommand
from quiz.models import Question


QUESTIONS = [
    # MATH (1-7)
    (1, "Murakkab hisob-kitoblar bilan ishlash menga qiziqarli", "math"),
    (2, "Statistika va raqamlar tahlil qilish yoqadi", "math"),
    (3, "Algebraik formulalar bilan ishlash oson", "math"),
    (4, "Grafiklar va diagrammalar o'qish menga qiyin emas", "math"),
    (5, "Mantiqiy tenglamalar yechish zavqli", "math"),
    (6, "Katta ma'lumotlar ichidan pattern topish qiziq", "math"),
    (7, "Ehtimollik va statistika menga tushunarli", "math"),

    # LOGIC (8-14)
    (8, "Muammolarni bosqichma-bosqich hal qilaman", "logic"),
    (9, "Xato topish va debug qilish menga yoqadi", "logic"),
    (10, "Algoritmlarni tushunish menga oson", "logic"),
    (11, "Qoidalar va tizimlar bilan ishlash yoqadi", "logic"),
    (12, "Kod o'qish va tushunish qiyin emas", "logic"),
    (13, "Mantiqiy o'yinlar (chess, puzzle) yoqadi", "logic"),
    (14, "Narsalarni qanday ishlashini tushunishga harakat qilaman", "logic"),

    # CREATIVE (15-21)
    (15, "Yangi narsalar yaratish menga zavq beradi", "creative"),
    (16, "Dizayn va vizual narsalar meni qiziqtiradi", "creative"),
    (17, "Foydalanuvchi uchun qulay interfeys yaratish yoqadi", "creative"),
    (18, "Rang, shrift, layout bilan ishlash qiziqarli", "creative"),
    (19, "Original g'oyalar topish menga oson", "creative"),
    (20, "Animatsiya va vizual effektlar qiziqtiradi", "creative"),
    (21, "Boshqalar ko'radigan mahsulot yaratish yoqadi", "creative"),

    # SOCIAL (22-28)
    (22, "Jamoa bilan ishlashni yaxshi ko'raman", "social"),
    (23, "Boshqalarga tushuntirish va o'rgatish yoqadi", "social"),
    (24, "Mijozlar bilan muloqot qilish qiyin emas", "social"),
    (25, "Loyiha boshqarish va rejalashtirish yoqadi", "social"),
    (26, "Boshqalar fikrini tinglash va tahlil qilaman", "social"),
    (27, "Jamoada muammolarni birgalikda hal qilish yoqadi", "social"),
    (28, "Prezentatsiya qilish va g'oyalarni taqdim etish yoqadi", "social"),

    # TECHNICAL (29-35)
    (29, "Kompyuter ichki tuzilishi qiziqtiradi", "technical"),
    (30, "Server va tarmoqlar qanday ishlashini bilmoqchiman", "technical"),
    (31, "Ma'lumotlar bazasi bilan ishlash qiziqarli", "technical"),
    (32, "API va backend tizimlar qanday ishlashini tushunaman", "technical"),
    (33, "Linux va terminal bilan ishlash qiyin emas", "technical"),
    (34, "Xavfsizlik va shifrlash mavzusi qiziqarli", "technical"),
    (35, "Cloud texnologiyalar (AWS, GCP) qiziqtiradi", "technical"),

    # INTEREST (36-40)
    (36, "Sun'iy intellekt haqida ko'p o'qiyman", "interest"),
    (37, "Mobile ilovalar yaratish qiziqtiradi", "interest"),
    (38, "Kelajakda o'z startupimni ochmoqchiman", "interest"),
    (39, "Yolg'iz ishlashdan ko'ra jamoada ishlashni afzal ko'raman", "interest"),
    (40, "Yangi texnologiyalarni birinchilardan o'rganishni yaxshi ko'raman", "interest"),
]


class Command(BaseCommand):
    help = '40 ta savolni bazaga qo\'shadi'

    def handle(self, *args, **kwargs):
        added = 0
        skipped = 0

        for order, text, category in QUESTIONS:
            obj, created = Question.objects.get_or_create(
                order=order,
                defaults={
                    'text': text,
                    'category': category,
                }
            )
            if created:
                added += 1
                self.stdout.write(self.style.SUCCESS(f'✅ {order}. {text[:40]}'))
            else:
                skipped += 1
                self.stdout.write(self.style.WARNING(f'⚠️  {order}. allaqachon bor'))

        self.stdout.write(self.style.SUCCESS(
            f'\n🎉 Tayyor! Qo\'shildi: {added} | O\'tkazildi: {skipped}'
        ))
