import os
import json
from pathlib import Path
import librosa
import numpy as np
import tensorflow as tf

BASE_DIR = Path(__file__).resolve().parent.parent

def prediction(audio_file):

    # Load the Prediction JSON File to Predict Target_Label
    with open('prediction.json', mode='r') as f:
        prediction_dict = json.load(f)

    # Extract the Audio_Signal and Sample_Rate from Input Audio
    audio, sample_rate =librosa.load(audio_file)

    # Extract the MFCC Features and Aggrigate
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_features = np.mean(mfccs_features, axis=1)

    # Reshape MFCC features to match the expected input shape for Conv1D both batch & feature dimension
    mfccs_features = np.expand_dims(mfccs_features, axis=0)
    mfccs_features = np.expand_dims(mfccs_features, axis=2)

    # Convert into Tensors
    mfccs_tensors = tf.convert_to_tensor(mfccs_features, dtype=tf.float32)

    # Load the Model and Prediction
    model = tf.keras.models.load_model('model/trained_model.h5')
    prediction = model.predict(mfccs_tensors)

    # Find the Maximum Probability Value
    target_label = np.argmax(prediction)

    # Find the Target_Label Name using Prediction_dict
    predicted_class = prediction_dict[str(target_label)]
    confidence = round(np.max(prediction)*100, 2)
    print(f'Predicted Class : {predicted_class}')
    print(f'Confidence : {confidence}%')

prediction(os.path.join(BASE_DIR, 'dataset/voice_of_birds/voice_of_birds/Andean Guan_sound/Andean Guan3.mp3'))