import os

preprocessor_path = os.path.abspath(os.path.join("artifacts", "preprocessor.pkl"))
print("Computed Path:", preprocessor_path)
print("Path Exists:", os.path.exists(preprocessor_path))
