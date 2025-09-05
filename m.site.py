from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configurações do Gmail 
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mateusferrari.am@gmail.com'
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')  # coloque sua variável de ambiente
app.config['MAIL_DEFAULT_SENDER'] = ('Portifólio Dev', os.getenv('EMAIL_USER'))

mail = Mail(app)

# Rotas 
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos", methods=['GET', 'POST'])
def contatos():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        gmail = request.form['gmail']
        assunto = request.form['assunto']

        corpo_email = f"""
        Novo contato recebido:

        Nome: {nome}
        Telefone: {telefone}
        Gmail: {gmail}
        Assunto: {assunto}
        """
        msg = Message(subject="Novo contato :)", recipients=[os.getenv('EMAIL_USER')], body=corpo_email)
        mail.send(msg)

        return redirect(url_for('homepage'))

    return render_template("contatos.html")

if __name__ == "__main__":
    app.run(debug=True)


