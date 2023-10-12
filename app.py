# import streamlit as st
# from src.ChickenDiseaseClassification.utils.common import decodeImage
# from src.ChickenDiseaseClassification.pipeline.predict import PredictionPipeline
# import os
# from keras.preprocessing import image
# import io

# class ClientApp:
#     def __init__(self):
#         self.filename = "inputImage.jpg"
#         self.classifier = PredictionPipeline(self.filename)
# clApp = ClientApp()
# def main():
#     st.title("Chicken Disease Classification")
#     st.write("Welcome to the world of vallabha scripts..!")
#     if st.button("Train Model"):
#         os.system("python main.py")
#         st.write("Training done successfully!")
#     uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
#     if uploaded_file is not None:
#         image_data = uploaded_file.read()
#         decodeImage(image_data, clApp.filename)
#         result = clApp.classifier.predict()
#         st.write(result)
# if __name__ == "__main__":
#     main()
import streamlit as st
from PIL import Image
import numpy as np
import io

from src.ChickenDiseaseClassification.pipeline.predict import PredictionPipeline  # Assuming your provided code is in a module named 'your_pipeline_module'

def load_and_preprocess_image(uploaded_file):
    image = Image.open(uploaded_file).resize((224, 224))
    test_image = np.array(image)
    test_image = np.expand_dims(test_image, axis=0)
    return test_image

def main():
    st.title("Chicken Disease Classification")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

        test_image = load_and_preprocess_image(uploaded_file)

        classifier = PredictionPipeline("inputImage.jpg")  # The filename is not needed since we're passing the image directly
        result = classifier.predict(test_image)
        
        st.write(result[0]['image'])

if __name__ == "__main__":
    main()
