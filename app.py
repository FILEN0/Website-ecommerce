try:
    from flask import Flask, redirect, url_for, request,render_template
    import mysql.connector as SQL
except Exception as erro:
    print("ERRO ao importar BIBLIOTECAS:",erro)
HOST="http://127.0.0.1:5000/"
loginHTML= "login.html"
indexHTML= "index.html"
viewHTMLpart1="view.html"
relationshipHTML="relationship.html"
def SQLJOIN(numJoin=None,numFilter='0'):    
    answer = SQLCONNECT()  
    print (answer)
    if (not answer):
        return redirect(HOST)
    
    if numFilter!='0':
        print([numJoin,numFilter])
        if numJoin=='1':
            SQL_DEFAULT=("ID (Pedido)","Data","Status","Cliente","Produto")
            if numFilter.isnumeric():     
                SQL_CURSOR=SQL_CONEXAO.cursor()
                SQL_COMMAND=f"""SELECT pedidos.pedido_id,pedidos.data_pedido,pedidos.status_pedido,Clientes.nome,Clientes.email
                                FROM Pedidos
                                INNER JOIN Clientes ON Pedidos.cliente_id=Clientes.cliente_id
                                WHERE Clientes.cliente_id={int(numFilter)};"""
                print(SQL_COMMAND)
                SQL_CURSOR.execute(SQL_COMMAND)
                SQL_DATA=SQL_CURSOR.fetchall()
                if SQL_DATA == None:
                    return [SQL_DEFAULT]
                SQL_DATA.insert(0,SQL_DEFAULT)
                return SQL_DATA
            else:
                return False
        elif numJoin=='2':
            SQL_DEFAULT=("ID","Produto","Preço","Categoria")
            if numFilter.isnumeric():     
                SQL_CURSOR=SQL_CONEXAO.cursor()
                SQL_COMMAND=f"""
                    SELECT Produtos.produto_id,Produtos.nome,Produtos.preco,Categorias.nome
                    FROM Produtos
                    INNER JOIN Categorias ON Categorias.categoria_id=Produtos.categoria_id
                    WHERE Categorias.categoria_id={int(numFilter)}
                    """
                print(SQL_COMMAND)
                SQL_CURSOR.execute(SQL_COMMAND)
                SQL_DATA=SQL_CURSOR.fetchall()
                if SQL_DATA == None:
                    return [SQL_DEFAULT]
                SQL_DATA.insert(0,SQL_DEFAULT)
                return SQL_DATA
            else:
                return False
        elif numJoin=='3':
            SQL_DEFAULT=("ID (Pedido)","Data","Status","Cliente","Produto")
            if numFilter.isnumeric():     
                SQL_CURSOR=SQL_CONEXAO.cursor()
                SQL_COMMAND=f"""
                    SELECT pedidos.pedido_id,pedidos.data_pedido,pedidos.status_pedido,Clientes.nome,Produtos.nome
                    FROM Pedidos
                    INNER JOIN Clientes ON Pedidos.cliente_id=Clientes.cliente_id
                    INNER JOIN ProdutosPedido ON Pedidos.pedido_id=ProdutosPedido.FK_pedido_id
                    INNER JOIN Produtos ON ProdutosPedido.FK_produto_id = Produtos.produto_id
                    WHERE Clientes.cliente_id={int(numFilter)}
                    """
                print(SQL_COMMAND)
                SQL_CURSOR.execute(SQL_COMMAND)
                SQL_DATA=SQL_CURSOR.fetchall()
                if SQL_DATA == None:
                    return [SQL_DEFAULT]
                SQL_DATA.insert(0,SQL_DEFAULT)
                return SQL_DATA
            else:
                return False
        elif numJoin=='4':
            SQL_DEFAULT=("Produto","Preço","Estoque","Categoria")
            if numFilter.isnumeric():     
                SQL_CURSOR=SQL_CONEXAO.cursor()
                SQL_COMMAND=f"""
                    SELECT Produtos.nome,Produtos.preco,Produtos.quantidade_estoque,Categorias.nome
                    FROM Produtos
                    INNER JOIN Categorias ON Categorias.categoria_id=Produtos.categoria_id
                    WHERE Categorias.categoria_id={int(numFilter)} AND Produtos.quantidade_estoque>0
                    """
                print(SQL_COMMAND)
                SQL_CURSOR.execute(SQL_COMMAND)
                SQL_DATA=SQL_CURSOR.fetchall()
                if SQL_DATA == None:
                    return [SQL_DEFAULT]
                SQL_DATA.insert(0,SQL_DEFAULT)
                return SQL_DATA
            else:
                return False
        elif numJoin=='7':
            SQL_DEFAULT=("ID","Data","Status","Cliente","Produto")
            print("joindedata")
            try:
                data=numFilter.split('-')
                data[0]=int(data[0])
                data[1]=int(data[1])
                data[2]=int(data[2])
            except:
                return False   
            print("joindedata pra int")  
            SQL_CURSOR=SQL_CONEXAO.cursor()
            SQL_COMMAND=f"""
                SELECT Pedidos.pedido_id,Pedidos.data_pedido,Pedidos.status_pedido,Clientes.nome,Produtos.nome
                FROM Pedidos
                INNER JOIN Clientes ON Pedidos.cliente_id = Clientes.cliente_id
                INNER JOIN ProdutosPedido ON Pedidos.pedido_id=ProdutosPedido.FK_pedido_id
                INNER JOIN Produtos ON Produtos.produto_id=ProdutosPedido.FK_produto_id
                WHERE Pedidos.data_pedido='{numFilter}'
                ORDER BY Pedidos.pedido_id
                """
            print(SQL_COMMAND)
            SQL_CURSOR.execute(SQL_COMMAND)
            SQL_DATA=SQL_CURSOR.fetchall()
            if SQL_DATA == None:
                return [SQL_DEFAULT]
            SQL_DATA.insert(0,SQL_DEFAULT)
            return SQL_DATA
            return
                

    else:
        if numJoin=='1':        
            SQL_DEFAULT=("ID","Cliente","Email","Endereço","Telefone")
            SQL_CURSOR=SQL_CONEXAO.cursor()
            SQL_COMMAND="SELECT * FROM CLIENTES"
            SQL_CURSOR.execute(SQL_COMMAND)
            SQL_DATA=SQL_CURSOR.fetchall()
            if SQL_DATA == None:
                return [SQL_DEFAULT]
            SQL_DATA.insert(0,SQL_DEFAULT)
            return SQL_DATA
        elif numJoin=='2':
            SQL_DEFAULT=("ID","Categoria","Descrição")
            SQL_CURSOR=SQL_CONEXAO.cursor()
            SQL_COMMAND="SELECT * FROM CATEGORIAS"
            SQL_CURSOR.execute(SQL_COMMAND)
            SQL_DATA=SQL_CURSOR.fetchall()
            if SQL_DATA == None:
                return [SQL_DEFAULT]
            SQL_DATA.insert(0,SQL_DEFAULT)
            return SQL_DATA
        elif numJoin=='3':
            SQL_DEFAULT=("ID","Cliente","Email","Endereço","Telefone")
            SQL_CURSOR=SQL_CONEXAO.cursor()
            SQL_COMMAND="SELECT * FROM CLIENTES"
            SQL_CURSOR.execute(SQL_COMMAND)
            SQL_DATA=SQL_CURSOR.fetchall()
            if SQL_DATA == None:
                return [SQL_DEFAULT]
            SQL_DATA.insert(0,SQL_DEFAULT)
            return SQL_DATA
        elif numJoin=='4':
            SQL_DEFAULT=("ID","Categoria","Descrição")
            SQL_CURSOR=SQL_CONEXAO.cursor()
            SQL_COMMAND="SELECT * FROM CATEGORIAS"
            SQL_CURSOR.execute(SQL_COMMAND)
            SQL_DATA=SQL_CURSOR.fetchall()
            if SQL_DATA == None:
                return [SQL_DEFAULT]
            SQL_DATA.insert(0,SQL_DEFAULT)
            return SQL_DATA
        elif numJoin=='5':
            SQL_DEFAULT=("ID (Pedido)","Data (Pedido)","Status (Pedido)","Cliente","Produto")
            SQL_CURSOR=SQL_CONEXAO.cursor()
            SQL_COMMAND='''
                SELECT pedidos.pedido_id,pedidos.data_pedido,pedidos.status_pedido,Clientes.nome,Produtos.nome FROM Pedidos
                INNER JOIN Clientes ON Pedidos.cliente_id = Clientes.cliente_id
                INNER JOIN ProdutosPedido ON Pedidos.pedido_id = ProdutosPedido.FK_pedido_id
                INNER JOIN Produtos ON ProdutosPedido.FK_produto_id = Produtos.produto_id WHERE pedidos.status_pedido<>"Concluído"
                ORDER BY pedidos.pedido_id'''
            SQL_CURSOR.execute(SQL_COMMAND)
            SQL_DATA=SQL_CURSOR.fetchall()
            if SQL_DATA == None:
                return [SQL_DEFAULT]
            SQL_DATA.insert(0,SQL_DEFAULT)
            return SQL_DATA
        elif numJoin=='6':
            SQL_DEFAULT=("Categoria","Média de Preço (R$)")
            SQL_CURSOR=SQL_CONEXAO.cursor()
            SQL_COMMAND='''
                SELECT Categorias.nome, AVG(Produtos.preco) FROM Categorias 
                INNER JOIN Produtos 
                ON Produtos.categoria_id=Categorias.categoria_id
                GROUP BY Categorias.categoria_id'''
            SQL_CURSOR.execute(SQL_COMMAND)
            SQL_DATA=SQL_CURSOR.fetchall()
            if SQL_DATA == None:
                return [SQL_DEFAULT]
            SQL_DATA.insert(0,SQL_DEFAULT)
            return SQL_DATA
        elif numJoin=='7':
            CALENDAR=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
            SQL_DEFAULT=("Dia","Mês","Ano")
            SQL_CURSOR=SQL_CONEXAO.cursor()
            SQL_COMMAND='''SELECT DISTINCT data_pedido from Pedidos order by data_pedido'''
            SQL_CURSOR.execute(SQL_COMMAND)
            SQL_DATA=SQL_CURSOR.fetchall()
            for i in range(len(SQL_DATA)):
                SQL_DATA[i]=SQL_DATA[i][0].split("-")[-1::-1]
                SQL_DATA[i][1]=CALENDAR[int(SQL_DATA[i][1])-1]
            if SQL_DATA == None:
                return [SQL_DEFAULT]
            SQL_DATA.insert(0,SQL_DEFAULT)
            return SQL_DATA
        elif numJoin=='8':
            SQL_DEFAULT=("Produto","Categoria")
            SQL_CURSOR=SQL_CONEXAO.cursor()
            SQL_COMMAND='''
                SELECT Produtos.nome,Categorias.nome 
                FROM Produtos 
                INNER JOIN Categorias ON Categorias.categoria_id=Produtos.categoria_id 
                WHERE Produtos.quantidade_estoque = 0
                ORDER BY Produtos.nome
                '''
            SQL_CURSOR.execute(SQL_COMMAND)
            SQL_DATA=SQL_CURSOR.fetchall()
            if SQL_DATA == None:
                return [SQL_DEFAULT]
            SQL_DATA.insert(0,SQL_DEFAULT)
            return SQL_DATA
        elif numJoin=='9':
            SQL_DEFAULT=("Cliente","Número de pedidos")
            SQL_CURSOR=SQL_CONEXAO.cursor()
            SQL_COMMAND='''
        SELECT Clientes.nome,COUNT(Pedidos.pedido_id)
        FROM Clientes 
        INNER JOIN Pedidos ON Pedidos.cliente_id = Clientes.cliente_id
        GROUP BY Clientes.cliente_id
        ORDER BY Clientes.nome
                '''
            SQL_CURSOR.execute(SQL_COMMAND)
            SQL_DATA=SQL_CURSOR.fetchall()
            if SQL_DATA == None:
                return [SQL_DEFAULT]
            SQL_DATA.insert(0,SQL_DEFAULT)
            return SQL_DATA
        else:
            SQL_DEFAULT=("Produto","Quantidade de pedidos")
            SQL_CURSOR=SQL_CONEXAO.cursor()
            SQL_COMMAND='''
                SELECT DISTINCT Produtos.nome, COUNT(ProdutosPedido.FK_produto_id)
                FROM Produtos
                INNER JOIN ProdutosPedido ON ProdutosPedido.FK_produto_id=Produtos.produto_id
                GROUP BY ProdutosPedido.FK_produto_id
                ORDER BY COUNT(ProdutosPedido.FK_produto_id) DESC, Produtos.nome
                '''
            SQL_CURSOR.execute(SQL_COMMAND)
            SQL_DATA=SQL_CURSOR.fetchall()
            if SQL_DATA == None:
                return [SQL_DEFAULT]
            SQL_DATA.insert(0,SQL_DEFAULT)
            return SQL_DATA
def SQLCONNECT():
    try:
        global SQL_CONEXAO
        SQL_CONEXAO=SQL.Connect(host='localhost',database='ecommerce',user='root',password='')
        print("Conectando...")            
        if SQL_CONEXAO.is_connected():
            print("Conectado!")
            return True
        else:
            print("Falha ao conectar!")
            return False
    except Exception as erro:
        print(f'ERRO em SQLCONNECT:{erro}')
        return False
    
app = Flask(__name__)
varENUNCIADO =["Consultar os pedidos de um cliente específico, exibindo os detalhes do pedido e as informações do cliente.",
                "Consultar os produtos de uma determinada categoria, exibindo os detalhes do produto e o nome da categoria.",
                "Consultar todos os pedidos realizados por um cliente específico, exibindo os detalhes do pedido, informações do cliente e nome do produto.",
                'Consultar os produtos em estoque de uma determinada categoria, exibindo o nome do produto, preço e quantidade em estoque.',
                'Consultar os pedidos que ainda não foram entregues, exibindo os detalhes do pedido, informações do cliente e nome do produto.',
                'Consultar a média de preços dos produtos de cada categoria, exibindo o nome da categoria e a média de preços.',
                'Consultar os pedidos realizados em uma determinada data, exibindo os detalhes do pedido, informações do cliente e nome do produto.',
                'Consultar os produtos que estão em falta no estoque, exibindo o nome do produto e nome da categoria.',
                'Consultar o número total de pedidos realizados por cada cliente, exibindo o nome do cliente e a quantidade de pedidos.',
                'Consultar os produtos mais vendidos, exibindo o nome do produto e a quantidade total de pedidos em que ele foi incluído.']




@app.route("/")
def login():
    return render_template(loginHTML)


@app.route("/index")
def indexlogado():
    return render_template(indexHTML)
@app.route("/relationship")
def relationship():
    return render_template(relationshipHTML)



@app.route("/login",methods=["POST"])
def index():
    if request.method !="POST":
        return redirect('127.0.0.1:5000/')
    host = request.form['host']
    user = request.form['user']
    password = request.form['password']
    banco = request.form['banco']
    porta = request.form['porta']
    if porta=="3306" and user=="root" and password=="" and banco=="ecommerce" and host=="localhost":
        answer = SQLCONNECT()  
        print (answer)
        if (not answer):
            return redirect(HOST)
        return redirect(HOST+'index')
    return redirect(HOST)

    
    return viewHTMLpart1+viewHTML_FORMAT
@app.route("/view/<joinNUM>",methods=["GET"])    
def view(joinNUM):
    if joinNUM not in ("1","2","3","4","5","6","7","8","9","10"):
        return redirect(HOST)
    reverseCALENDAR={
        "Mês":"0",
        "Janeiro":"01",
        "Fevereiro":"02",
        "Março":"03",
        "Abril":"04",
        "Maio":"05",
        "Junho":"06",
        "Julho":"07",
        "Agosto":"08",
        "Setembro":"09",
        "Outubro":"10",
        "Novembro":"11",
        "Dezembro":"12"
    }
    ROW_DATA_FULL=""

    SQL_DATA = SQLJOIN(joinNUM)    
    i=0
    for SQL_ROW in SQL_DATA:         
        if joinNUM == "7":
            print(joinNUM) 
            SQL_ID = SQL_ROW[2]+"-"+reverseCALENDAR[SQL_ROW[1]]+"-"+SQL_ROW[0]
        else:
            SQL_ID=SQL_ROW[0]
            print(joinNUM) 
        ROW_DATA=f"""<tr>"""
        for SQL_FIELD in SQL_ROW:
            ROW_DATA+=f"""<td>{f'<a href="{joinNUM}/{SQL_ID}">' if i!=0 and joinNUM in("1","2","3","4","7") else '' }{SQL_FIELD}{f'</a>' if i!=0 and joinNUM in("1","2","3","4","7") else '' }</td>"""
        ROW_DATA+="""</tr>
                """        
        ROW_DATA_FULL+=ROW_DATA
        i+=1
    viewHTML_FORMAT=f"""
                                    <div class="title">{varENUNCIADO[int(joinNUM)-1]}</div>
                                <table class="tabela">
                                    {ROW_DATA_FULL}
                                </table>
                            </div>
                        </main>
                    </body>
                    </html>
                    """
    if request.method !="GET":
        return redirect(HOST)
    
    return render_template(viewHTMLpart1)+viewHTML_FORMAT.format()

@app.route("/view/<joinWITHFILTER>/<joinFILTER>",methods=["GET"])    
def viewfiltered(joinWITHFILTER,joinFILTER="0"):    
    if joinWITHFILTER not in ("1","2","3","4","7"):
        return redirect(HOST)
    
    ROW_DATA_FULL=""

    SQL_DATA = SQLJOIN(joinWITHFILTER,joinFILTER)
    if SQL_DATA==False:
        return redirect(HOST)
    print(SQL_DATA)
    i=0
    for SQL_ROW in SQL_DATA:                
        SQL_ID=SQL_ROW[0]
        ROW_DATA=f"""<tr>"""
        for SQL_FIELD in SQL_ROW:
            ROW_DATA+=f"""<td>{SQL_FIELD}</td>"""
        ROW_DATA+="""</tr>
                """        
        ROW_DATA_FULL+=ROW_DATA
        i+=1
    viewHTML_FORMAT=f"""
                                    <div class="title">{varENUNCIADO[int(joinWITHFILTER)-1]}</div>
                                <table class="tabela">
                                    {ROW_DATA_FULL}
                                </table>
                            </div>
                        </main>
                    </body>
                    </html>
                    """
    if request.method !="GET":
        return redirect(HOST)
    
    return render_template(viewHTMLpart1)+viewHTML_FORMAT.format()


        

if __name__=="__main__":
    app.run(debug=True)