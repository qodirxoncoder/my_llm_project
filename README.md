# 🤖 LLM Chatbot — O'rganish Loyihasi

Groq API va LLaMA modeli yordamida qurilgan oddiy, xotirali chatbot. Bu loyiha LLM (Large Language Model) texnologiyalarini o'rganish maqsadida yaratilgan.

---

## 🚀 Imkoniyatlar

- Groq API orqali LLaMA 3.1 modeli bilan muloqot
- Xotirali suhbat — bot oldingi savollarni eslab qoladi
- `.env` fayl orqali API kalitlarni xavfsiz saqlash

---

## 🛠️ Texnologiyalar

- **Python 3.14**
- **Groq API** — LLM so'rovlari uchun
- **LLaMA 3.1 8B** — til modeli
- **python-dotenv** — muhit o'zgaruvchilarini boshqarish

---

## ⚙️ O'rnatish

### 1. Reponi klon qiling
```bash
git clone https://github.com/username/my_llm_project.git
cd my_llm_project
```

### 2. Virtual muhit yarating
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Kutubxonalarni o'rnating
```bash
pip install -r requirements.txt
```

### 4. API kalitni sozlang
`.env.example` fayldan nusxa oling:
```bash
cp .env.example .env
```

`.env` faylga Groq API kalitingizni kiriting:
```
GROQ_API_KEY=gsk_...
```

> API kalitni [console.groq.com](https://console.groq.com) dan olishingiz mumkin — bepul!

---

## ▶️ Ishga tushirish

```bash
python3 main.py
```

Chiqish uchun `exit` yozing.

---

## 📁 Loyiha strukturasi

```
my_llm_project/
├── .env              # API kalit (GitHub ga yuklanmaydi)
├── .env.example      # Namuna env fayl
├── .gitignore        # Git ignore qoidalari
├── requirements.txt  # Kutubxonalar ro'yxati
├── main.py           # Asosiy chatbot kodi
└── README.md         # Hujjat
```

---

## 📚 Keyingi qadamlar

- [ ] System prompt qo'shish
- [ ] FastAPI bilan backend yaratish
- [ ] RAG (o'z hujjatiga savol berish) qo'shish

---

## 👤 Muallif

O'rganish jarayonida yaratildi 🚀
