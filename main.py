import jwt

# criando um token utilizando JWT


def create_token(data, secret):
    return jwt.encode(data, secret, 'HS256')

# verifição se o token está correto


def verify_signature(token):
    try:
        return jwt.decode(token, 'acelera')
    except:
        return {"error": 2}


# atribuindo a variavel token
token = create_token({"language": "Python"}, 'acelera')

# atribuindo a variavel token
token_decoded = verify_signature(token)

print(token)

print(token_decoded)
