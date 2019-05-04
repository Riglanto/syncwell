import firebase_admin
from firebase_admin import credentials, firestore
from getkey import getkey, keys

def get_logger(name):
    return lambda x: print(f"{name}: {x}")

def client(name):
    cred = credentials.Certificate("credentials.json")
    options = {
        "databaseURL": "https://syncwell-de7ee.firebaseio.com/"
    }
    app = firebase_admin.initialize_app(cred, options, name)

    db = firestore.client(app)
    print(f"{app.name} initiated.")
    return db

def listener(name="Listener"):
    db = client(name)
    log = get_logger(name)
    def on_snapshot(doc_snapshot, changes, read_time):
        doc = doc_snapshot[0]
        log(f"Received updated {doc.id}: {doc.to_dict()['lastValue']}")

    ref = db.collection("users").document("test_user")

    doc_watch = ref.on_snapshot(on_snapshot)

def sender(name="Sender"):
    db = client(name)
    log = get_logger(name)
    log("Press any number to send update or q to exit...")
    key = None
    while key != keys.Q:
        key = getkey()
        if key.isnumeric():
            log(f"Sent {key}")
            db.collection("users").document("test_user").set({"lastValue": key})

listener()
sender()