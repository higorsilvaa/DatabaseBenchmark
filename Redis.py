
import redis
import time

my_server = redis.Redis("127.0.0.1")

def insereString(arq):
    tempo = 0
    for i in arq:
        linha = i.split("\n")[0]
        chave = linha.split(" ")[0]
        valor = linha.split(" ")[1]

        ini = time.time()
        my_server.set(chave, valor)
        fim = time.time()
        tempo += fim - ini
    return tempo

def insereNumber(arq):
    tempo = 0
    for i in arq:
        linha = i.split("\n")[0]
        chave = linha.split(" ")[0]
        valor = linha.split(" ")[1]

        ini = time.time()
        my_server.set(chave, valor)
        fim = time.time()
        tempo += fim - ini
    return tempo

aluno100String = open("Aluno100String.txt", "r")
aluno1000String = open("Aluno1000String.txt", "r")
aluno10000String = open("Aluno10000String.txt", "r")
aluno100000String = open("Aluno10000String.txt", "r")
aluno1000000String = open("Aluno10000String.txt", "r")

aluno100Number = open("Aluno100Number.txt", "r")
aluno1000Number = open("Aluno1000Number.txt", "r")
aluno10000Number = open("Aluno10000Number.txt", "r")
aluno100000Number = open("Aluno10000Number.txt", "r")
aluno1000000Number = open("Aluno10000Number.txt", "r")

aluno100StringUpdate = open("Aluno100StringUpdate.txt", "r")
aluno1000StringUpdate = open("Aluno1000StringUpdate.txt", "r")
aluno10000StringUpdate = open("Aluno10000StringUpdate.txt", "r")
aluno100000StringUpdate = open("Aluno100000StringUpdate.txt", "r")
aluno1000000StringUpdate = open("Aluno1000000StringUpdate.txt", "r")

aluno100NumberUpdate = open("Aluno100NumberUpdate.txt", "r")
aluno1000NumberUpdate = open("Aluno1000NumberUpdate.txt", "r")
aluno10000NumberUpdate = open("Aluno10000NumberUpdate.txt", "r")
aluno100000NumberUpdate = open("Aluno100000NumberUpdate.txt", "r")
aluno1000000NumberUpdate = open("Aluno1000000NumberUpdate.txt", "r")

curso = open("Curso.txt", "r")
cursoDisc = open("CursoDisciplina.txt", "r")
disciplina = open("Disciplina.txt", "r")


t1 = insereString(aluno100String)
t2 = insereNumber(aluno100Number)

t3 = insereString(aluno1000String)
t4 = insereNumber(aluno1000Number)

t5 = insereString(aluno10000String)
t6 = insereNumber(aluno10000Number)

t7 = insereString(aluno100000String)
t8 = insereNumber(aluno100000Number)

t9 = insereString(aluno1000000String)
t10 = insereNumber(aluno1000000Number)

t1 = t1/100
t2 = t2/100
t3 = t3/1000
t4 = t4/1000
t5 = t5/10000
t6 = t6/10000
t7 = t7/100000
t8 = t8/100000
t9 = t9/1000000
t10 = t10/1000000

print(f"Tempo 100 Inserções (String): {t1:05f}")
print(f"Tempo 100 Inserções (Number): {t2:05f}")
print(f"Tempo 1000 Inserções (String): {t3:05f}")
print(f"Tempo 1000 Inserções (Number): {t4:05f}")
print(f"Tempo 10000 Inserções (String): {t5:05f}")
print(f"Tempo 10000 Inserções (Number): {t6:05f}")
print(f"Tempo 100000 Inserções (String): {t7:05f}")
print(f"Tempo 100000 Inserções (Number): {t8:05f}")
print(f"Tempo 1000000 Inserções (String): {t9:05f}")
print(f"Tempo 1000000 Inserções (Number): {t10:05f}")

t1_update = insereString(aluno100StringUpdate)
t2_update = insereNumber(aluno100NumberUpdate)

t3_update = insereString(aluno1000StringUpdate)
t4_update = insereNumber(aluno1000NumberUpdate)

t5_update = insereString(aluno10000StringUpdate)
t6_update = insereNumber(aluno10000NumberUpdate)

t7_update = insereString(aluno100000StringUpdate)
t8_update = insereNumber(aluno100000NumberUpdate)

t9_update = insereString(aluno1000000StringUpdate)
t10_update = insereNumber(aluno1000000NumberUpdate)

t1_update = t1_update/100
t2_update = t2_update/100
t3_update = t3_update/1000
t4_update = t4_update/1000
t5_update = t5_update/10000
t6_update = t6_update/10000
t7_update = t7_update/100000
t8_update = t8_update/100000
t9_update = t9_update/1000000
t10_update = t10_update/1000000

print(f"Tempo 100 Update (String): {t1_update:05f}")
print(f"Tempo 100 Update (Number): {t2_update:05f}")
print(f"Tempo 1000 Update (String): {t3_update:05f}")
print(f"Tempo 1000 Update (Number): {t4_update:05f}")
print(f"Tempo 10000 Update (String): {t5_update:05f}")
print(f"Tempo 10000 Update (Number): {t6_update:05f}")
print(f"Tempo 100000 Update (String): {t7_update:05f}")
print(f"Tempo 100000 Update (Number): {t8_update:05f}")
print(f"Tempo 1000000 Update (String): {t9_update:05f}")
print(f"Tempo 1000000 Update (Number): {t10_update:05f}")

insereString(cursoDisc)
insereString(disciplina)
insereString(curso)

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

curso.close()
cursoDisc.close()
disciplina.close() 
