from flask import Flask, jsonify, request
import json
app = Flask(__name__)

desenvolvedores = [
    {'nome':'Rafael',
     'habilidades':['Python','Flask',]
     },
    {'nome':'Radames',
     'habilidades':['Python', 'Django']
     },
    {'nome':'Marcelo',
     'habilidades':['JavaScript', 'Java']}

]
#devolde deleta e altera um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET','PUT','DELETE']) #matodo PUT serve para alteração
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desevolvedor de id {} não existe'.format(id)
            response = {'status':'falha','menságem':mensagem}

        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == "DELETE":
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso','mensagem':'resgistro excluido'})

#mostrar todos e permite incluir um novo
@app.route('/dev/', methods=['POST','GET'])
def lista_deselvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status':'sucesso','mensagem':'registro iserido'})

    elif request.method == "GET":
        return jsonify(desenvolvedores)



if __name__ == '__main__':
    app.run(debug=True)


