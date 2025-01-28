# Machine Learning Pipeline - End-to-End Setup

This document provides step-by-step instructions to set up and run the ML pipeline, including environment setup, model training, deployment, and Dockerization for cloud deployment.

---

## 1️⃣ Create a Conda Virtual Environment (Python 3.9)
To create and activate a virtual environment named **mlopproject**, run the following commands:

```bash
conda create --name mlopproject python=3.9 -y
conda activate mlopproject
pip install -r requirements.txt
```

---

## 2️⃣ Automate Environment Setup with a Bash Script
You can automate the environment setup using the following script.

### **Save the script below as `setup_env.sh` and run:**
```bash
bash setup_env.sh
```

### **`setup_env.sh` (Bash Script)**
```bash
#!/bin/bash

# Create Conda virtual environment
echo "Creating Conda environment (mlopproject) with Python 3.9..."
conda create --name mlopproject python=3.9 -y

# Activate the environment
echo "Activating the Conda environment..."
source activate mlopproject

# Install required dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo "Setup complete! Virtual environment is ready."
```

---

## 3️⃣ Run MLflow Tracking UI
To track experiments, start MLflow on **port 5001** using the command:

```bash
mlflow ui --port 5001
```

This will launch the MLflow dashboard, accessible at **http://localhost:5001**.

---

## 4️⃣ Train the Machine Learning Model
Run the model training script to preprocess data, train the model, and save artifacts.

```bash
python src/pipeline/model_trainer.py
```

---

## 5️⃣ Deploy the Model (Flask & FastAPI)

### **Flask Deployment (Port 5000)**
Run the Flask app using:

```bash
python app.py
```

The Flask app will be accessible at: **http://localhost:5000**

### **FastAPI Deployment (Port 8080)**
Run the FastAPI app using:

```bash
python app_fastapi.py
```

The FastAPI app will be accessible at: **http://localhost:8080/docs**

---

## 6️⃣ Build a Docker Image for Cloud Deployment
To containerize the project, build a **Docker image** and tag it as **mlopproject**:

```bash
docker build -t mlopproject .
```

Run the Docker container:

```bash
docker run -p 5000:5000 mlopproject
```

💡 **This Docker image can be used for cloud deployment** (AWS, GCP, Azure, etc.).

---

## 📌 Final Notes
- Ensure **Conda is installed** before running the setup script.
- Modify **Flask/MLflow ports** if necessary.
- The Docker image can be pushed to a registry for cloud deployment.

✅ **You're now ready to run the ML pipeline!** 🚀

