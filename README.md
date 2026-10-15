# 🌧️ Indonesia Weather Rain Prediction: 3-Model Benchmark Comparison

Proyek komparasi dan analisis mendalam *step-by-step* untuk memprediksi apakah hujan akan turun dalam kurun waktu 6 jam ke depan (`rain_next_6h`) di wilayah Indonesia, menggunakan pendekatan **Machine Learning Klasik** dan **Deep Learning (TensorFlow)**.

---

## 📌 Ringkasan Proyek

- **Tujuan**: Klasifikasi biner untuk memprediksi potensi hujan (`rain_next_6h = 1` vs `0`).
- **Dataset**: [Indonesia Hourly Weather for Rain Prediction](https://www.kaggle.com/datasets/karanroyka/indonesia-hourly-weather-for-rain-prediction)
- **Ukuran Data**: ~147.264 data training, 31.560 data validasi, dan 31.560 data test.
- **Fitur yang Digunakan**: 11 variabel meteorologi & temporal (`temperature_2m`, `relative_humidity_2m`, `apparent_temperature`, `surface_pressure`, `cloud_cover`, `wind_speed_10m`, `wind_direction_10m`, `precipitation`, `rain`, `hour`, `month`).
- **Data Leakage Prevention**: Kolom masa depan seperti `rain_sum_next_6h` di-drop sebelum training.

---

## 🔬 Model yang Dikomparasikan

1. **Model 1: Logistic Regression** *(ML Biasa 1 - Linear Baseline)*  
   Model linear cepat terstandarisasi (`StandardScaler`) untuk baseline performa dan interpretasi langsung koefisien fitur.
2. **Model 2: Random Forest Classifier** *(ML Biasa 2 - Tree-Based Ensemble)*  
   Model ensemble non-linear berbasis 100 decision trees (`max_depth=16`, `n_jobs=-1`) yang menangkap interaksi cuaca kompleks dan mengukur *Feature Importance*.
3. **Model 3: Deep Neural Network / MLP** *(Deep Learning - TensorFlow & Keras)*  
   Arsitektur sekuensial multi-layer:
   - `Dense(128, relu)` + `BatchNormalization` + `Dropout(0.3)`
   - `Dense(64, relu)` + `Dropout(0.2)`
   - `Dense(32, relu)`
   - `Dense(1, sigmoid)`
   - Callbacks: `EarlyStopping` (restore best weights) & `ReduceLROnPlateau`.

---

## 📊 Hasil Evaluasi & Benchmark

Pengujian dilakukan pada **Test Set (31.560 baris data)** yang independen dari proses training:

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC | Training Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression** | 82.90% | 87.39% | 75.60% | 0.8107 | 0.9130 | **~0.2 s** ⚡ |
| **Random Forest** | 85.09% | **91.87%** 🏆 | 75.92% | 0.8314 | 0.9326 | ~2.3 s |
| **TensorFlow DNN** | **85.30%** 🏆 | 90.95% | **77.34%** 🏆 | **0.8360** 🏆 | **0.9335** 🏆 | ~15.1 s |

### 💡 Insight Utama:
- **Random Forest** mencetak **Precision tertinggi (91.87%)** dengan alarm palsu (*False Positives*) terendah (hanya 1.027 dari 31.560 data test). Sangat ideal untuk layanan publik yang mengutamakan kepastian ramalan.
- **TensorFlow DNN** mencetak **Akurasi (85.30%)**, **F1-Score (0.8360)**, dan **Recall (77.34%) tertinggi**, paling sedikit kecolongan kejadian hujan yang sebenarnya terjadi.
- **Logistic Regression** menjadi baseline yang solid dengan ROC-AUC di atas 0.91 dan waktu komputasi super instan (0.2 detik).

---

## 📁 Struktur Repositori

```text
├── dataset/                                # Folder penyimpanan dataset lokal (.csv)
│   └── .gitkeep
├── download_dataset.py                     # Script otomatis download & setup dataset
├── weather_rain_model_comparison.ipynb     # Notebook step-by-step komparasi model
├── requirements.txt                        # Daftar dependensi library
├── .gitignore                              # Mengabaikan venv, cache, & dataset besar
└── README.md                               # Dokumentasi proyek
```

---

## 🚀 Panduan Instalasi & Menjalankan

### 1. Clone Repositori
```bash
git clone https://github.com/afebrioo/indonesia-weather-rain-prediction.git
cd indonesia-weather-rain-prediction
```

### 2. Buat & Aktifkan Virtual Environment
```bash
# Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependensi
```bash
pip install -r requirements.txt
```

### 4. Download Dataset
Jalankan script untuk mengunduh dataset secara otomatis ke folder `./dataset/`:
```bash
python download_dataset.py
```

### 5. Jalankan Notebook
Buka [weather_rain_model_comparison.ipynb](weather_rain_model_comparison.ipynb) di VS Code / Jupyter:
```bash
jupyter notebook
```
Pastikan kernel yang dipilih mengarah ke kernel virtual environment (`.venv`).
