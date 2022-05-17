import requests
from flask import Flask, render_template, request, url_for

app = Flask(__name__)
api_key = "k_7e4awbkm"

def get_by_title(title):
	url = f'https://imdb-api.com/API/Search/{api_key}/{title}'
	r = requests.get(url).json()
	return r

def get_show(title):
	results = get_by_title(title)
	
	results = results['results']

	first_result = results[0]

	print("first result: {}".format(first_result))

	id = first_result['id']

	#print("r: {}".format(r))

	return first_result
	

@app.route('/')
@app.route('/index')
def index_get():
	return render_template('index.html')



@app.route('/', methods=["POST"])
def index_post():
	
	title = request.form.get('title')

	if title:
		message = "Poster for {} goes here".format(title)
		info = get_show(title)
		image = info['image']
		return render_template('index.html', message=message, image=image)
	
	#return render_template('index.html')


if __name__=="__main__":
	app.run()