import uuid
def generar_token():
    token = str(uuid.uuid4())
    token_final=token[:6]
    return token_final



