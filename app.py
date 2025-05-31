from flask import Flask
from flasgger import Swagger
from routes.usuario.usuario_route import usuario_bp
from routes.vacinas.vacinas_route import vacinas_bp
from routes.pet_usuario.pet_usuario_route import pet_usuario_bp
from routes.pet.pet_route import pet_bp
from routes.medicamentos.medicamentos_route import medicamento_bp
from routes.historico_consulta.historico_consulta_route import historico_bp
from routes.dieta.dieta_route import dieta_bp
from routes.agenda_pet_usuario.agenda_pet_usuario_route import agenda_pet_usuario_bp
from routes.agenda.agenda_route import agenda_bp



app = Flask(__name__)
swagger = Swagger(app)

app.register_blueprint(usuario_bp, url_prefix="/usuarios")
app.register_blueprint(vacinas_bp, url_prefix="/vacinas") 
app.register_blueprint(pet_usuario_bp, url_prefix="/pet_usuario")
app.register_blueprint(pet_bp, url_prefix="/pets")
app.register_blueprint(medicamento_bp, url_prefix="/medicamentos")
app.register_blueprint(historico_bp, url_prefix="/historico_consultas")
app.register_blueprint(dieta_bp, url_prefix="/dietas")
app.register_blueprint(agenda_pet_usuario_bp, url_prefix="/agenda_pet_usuario")
app.register_blueprint(agenda_bp, url_prefix="/agenda")

@app.route("/")
def home():
    return "🚀 API AgendaPET está rodando!"

if __name__ == "__main__":
    app.run(debug=True)
