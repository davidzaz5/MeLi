
import yara
from db.basededatos import Database
from pydantic import BaseModel



db = Database()   

class items(BaseModel): 
  
    rule: str

class Yaratexto :

    def textanalisis(self,texto:str):

        try:    
           
            scan = yara.compile(filepath="./rulesyara/reglasyarabd.txt")
            matches = scan.match(data=texto)
            db.insertOnetxt(texto, str(matches))
            return(matches)
           
            
        except yara.Error as e:
            return(e)
    

        

#palabras="3428354668545667"
#print(str(Yaratexto.textanalisis(palabras)))



class Yaraarchivo :

    def archivoanalisis(texto:str,name:str):

        try:    
           
            scan = yara.compile(filepath="./rulesyara/reglasyarabd.txt")
            matches = scan.match(data=texto)
            db.insertOnefile(name,str(matches))
            return(name,matches)
           
            
        except yara.Error as e:
            return(e)
    