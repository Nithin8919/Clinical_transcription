from transformers import pipeline

def generate_summary(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']
