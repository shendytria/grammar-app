# GrammaFix AI

Grammar Error Correction System using **Natural Language Processing (NLP)** and **T5-base Fine-Tuned Model**

---

## 📖 Deskripsi

GrammaFix AI merupakan aplikasi berbasis **Natural Language Processing (NLP)** yang dirancang untuk melakukan **Grammar Error Correction (GEC)** pada kalimat berbahasa Inggris secara otomatis.

Sistem ini memanfaatkan model **T5-base** yang telah melalui proses **fine-tuning** menggunakan dataset Grammar Error Correction sehingga mampu mendeteksi dan memperbaiki berbagai kesalahan tata bahasa, seperti:

- Subject-Verb Agreement
- Verb Tense
- Article (a, an, the)
- Plural dan Singular Noun
- Preposition
- Pronoun
- Word Order
- Kesalahan Grammar lainnya

Aplikasi dikembangkan menggunakan **Python**, **PyTorch**, **Hugging Face Transformers**, dan **Gradio** sehingga pengguna dapat melakukan koreksi grammar secara real-time melalui antarmuka web yang sederhana dan interaktif.

---

# ✨ Fitur

- ✅ Grammar Error Correction otomatis
- ✅ Koreksi grammar secara real-time
- ✅ Menampilkan waktu inferensi
- ✅ Antarmuka web interaktif menggunakan Gradio
- ✅ Contoh kalimat untuk pengujian
- ✅ Menggunakan model Deep Learning berbasis Transformer

---

# 🧠 Bidang Penelitian

- Artificial Intelligence (AI)
- Deep Learning
- Natural Language Processing (NLP)
- Grammar Error Correction (GEC)

---

# ⚙️ Teknologi yang Digunakan

| Teknologi | Keterangan |
|-----------|------------|
| Python | Bahasa Pemrograman |
| PyTorch | Framework Deep Learning |
| Hugging Face Transformers | Fine-Tuning dan Inference Model |
| T5-base | Pre-trained Language Model |
| Gradio | User Interface |
| SentencePiece | Tokenizer |

---

# 🤖 Informasi Model

| Informasi | Detail |
|-----------|--------|
| Model | T5-base |
| Task | Grammar Error Correction |
| Bidang | Natural Language Processing |
| Framework | Hugging Face Transformers |
| Fine-Tuning | Ya |
| Interface | Gradio |

---

# 🔍 Alur Sistem

1. Pengguna memasukkan kalimat berbahasa Inggris.
2. Sistem melakukan preprocessing dengan tokenizer T5.
3. Model T5 melakukan proses inferensi.
4. Model menghasilkan kalimat yang telah diperbaiki.
5. Hasil ditampilkan kepada pengguna beserta waktu proses inferensi.

---

# 📂 Struktur Project

```text
grammar-app/
│
├── app.py
├── requirements.txt
├── README.md
├── screenshots/
│   ├── antarmuka.png
│   └── result.png
│
└── grammafix-finetuned/
    ├── config.json
    ├── tokenizer.json
    ├── tokenizer_config.json
    ├── special_tokens_map.json
    ├── generation_config.json
    └── model.safetensors
```

> **Catatan:** Folder `grammafix-finetuned` tidak disertakan di repository GitHub karena ukuran model cukup besar (~880 MB).

---

# 📷 Tampilan Aplikasi

<img width="2880" height="2402" alt="image" src="https://github.com/user-attachments/assets/2b3384c2-59c8-493f-b098-d72213ade2a6" />
<img width="2880" height="2402" alt="image" src="https://github.com/user-attachments/assets/34b0e573-65ce-487e-b0d4-4851c495983a" />

---

# 🚀 Instalasi

## 1. Clone Repository

```bash
git clone https://github.com/shendytria/grammar-app.git
```

## 2. Masuk ke Folder Project

```bash
cd grammar-app
```

## 3. Membuat Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Mac / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 4. Install Dependency

```bash
pip install -r requirements.txt
```

---

# 📥 Download Model

Model tidak disertakan pada repository GitHub karena ukuran file yang cukup besar.

Silakan unduh model melalui:

**Google Drive:**  
*https://drive.google.com/drive/folders/1fWu6AM29TOTcTb4-SRVA-muuWWBljhFa?usp=sharing*

Setelah selesai diunduh, letakkan folder:

```text
grammafix-finetuned
```

sejajar dengan file `app.py`.

Struktur akhirnya menjadi:

```text
grammar-app/
├── app.py
├── grammafix-finetuned/
└── screenshots/
```

---

# ▶️ Menjalankan Program

```bash
python app.py
```

Setelah program berjalan, Gradio akan menampilkan URL, misalnya:

```text
Running on local URL:  http://127.0.0.1:7860
Running on public URL: https://63bd143d26a2bbdd99.gradio.live
```

Buka URL tersebut melalui browser.

---

# 💡 Contoh Penggunaan

### Input

```text
She go to school yesterday.
```

### Output

```text
She went to school yesterday.
```

---

### Input

```text
I has a apple.
```

### Output

```text
I have an apple.
```

---

### Input

```text
The childrens are playing in garden.
```

### Output

```text
The children are playing in the garden.
```

---

# 📌 Kebutuhan Sistem

### Minimum

- Python 3.9+
- RAM 8 GB
- Storage ±2 GB

### Rekomendasi

- RAM 16 GB
- Apple Silicon / NVIDIA GPU (Opsional)

---

# 👩‍💻 Pengembang

**Shendy Tria Amelyana**
**Vanesha Amanda Yatinde**
**Lutfania**

Program Studi D4 Teknik Informatika

Universitas Airlangga

---

# 📄 Lisensi

Repository ini dibuat untuk keperluan pembelajaran, penelitian, dan pengembangan sistem berbasis Natural Language Processing (NLP).
