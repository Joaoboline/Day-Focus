from flask_sqlalchemy import SQLAlchemy

# Instância do SQLAlchemy
db = SQLAlchemy()

class Tarefa(db.Model):
    __tablename__ = 'tarefas'  # Nome da tabela no banco de dados

    id = db.Column(db.Integer, primary_key=True)  # Identificador único
    titulo = db.Column(db.String(100), nullable=False)  # Título da tarefa
    descricao = db.Column(db.String(255), nullable=True)  # Descrição da tarefa
    vencimento = db.Column(db.Date, nullable=False)  # Data de vencimento
    prioridade = db.Column(db.String(10), nullable=False)  # Prioridade da tarefa
    concluida = db.Column(db.Boolean, default=False)  # Status da tarefa

    def __repr__(self):
        return f'<Tarefa {self.titulo}>'
