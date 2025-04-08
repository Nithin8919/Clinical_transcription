from gtts import gTTS
import os

text = """Good morning, Mr. Thompson. I understand you've been experiencing chest pain for the last three days. Can you describe the nature of the pain—does it feel sharp, dull, or like pressure on your chest?
Also, have you noticed shortness of breath, dizziness, or fatigue during normal activities?
Based on your history of hypertension and diabetes, I’d like to run an EKG and check your troponin levels to rule out any cardiac event.
We’ll also update your medications — I’m increasing your Lisinopril dosage to 20mg daily and adding Atorvastatin 10mg for cholesterol management.
After today’s visit, we’ll schedule a cardiology referral, and I recommend avoiding strenuous activity until we get those results back.
You’ll receive a care summary with today’s updates and follow-up instructions, and our team will contact you for a telehealth check-in next Tuesday."
tts = gTTS(text)
tts.save("output.mp3")"""

# If you want to play it (macOS only):
os.system("afplay output.mp3")
