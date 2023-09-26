from flask import Flask
from config import Config

def init_app():
	app= Flask (__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
	app.config.from_object(Config)

	@app.route('/')
	def hello_world():
		return 'Hola mundo'

	@app.route('/academia/')
	def bienvenido():
		return 'bienvenidos a la Academia'

	@app.route('/about')
	def mensaje():
		return 'Programación'

	@app.route('/perfil/<int:user_id>')
	def perfil(user_id):
		return f'Bienvenido {user_id}!'

	@app.route('/actors/<int:actor_id>', methods = ['GET'])
	def get_actor (actor_id):
		query= "SELECT actor_id, first_name, last_name, last_update FROM sakila.actor;"
		params= actor_id,
		result= DatabaseConnection.fetch_one(query, params)
		if result is not None:
			return {
			"id": result[0],
			"nombre": result[1],
			"apellido": result[2],
			"ultima_actualizacion": result[3]
			}, 200
		return {"msg": "No se encontró el actor"}, 404

	@app.route ('/actors/', methods= ['GET'])
	def get_actors():
		query= "SELECT actor_id, first_name, last_name, last_update FROM sakila.actor;"
		results= DatabaseConnection.fetch_all(query)
		actors=[]
		total= 0
		if result in results:
			actors.append({
				"id": result[0],
				"nombre": result[1],
				"apellido": result[2],
				"ultima_actualizacion": result[3]
			}), 200
		total=len(actors)
		diccionario= {
			"customer": actors,
			"total": total
		}
		return diccionario

	@app.route('/actors', methods= ['POST'])
	def create_actor():
		query= "INSERT INTO sakila.actor first_name, last_name, last_update"
		request.args.get('last_update', '')
		DatabaseConnection.execute_query (query,params)
		return {"msg": "Actor creado con éxito"}, 201
		
	return app
