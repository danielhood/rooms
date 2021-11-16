import os.path
import pickle

def load(filename):
        if not os.path.isfile(filename + ".pickle"):
            return

        with open(filename + ".pickle", "rb") as f:
            return pickle.load(f)

def save(filename, data):
    with open(filename + ".pickle", "wb") as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
