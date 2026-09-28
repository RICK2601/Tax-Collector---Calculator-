from flask import Flask, render_template
import tax
  app = Flask(_name_)


  @app.route('/')
  def index():
      return render_template("index.html")

  @app.route('/calculate', methods=['POST'])
  def calculate():
      income = request.form['income']
      deductions = request.form['deductions']
      old_tax, new_tax = tax.compare_and_calculate(int(income), int(deductions))
      if new_tax < old_tax:
          choose = 'New Tax Regime'
          Benefit = old_tax - new_tax
     else:
         choose = 'old Tax Regime'
         Benefit = new_tax - old_tax
     return render_template("index.html", ot = old_tax, nt = new_tax, benefit = benefit, choose = choose)


   if _name_ == '_main_':
      app.run(debug=True, port=8000)
