listaRes=[]
def ulam(n):
	if n==1:
		print(n)
		listaRes.append(n)
		return 1
	elif n%2==0:
		print(n/2)
		listaRes.append(n/2)
		ulam(n/2)
	else:
		print(n*3+1)
		listaRes.append(n*3+1)
		ulam(n*3+1)
if __name__ == '__main__':
	fin=open("arch.txt","r")
	n=int(fin.read())
	ulam(n)
	print(listaRes)
	fout=open("resTarea.txt","w")
	for num in listaRes:
		fout.write(str(num)+"\n")
	fin.close()
	fout.close()






