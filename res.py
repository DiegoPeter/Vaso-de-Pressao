import sqlite3
from tkinter import messagebox


class resultados:
    def __init__(self, nome, diam, pre, ejunta, tcasco, matcasco, ttampo=None, mattampo=None, angcone=None, espcasco=None, esptampo=None):
        self.nome = nome
        self.diam = diam
        self.pre = pre
        self.ejunta = ejunta
        self.tcasco = tcasco
        self.matcasco = matcasco
        self.mattampo = mattampo
        self.ttampo = ttampo
        self.angcone = angcone
        self.espcasco = espcasco
        self.esptampo = esptampo

    def load_from_nome(nome):
        conn = sqlite3.connect('resultados.db')
        cursor1 = conn.cursor()
        cursor1.execute(f"SELECT *, oid FROM vaso WHERE nome=\"{nome}\"")
        records = cursor1.fetchall()
        if len(records) == 1:
            record = records[0]
            return resultados(nome=record[0], diam=record[1], pre=record[2], ejunta=record[3], tcasco=record[4], matcasco=record[5], ttampo=record[6], mattampo=record[7], angcone=record[8], espcasco=record[9], esptampo=record[10])
        conn.commit()
        conn.close()
        return None

    def save(self):
        conn = sqlite3.connect('resultados.db')
        cursor1 = conn.cursor()
        cursor1.execute("SELECT *, oid FROM vaso")
        records = cursor1.fetchall()
        shouldInsert = True
        for record in records:
            if record[0] == self.nome:
                aux = messagebox.askquestion(
                    "Erro", "Já existe um projeto com este nome.\nDeseja sobreescrever?")
                if aux == 'no':
                    shouldInsert = False
        if shouldInsert:
            cursor1.execute("""INSERT INTO vaso VALUES (:nome, :diam, :pre, :ejunta, :tcasco, :matcasco,:ttampo, :mattampo, :angcone, :espcasco, :esptampo) ON CONFLICT(nome) 
            DO UPDATE SET 
            nome=self.nome, 
            diam=self.diam, 
            pre= self.pre, 
            ejunta=self.ejunta, 
            tcasco=self.tcasco, 
            matcasco=self.matcasco,
            mattampo=self.mattampo,
            ttampo=self.ttampo,
            angcone=self.angcone,
            espcasco=self.espcasco,
            esptampo=self.esptampo""",
                            {
                                "nome": self.nome,
                                "diam": self.diam,
                                "pre": self.pre,
                                "ejunta": self.ejunta,
                                "tcasco": self.tcasco,
                                "matcasco": self.matcasco,
                                "mattampo": self.mattampo,
                                "ttampo": self.ttampo,
                                "angcone": self.angcone,
                                "espcasco": self.espcasco,
                                "esptampo": self.esptampo,
                            }
                            )
        conn.commit()
        conn.close()
