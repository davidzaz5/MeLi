from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile
from db.basededatos import Database
from rulesyara.reglas_yara import Yaratexto, Yaraarchivo




app = FastAPI() 
db = Database()                            #permite acceder a las funciones dentro de database.py
yaratxt = Yaratexto ()


class items(BaseModel): 
    name: str
    rule: str
   

class textos(BaseModel):
    texto:str
    
   
def DataFromDb():                          # recuperador de datos
    listData = []
    file=open("./rulesyara/reglasyarabd.txt","w")
    for data in db.getData():
        listData.append({"id": data[0], 
                        "name": data[1], 
                        "rule": data[2]})
        file.write(str(data[2]))
    
    file.close()
    
    return listData

                                        ##########################
                                        #####Agregar Yara#########
                                        ##########################
@app.get(path="/")                      #recupera los datos de la tabla
def getrules():

    return DataFromDb()

@app.post(path="/api/rule")              #inserta en tabla Yara
def addrule(item: items):
    db.insertOne(item.name, item.rule)
    return DataFromDb()

@app.put(path="/api/rule/{id:int}/")      #edita de la tabla Yara
def updaterule(id, item: items):
    db.updateData(id, [item.name, item.rule])
    return DataFromDb()

@app.delete(path="/api/rule/{id:int}/")   #elimina de la tabla Yara
def deleteule(id):
    db.deleteOFromDb(id)
    return DataFromDb()

##########################################################
## Analisis de Texto ##
##########################################################
@app.post(path="/api/analyze/texto")            
async def textanalisys(item: textos):
    return(str(yaratxt.textanalisis(item.texto)))
##########################################################

##########################################################
## Analisis de Archivos ##
##########################################################
@app.post(path="/api/analyze/file")            
async def create_upload_file(file: UploadFile):  
    name=file.filename
    contenido = file.file.read()
    file.close() 
    return (str(Yaraarchivo.archivoanalisis(contenido,name)))
    
##########################################################

