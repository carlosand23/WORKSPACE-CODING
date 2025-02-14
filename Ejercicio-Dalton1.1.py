Curso_de_Dalton = 1.5
Curso_minimo = 2.5
Curso_promedio = 4
Curso_lento = 7

Diferencia_curso_minimo = f"El curso de Dalto es un {100 - Curso_de_Dalton / Curso_minimo *100} % mas rapido" 
print(Diferencia_curso_minimo)
Diferencia_curso_promedio = f"El curso de Dalto es un {100 - Curso_de_Dalton / Curso_promedio *100}% mas rapido"
print(Diferencia_curso_promedio)
Diferencia_curso_lento = f"El curso de Dalto es un {round(100 - (Curso_de_Dalton / Curso_lento *100),2)}% mas rapido"
print(Diferencia_curso_lento)