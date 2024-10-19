from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descrição = db.Column(db.Text, nullable=True)
    vencimento = db.Column(db.DateTime, nullable=False)
    prioridade = db.Column(db.String(20), nullable=False)
    concluida = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Name %r>' % self.titulo