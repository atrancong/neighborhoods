from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('mapless.html')

@app.route('/leafletQuickStart')
def leaflet():
  return render_template('leafletQuickStart.html')

@app.route('/leafletMaptime')
def leaflet():
  return render_template('leafletMaptime.html')

if __name__ == '__main__':
  app.run(port=33507)
