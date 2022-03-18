from flask import Flask, render_template
app = Flask('app')

todos = [
  {'name': 'Estudar Python', 
  'complete': False
  },
  {
    'name': 'Estudar Javascript',
    'complete': False
  },
  {
    'name': 'Fazer exercicio 1',
    'complete': True
  }
  
]
@app.route('/')
def index():
  return render_template('index.html',
                        todos = todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)