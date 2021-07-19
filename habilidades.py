from flask_restful import Resource


habilidades = ['Python', 'Java','JavaScript','Ruby']
class Habilidades(Resource):
    def get(self):
        return habilidades

