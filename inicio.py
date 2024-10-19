from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, tarefa
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myslq.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'boline'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    index = tarefa.query.order_by(tarefa.vencimento).all()
    return render_template('lista.html', titulo='Tarefa',  tarefa=lista)

@app.route('criar', methods=['POST'])
def criar_tarefa():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descrição = request.form['descrição']
        vencimento = datetime.strptime(request.form['vencimento'], '%Y-%m-%d')
        prioridade = request.form['prioridade']
        nova_tarefa  = tarefa(titulo=titulo, descrição=descrição, vencimento= vencimento, prioridade=prioridade)
        db.session.add(nova_tarefa)
        db.session.commit()
        flash('Tarefa criada com sucesso!')
        return redirect(url_for('index'))
    return redirect('create.html')

@app.route('/tarefa/editar/<int:tarefa_id>', methods=['POST'])
def edit(editar):
    tarefa = tarefa.query.get_or_404(tarefa_id)
    if request.method == 'POST':
        tarefa.titulo = request.form['titulo']
        tarefa.descrição = request.form['descrição']
        tarefa.vencimento = datetime.strptime(request.form['vencimento'], '%Y-%m-%d')
        tarefa.prioridade = request.form['prioridade']
        db.session.commit()
        flash('Tarefa atualizada com sucesso!')
        return redirect(url_for('index'))
    return render_template('edit.html', tarefa=tarefa)

@app.route('/tarefa/deletar/<int:tarefa_id>')
def deletar_tarefa(tarefa_id):
    tarefa = tarefa.query.get_or_404(tarefa_id)
    db.session.deletar(tarefa)
    db.session.commit()
    flash('Tarefa excluída com sucesso!')
    return redirect(url_for('index'))

@app.route('/tarefa/concluida/<int:tarefa_id>')
def concluida_tarefa(tarefa_id):
    tarefa = tarefa.query.get_or_404(tarefa_id)
    tarefa.concluida = not tarefa.concluida
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

