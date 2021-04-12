#!/usr/bin/env python
from flask import Flask, render_template,request,redirect
import erathosten,os
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('basic.html')
@app.route('/zisti/',methods=['POST'])
def zisti():
    if request.method=='POST':
        form=request.form
        num=form['cislo']
        try:
            num=int(num)
        except ValueError:
            return render_template('zisti.html',chyba='Toto nie je cislo')
        courobit=form['courobit']
        if courobit=='prve':
            return  render_template('zisti.html',title="Prvých {num} prvočísel".format(num=num), vysledok=sformatuj(erathosten.primes(int(num)),num))
        elif courobit =='vsetky':
            return  render_template('zisti.html',title="Všetky prvočísla < {num}".format(num=num), vysledok=sformatuj(erathosten.primesrange(int(num)),num))
  
        else:
            return  render_template('zisti.html',title="Je čislo {num} prvočíslo?".format(num=num), vysledok=sformatuj(erathosten.isprime(int(num)),num))
def sformatuj(vec,cislo):
    if isinstance(vec,bool):
        if vec:
            return 'Ano, číslo {cislo} je prvočíslo.'.format(cislo=cislo)
        else:
            return 'Nie, číslo {cislo} nie je prvočíslo.'.format(cislo=cislo)
    elif isinstance(vec,list):
        return' '.join([str(i) for i in vec])
    else:
        return 'Niekde je chIba'
app.run(debug=True)
