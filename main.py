from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from transformers import pipeline
import os

# Function to get the next file count for saving new files
def get_next_file_count(prefix, suffix):
    count = 1
    # Iterate over files in the current directory
    while True:
        filename = f"{prefix}_{count}{suffix}"
        # If the file does not exist, we've found our count
        if not os.path.exists(filename):
            return count
        count += 1

# Function to check if the file is a .wav file
def is_wav_file(filename):
    return filename.lower().endswith('.wav')

# Set up the authenticator and service instance
api_key = 'IF_4XOg1OpRYrAA-ac3JH66Apw-j9EvpKyxYW4XY6Uay'

service_url = 'https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/8f89aa33-4576-4667-a646-892c1529af8b'

authenticator = IAMAuthenticator(api_key)
speech_to_text = SpeechToTextV1(authenticator=authenticator)
speech_to_text.set_service_url(service_url)

# Load the summarization pipeline
summarizer = pipeline("summarization", model="Falconsai/text_summarization")

# Ask the user for a .wav file
while True:
    file_path = input("Please enter the path to your audio file and make sure it ends with '.wav': ")
    if is_wav_file(file_path):
        try:
            with open(file_path, 'rb') as audio_file:
                print("File is valid and will be processed.")
                break
        except FileNotFoundError:
            print("File not found. Please try again.")
    else:
        print("The file is not a .wav file. Please enter a valid .wav audio file.")

# Transcribe the audio file
with open(file_path, 'rb') as audio_file:
    recognition_result = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/wav',
        model='en-US_BroadbandModel'
    ).get_result()

# Determine the filename with the next count number
file_prefix = 'transcription'
file_suffix = '.txt'
file_count = get_next_file_count(file_prefix, file_suffix)
transcription_filename = f"{file_prefix}_{file_count}{file_suffix}"

# Save the transcription to a text file
with open(transcription_filename, 'w') as transcription_file:
    for result in recognition_result['results']:
        transcription_file.write(result['alternatives'][0]['transcript'] + "\n")
print(f"Transcription has been saved to {transcription_filename}.")

# Summarize the transcription and save the summary
with open(transcription_filename, 'r') as transcription_file:  # Ensure you read from the transcription file
    transcript = transcription_file.read()

# Summarize the text using the summarizer
summary = summarizer(transcript, max_length=130, min_length=30, do_sample=False)

# Extract the summary text and save it
summary_text = summary[0]['summary_text']
summary_filename = f"{file_prefix}_{file_count}_summary.txt"
with open(summary_filename, 'w') as summary_file:
    summary_file.write(summary_text)

print(f"Transcription has been summarized and saved to {summary_filename}.")
