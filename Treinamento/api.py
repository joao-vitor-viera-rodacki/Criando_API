from flask import Flask, request

from main import cadastraUsuatio

app = Flask('Usuarios')

@app.route('/test', methods=['GET'])
def cadastra_usuario():
    body = request.get_json()

    if('nome' not in body):
        return gerarResponse(400,'nome é um requesito obrigatorio')
    
    if('idade' not in body):
        return gerarResponse(400,'idade é um requesito obrigatorio')

    if('email' not in body):
        return gerarResponse(400,'email é um requesito obrigatorio')
    
    user_dados = cadastraUsuatio(body['nome'], body['idade'], body['email'])
    return gerarResponse(200,'Usuario Criado','user',user_dados)

def gerarResponse(status, mensagem ,nome_do_conteudo=False, conteudo=False):
    response = {}
    response['status'] = status
    response['mensagem'] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo
    
    return response
    
app.run()
