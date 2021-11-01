from flask import Flask, json, jsonify,request
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()


app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'ingreso_empresa'
mysql.init_app(app)

@app.route('/')
def index_route():
    return "Sistema de control empresa Costa Autos"

@app.route('/cliente', methods={'GET','POST'})
def index_cliente():
    if (request.method == 'POST'):
        nuevo_cliente = request.get_json();
        print(nuevo_cliente)
        cliente_id = nuevo_cliente['cliente_id']
        cliente_tipocedula = nuevo_cliente['cliente_tipocedula']
        cliente_nombre = nuevo_cliente['cliente_nombre']
        cliente_apellido = nuevo_cliente['cliente_apellido']
        cliente_calificacioncredito = nuevo_cliente['cliente_calificacioncredito']
        cliente_direccion= nuevo_cliente['cliente_direccion']
        cliente_telefono = nuevo_cliente['cliente_telefono']
        cliente_fechadenacimiento = nuevo_cliente['cliente_fechadenacimiento']

        conn = mysql.connect()
        cur = conn.cursor()

        cur.execute("INSERT INTO cliente(cliente_id,cliente_tipocedula,cliente_nombre,cliente_apellido,cliente_calificacioncredito,cliente_direccion,cliente_telefono,cliente_fechadenacimiento)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(cliente_id,cliente_tipocedula,cliente_nombre,cliente_apellido,cliente_calificacioncredito,cliente_direccion,cliente_telefono,cliente_fechadenacimiento))
        conn.commit()
        cur.close()
        return jsonify({"Response" : "Cliente Agregado con Exito :)"}),201

    else:
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM cliente")
        data_cliente = cur.fetchall()
        responseData = [] 
        for cliente in data_cliente:
            responseData.append(
        {        
      
        "Autentificacion ID cliente": cliente[0],
        "Tipo de cedula": cliente [1] ,
        "Nombre":  (cliente)[2] +" "+ (cliente) [3],
        "Calificacion del credito": cliente[4],
        "Direccion": cliente[5],
        "Telefono": cliente[6],
        "Fecha De Nacimiento": cliente[7],
        }
        ) 
        cur.execute("SELECT * FROM vendedor")
        data_vendedor = cur.fetchall()
        responseData1 = []
        for vendedor in data_vendedor:
            responseData1.append({
        "Autentificacion": vendedor[0],
        "Nombre": vendedor[1] + ' '+ vendedor[2],
        "Numero de Telefono": vendedor[7]})
        cur.execute("SELECT * FROM ventas")
        data_ventas = cur.fetchall()
        responseData2 = []
        for ventas in data_ventas:
            responseData2.append({
            "Venta CIV": ventas[0],
            "Codigo Consecutivo": ventas[1],
            "Monto": ventas[5],
            "Fecha de venta": ventas[6],
            "Tipo de Automovil": ventas[8] + " " + ventas[9] + " " + ventas[10]
        })
        return jsonify ({"Cliente": responseData, "Vendedor Info": responseData1, "Ventas Registro": responseData2}),201

    


@app.route('/vendedor', methods ={'POST', 'GET'})
def index_vendedor():
    if (request.method == 'POST'):
        nuevo_vendedor = request.get_json();
        print(nuevo_vendedor)
        vendedor_CIV = nuevo_vendedor['vendedor_CIV']
        vendedor_nombre = nuevo_vendedor['vendedor_nombre']
        vendedor_apellido = nuevo_vendedor['vendedor_apellido']
        vendedor_fechadenacimiento = nuevo_vendedor['vendedor_fechadenacimiento']
        vendedor_tipo = nuevo_vendedor['vendedor_tipo']
        vendedor_salario= nuevo_vendedor['vendedor_salario']
        vendedor_direccion = nuevo_vendedor['vendedor_direccion']
        vendedor_telefono = nuevo_vendedor['vendedor_telefono']
        vendedor_porcentaje = nuevo_vendedor['vendedor_porcentaje']
        vendedor_monto = nuevo_vendedor['vendedor_monto']
        
        conn = mysql.connect()
        cur = conn.cursor()

        cur.execute("INSERT INTO vendedor(vendedor_CIV,vendedor_nombre,vendedor_apellido,vendedor_fechadenacimiento,vendedor_tipo,vendedor_salario,vendedor_direccion,vendedor_telefono,vendedor_porcentaje,vendedor_monto)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(vendedor_CIV,vendedor_nombre,vendedor_apellido,vendedor_fechadenacimiento,vendedor_tipo,vendedor_salario,vendedor_direccion,vendedor_telefono,vendedor_porcentaje,vendedor_monto))
        conn.commit()
        cur.close()
        return jsonify({"Response" : "Vendedor Agregado con Exito :)"}),201

    else:
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM vendedor")
   

        data_vendedores = cur.fetchall()
        responseData = []
        for vendedor in data_vendedores:
            responseData.append(
        {
         "Vendedor CIV": vendedor[0],
         "Vendedor Nombre": vendedor[1] + ' '+ vendedor[2],
         "Fecha de nacimiento": vendedor [3],
         "Tipo de vendedor": vendedor[4],
         "Salario": vendedor[5],
         "Direccion": vendedor[6],
         "Numero de contacto": vendedor[7],
         "Porcentaje": vendedor[8],
         "Monto" : vendedor[9],

        }) 
        cur.execute("SELECT * FROM cliente")
        data_cliente = cur.fetchall()
        responseData1 = []
        for cliente in data_cliente:
         responseData1.append({
             "Autentificacion": cliente[0],
             "Nombre": cliente[2] + ' ' + cliente[3],
             "Numero de Telefono": cliente[6]})
        return jsonify ({"Almacenaje Vendedores": responseData, "Clientes": responseData1}),200





    
@app.route('/ventas', methods={'POST','GET'})
def index_ventas():
    if (request.method == 'POST'):
        nueva_venta = request.get_json();
        print(nueva_venta)
        venta_CUV = nueva_venta['venta_CUV']
        venta_codigo = nueva_venta['venta_codigo']
        venta_numerocontrato = nueva_venta['venta_numerocontrato']
        venta_vendedores = nueva_venta['venta_vendedores']
        venta_clientes = nueva_venta['venta_clientes']
        ventas_monto = nueva_venta['venta_monto']
        ventas_fechaventa = nueva_venta['venta_fechaventa']
        venta_producto = nueva_venta['venta_producto']
        venta_marca = nueva_venta['venta_marca']
        venta_monto = nueva_venta['venta_modelo']
        venta_ano = nueva_venta['venta_ano']
        
        conn = mysql.connect()
        cur = conn.cursor()

        cur.execute("INSERT INTO ventas(venta_CUV,venta_codigo,venta_numerocontrato,venta_vendedores,venta_clientes,venta_monto,venta_fechaventa,venta_producto,venta_marca,venta_modelo,venta_ano)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",())
        conn.commit()
        cur.close()
        return jsonify({"Response" : "Venta Agregada con Exito :)"}),201
    else:
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM ventas")
   

        data_ventas = cur.fetchall()
        responseData = []
        for ventas in data_ventas:
         responseData.append(
        {
        "Venta_CUV": ventas[0],
        "Codigo de Ventas": ventas [1] ,
        "Numero de contrato": ventas [2] , 
        "Vendedores ": ventas [3],
        "Clientes": ventas[4],
        "Monto": ventas[5],
        "Fecha de venta": ventas[6],
        "Producto": ventas[7],
        "Tipo Automovil: ": ventas[8] + " " +  (ventas)[9] + " " +   (ventas)[10],
        })
        cur.execute("SELECT * FROM cliente")
        data_cliente = cur.fetchall()
        responseData1 = []
        for cliente in data_cliente:
            responseData1.append({
            "Autentificacion": cliente[0],
             "Nombre": cliente[2] + ' ' + cliente[3],
             "Numero de Telefono": cliente[6]})
        cur.execute("SELECT * FROM vendedor")
        data_vendedores = cur.fetchall()
        responseData2 = []
        for vendedor in data_vendedores:
            responseData2.append({
            "Vendedor CIV": vendedor[0],
            "Nombre Completo": vendedor[1] + " " + vendedor[2],
            "Numero de telefono": vendedor[7],
            "Porcentaje": vendedor[8]
        })
 
    return jsonify ({"Informacion Ventas": responseData, "Clientes": responseData1, "Vendedores": responseData2}),200

@app.route('/cliente/<int:cliente_id>')
def cliente_id(cliente_id):
    conn = mysql.connect()
    cur = conn.cursor()

    cur.execute('SELECT * FROM cliente WHERE cliente_id=%s',(cliente_id))
    data_cliente = cur.fetchone()
    
    if data_cliente == None:
         return jsonify({"response": "No se encontratron Registros con ese ID"}),200
    else:
        return jsonify({"response": {
            "Autentificacion ID cliente": data_cliente[0],
            "Tipo de cedula": data_cliente [1] ,
            "Nombre":  (data_cliente)[2] +" "+ (data_cliente) [3],
            "Calificacion del credito": data_cliente[4],
            "Direccion": data_cliente[5],
            "Telefono": data_cliente[6],
            "Fecha De Nacimiento": data_cliente[7],
        }}),302

@app.route('/vendedor/<int:vendedor_CIV>')
def vendedor_CIV(vendedor_CIV):
    conn = mysql.connect()
    cur = conn.cursor()

    cur.execute('SELECT * FROM vendedor WHERE vendedor_CIV= %s',(vendedor_CIV)) 
    data_vendedor = cur.fetchone()

    if data_vendedor == None:
        return jsonify({"response":"No se encuentran registros con ese ID "+ str (vendedor_CIV) }),200
    else:
        return jsonify({"response":{
         "Vendedor CIV": data_vendedor[0],
         "Vendedor Nombre": data_vendedor[1] + ' '+ data_vendedor[2],
         "Fecha de nacimiento": data_vendedor [3],
         "Tipo de vendedor": data_vendedor[4],
         "Salario": data_vendedor[5],
         "Direccion": data_vendedor[6],
         "Numero de contacto": data_vendedor[7],
         "Porcentaje": data_vendedor[8],
         "Monto" : data_vendedor[9],
         }}),300  

@app.route('/ventas/<int:venta_CUV>')
def venta_CUV(venta_CUV):
    conn = mysql.connect()
    cur = conn.cursor()

    cur.execute('SELECT * FROM ventas WHERE venta_CUV= %s',(venta_CUV)) 
    data_ventas = cur.fetchone()

    if data_ventas == None:
        return jsonify({"response":"No se encuentran registros con ese ID "+str (venta_CUV) }),200
    else:
        return jsonify({"response":{
          "Venta_CUV": data_ventas[0],
          "Codigo de Ventas":data_ventas [1] ,
          "Numero de contrato": data_ventas [2] , 
          "Vendedores ": data_ventas [3],
          "Clientes": data_ventas[4],
          "Monto": data_ventas[5],
          "Fecha de venta": data_ventas[6],
          "Producto": data_ventas[7],
          "Tipo Automovil: ": data_ventas[8] + " " +  (data_ventas)[9] + " " +   (data_ventas)[10],
         }}),300 