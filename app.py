from flask import Flask , render_template

app = Flask(__name__)

JOBS = [
  {
    'id' : 1,
    'title' : 'Data Analyst',
    'location': 'India',
    'salary' :'Rs. 10,00,000'
  },
  {
    'id' : 2,
    'title' : 'Data Sceintist',
    'location' : 'USA',
    'salary' : ' $100,000'
  },
  {
    'id' : 3,
    'title' : 'Web Dev',
    'location' : 'UK',
    'salary' : '200,000 euro'
  },
  {
    'id' : 4,
    'title' : 'ML enginner',
    'location' : 'India',
    
  },
  {
    'id' : 5,
    'title' : 'AI enginner',
    'location' : 'India',
    
  },
  {
    'id' : 6,
    'title' : 'AI enginner',
    'location' : 'India',

  }
]
@app.route("/")
def index():
  return render_template("home.html" , jobs = JOBS)
  



app.run(host = '0.0.0.0' , debug = True)

