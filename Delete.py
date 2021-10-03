import redis
import time

my_server = redis.Redis("127.0.0.1")

def deleta(arq):
    tempo = 0
    for i in arq:
        linha = i.split("\n")[0]
        chave = linha.split(" ")[0]
        
        #print(chave)
        ini = time.time()
        my_server.delete(chave)
        fim = time.time()
        tempo += fim - ini
    return tempo

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

t1_del = deleta(aluno100StringUpdate)
t2_del = deleta(aluno100NumberUpdate)

t3_del = deleta(aluno1000StringUpdate)
t4_del = deleta(aluno1000NumberUpdate)

t5_del = deleta(aluno10000StringUpdate)
t6_del = deleta(aluno10000NumberUpdate)

t7_del = deleta(aluno100000StringUpdate)
t8_del = deleta(aluno100000NumberUpdate)

t9_del = deleta(aluno1000000StringUpdate)
t10_del = deleta(aluno1000000NumberUpdate)

t1_del = t1_del/100
t2_del = t2_del/100
t3_del = t3_del/1000
t4_del = t4_del/1000
t5_del = t5_del/10000
t6_del = t6_del/10000
t7_del = t7_del/100000
t8_del = t8_del/100000
t9_del = t9_del/1000000
t10_del = t10_del/1000000

print(f"Tempo 100 Delete (String): {t1_del:05f}")
print(f"Tempo 100 Delete (Number): {t2_del:05f}")
print(f"Tempo 1000 Delete (String): {t3_del:05f}")
print(f"Tempo 1000 Delete (Number): {t4_del:05f}")
print(f"Tempo 10000 Delete (String): {t5_del:05f}")
print(f"Tempo 10000 Delete (Number): {t6_del:05f}")
print(f"Tempo 100000 Delete (String): {t7_del:05f}")
print(f"Tempo 100000 Delete (Number): {t8_del:05f}")
print(f"Tempo 1000000 Delete (String): {t9_del:05f}")
print(f"Tempo 1000000 Delete (Number): {t10_del:05f}")


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