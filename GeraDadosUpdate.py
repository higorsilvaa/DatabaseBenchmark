import random

aluno100StringUpdate = open("Aluno100StringUpdate.txt", "w")
aluno1000StringUpdate = open("Aluno1000StringUpdate.txt", "w")
aluno10000StringUpdate = open("Aluno10000StringUpdate.txt", "w")
aluno100000StringUpdate = open("Aluno100000StringUpdate.txt", "w")
aluno1000000StringUpdate = open("Aluno1000000StringUpdate.txt", "w")

aluno100NumberUpdate = open("Aluno100NumberUpdate.txt", "w")
aluno1000NumberUpdate = open("Aluno1000NumberUpdate.txt", "w")
aluno10000NumberUpdate = open("Aluno10000NumberUpdate.txt", "w")
aluno100000NumberUpdate = open("Aluno100000NumberUpdate.txt", "w")
aluno1000000NumberUpdate = open("Aluno1000000NumberUpdate.txt", "w")

for i in range(0, 100):
    aluno100StringUpdate.writelines(f"aluno_{i}_nome Higor{i}\n")
    aluno100StringUpdate.writelines(f"aluno_{i}_sexo m\n")
    aluno100StringUpdate.writelines(f"aluno_{i}_cidade Torres\n")
    aluno100StringUpdate.writelines(f"aluno_{i}_uf RS\n")
    aluno100StringUpdate.writelines(f"aluno_{i}_email higor.aluno@unipampa\n")

for i in range(0, 100):
    num_ale = random.randint(0,9999999999)
    semestre_aleatorio = random.randint(1,8)
    cod_curso = random.randint(1,4)
    aluno100NumberUpdate.writelines(f"aluno_{i}_matricula {num_ale}\n")
    aluno100NumberUpdate.writelines(f"aluno_{i}_semestre {semestre_aleatorio}\n")
    aluno100NumberUpdate.writelines(f"aluno_{i}_nasc 01012000\n")
    aluno100NumberUpdate.writelines(f"aluno_{i}_codCurso {cod_curso}\n")

for i in range(0, 1000):
    aluno1000StringUpdate.writelines(f"aluno_{i}_nome Higor{i}\n")
    aluno1000StringUpdate.writelines(f"aluno_{i}_sexo m\n")
    aluno1000StringUpdate.writelines(f"aluno_{i}_cidade Torres\n")
    aluno1000StringUpdate.writelines(f"aluno_{i}_uf RS\n")
    aluno1000StringUpdate.writelines(f"aluno_{i}_email higor.aluno@unipampa\n")

for i in range(0, 1000):
    num_ale = random.randint(0,9999999999)
    semestre_aleatorio = random.randint(1,8)
    cod_curso = random.randint(1,4)
    aluno1000NumberUpdate.writelines(f"aluno_{i}_matricula {num_ale}\n")
    aluno1000NumberUpdate.writelines(f"aluno_{i}_semestre {semestre_aleatorio}\n")
    aluno1000NumberUpdate.writelines(f"aluno_{i}_nasc 01012000\n")
    aluno1000NumberUpdate.writelines(f"aluno_{i}_codCurso {cod_curso}\n")

for i in range(0, 10000):
    aluno10000StringUpdate.writelines(f"aluno_{i}_nome Higor{i}\n")
    aluno10000StringUpdate.writelines(f"aluno_{i}_sexo m\n")
    aluno10000StringUpdate.writelines(f"aluno_{i}_cidade Torres\n")
    aluno10000StringUpdate.writelines(f"aluno_{i}_uf RS\n")
    aluno10000StringUpdate.writelines(f"aluno_{i}_email higor.aluno@unipampa\n")

for i in range(0, 10000):
    num_ale = random.randint(0,9999999999)
    semestre_aleatorio = random.randint(1,8)
    cod_curso = random.randint(1,4)
    aluno10000NumberUpdate.writelines(f"aluno_{i}_matricula {num_ale}\n")
    aluno10000NumberUpdate.writelines(f"aluno_{i}_semestre {semestre_aleatorio}\n")
    aluno10000NumberUpdate.writelines(f"aluno_{i}_nasc 01012000\n")
    aluno10000NumberUpdate.writelines(f"aluno_{i}_codCurso {cod_curso}\n")

for i in range(0, 100000):
    aluno100000StringUpdate.writelines(f"aluno_{i}_nome Higor{i}\n")
    aluno100000StringUpdate.writelines(f"aluno_{i}_sexo m\n")
    aluno100000StringUpdate.writelines(f"aluno_{i}_cidade Torres\n")
    aluno100000StringUpdate.writelines(f"aluno_{i}_uf RS\n")
    aluno100000StringUpdate.writelines(f"aluno_{i}_email higor.aluno@unipampa\n")

for i in range(0, 100000):
    num_ale = random.randint(0,9999999999)
    semestre_aleatorio = random.randint(1,8)
    cod_curso = random.randint(1,4)
    aluno100000NumberUpdate.writelines(f"aluno_{i}_matricula {num_ale}\n")
    aluno100000NumberUpdate.writelines(f"aluno_{i}_semestre {semestre_aleatorio}\n")
    aluno100000NumberUpdate.writelines(f"aluno_{i}_nasc 01012000\n")
    aluno100000NumberUpdate.writelines(f"aluno_{i}_codCurso {cod_curso}\n")

for i in range(0, 1000000):
    aluno1000000StringUpdate.writelines(f"aluno_{i}_nome Higor{i}\n")
    aluno1000000StringUpdate.writelines(f"aluno_{i}_sexo m\n")
    aluno1000000StringUpdate.writelines(f"aluno_{i}_cidade Torres\n")
    aluno1000000StringUpdate.writelines(f"aluno_{i}_uf RS\n")
    aluno1000000StringUpdate.writelines(f"aluno_{i}_email higor.aluno@unipampa\n")

for i in range(0, 1000000):
    num_ale = random.randint(0,9999999999)
    semestre_aleatorio = random.randint(1,8)
    cod_curso = random.randint(1,4)
    aluno1000000NumberUpdate.writelines(f"aluno_{i}_matricula {num_ale}\n")
    aluno1000000NumberUpdate.writelines(f"aluno_{i}_semestre {semestre_aleatorio}\n")
    aluno1000000NumberUpdate.writelines(f"aluno_{i}_nasc 01012000\n")
    aluno1000000NumberUpdate.writelines(f"aluno_{i}_codCurso {cod_curso}\n")


aluno100StringUpdate.close()
aluno1000StringUpdate.close()
aluno10000StringUpdate.close()
aluno100000StringUpdate.close()
aluno1000000StringUpdate.close()

aluno100NumberUpdate.close()
aluno1000NumberUpdate.close()
aluno10000NumberUpdate.close()
aluno100000NumberUpdate.close()
aluno1000000NumberUpdate.close()