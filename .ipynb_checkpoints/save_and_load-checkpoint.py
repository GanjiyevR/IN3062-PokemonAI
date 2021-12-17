{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0e892dc8",
   "metadata": {},
   "outputs": [],
   "source": [
    "from tensorflow.keras.models import load_model\n",
    "\n",
    "def save_model(model, save_path, name):\n",
    "    #Save the neural network to HDF5 and added a flag incase I want to adjust the model without saving\n",
    "    save = input(\"Save model?: y/n\")\n",
    "    if (save == \"y\"):\n",
    "        model.save(os.save_path.join(path,(name + \".h5\")))\n",
    "\n",
    "def model_loader(model, save_path, name):\n",
    "    model = load_model(os.path.join(save_path,(name + \".h5\")))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
