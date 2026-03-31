import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

data = {
    "umur": [2, 3, 4, 5, 3, 4, 5],
    "berat": [10, 12, 14, 16, 11, 13, 15],
    "tinggi": [80, 90, 100, 110, 85, 95, 105],
    "status": [0, 1, 1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

X = df[["umur", "berat", "tinggi"]]
y = df["status"]

model = DecisionTreeClassifier()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model berhasil dibuat!")