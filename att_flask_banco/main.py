from flask import Flask, render_template, request, redirect, url_for, flash
from att_flask_banco.controller.aluno_controller import AlunoController
from att_flask_banco.controller.curso_controller import CursoController
from att_flask_banco.model.aluno import Aluno
from att_flask_banco.model.curso import Curso

app = Flask(__name__)
app.secret_key = '123'
controle_aluno = AlunoController()
controle_curso = CursoController()

@app.route("/")
def index():
    return render_template("index.html", titulo="Página Inicial")

# CRUD para Aluno
@app.route("/listar-alunos")
def listar_alunos():
    alunos = controle_aluno.listarTodosRegistros(Aluno())
    return render_template("aluno/lista_aluno.html", titulo="Lista de Alunos", lista=alunos)

@app.route("/buscar-aluno", methods=["GET", "POST"])
def buscar_aluno():
    if request.method == "POST":
        id_aluno = request.form["id"]
        aluno = Aluno()
        aluno.set_idalunos = id_aluno
        resultado = controle_aluno.pesquisaCodigo(aluno)
        print(resultado)
        return render_template("aluno/resultado_aluno.html", aluno=resultado)

    lista_alunos = controle_aluno.listarTodosRegistros(Aluno())
    return render_template("aluno/buscar_aluno.html", lista_alunos=lista_alunos)


@app.route("/cadastrar-aluno", methods=["GET", "POST"])
def cadastrar_aluno():
    cursos = controle_curso.listarTodosRegistros(Curso())
    if request.method == "POST":
        aluno = Aluno()
        aluno.set_alunoscol = request.form["alunoscol"]
        aluno.set_nome = request.form["nome"]
        aluno.set_cidade = request.form["cidade"]
        aluno.set_uf = request.form["uf"]
        aluno.set_cep = request.form["cep"]
        aluno.set_email = request.form["email"]
        aluno.set_prontuario = request.form["prontuario"]
        aluno.set_idcurso = int(request.form["curso_idcursos"])
        controle_aluno.incluir_aluno(aluno)
        return redirect(url_for("listar_alunos"))

    return render_template("aluno/cadastro_aluno.html", titulo="Cadastro de Alunos",cursos=cursos)


@app.route("/editar-aluno/<int:id>", methods=["GET", "POST"])
def editar_aluno(id):
    if request.method == "POST":
        aluno = Aluno()
        aluno.set_idalunos = id
        aluno.set_alunoscol = request.form["alunoscol"]
        aluno.set_nome = request.form["nome"]
        aluno.set_cidade = request.form["cidade"]
        aluno.set_uf = request.form["uf"]
        aluno.set_cep = request.form["cep"]
        aluno.set_email = request.form["email"]
        aluno.set_prontuario = request.form["prontuario"]
        aluno.set_idcurso = request.form["curso_idcursos"]
        controle_aluno.alterar_aluno(aluno)
        return redirect(url_for("listar_alunos"))

    aluno = Aluno()
    aluno.set_idalunos = id
    resultado = controle_aluno.pesquisaCodigo(aluno)
    cursos = controle_curso.listarTodosRegistros(Curso())
    return render_template("aluno/editar_aluno.html", pessoa=resultado, cursos=cursos)


@app.route("/remover-aluno/<int:id>")
def remover_aluno(id):
    aluno = Aluno()
    aluno.set_idalunos = id
    controle_aluno.excluir_aluno(aluno)
    return redirect(url_for("listar_alunos"))

# CRUD para Curso
@app.route("/listar-cursos")
def listar_cursos():
    cursos = controle_curso.listarTodosRegistros(Curso())
    return render_template("curso/lista_curso.html", titulo="Lista de Cursos", lista=cursos)


@app.route("/buscar-curso", methods=["GET", "POST"])
def buscar_curso():
    if request.method == "POST":
        id_curso = request.form["idcurso"]
        curso = Curso()
        curso.set_idcursos = id_curso
        resultado = controle_curso.pesquisaCodigo(curso)
        return render_template("curso/resultado_curso.html", curso=resultado)

    cursos = controle_curso.listarTodosRegistros(Curso())
    return render_template("curso/buscar_curso.html", lista_cursos=cursos)


@app.route("/cadastrar-curso", methods=["GET", "POST"])
def cadastrar_curso():
    if request.method == "POST":
        curso = Curso()
        curso.set_nomecurso = request.form["nomecurso"]
        curso.set_sigla = request.form["sigla"]
        controle_curso.incluir_curso(curso)
        return redirect(url_for("listar_cursos"))
    return render_template("curso/cadastro_curso.html", titulo="Cadastro de Curso")

@app.route("/editar-curso/<int:id>", methods=["GET", "POST"])
def editar_curso(id):
    if request.method == "POST":
        curso = Curso()
        curso.set_idcursos = id
        curso.set_nomecurso = request.form["nomecurso"]
        curso.set_sigla = request.form["sigla"]
        controle_curso.alterar_curso(curso)
        return redirect(url_for("listar_cursos"))

    curso = Curso()
    curso.set_idcursos = id
    resultado = controle_curso.pesquisaCodigo(curso)
    return render_template("curso/editar_curso.html", curso=resultado)


@app.route("/remover-curso/<int:id>")
def remover_curso(id):
    curso = Curso()
    curso.set_idcursos = id
    controle_curso.deletar_curso(curso)
    return redirect(url_for("listar_cursos"))

if __name__ == "__main__":
    app.run(debug=True)
