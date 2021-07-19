import json
from flask import Flask, request
from habilidades import Habilidades
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

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


class Desenvolvedor(Resource):
    def get(self,id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desevolvedor de id {} não existe'.format(id)
            response = {'status': 'falha', 'menságem': mensagem}

        return response

    def put(self,id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self,id):
        desenvolvedores.pop(id)
        return {'status':'sucesso','mensagem':'resgistro excluido'}

class ListaDeselvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]



api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDeselvolvedores,'/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)
