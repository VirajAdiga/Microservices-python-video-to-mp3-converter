import json


def notification(message):
    message = json.loads(message)
    mp3_fid = message["mp3_fid"]
    receiver_address = message["username"]

    # Sending mail

    print("Mail Sent")
    print(f"User - {receiver_address} received mp3 id - {mp3_fid}")
