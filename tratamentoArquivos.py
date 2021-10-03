import random

aluno100String = open("Aluno100String.txt", "w")
aluno1000String = open("Aluno1000String.txt", "w")
aluno10000String = open("Aluno10000String.txt", "w")
aluno100000String = open("Aluno100000String.txt", "w")
aluno1000000String = open("Aluno1000000String.txt", "w")

aluno100Number = open("Aluno100Number.txt", "w")
aluno1000Number = open("Aluno1000Number.txt", "w")
aluno10000Number = open("Aluno10000Number.txt", "w")
aluno100000Number = open("Aluno100000Number.txt", "w")
aluno1000000Number = open("Aluno1000000Number.txt", "w")

for i in range(0, 100):
    aluno100String.writelines(f"aluno_{i}_nome Laura{i}\n")
    aluno100String.writelines(f"aluno_{i}_sexo f\n")
    aluno100String.writelines(f"aluno_{i}_cidade Ijui\n")
    aluno100String.writelines(f"aluno_{i}_uf RS\n")
    aluno100String.writelines(f"aluno_{i}_email aluno@unipampa\n")

for i in range(0, 100):
    num_ale = random.randint(0,9999999999)
    semestre_aleatorio = random.randint(1,8)
    cod_curso = random.randint(1,4)
    aluno100Number.writelines(f"aluno_{i}_matricula {num_ale}\n")
    aluno100Number.writelines(f"aluno_{i}_semestre {semestre_aleatorio}\n")
    aluno100Number.writelines(f"aluno_{i}_nasc 18042000\n")
    aluno100Number.writelines(f"aluno_{i}_codCurso {cod_curso}\n")

for i in range(0, 1000):
    aluno1000String.writelines(f"aluno_{i}_nome Laura{i}\n")
    aluno1000String.writelines(f"aluno_{i}_sexo f\n")
    aluno1000String.writelines(f"aluno_{i}_cidade Ijui\n")
    aluno1000String.writelines(f"aluno_{i}_uf RS\n")
    aluno1000String.writelines(f"aluno_{i}_email aluno@unipampa\n")

for i in range(0, 1000):
    num_ale = random.randint(0,9999999999)
    semestre_aleatorio = random.randint(1,8)
    cod_curso = random.randint(1,4)
    aluno1000Number.writelines(f"aluno_{i}_matricula {num_ale}\n")
    aluno1000Number.writelines(f"aluno_{i}_semestre {semestre_aleatorio}\n")
    aluno1000Number.writelines(f"aluno_{i}_nasc 18042000\n")
    aluno1000Number.writelines(f"aluno_{i}_codCurso {cod_curso}\n")

for i in range(0, 10000):
    aluno10000String.writelines(f"aluno_{i}_nome Laura{i}\n")
    aluno10000String.writelines(f"aluno_{i}_sexo f\n")
    aluno10000String.writelines(f"aluno_{i}_cidade Ijui\n")
    aluno10000String.writelines(f"aluno_{i}_uf RS\n")
    aluno10000String.writelines(f"aluno_{i}_email aluno@unipampa\n")

for i in range(0, 10000):
    num_ale = random.randint(0,9999999999)
    semestre_aleatorio = random.randint(1,8)
    cod_curso = random.randint(1,4)
    aluno10000Number.writelines(f"aluno_{i}_matricula {num_ale}\n")
    aluno10000Number.writelines(f"aluno_{i}_semestre {semestre_aleatorio}\n")
    aluno10000Number.writelines(f"aluno_{i}_nasc 18042000\n")
    aluno10000Number.writelines(f"aluno_{i}_codCurso {cod_curso}\n")

for i in range(0, 100000):
    aluno100000String.writelines(f"aluno_{i}_nome Laura{i}\n")
    aluno100000String.writelines(f"aluno_{i}_sexo f\n")
    aluno100000String.writelines(f"aluno_{i}_cidade Ijui\n")
    aluno100000String.writelines(f"aluno_{i}_uf RS\n")
    aluno100000String.writelines(f"aluno_{i}_email aluno@unipampa\n")

for i in range(0, 100000):
    num_ale = random.randint(0,9999999999)
    semestre_aleatorio = random.randint(1,8)
    cod_curso = random.randint(1,4)
    aluno100000Number.writelines(f"aluno_{i}_matricula {num_ale}\n")
    aluno100000Number.writelines(f"aluno_{i}_semestre {semestre_aleatorio}\n")
    aluno100000Number.writelines(f"aluno_{i}_nasc 18042000\n")
    aluno100000Number.writelines(f"aluno_{i}_codCurso {cod_curso}\n")

for i in range(0, 1000000):
    aluno1000000String.writelines(f"aluno_{i}_nome Laura{i}\n")
    aluno1000000String.writelines(f"aluno_{i}_sexo f\n")
    aluno1000000String.writelines(f"aluno_{i}_cidade Ijui\n")
    aluno1000000String.writelines(f"aluno_{i}_uf RS\n")
    aluno1000000String.writelines(f"aluno_{i}_email aluno@unipampa\n")

for i in range(0, 1000000):
    num_ale = random.randint(0,9999999999)
    semestre_aleatorio = random.randint(1,8)
    cod_curso = random.randint(1,4)
    aluno1000000Number.writelines(f"aluno_{i}_matricula {num_ale}\n")
    aluno1000000Number.writelines(f"aluno_{i}_semestre {semestre_aleatorio}\n")
    aluno1000000Number.writelines(f"aluno_{i}_nasc 18042000\n")
    aluno1000000Number.writelines(f"aluno_{i}_codCurso {cod_curso}\n")


aluno100String.close()
aluno1000String.close()
aluno10000String.close()
aluno100000String.close()
aluno1000000String.close()

aluno100Number.close()
aluno1000Number.close()
aluno10000Number.close()
aluno100000Number.close()
aluno1000000Number.close()