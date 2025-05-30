from flask import Flask
from flasgger import Swagger
from routes.usuario.usuario_route import usuario_bp
from routes.vacinas.vacinas_route import vacinas_bp

app = Flask(__name__)
swagger = Swagger(app)

app.register_blueprint(usuario_bp, url_prefix="/usuarios")
app.register_blueprint(vacinas_bp, url_prefix="/vacinas") 

@app.route("/")
def home():
    return "🚀 API AgendaPET está rodando!"

if __name__ == "__main__":
    app.run(debug=True)
