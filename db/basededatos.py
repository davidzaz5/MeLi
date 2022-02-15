import sqlite3

class Database:
    def __init__(self):
        if __name__ == "__main__":
            self.connection = sqlite3.connect("./db/database.db")
        else:
            self.connection = sqlite3.connect("./db/database.db", check_same_thread=False)
        
            self.cursor = self.connection.cursor()
    
    def insertOne(self,name:str, rule:str):
        queryData = [name, rule,]
        self.cursor.execute("INSERT INTO Yara(name, rule) VALUES(?, ?)", queryData)
        self.connection.commit()

    def getData(self):
        self.cursor.execute("SELECT * FROM Yara")
        return self.cursor.fetchall()

    def updateData(self, id:int, data:list):
        self.cursor.execute(f"UPDATE Yara SET name='{data[0]}', rule='{data[1]}' WHERE id='{id}'")
        self.connection.commit()

    def deleteOFromDb(self, id:int):

        self.cursor.execute(f"DELETE FROM yara WHERE id = '{id}'")
        self.connection.commit()

    def insertOnetxt(self,texto:str, rule:str):
        queryData = [texto, rule,]
        self.cursor.execute("INSERT INTO Textos(texto, rules) VALUES(?, ?)", queryData)
        self.connection.commit()
    
    def insertOnefile(self,archivo:str, rule:str):
        queryData = [archivo, rule,]
        self.cursor.execute("INSERT INTO Archivos(archivo, rules) VALUES(?, ?)", queryData)
        self.connection.commit()