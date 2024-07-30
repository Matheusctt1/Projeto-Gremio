import services.dataBase as db

def cadastrarAcao(acao):
    count = db.cursor.execute("""
    INSERT INTO BD_ACOES ([Adversario+Data],[Atleta],[Tipo de Ação],[X],[Y])
    VALUES (?,?,?,?,?)""",
    acao.advData, acao.atleta, acao.acao, acao.X, acao.Y).rowcount
    db.cnxn.commit()

