from flask import Flask, jsonify, request, render_template
import jwt

app = Flask(__name__)


@app.route("/")
def initial_page():
    return render_template('login_page.html')



# Rota responsável pela validação das informações fornecidas no cadastro
@app.route("/validate")
def validate():
    if request.method == 'POST':
        try:
            data_info = request.json
        except Exception as e:
            return jsonify({
                'Status': False,
                'Message': e
            }), 400















if __name__ == "__main__":
    app.run(debug=True)