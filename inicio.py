from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tarefas = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nova_tarefa = request.form.get('tarefa')
        if nova_tarefa:
            tarefas.append(nova_tarefa)
        return redirect(url_for('index'))

    return render_template('index.html', tarefas=tarefas)

@app.route('/remover/<int:indice>', methods=['POST'])
def remover(indice):
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
