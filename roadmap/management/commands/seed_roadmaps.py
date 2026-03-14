from django.core.management.base import BaseCommand
from roadmap.models import Roadmap, RoadmapStep


ROADMAPS = {
    'data_science': {
        'title': 'Data Science',
        'description': 'Python dan ML gacha junior darajaga',
        'total_hours': 400,
        'steps': [
            ('Python basics', 60, 'Syntax, funksiyalar, OOP'),
            ('Pandas & NumPy', 50, 'Ma\'lumotlar bilan ishlash'),
            ('Data Visualization', 40, 'Matplotlib, Seaborn'),
            ('Statistics', 50, 'Ehtimollik, statistika asoslari'),
            ('Machine Learning', 80, 'Sklearn, modellar'),
            ('Real Projects', 120, 'Portfolio loyihalari'),
        ]
    },
    'backend': {
        'title': 'Backend Development',
        'description': 'Python backend developer yo\'li',
        'total_hours': 350,
        'steps': [
            ('Python basics', 50, 'Syntax, OOP, funksiyalar'),
            ('Django', 80, 'Models, views, templates'),
            ('Django REST Framework', 60, 'API yaratish'),
            ('PostgreSQL', 50, 'Database asoslari'),
            ('Git & GitHub', 20, 'Version control'),
            ('Deploy', 40, 'Server, Nginx, Docker asoslari'),
            ('Real Projects', 50, 'Portfolio loyihalari'),
        ]
    },
    'frontend': {
        'title': 'Frontend Development',
        'description': 'HTML dan React gacha',
        'total_hours': 350,
        'steps': [
            ('HTML & CSS', 60, 'Asoslar, Flexbox, Grid'),
            ('JavaScript', 80, 'ES6+, DOM, async'),
            ('React', 100, 'Components, hooks, state'),
            ('Git & GitHub', 20, 'Version control'),
            ('Real Projects', 90, 'Portfolio loyihalari'),
        ]
    },
    'ml': {
        'title': 'Machine Learning',
        'description': 'ML Engineer yo\'li',
        'total_hours': 450,
        'steps': [
            ('Python & Math', 70, 'Python, algebra, calculus'),
            ('Pandas & NumPy', 50, 'Ma\'lumotlar bilan ishlash'),
            ('ML Algorithms', 100, 'Regression, classification, clustering'),
            ('Deep Learning', 100, 'Neural networks, TensorFlow'),
            ('MLOps basics', 50, 'Model deploy qilish'),
            ('Real Projects', 80, 'Portfolio loyihalari'),
        ]
    },
    'flutter': {
        'title': 'Flutter Mobile',
        'description': 'Flutter bilan mobile app yaratish',
        'total_hours': 350,
        'steps': [
            ('Dart basics', 50, 'Dart sintaksis va OOP'),
            ('Flutter UI', 80, 'Widgets, layouts'),
            ('State Management', 60, 'Provider, Riverpod'),
            ('API Integration', 50, 'HTTP, REST API'),
            ('Real Projects', 110, 'Portfolio loyihalari'),
        ]
    },
    'android': {
        'title': 'Android Development',
        'description': 'Kotlin bilan Android dasturlash',
        'total_hours': 400,
        'steps': [
            ('Kotlin basics', 60, 'Sintaksis, OOP'),
            ('Android UI', 80, 'XML layouts, activities'),
            ('Jetpack Compose', 70, 'Modern UI'),
            ('API Integration', 50, 'Retrofit, REST'),
            ('Real Projects', 140, 'Portfolio loyihalari'),
        ]
    },
    'ios': {
        'title': 'iOS Development',
        'description': 'Swift bilan iOS dasturlash',
        'total_hours': 400,
        'steps': [
            ('Swift basics', 60, 'Sintaksis, OOP'),
            ('UIKit', 80, 'Interface builder'),
            ('SwiftUI', 80, 'Modern UI framework'),
            ('API Integration', 50, 'URLSession, REST'),
            ('Real Projects', 130, 'Portfolio loyihalari'),
        ]
    },
    'devops': {
        'title': 'DevOps',
        'description': 'DevOps Engineer yo\'li',
        'total_hours': 400,
        'steps': [
            ('Linux basics', 60, 'Terminal, commands'),
            ('Git & CI/CD', 50, 'GitHub Actions'),
            ('Docker', 70, 'Containerization'),
            ('Kubernetes', 80, 'Orchestration'),
            ('Cloud (AWS)', 90, 'EC2, S3, RDS'),
            ('Real Projects', 50, 'Portfolio loyihalari'),
        ]
    },
    'cybersecurity': {
        'title': 'Cybersecurity',
        'description': 'Kiberxavfsizlik yo\'li',
        'total_hours': 400,
        'steps': [
            ('Networking basics', 60, 'TCP/IP, DNS, HTTP'),
            ('Linux & Terminal', 60, 'Kali Linux'),
            ('Web Security', 80, 'OWASP Top 10'),
            ('Ethical Hacking', 100, 'Penetration testing'),
            ('Real Projects', 100, 'CTF va amaliy mashqlar'),
        ]
    },
    'blockchain': {
        'title': 'Blockchain Development',
        'description': 'Blockchain developer yo\'li',
        'total_hours': 400,
        'steps': [
            ('Blockchain basics', 50, 'How blockchain works'),
            ('Solidity', 100, 'Smart contracts'),
            ('Web3.js / Ethers.js', 80, 'Frontend integration'),
            ('DeFi protocols', 70, 'DeFi asoslari'),
            ('Real Projects', 100, 'Portfolio loyihalari'),
        ]
    },
    'game_dev': {
        'title': 'Game Development',
        'description': 'Game developer yo\'li',
        'total_hours': 400,
        'steps': [
            ('Python / C# basics', 60, 'Dasturlash asoslari'),
            ('Unity basics', 100, '2D/3D game engine'),
            ('Game Physics', 60, 'Harakat, collisions'),
            ('Game Design', 50, 'Level design, UX'),
            ('Real Projects', 130, 'Portfolio o\'yinlar'),
        ]
    },
    'ui_ux': {
        'title': 'UI/UX Design',
        'description': 'UI/UX designer yo\'li',
        'total_hours': 300,
        'steps': [
            ('Design basics', 50, 'Rang, tipografiya, kompozitsiya'),
            ('Figma', 80, 'Interface design tool'),
            ('UX Research', 60, 'User research, usability'),
            ('Prototyping', 50, 'Wireframe, prototype'),
            ('Real Projects', 60, 'Portfolio loyihalari'),
        ]
    },
    'cloud': {
        'title': 'Cloud Engineering',
        'description': 'Cloud engineer yo\'li',
        'total_hours': 400,
        'steps': [
            ('Linux & Networking', 60, 'Asoslar'),
            ('AWS basics', 100, 'EC2, S3, RDS, Lambda'),
            ('Infrastructure as Code', 70, 'Terraform'),
            ('Docker & Kubernetes', 80, 'Containerization'),
            ('Real Projects', 90, 'Portfolio loyihalari'),
        ]
    },
    'ai_engineering': {
        'title': 'AI Engineering',
        'description': 'AI Engineer yo\'li',
        'total_hours': 450,
        'steps': [
            ('Python & Math', 70, 'Python, linear algebra'),
            ('ML basics', 80, 'Classical ML'),
            ('Deep Learning', 100, 'PyTorch, TensorFlow'),
            ('LLMs & Prompt Eng', 80, 'GPT, Claude, Gemini'),
            ('AI APIs', 50, 'OpenAI, LangChain'),
            ('Real Projects', 70, 'Portfolio loyihalari'),
        ]
    },
    'qa': {
        'title': 'QA / Testing',
        'description': 'QA Engineer yo\'li',
        'total_hours': 300,
        'steps': [
            ('Testing basics', 50, 'Manual testing asoslari'),
            ('Python basics', 50, 'Dasturlash asoslari'),
            ('Selenium', 70, 'Web automation'),
            ('API Testing', 60, 'Postman, pytest'),
            ('Real Projects', 70, 'Portfolio loyihalari'),
        ]
    },
}


class Command(BaseCommand):
    help = 'Barcha roadmaplarni bazaga qo\'shadi'

    def handle(self, *args, **kwargs):
        for field_name, data in ROADMAPS.items():
            roadmap, created = Roadmap.objects.get_or_create(
                field_name=field_name,
                defaults={
                    'title': data['title'],
                    'description': data['description'],
                    'total_hours': data['total_hours'],
                }
            )

            if created:
                for i, (title, hours, desc) in enumerate(data['steps'], 1):
                    RoadmapStep.objects.create(
                        roadmap=roadmap,
                        order=i,
                        title=title,
                        hours_needed=hours,
                        description=desc,
                    )
                self.stdout.write(self.style.SUCCESS(f'✅ {field_name} qo\'shildi'))
            else:
                self.stdout.write(self.style.WARNING(f'⚠️  {field_name} allaqachon bor'))

        self.stdout.write(self.style.SUCCESS('🎉 Barcha roadmaplar tayyor!'))
