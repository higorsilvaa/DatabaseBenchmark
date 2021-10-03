from matplotlib.pyplot import *
from mysql.connector import connect
import time
import numpy as np
from statistics import median

HOST='localhost'
DATABASE='finalwork'
USER='root'
PASSWORD='1979'

def show_tables(cursor):
	command = 'SHOW TABLES FROM finalwork ;'
	cursor.execute(command)
	resultado = cursor.fetchall() # Recupera o resultado:
	
	for i in resultado:
		table_name = i[0]
		print(table_name)
		
		command = 'DESC %s ;' % table_name
		cursor.execute(command)
		columns = cursor.fetchall()
		
		for j in columns:
			column_name = j[0]
			print('\t', column_name)

def reseta_tables(cursor):
	commands = [
		'DELETE FROM Aluno ;',
		'DELETE FROM Curso ;',
		'DELETE FROM Disciplina ;',
		'DELETE FROM CursoDisc ;'
	]
	
	for i in commands:
		cursor.execute(i)

def run_insert_string(cursor, nreg):
	reseta_tables(cursor)
	command = "INSERT INTO Curso VALUE (1, 'Ciência da Computação', 'Letícia Gindri', 'Alegrete') ;"
	cursor.execute(command)
	
	time_insert = []
	for i in range(nreg):
		command = "INSERT INTO Aluno VALUE (%i, 'Jose', %i, '2021-09-25', 'M', 'Torres', 'RS', 'jose@gmail.com', 1);" % (i,i)
		y = time.time()
		cursor.execute(command)
		time_insert.append(time.time()-y)
	
	return time_insert

def run_update_string(cursor, nreg):
	time_update = []
	for i in range(nreg):
		command = "UPDATE Aluno SET nome = 'Rafael' WHERE matricula = %i ;" % (i)
		y = time.time()
		cursor.execute(command)
		time_update.append(time.time()-y)
	
	return time_update

def run_delete_string(cursor, nreg):
	time_delete = []
	for i in range(nreg):
		command = "DELETE FROM Aluno WHERE matricula = %i ;" % (i)
		y = time.time()
		cursor.execute(command)
		time_delete.append(time.time()-y)
	
	return time_delete

def run_insert_number(cursor, nreg):
	reseta_tables(cursor)
	
	time_insert = []
	for i in range(nreg):
		command = "INSERT INTO CursoDisc VALUE (%i, %i, %i);" % (i,i,i)
		y = time.time()
		cursor.execute(command)
		time_insert.append(time.time()-y)
	
	return time_insert

def run_update_number(cursor, nreg):
	time_update = []
	for i in range(nreg):
		command = "UPDATE CursoDisc SET semestre_ofertada = 1 WHERE cod_disc = %i ;" % (i)
		y = time.time()
		cursor.execute(command)
		time_update.append(time.time()-y)
	
	return time_update

def run_delete_number(cursor, nreg):
	time_delete = []
	for i in range(nreg):
		command = "DELETE FROM CursoDisc WHERE cod_disc = %i ;" % (i)
		y = time.time()
		cursor.execute(command)
		time_delete.append(time.time()-y)
	
	return time_delete

def gera_grafico(x, y1, y2, titleGraf='Sem Título', t='.', col1='blue', col2='red', label1='String', label2='Number'):
	label1 = label1 + ' (%f' % (np.mean(y1)) + ')'
	label2 = label2 + ' (%f' % (np.mean(y2)) + ')'
	plot(x, y1, t, color=col1, label=label1)
	plot(x, y2, t, color=col2, label=label2)
	title(titleGraf)
	legend()
	xlabel('número da operação')
	ylabel('tempo de processamento(s)')
	
	#plot(x, np.ones(len(x))*np.mean(y1), color=color1)
	#text(x[-1]+.1,np.mean(y1),'%.5f'%(np.mean(y1)))
	
	#plot(x, np.ones(len(x))*np.mean(y2), color=color2)
	#text(x[-1]+.1,np.mean(y2),'%.5f'%(np.mean(y2)))
	
	figure = gcf()
	figure.set_size_inches(8, 6)
	
	savefig('%s.png' % titleGraf, format='png', dpi=500)
	clf()

if __name__ == '__main__':
	connection = connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)

	if connection.is_connected():
		cursor = connection.cursor()

		time_average = []
		
		#==============================================
		#==============================================
		N = 100
		
		auxS = run_insert_string(cursor, N)
		time_average.append(sum(auxS)/float(len(auxS)))
		
		auxN = run_insert_number(cursor, N)
		time_average.append(sum(auxN)/float(len(auxN)))
		
		gera_grafico(range(1,N+1), auxS, auxN, titleGraf='Inserção de %i pontos'%(N))
		#==============================================
		N = 1000
		
		auxS = run_insert_string(cursor, N)
		time_average.append(sum(auxS)/float(len(auxS)))
		
		auxN = run_insert_number(cursor, N)
		time_average.append(sum(auxN)/float(len(auxN)))
		
		gera_grafico(range(1,N+1), auxS, auxN, titleGraf='Inserção de %i pontos'%(N))
		#==============================================
		N = 10000
		
		auxS = run_insert_string(cursor, N)
		time_average.append(sum(auxS)/float(len(auxS)))
		
		auxN = run_insert_number(cursor, N)
		time_average.append(sum(auxN)/float(len(auxN)))
		
		gera_grafico(range(1,N+1), auxS, auxN, titleGraf='Inserção de %i pontos'%(N))
		#==============================================
		N = 100000
		
		auxS = run_insert_string(cursor, N)
		time_average.append(sum(auxS)/float(len(auxS)))
		
		auxN = run_insert_number(cursor, N)
		time_average.append(sum(auxN)/float(len(auxN)))
		
		gera_grafico(range(1,N+1), auxS, auxN, titleGraf='Inserção de %i pontos'%(N))
		#==============================================		
		N = 1000000
		
		auxS = run_insert_string(cursor, N)
		time_average.append(sum(auxS)/float(len(auxS)))
		
		auxN = run_insert_number(cursor, N)
		time_average.append(sum(auxN)/float(len(auxN)))
		
		gera_grafico(range(1,N+1), auxS, auxN, titleGraf='Inserção de %i pontos'%(N))
		#==============================================
		#==============================================
		N = 100
		
		auxS = run_update_string(cursor, N)
		time_average.append(sum(auxS)/float(len(auxS)))
		
		auxN = run_update_number(cursor, N)
		time_average.append(sum(auxN)/float(len(auxN)))
		
		gera_grafico(range(1,N+1), auxS, auxN, titleGraf='Atualização de %i pontos'%(N))
		#==============================================
		N = 1000
		
		auxS = run_update_string(cursor, N)
		time_average.append(sum(auxS)/float(len(auxS)))
		
		auxN = run_update_number(cursor, N)
		time_average.append(sum(auxN)/float(len(auxN)))
		
		gera_grafico(range(1,N+1), auxS, auxN, titleGraf='Atualização de %i pontos'%(N))
		#==============================================
		N = 10000
		
		auxS = run_update_string(cursor, N)
		time_average.append(sum(auxS)/float(len(auxS)))
		
		auxN = run_update_number(cursor, N)
		time_average.append(sum(auxN)/float(len(auxN)))
		
		gera_grafico(range(1,N+1), auxS, auxN, titleGraf='Atualização de %i pontos'%(N))
		#==============================================
		N = 100000
		
		auxS = run_update_string(cursor, N)
		time_average.append(sum(auxS)/float(len(auxS)))
		
		auxN = run_update_number(cursor, N)
		time_average.append(sum(auxN)/float(len(auxN)))
		
		gera_grafico(range(1,N+1), auxS, auxN, titleGraf='Atualização de %i pontos'%(N))
		#==============================================
		N = 1000000
		
		auxS = run_update_string(cursor, N)
		time_average.append(sum(auxS)/float(len(auxS)))
		
		auxN = run_update_number(cursor, N)
		time_average.append(sum(auxN)/float(len(auxN)))
		
		gera_grafico(range(1,N+1), auxS, auxN, titleGraf='Atualização de %i pontos'%(N))
		#==============================================
		#==============================================
		N = 100
		
		auxS = run_delete_string(cursor, N)
		time_average.append(sum(auxS)/float(len(auxS)))
		
		auxN = run_delete_number(cursor, N)
		time_average.append(sum(auxN)/float(len(auxN)))
		
		gera_grafico(range(1,N+1), auxS, auxN, titleGraf='Deleção de %i pontos'%(N))
		#==============================================
		N = 1000
		
		auxS = run_delete_string(cursor, N)
		time_average.append(sum(auxS)/float(len(auxS)))
		
		auxN = run_delete_number(cursor, N)
		time_average.append(sum(auxN)/float(len(auxN)))
		
		gera_grafico(range(1,N+1), auxS, auxN, titleGraf='Deleção de %i pontos'%(N))
		#==============================================
		N = 10000
		
		auxS = run_delete_string(cursor, N)
		time_average.append(sum(auxS)/float(len(auxS)))
		
		auxN = run_delete_number(cursor, N)
		time_average.append(sum(auxN)/float(len(auxN)))
		
		gera_grafico(range(1,N+1), auxS, auxN, titleGraf='Deleção de %i pontos'%(N))
		#==============================================
		N = 100000
		
		auxS = run_delete_string(cursor, N)
		time_average.append(sum(auxS)/float(len(auxS)))
		
		auxN = run_delete_number(cursor, N)
		time_average.append(sum(auxN)/float(len(auxN)))
		
		gera_grafico(range(1,N+1), auxS, auxN, titleGraf='Deleção de %i pontos'%(N))
		#==============================================
		N = 1000000
		
		auxS = run_delete_string(cursor, N)
		time_average.append(sum(auxS)/float(len(auxS)))
		
		auxN = run_delete_number(cursor, N)
		time_average.append(sum(auxN)/float(len(auxN)))
		
		gera_grafico(range(1,N+1), auxS, auxN, titleGraf='Deleção de %i pontos'%(N))
		#==============================================
		#==============================================
		
		for i in range(len(time_average)):
			if i % 2 == 0 and i != 0:
				print()
			if i % 5 == 0 and i != 0:
				print()
			print(time_average[i], end=' ')
		print()
		
		connection.commit()
		cursor.close()
		connection.close()
	else:
		print("Something is wrong!")

	#for i in cursor.description: print(i[0])
