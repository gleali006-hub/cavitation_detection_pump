import tensorflow as tf

# Path file H5 
h5_model_path = 'DEF_MODEL.h5'
# Path to save TFLite file
tflite_model_path = 'DEF_MODEL_CONV.tflite'


model = tf.keras.models.load_model(h5_model_path, compile=False)

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

with open(tflite_model_path, 'wb') as f:
    f.write(tflite_model)

print(f"Conversion completed! File saved as '{tflite_model_path}'")
