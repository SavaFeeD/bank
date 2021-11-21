from hashlib import sha256


def proceed_release(body, chat_id):
    print(body, chat_id)


def get_hash(value):
    return sha256(value.encode('utf-8')).hexdigest()
