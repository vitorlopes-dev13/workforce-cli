import sqlite3
from model import Funcionario
DB_PATH = "empresa.db"

def conectar():
    return sqlite3.connect(DB_PATH)

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL,
        ativo INTEGER NOT NULL
    )
    """)
    conexao.commit()
    conexao.close()

def adicionar_funcionario(nome, cargo):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    INSERT INTO funcionarios (nome, cargo, ativo)
    VALUES (?, ?, ?)
    """, (nome, cargo, 1))
    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()
    return novo_id

def buscar_funcionarios(apenas_ativos=False):
    conexao = conectar()
    cursor = conexao.cursor()
    if apenas_ativos:
        cursor.execute(
            "SELECT id, nome, cargo, ativo FROM funcionarios WHERE ativo = 1 ORDER BY id"
        )
    else:
        cursor.execute(
            "SELECT id, nome, cargo, ativo FROM funcionarios ORDER BY id"
        )
    registros = cursor.fetchall()
    conexao.close()
    funcionarios = []
    for r in registros:
        funcionarios.append(Funcionario(
            id=r[0],
            nome=r[1],
            cargo=r[2],
            ativo=bool(r[3])
        ))
    return funcionarios

def desativar_funcionario(funcionario_id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    UPDATE funcionarios
    SET ativo = 0
    WHERE id = ? AND ativo = 1
    """, (funcionario_id,))
    conexao.commit()
    alterou = cursor.rowcount > 0
    conexao.close()
    return alterou

def contar_ativos_inativos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT
        SUM(CASE WHEN ativo = 1 THEN 1 ELSE 0 END),
        SUM(CASE WHEN ativo = 0 THEN 1 ELSE 0 END)
    FROM funcionarios
    """)
    row = cursor.fetchone()
    conexao.close()
    ativos = row[0] or 0
    inativos = row[1] or 0
    return ativos, inativos

def buscar_avancado(nome_parte=None, cargo_parte=None, apenas_ativos=None):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT id, nome, cargo, ativo FROM funcionarios"
    filtros = []
    params = []
    if nome_parte:
        filtros.append("LOWER(nome) LIKE ?")
        params.append(f"%{nome_parte.lower()}%")
    if cargo_parte:
        filtros.append("LOWER(cargo) LIKE ?")
        params.append(f"%{cargo_parte.lower()}%")
    if apenas_ativos is True:
        filtros.append("ativo = 1")
    elif apenas_ativos is False:
        filtros.append("ativo = 0")
    if filtros:
        sql += " WHERE " + " AND ".join(filtros)
    sql += " ORDER BY id"
    cursor.execute(sql, tuple(params))
    registros = cursor.fetchall()
    conexao.close()

    funcionarios = []
    for r in registros:
        funcionarios.append(Funcionario(
            id=r[0],
            nome=r[1],
            cargo=r[2],
            ativo=bool(r[3])
        ))
    return funcionarios
