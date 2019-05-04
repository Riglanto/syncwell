To start the app:

```
python -m venv .env
pip install -r requirements.txt
source .env/bin/activate
python app.py
```

Technologies used for demo:

- Python
- firebase SDK

Notes:

- Firestore is a cross platform solution for realtime databases.
- Can be easily used with web or mobile platforms.
- Data is synced live using listeners.
- Scaling and traffic is handled by google.
- User athentication can be done using JWT token and provided signin methods like gmail etc.
