import time
import gradio as gr
import torch
from transformers import T5ForConditionalGeneration, AutoTokenizer

MODEL_PATH = "grammafix-finetuned"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()


def predict(text):
    if not text or not text.strip():
        return "", "Silakan masukkan kalimat terlebih dahulu."

    start = time.time()

    inputs = tokenizer(
        "grammar: " + text.strip(),
        return_tensors="pt",
        max_length=128,
        truncation=True
    )
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=128,
            num_beams=4,
            early_stopping=True
        )

    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    elapsed = round(time.time() - start, 2)

    status = (
        "Tidak ada perubahan"
        if result.strip().lower() == text.strip().lower()
        else "Perubahan berhasil diterapkan"
    )

    return result, f"Waktu proses: {elapsed}s | {status}"


css = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* { font-family: 'Inter', sans-serif !important; }

html, body,
.gradio-container,
.main, .wrap, .contain,
div[class*="gradio"],
div[class*="svelte-"],
div[class*="app"],
section, .tabs, .tabitem,
.gap, .panel, .form {
    background-color: #F5F7FA !important;
    background: #F5F7FA !important;
    color: #111827 !important;
}

.gradio-container {
    max-width: 1060px !important;
    margin: 0 auto !important;
}

#header {
    background: #FFFFFF !important;
    border: 1px solid #E5E7EB;
    border-radius: 16px;
    padding: 36px 28px;
    margin: 20px 0 20px 0;
    text-align: center;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

#header h1 {
    color: #111827 !important;
    font-size: 1.9rem;
    font-weight: 800;
    margin: 0;
}

#header p {
    color: #6B7280 !important;
    font-size: 0.95rem;
    margin: 8px 0 0 0;
}

.stat {
    background: #FFFFFF !important;
    border: 1px solid #E5E7EB;
    border-radius: 12px;
    padding: 14px 18px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}

.stat .lbl {
    color: #9CA3AF;
    font-size: 0.72rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.stat .val {
    color: #111827;
    font-size: 1.05rem;
    font-weight: 700;
    margin-top: 3px;
}

.card {
    background: #FFFFFF !important;
    border: 1px solid #E5E7EB;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

.card-title {
    background: #5BA4CF !important;
    color: #FFFFFF !important;
    padding: 14px 20px;
    font-size: 16px;
    font-weight: 700;
    letter-spacing: 0.4px;
    margin: 0;
}

.card-body {
    padding: 16px 18px;
    background: #FFFFFF !important;
}

textarea,
textarea:hover,
textarea:focus,
textarea:active,
[data-testid="textbox"] textarea {
    background: #FFFFFF !important;
    color: #111827 !important;
    -webkit-text-fill-color: #111827 !important;
    border: 1px solid #D9E4EF !important;
    border-radius: 12px !important;
    box-shadow: none !important;
    padding: 14px !important;
    font-size: 0.95rem !important;
    outline: none !important;
}

textarea:focus {
    border-color: #5BA4CF !important;
}

#btn-submit {
    background: #111827 !important;
    color: #FFFFFF !important;
    font-weight: 600 !important;
    border-radius: 10px !important;
    border: none !important;
    height: 44px;
    box-shadow: none !important;
}

#btn-submit:hover {
    background: #1F2937 !important;
}

#btn-clear {
    background: #FFFFFF !important;
    color: #374151 !important;
    border: 1px solid #E5E7EB !important;
    border-radius: 10px !important;
    font-weight: 500 !important;
    height: 44px;
    box-shadow: none !important;
}

#btn-clear:hover {
    background: #F9FAFB !important;
}

.ex-btn {
    background: #F9FAFB !important;
    color: #374151 !important;
    border: 1px solid #E5E7EB !important;
    border-radius: 8px !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    height: 40px;
    width: 100%;
    box-shadow: none !important;
}

.ex-btn:hover {
    background: #F3F4F6 !important;
    border-color: #D1D5DB !important;
}

#status p {
    color: #6B7280 !important;
    font-size: 0.83rem;
    margin: 8px 0 0 0;
}

#footer {
    text-align: center;
    color: #9CA3AF !important;
    font-size: 0.78rem;
    margin: 24px 0 8px 0;
}

footer {
    visibility: hidden;
}
"""


examples = [
    "She go to school yesterday.",
    "I has a apple.",
    "He don't like coffee.",
    "They is playing football.",
    "We was very happy to see you.",
    "The childrens are playing in garden.",
]


theme = gr.themes.Base(
    primary_hue="slate",
    neutral_hue="slate",
    text_size="md",
)


with gr.Blocks(title="GrammaFix AI", css=css, theme=theme) as demo:

    gr.HTML("""
        <div id="header">
            <h1>GrammaFix AI</h1>
            <p>English Grammar Correction &mdash; Fine-Tuned T5 Model</p>
        </div>
    """)

    with gr.Row():
        gr.HTML("<div class='stat'><div class='lbl'>Model</div><div class='val'>T5-base Fine-Tuned</div></div>")
        gr.HTML("<div class='stat'><div class='lbl'>Dataset</div><div class='val'>3.000 Sampel</div></div>")
        gr.HTML("<div class='stat'><div class='lbl'>Inference</div><div class='val'>Real-time</div></div>")
        gr.HTML("<div class='stat'><div class='lbl'>Task</div><div class='val'>Grammar Correction</div></div>")

    gr.HTML("<div style='height:18px'></div>")

    with gr.Row(equal_height=True):
        with gr.Column():
            with gr.Group(elem_classes="card"):
                gr.HTML("<div class='card-title'>Kalimat Asli</div>")
                with gr.Column(elem_classes="card-body"):
                    input_box = gr.Textbox(
                        lines=8,
                        placeholder="Ketik kalimat berbahasa Inggris di sini...",
                        show_label=False
                    )

                    with gr.Row():
                        btn_clear = gr.Button("Bersihkan", elem_id="btn-clear")
                        btn_submit = gr.Button("Perbaiki Grammar", elem_id="btn-submit", scale=2)

        with gr.Column():
            with gr.Group(elem_classes="card"):
                gr.HTML("<div class='card-title'>Hasil Koreksi</div>")
                with gr.Column(elem_classes="card-body"):
                    output_box = gr.Textbox(
                        lines=8,
                        show_label=False,
                        interactive=False
                    )
                    status_box = gr.Markdown("", elem_id="status")

    gr.HTML("<div style='height:18px'></div>")

    with gr.Group(elem_classes="card"):
        gr.HTML("<div class='card-title'>Contoh Kalimat</div>")
        with gr.Column(elem_classes="card-body"):
            with gr.Row():
                ex_btn1 = gr.Button(examples[0], elem_classes="ex-btn")
                ex_btn2 = gr.Button(examples[1], elem_classes="ex-btn")
                ex_btn3 = gr.Button(examples[2], elem_classes="ex-btn")

            with gr.Row():
                ex_btn4 = gr.Button(examples[3], elem_classes="ex-btn")
                ex_btn5 = gr.Button(examples[4], elem_classes="ex-btn")
                ex_btn6 = gr.Button(examples[5], elem_classes="ex-btn")

    gr.HTML("<div style='height:18px'></div>")

    gr.HTML("""
        <div class="card">
            <div class="card-title">Tentang</div>
            <div class="card-body">
                <p style="color:#4B5563; font-size:0.92rem; line-height:1.8; margin:0;">
                GrammaFix AI menggunakan model <strong>T5-base</strong> yang di-fine-tune
                untuk Grammar Error Correction. Mampu mendeteksi dan memperbaiki
                subject-verb agreement, tenses, artikel, dan lainnya secara otomatis.
                Dibangun dengan Hugging Face Transformers, PyTorch, dan Gradio.
                </p>
            </div>
        </div>
    """)

    gr.HTML("<div id='footer'>GrammaFix AI &mdash; Grammar Correction System</div>")

    btn_submit.click(
        fn=predict,
        inputs=input_box,
        outputs=[output_box, status_box]
    )

    input_box.submit(
        fn=predict,
        inputs=input_box,
        outputs=[output_box, status_box]
    )

    btn_clear.click(
        fn=lambda: ("", "", ""),
        outputs=[input_box, output_box, status_box]
    )

    ex_btn1.click(fn=lambda: examples[0], outputs=input_box)
    ex_btn2.click(fn=lambda: examples[1], outputs=input_box)
    ex_btn3.click(fn=lambda: examples[2], outputs=input_box)
    ex_btn4.click(fn=lambda: examples[3], outputs=input_box)
    ex_btn5.click(fn=lambda: examples[4], outputs=input_box)
    ex_btn6.click(fn=lambda: examples[5], outputs=input_box)


demo.launch(share=True)