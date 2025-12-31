# Property Price Prediction

Live demo: https://property-price-prediction-34o4.onrender.com

A small Flask-based project for predicting property prices using a trained machine learning model.

**Project Overview**

- **Description:** Web UI + scripts to train a model and predict property prices from input features.
- **Built with:** Python, scikit-learn, Flask (simple frontend in [templates/index.html](templates/index.html) and styles in [static/style.css](static/style.css)).

**Repository Structure**

- **App:** [app.py](app.py) — Flask web application serving the prediction UI.
- **Training:** [train.py](train.py) — Script to train the model and save artifacts.
- **Prediction (CLI):** [predict.py](predict.py) — Script to run a single prediction using saved artifacts.
- **Model artifacts:** [model.joblib](model.joblib), [scaler.joblib](scaler.joblib), [features_name.joblib](features_name.joblib)
- **Data:** [data/property.csv](data/property.csv)
- **Templates & Static:** [templates/index.html](templates/index.html), [static/style.css](static/style.css)
- **Dependencies:** [requirements.txt](requirements.txt)

**Quick Start**

- **1) Create and activate a virtual environment (recommended):**

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

- **2) Install dependencies:**

```bash
pip install -r requirements.txt
```

- **3) Run the web app:**

```bash
python app.py
# Open http://127.0.0.1:5000 in your browser
```

- **4) Train the model (if you want to retrain):**

```bash
python train.py
```

- **5) Make a CLI prediction:**

```bash
python predict.py
# check the script for required input format or example usage
```

**Model Artifacts**

- **model.joblib:** Trained regression model saved with joblib.
- **scaler.joblib:** Feature scaler used during training.
- **features_name.joblib:** Ordered list of feature names expected by the model.

Keep these files in the project root so `app.py` and `predict.py` can load them.

**Data**

- The sample dataset is at [data/property.csv](data/property.csv). Use it to retrain or extend the dataset.

**Notes & Tips**

- If you retrain, ensure the same preprocessing and feature order are used so the web app and `predict.py` remain compatible.
- Inspect `train.py` to see how the scaler and `features_name` are generated and saved.

**Contributing**

- Bug reports and improvements are welcome. Open an issue or submit a PR with small, focused changes.

**License & Credits**

- Add a license file if you intend to publish this project publicly. Credits to libraries used in `requirements.txt`.

---

If you want, I can also:

- Add example input JSON for `predict.py`.
- Add a minimal `README` badge or quick screenshots of the UI.
