import os
import re
path = 'C:\\Users\\VE522FZ\\OneDrive - EY\\Documents\\Concilicaciones Bancarias\\TALISMAN SA\\BBVA\\GS\\2101016022\\EXTRACTO\\TXT\\'
lstFiles = []
lista = []
count_lineas = 0
words = []
datos =[]
c = 0
Cod_Cliente = ""
Categoria = ""
Moneda = ""
Nro_Operacion = ""
i = 0
dris_ = []
Linea = ""
regex=re.compile(r"[0-5][0-9]:[0-5][0-9]:[0-5][0-9]")
#Lista con todos los ficheros del directorio:
lstdirs2=[]
lstDir = os.listdir(path)


for dirs in lstDir:
    (nombreFichero, extension) = os.path.splitext(dirs)
    if(extension == ".txt"):
        dris_.append(path+dirs)


Path = "C:\\Users\\VE522FZ\\OneDrive - EY\\Documents\\Concilicaciones Bancarias\\TALISMAN SA\\BBVA\\GS\\2101016022\\EXTRACTO\\CONSOLIDADO\\Consolidado_{}_BBVA.txt".format("AJ Vierci")
docu = open(Path,"w")            
x = 1
cabecera = ['fecha conf.', 'fecha tran.', 'Numero de documento','Descripcion de la transaccion','importe debito', 'importe credito', 'Saldo Act.', 'Numero de cuenta', 'Saldo', 'moneda', 'archivo','Perido']
docu.write("^".join(cabecera)+"\n") 
for archivos in dris_:
    path_=archivos
    f = open(path_, "r")
    mes = path_.split('\\')
    lines = []
    lines = f.readlines()
    lista =[]
    count_lineas=0
    lista2=[]
    
    for line in lines:
        vector= line.split("  ")
        
        test_list=vector
        vector2=line
        
        lista.append(test_list)
        
        if len(vector2.replace("\n",""))<200:
            line=vector2.replace("\n","")+((200-len(vector2.replace("\n","")))*" ")
            lista2.append(line)
        else:
            lista2.append(line)
        count_lineas +=1
    
    for c in range(0,count_lineas):
            if len(lista[c])>0:
                
                if len(lista[c])>=2:
                    
                    if len([ i for i in range(0,len(lista[c])-1) if re.search("GS$",lista[c][i].replace(" ","")) or re.search("USD$",lista[c][i].replace(" ",""))])>0:
                       

                        for i,elem in enumerate(lista[c]):
                            auxgs = re.findall(r'\s+GS$',elem)
                            auxusd = re.findall(r'\s+USD$', elem)
                            auxgs1 = "".join(auxgs)
                            auxusd1 = "".join(auxusd)


                            if auxgs1 in lista[c]:
                                moneda="GS"
                                
                            elif auxusd1 in lista[c]:
                                moneda="USD"
                                
                    if len([ i for i in range(0,len(lista[c])-1) if re.search("^Cuenta:",lista[c][i].replace(" ",""))])>0:
                        vector_2=[i for i in lista[c] if i!=""]
                        Numero_de_cuenta_=vector_2[0].split(" ")
                        Numero_de_cuenta_=[i for i in Numero_de_cuenta_ if i!=""]
                        Numero_de_cuenta=Numero_de_cuenta_[1]
                       
                    
                    if "Saldo Anterior:" in lista[c]:
                        vector_3=[i for i in lista[c] if i!=""]
                        Saldo_Anterior=vector_3[-1].split(" ")[-1].replace("\n","")
                        
                    obre= re.compile(r'\d\d/\d\d/\d\d\d\d$')#formato de fecha
                    for i in range(len(lista)):
                        for j in range(len(lista[i])):
                            if len(obre.findall(lista[i][j])) != 0:
                                estado_al = obre.findall(lista[i][j])
                                break     
                    
                    sin_mov = re.compile(r'Sin Movimientos')
                    test = list()
                    for i in range(len(lista)):
                        for j in range(len(lista[i])):
                            if len(sin_mov.findall(lista[i][j])) != 0:
                                test.append(sin_mov.findall(lista[i][j]))
                                break
                    
                    if len([ i for i in range(0,len(lista[c])-1) if re.search(r"^\d\d/\d\d$",(lista[c][i].replace(" ","")))])>1:
                        
                        vector_3=[i for i in lista[c] if i!=""] 
                        vector_3=[i.replace("\n","") for i in vector_3]
                        
                        line=vector_3
                        
                        line.append(Numero_de_cuenta.replace("\n",""))
                        line.append(Saldo_Anterior.replace("\n",""))
                        line.append(moneda)
                        line.append(str(mes[-1].replace("\n","")))
                        line.append("".join(estado_al))
                        
                        docu.write("^".join(line)+"\n")
                    
                    

                    lista_obj= re.compile(r'\s*Sin Movimientos\s*')
                    lista_mon = re.compile(r'\s*USD')
                    
                    vector_cuenta = [i for i in lista[c] if i!='']
                    
                    patern = re.compile(r'\s*USD')
                    if len(patern.findall(vector_cuenta[0].replace(" ",""))) != 0:
                        monedasn = patern.findall(vector_cuenta[0].replace(" ",""))
                        numero_de_cuenta_sn=vector_cuenta[1]
                        Saldo_Anterior_sn = vector_cuenta[5]
                        
                    patern = re.compile(r'\s*GS')
                    if len(patern.findall(vector_cuenta[0].replace(" ",""))) != 0:
                        monedasn = patern.findall(vector_cuenta[0].replace(" ",""))
                        numero_de_cuenta_sn=vector_cuenta[1]
                        Saldo_Anterior_sn = vector_cuenta[5]
                    
                    for elem in lista[c]:
                        
                        if len(lista_obj.findall(elem))>0:
                            detlle_sm = ["","","",elem.replace("\n",""),"0,00","0,00","0,00"]
                                                   
 
                            detlle_sm.append(numero_de_cuenta_sn.replace("\n",""))
                            detlle_sm.append(Saldo_Anterior_sn.replace("\n",""))
                            detlle_sm.append("".join(monedasn))
                            detlle_sm.append(str(mes[-1].replace("\n","")))
                            detlle_sm.append("".join(estado_al))
                            docu.write("^".join(detlle_sm) + "\n")

                        

docu.close()

