import streamlit as st
import json
from utils.transcriber import transcribe_audio
from utils.icd_extractor import extract_icd_codes
from utils.summary_generator import generate_summary
from utils.meat_tagger import tag_meat_compliance

st.set_page_config(page_title="Clinical Transcription MVP", layout="wide")
st.title("🩺 Clinical Transcription & ICD-10 Automation")

uploaded_file = st.file_uploader("📤 Upload audio file (WAV or MP3)", type=["wav", "mp3"])

if uploaded_file:
    with open("data/sample.wav", "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("🔍 Transcribing audio..."):
        transcript = transcribe_audio("data/sample.wav")
    st.subheader("📄 Transcript")
    st.text_area("Transcript Output", transcript, height=200)

    with st.spinner("🧠 Extracting ICD-10 Codes..."):
        icd_codes = extract_icd_codes(transcript)
    st.subheader("🏷️ ICD-10 Codes")
    st.write(icd_codes)

    with st.spinner("✅ Tagging MEAT Compliance..."):
        meat_tags = tag_meat_compliance(transcript, icd_codes)
    st.subheader("📌 MEAT Compliance Tags")
    st.json(meat_tags)

    with st.spinner("📚 Generating Structured Summary..."):
        summary = generate_summary(transcript)
    st.subheader("🗂️ Structured Summary")
    st.text_area("Summary Output", summary, height=200)

    # Optional: FHIR-style JSON export
    if st.button("📦 Export as JSON (FHIR-style)"):
        result_json = {
            "transcript": transcript,
            "icd_10_codes": icd_codes,
            "meat_tags": meat_tags,
            "summary_of_care": summary,
            "follow_up": ["Order relevant tests", "Schedule specialist visit"]
        }
        st.download_button("Download JSON", json.dumps(result_json, indent=2), file_name="transcription_summary.json", mime="application/json")
