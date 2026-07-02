# GrammaFix AI

## 📖 Deskripsi

GrammaFix AI merupakan aplikasi berbasis Artificial Intelligence yang digunakan untuk melakukan koreksi tata bahasa (Grammar Error Correction) pada kalimat berbahasa Inggris. Sistem ini memanfaatkan model T5-base yang telah di-fine-tune menggunakan dataset Grammar Error Correction sehingga mampu memperbaiki berbagai kesalahan grammar secara otomatis.

---

## ✨ Fitur

- Koreksi grammar bahasa Inggris secara otomatis
- Antarmuka interaktif menggunakan Gradio
- Menampilkan hasil koreksi secara real-time
- Menampilkan waktu proses inferensi
- Contoh kalimat untuk pengujian

---

## 🛠️ Teknologi yang Digunakan

- Python
- PyTorch
- Hugging Face Transformers
- Gradio
- SentencePiece

---

## 🤖 Model

| Informasi | Detail |
|-----------|--------|
| Model | T5-base |
| Task | Grammar Error Correction |
| Framework | Hugging Face Transformers |
| Fine-tuning | Ya |

---

## 📂 Struktur Project

```text
grammar-app/
│
├── app.py
├── requirements.txt
├── README.md
├── screenshots/
└── grammafix-finetuned/   (tidak disertakan di repository)
```

---

## 📷 Tampilan Aplikasi

<img width="2880" height="2402" alt="image" src="https://github.com/user-attachments/assets/2b3384c2-59c8-493f-b098-d72213ade2a6" />
<img width="2880" height="2402" alt="image" src="https://github.com/user-attachments/assets/34b0e573-65ce-487e-b0d4-4851c495983a" />

---

## 🚀 Cara Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/username/grammar-app.git
```

### 2. Masuk ke Folder Project

```bash
cd grammar-app
```

### 3. Buat Virtual Environment

```bash
python -m venv venv
```

Aktivasi:

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### 4. Install Dependency

```bash
pip install -r requirements.txt
```

### 5. Download Model

Karena ukuran model cukup besar (~880 MB), model tidak disertakan dalam repository GitHub.

Silakan download melalui:

📥 Google Drive

https://drive.google.com/drive/folders/1fWu6AM29TOTcTb4-SRVA-muuWWBljhFa?usp=sharing

Setelah diunduh, letakkan folder:

```
grammafix-finetuned/
```

di root project sehingga struktur menjadi:

```
grammar-app/
├── app.py
├── grammafix-finetuned/
└── ...
```

### 6. Jalankan Program

```bash
python app.py
```

---

## 📌 Contoh Penggunaan

Input

```
She go to school yesterday.
```

Output

```
She went to school yesterday.
```

---

## 👩‍💻 Author

Shendy Tria Amelyana    434231003

Vanesha Amanda Yatinde  434231102

Lutfania                434231119

---

## 📄 Lisensi

D4 Teknik Informatika

Universitas Airlangga
