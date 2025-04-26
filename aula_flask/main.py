from flask import Flask, render_template,request,redirect

app = Flask(__name__)
dados=[]
dados_produto=[]

@app.route('/')
def principal():
    return render_template('index.html')

##CLIENTE
@app.route('/cadastrar-cliente')
def cadastrar():
    return render_template('cliente/cadastro.html',titulo='Cadastrar')

@app.route('/salvar-cliente',methods=['POST'])
def salvar():
    id = request.form['id']
    nome = request.form['nome']
    endereco = request.form['endereco']
    dados.append({'id': id, 'nome': nome, 'endereco': endereco})
    return redirect('/lista-cliente')

@app.route('/lista-cliente')
def listar():
    return render_template('cliente/lista.html',
                           lista=dados,
                           titulo='Lista de Pessoas Cadastradas')
@app.route('/remover-cliente/<int:id>')
def remover(id):
    dados.pop(id-1)
    return redirect('/lista-cliente')

@app.route('/editar-cliente/<int:id>')
def editar(id):
    pessoa = next((p for p in dados if int(p['id']) == int(id)),
                  None)
    if pessoa:
        return render_template('cliente/editar.html',
                                                 pessoa=pessoa)
    return redirect('/lista-cliente')

@app.route('/atualizar-cliente', methods=['POST'])
def atualizar():
    global dados
    id = int(request.form['id'])
    nome = request.form['nome']
    endereco = request.form['endereco']

    for p in dados:
        if int(p['id']) == id:
            p['nome'] = nome
            p['endereco'] = endereco
            break
    return redirect('/lista-cliente')

@app.route('/contato')
def contato():
    return render_template('cliente/contato.html',email='vfmaziero@hotmail.com')

@app.route('/buscar-cliente')
def buscar():
    return render_template('cliente/buscar.html')

@app.route('/resultado-cliente')
def resultado():
    try:
        id_busca = int(request.args.get('id'))
        pessoa = next((p for p in dados if int(p['id']) == int(id_busca)), None)
    except (ValueError, TypeError):
        pessoa = None
    return render_template('cliente/resultado.html', pessoa=pessoa)


##PRODUTO
@app.route('/cadastrar-produto')
def cadastrar_produto():
    return render_template('produto/cadastro_produto.html',titulo='Cadastrar')

@app.route('/salvar-produto',methods=['POST'])
def salvar_produto():
    id = request.form['id']
    descricao = request.form['descricao']
    valor = request.form['valor']
    dados_produto.append({'id': id, 'descricao': descricao, 'valor': valor})
    return redirect('/lista-produto')

@app.route('/lista-produto')
def listar_produto():
    return render_template('produto/lista_produto.html',
                           lista=dados_produto,
                           titulo='Lista de Produtos Cadastrados')

@app.route('/remover-produto/<int:id>')
def remover_produto(id):
    dados_produto.pop(id-1)
    return redirect('/lista-produto')

@app.route('/editar-produto/<int:id>')
def editar_produto(id):
    produto = next((p for p in dados_produto if int(p['id']) == int(id)),
                  None)
    if produto:
        return render_template('produto/editar_produto.html',
                                                 produto=produto)
    return redirect('/lista-produto')

@app.route('/atualizar-produto', methods=['POST'])
def atualizar_produto():
    global dados_produto
    id = int(request.form['id'])
    descricao = request.form['descricao']
    valor = request.form['valor']

    for p in dados_produto:
        if int(p['id']) == id:
            p['descricao'] = descricao
            p['valor'] = valor
            break
    return redirect('/lista-produto')


@app.route('/buscar-produto')
def buscar_produto():
    return render_template('produto/buscar_produto.html')

@app.route('/resultado-produto')
def resultado_produto():
    try:
        id_busca = int(request.args.get('id'))
        produto = next((p for p in dados_produto if int(p['id']) == int(id_busca)), None)
    except (ValueError, TypeError):
        produto = None
    return render_template('produto/resultado_produto.html', produto=produto)


if __name__ == '__main__':
    app.run(debug=True)

