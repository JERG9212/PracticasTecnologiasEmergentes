# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 18:08:10 2020
@author: JERG
""" 
from experta import Rule, Fact, KnowledgeEngine, OR, AND
from random import choice
class Cajero(KnowledgeEngine):
    @Rule( AND(AND(AND(OR(Fact(tarjeta='funcional'), Fact(cuentaBancaria='si')),Fact(nip='aceptado')), Fact(saldo='suficiente')),Fact(saldo_cajero='suficiente')) )
    def retiroExitoso(self):
        print("Retiro exitoso")  
    @Rule( OR(OR(OR(AND(Fact(tarjeta='no_funcional'), Fact(cuentaBancaria='no')),Fact(nip='no_aceptado')),Fact(saldo='insuficiente')), Fact(saldo_cajero='insuficiente')) )
    def retiroNoExitoso(self):
        print("Retiro NO exitoso")
        
engine = Cajero()
engine.reset()
engine.declare(Fact(tarjeta = choice(['funcional','no_funcional'])))
engine.declare(Fact(cuentaBancaria = choice(['si','no'])))
engine.declare(Fact(nip = choice(['acep tado','no_aceptado'])))
engine.declare(Fact(saldo = choice(['suficiente','insuficiente'])))
engine.declare(Fact(saldo_cajero = choice(['suficiente','insuficiente'])))
engine.run()