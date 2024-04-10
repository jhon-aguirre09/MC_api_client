from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse

from requests import request

app = FastAPI()

app.title = "App Client"

@app.post('/create', tags=['Create Person'])
def person_creation(
		id: int = Body(0),
		name: str = Body(''),
		identification: int = Body(0),
		email: str = Body(''),
		direction: str = Body(''),
		phone: int = Body('')
	):
	data = {
		'id': id,
		'name': name,
		'identification': identification,
		'email':email,
		'direction': direction,
		'phone': phone
	}
	url = 'http://localhost:8005/create'
	r = request('post', url, json=data)
	if r.status_code == 201:
		return JSONResponse(status_code=201)
	else:
		return JSONResponse(status_code=400)
	
@app.get('/people/{pk}', tags=['Detail Person'])
def get_person(pk: int):
	params = {
		'pk': pk,
	}
	url = 'http://localhost:8005/people/'
	r = request('get', url, params=params)
	return r.json()


@app.get('/people', tags=['List People'])
def get_people():
	url = 'http://localhost:8005/people'
	r = request('get', url)
	return r.json()