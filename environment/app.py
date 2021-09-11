

from flask import Flask, app, render_template,request
from flask.helpers import url_for
from werkzeug.utils import redirect
from joblib import load
import numpy as np
import random
app=Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    if request.method=='POST':
      Crime=request.form['crime']
      Resident=request.form['resident land proportion']
      Indus=request.form['industrilization']
      River=request.form['River']
      Pollution=request.form['pollution']
      Rooms=request.form['rooms']
      Age=request.form['Age']
      Empcenters=request.form['distance to employment centres']
      Highway=request.form['no. of highways']
      Tax=request.form['tax']
      PTratio=request.form['teacherstudent']
      B=50
      Lstat=request.form['lower status people']
      model=load('Dragon.joblib')
      input=np.array([[Crime , Resident,   Indus,  River,  Pollution,  Rooms,  Age,  Empcenters,   Highway,  Tax,  PTratio, B, Lstat]])
      # print(request.form['b'])
      # A=request.form['River']
      Answer=model.predict(input)
      # ABC=Answer.astype(np.float32)
      # print(str(ABC*24.2))
      # print(Answer[0])
      FinalAnswer=Answer*70000*random.randint(1,7)
      return redirect(url_for("result",res=format(FinalAnswer[0],'.2f')))
      
    return render_template('index.html')

@app.route('/<res>')
def result(res):
  # return f"<h1>{res}</h1>"
  return render_template('result.html',result=res)

if __name__=="__main__":
    app.run(debug=True, port=8000)
