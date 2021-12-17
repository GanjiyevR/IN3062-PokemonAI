import os
from tensorflow.keras.models import load_model

def save_model(model, save_path, name):
    #Save the neural network to HDF5 and added a flag incase I want to adjust the model without saving
    save = input("Save model? y/n : ")
    if (save == "y"):
        model.save(os.path.join(save_path,(name + ".h5")))

def model_loader(save_path, name):
    model = load_model(os.path.join(save_path,(name + ".h5")))
    return model
