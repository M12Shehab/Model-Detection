# -----------------------------------------------------------------------------
# Copyright (c) 2024 Mohammed A. Shehab
# All rights reserved.
#
# This software is licensed under the terms of the MIT license.
# For details, see the LICENSE file in the root directory of this distribution.
# -----------------------------------------------------------------------------
import pickle   # import the pickle module to load the trained model    
import re    # import the re module to use regular expressions
from pathlib import Path    # import the Path module to get the current directory

__version__ = "0.0.1"   # define the model version, this update every time we update the model

BASE_DIR = Path(__file__).resolve(strict=True).parent   # get the current directory inside the container

with open(f"{BASE_DIR}/trained_pipline-{__version__}.pkl", 'rb') as f:  # load the trained model
    model = pickle.load(f)  

# define the classes (langaues) that model can predict
classes = [
    "Arabic",
    "Danish",
    "Dutch",
    "English",
    "French",
    "German",
    "Greek",
    "Hindi",
    "Italian",
    "Kannada",
    "Malayalam",
    "Portugeese",
    "Russian",
    "Spanish",
    "Sweedish",
    "Tamil",
    "Turkish",
]
# define the predict_pipeline function that called from the API
def predict_pipeline(text):  
    """
    This function takes the text as input and return the predicted language
    text: str: the text that we want to predict its language
    return: str: the predicted language
    """
    # preprocess the text
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)   # remove special characters
    text = re.sub(r"[[]]", " ", text)                       # remove square brackets and the content inside them
    text = text.lower()                                     # convert the text to lowercase (normalization)
    pred = model.predict([text])                            # predict the language
    return classes[pred[0]]                                # return the predicted language