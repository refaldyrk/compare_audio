# Audio Comparison App

This is a simple Flask web application for comparing audio files based on their MFCC (Mel-Frequency Cepstral Coefficients) features using cosine similarity. The application allows users to upload two audio files and set a similarity threshold. The server then compares the audio files and returns whether they are deemed similar or not based on the specified threshold.

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You can install the required Python packages using the following command:

```bash
pip install flask librosa numpy scikit-learn
```

### Running the Application

1. Clone the repository:

```bash
git clone https://github.com/refaldyrk/compare_audio.git
cd compare_audio
```

2. Run the Flask application:

```bash
python app.py
```

The application will be accessible at `http://127.0.0.1:5000/` in your web browser.

## Usage

1. Upload two audio files for comparison.
2Click the "Compare" button to initiate the comparison.

## API Endpoint

### `/compare_audio` (POST)

- **Parameters:**
  - `base_audio`: The base audio file (required).
  - `input_audio`: The input audio file (required).
- **Response:**
  - JSON object with the result of the comparison.

```json
{
  "result": "similar" or "not similar"
}
```

## Example Usage

```python
import requests
import os

url = "http://127.0.0.1:5000/compare_audio"
files = {
    "base_audio": open("path/to/base_audio.wav", "rb"),
    "input_audio": open("path/to/input_audio.wav", "rb"),
}
response = requests.post(url, files=files)
result = response.json()

print(f"The audio files are {result['result']}.")
```