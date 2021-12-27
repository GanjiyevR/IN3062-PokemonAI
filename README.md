# IN3062-PokemonAI
A collaborative project between myself and Nathan Odibo, on the IN3062 module, where we are creating an AI based around pokemon.

Coding was done within Jupyter Notebook.
Outputs for our model have been generated in advance and the respective models have been saved (see the save files under "Other files" within this readme).
The dataset used for these ouputs is "pokemon.csv"

Code:
doodlesLegendary.ipynb and doodlesStats.ipynb (are the 2 classification modules for legendaries and types, they are independent from each other)

Code that generates the model (for each of classification task) generaly operates by:
- importing and shuffling the dataset (shuffling is done on a fixed seed defined within this step)
- splitting the dataset to training and testing/holdout sets
- fitting the data to the Sequential model and compiling it (also saves the model at the end of this step)
- fitting the data displaying the results if we perform the classification on knn and a random forest model
- displaying the data in a PCA (commented out but output was generated to avoid the confussion matrix in the next section from becomming harder to read)
  (also contains another commented out section that displays the PCA for each individual target)
- Displaying the results of the model saved in the "seqKFold.h5" along with a confussion matrix

Datasets:
- pokemon.csv (the primary dataset used in the 2 codebases)
- pokemonAlteredType.csv (an altered dataset for the Type classifier that replaced the type "normal" in the "Type1" column with the type in "Type2" if there was one

Other files:
- save_and_load.py (a file made to simplify the saving and loading of the sequential models generated, imported in both of the model code files)
- seqKFold.h5 (the save file for the type classification model)
- seqKFoldLegendary.h5 (the save file for the legendary classification model)
