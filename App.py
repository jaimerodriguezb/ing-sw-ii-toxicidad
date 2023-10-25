from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS

from modelo.medidor_toxicidad import MedidorToxicidad

app = Flask(__name__)
CORS(app)
medir = MedidorToxicidad()

api = Api(
    app, 
    version='1.0', 
    title='medidior de toxicidad',
    description='Medidor de toxicidad')

ns = api.namespace('medidor')

medidor = api.parser()

medidor.add_argument(
    'Comentario',
    type=str, 
    required=True,
    help='Ingrese un comentario ...', 
    location='args')

resource_fields = api.model('Resource', {
    'Toxicidad': fields.String,
})

@ns.route('/Sentimientos')
class AnalizadorApi(Resource):

    @api.doc(parser=medidor)
    @api.marshal_with(resource_fields)
    def get(self):
        args = medidor.parse_args()

        return{
            'Toxicidad': medir.medir_toxicidad(args['Comentario'])
        }, 200

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)