import streamlit as st
import pulp
import time
import pandas as pd
from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value

# Título general de la aplicación
st.title("Ejercicios de Optimización")

# Menú de selección de tema
tema = st.radio(
    "Seleccionar Tema",
    ("Ejercicio 8.1: Método Branch and Bound",
     "Ejercicio 8.2: Tiempo de Cálculo para Problema LP",
     "Ejercicio 8.3: Minimización usando Cortes de Gomory",
     "Ejercicio 8.4: Maximización usando Cortes de Gomory",
     "Ejercicio 8.5: Maximización de NPV para Proyectos de R&D")
)

if tema == "Ejercicio 8.1: Método Branch and Bound":
    st.subheader("Ejercicio 8.1: Método Branch and Bound")
    prob = pulp.LpProblem("Maximizar_P", pulp.LpMaximize)
    x1 = pulp.LpVariable("x1", lowBound=0, cat="Integer")
    x2 = pulp.LpVariable("x2", lowBound=0, cat="Integer")
    x3 = pulp.LpVariable("x3", lowBound=0, cat="Integer")
    prob += 4 * x1 + 3 * x2 + 3 * x3, "Función Objetivo"
    prob += 4 * x1 + 2 * x2 + x3 <= 10
    prob += 3 * x1 + 4 * x2 + 2 * x3 <= 14
    prob += 2 * x1 + x2 + 3 * x3 <= 7
    prob.solve()
    st.write(f"Estado: {pulp.LpStatus[prob.status]}")
    st.write(f"Valor óptimo de la función objetivo: {pulp.value(prob.objective)}")
    for variable in prob.variables():
        st.write(f"{variable.name} = {variable.varValue}")

elif tema == "Ejercicio 8.2: Tiempo de Cálculo para Problema LP":
    st.subheader("Ejercicio 8.2: Tiempo de Cálculo para Problema LP")
    
    # Problema LP Continuo
    prob_lp = pulp.LpProblem("Maximizar_P_LP", pulp.LpMaximize)
    x1 = pulp.LpVariable("x1", lowBound=0)
    x2 = pulp.LpVariable("x2", lowBound=0)
    x3 = pulp.LpVariable("x3", lowBound=0)
    prob_lp += 4 * x1 + 3 * x2 + 3 * x3, "Función Objetivo"
    prob_lp += 4 * x1 + 2 * x2 + x3 <= 10
    prob_lp += 3 * x1 + 4 * x2 + 2 * x3 <= 14
    prob_lp += 2 * x1 + x2 + 3 * x3 <= 7
    start_time = time.time()
    prob_lp.solve()
    tiempo_calculo_lp = time.time() - start_time
    st.write(f"Tiempo de cálculo LP continuo: {tiempo_calculo_lp:.4f} segundos")
    st.write(f"Estado LP continuo: {pulp.LpStatus[prob_lp.status]}")
    st.write(f"Valor óptimo LP continuo: {pulp.value(prob_lp.objective)}")
    for variable in prob_lp.variables():
        st.write(f"{variable.name} = {variable.varValue}")

    # Problema LP con Enteros
    prob_entero = pulp.LpProblem("Maximizar_P", pulp.LpMaximize)
    x1 = pulp.LpVariable("x1", lowBound=0, cat="Integer")
    x2 = pulp.LpVariable("x2", lowBound=0, cat="Integer")
    x3 = pulp.LpVariable("x3", lowBound=0, cat="Integer")
    prob_entero += 4 * x1 + 3 * x2 + 3 * x3, "Función Objetivo"
    prob_entero += 4 * x1 + 2 * x2 + x3 <= 10
    prob_entero += 3 * x1 + 4 * x2 + 2 * x3 <= 14
    prob_entero += 2 * x1 + x2 + 3 * x3 <= 7
    start_time = time.time()
    prob_entero.solve()
    tiempo_calculo_entero = time.time() - start_time
    st.write(f"Tiempo de cálculo LP con enteros: {tiempo_calculo_entero:.4f} segundos")
    st.write(f"Estado LP con enteros: {pulp.LpStatus[prob_entero.status]}")
    st.write(f"Valor óptimo LP con enteros: {pulp.value(prob_entero.objective)}")
    for variable in prob_entero.variables():
        st.write(f"{variable.name} = {variable.varValue}")

elif tema == "Ejercicio 8.3: Minimización usando Cortes de Gomory":
    st.subheader("Ejercicio 8.3: Minimización usando Cortes de Gomory")
    prob_gomory = pulp.LpProblem("Minimizar_C", pulp.LpMinimize)
    x = pulp.LpVariable("x", lowBound=0, cat="Integer")
    y = pulp.LpVariable("y", lowBound=0, cat="Integer")
    prob_gomory += x - y, "Función Objetivo"
    prob_gomory += 3 * x + 4 * y <= 6
    prob_gomory += x - y <= 1
    prob_gomory.solve()
    st.write(f"Estado: {pulp.LpStatus[prob_gomory.status]}")
    st.write(f"Valor óptimo de la función objetivo: {pulp.value(prob_gomory.objective)}")
    for variable in prob_gomory.variables():
        st.write(f"{variable.name} = {variable.varValue}")

elif tema == "Ejercicio 8.4: Maximización usando Cortes de Gomory":
    st.subheader("Ejercicio 8.4: Maximización usando Cortes de Gomory")
    prob_gomory = pulp.LpProblem("Maximizar_P", pulp.LpMaximize)
    x1 = pulp.LpVariable("x1", lowBound=0, cat="Integer")
    x2 = pulp.LpVariable("x2", lowBound=0, cat="Integer")
    x3 = pulp.LpVariable("x3", lowBound=0, cat="Integer")
    prob_gomory += 4 * x1 + 3 * x2 + 3 * x3, "Función Objetivo"
    prob_gomory += 4 * x1 + 2 * x2 + x3 <= 10
    prob_gomory += 3 * x1 + 4 * x2 + 2 * x3 <= 14
    prob_gomory += 2 * x1 + x2 + 3 * x3 <= 7
    prob_gomory.solve()
    st.write(f"Estado: {pulp.LpStatus[prob_gomory.status]}")
    st.write(f"Valor óptimo de la función objetivo: {pulp.value(prob_gomory.objective)}")
    for variable in prob_gomory.variables():
        st.write(f"{variable.name} = {variable.varValue}")

elif tema == "Ejercicio 8.5: Maximización de NPV para Proyectos de R&D":
    st.subheader("Ejercicio 8.5: Maximización de NPV para Proyectos de R&D")
    npv = [141, 187, 163, 155, 189, 127]
    costs = [
        [75, 90, 80, 20, 100, 50],
        [25, 50, 60, 10, 32, 20],
        [20, 25, 25, 10, 10, 10],
        [15, 15, 15, 8, 10, 10],
        [10, 10, 15, 5, 8, 5]
    ]
    budgets = [250, 75, 50, 50, 50]
    model = LpProblem("Maximizar_NPV", LpMaximize)
    x = [LpVariable(f"x{i+1}", cat="Binary") for i in range(6)]
    model += lpSum(npv[i] * x[i] for i in range(6)), "NPV_Total"
    for year in range(5):
        model += lpSum(costs[year][i] * x[i] for i in range(6)) <= budgets[year]
    model.solve()
    st.write(f"Estado del problema: {'Óptimo' if model.status == 1 else 'No Óptimo'}")
    st.write(f"Valor óptimo de NPV: {value(model.objective)}")
    seleccionados = [f"Proyecto {i+1}" for i in range(6) if x[i].value() == 1]
    no_seleccionados = [f"Proyecto {i+1}" for i in range(6) if x[i].value() == 0]
    st.write("Proyectos Seleccionados:", ", ".join(seleccionados))
    st.write("Proyectos No Seleccionados:", ", ".join(no_seleccionados))
