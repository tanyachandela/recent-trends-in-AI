# Fashion Classifier Web App

## Steps to Run Locally
1. Clone the repo
2. Go to backend folder: `cd backend`
3. Install dependencies: `pip install -r requirements.txt`
4. Run backend: `python app.py`
5. Open `frontend/index.html` in browser

## Deployment
- Deploy backend (Flask) on Render/Railway.
- Deploy frontend (HTML+JS) on Vercel.
- Update `script.js` fetch URL with your deployed backend API endpoint.

## API Endpoint
POST `/predict` with `file` (image) → returns JSON `{prediction: "class_name"}`
