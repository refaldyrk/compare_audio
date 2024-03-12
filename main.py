from flask import Flask, request, jsonify
import librosa
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

def compare_audio(base_audio, input_audio, threshold=0.5):
    n_fft = 2048
    hop_length = 512

    base_features = librosa.feature.mfcc(y=base_audio, n_fft=n_fft, hop_length=hop_length)
    input_features = librosa.feature.mfcc(y=input_audio, n_fft=n_fft, hop_length=hop_length)

    base_features = (base_features - np.mean(base_features, axis=1, keepdims=True)) / np.std(base_features, axis=1, keepdims=True)
    input_features = (input_features - np.mean(input_features, axis=1, keepdims=True)) / np.std(input_features, axis=1, keepdims=True)

    min_frames = min(base_features.shape[1], input_features.shape[1])
    base_features = base_features[:, :min_frames]
    input_features = input_features[:, :min_frames]

    similarity = cosine_similarity(base_features.T, input_features.T)[0, 0]

    return similarity >= threshold

@app.route('/compare_audio', methods=['POST'])
def api_compare_audio():
    if 'base_audio' not in request.files or 'input_audio' not in request.files:
        return jsonify({'error': 'Missing audio files'}), 400

    base_audio_file = request.files['base_audio']
    input_audio_file = request.files['input_audio']

    base_audio, _ = librosa.load(base_audio_file)
    input_audio, _ = librosa.load(input_audio_file)

    threshold = float(request.form.get('threshold', 0.4))

    result = compare_audio(base_audio, input_audio, threshold)

    result_str = 'similar' if result else 'not similar'

    return jsonify({'result': result_str})

if __name__ == '__main__':
    app.run(debug=True)
