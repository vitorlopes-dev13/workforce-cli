def listar_funcionarios(funcionarios):
    if not funcionarios:
        return []
    return [
        f"{f.id} - {f.nome} - {f.cargo} - {f.situacao()}"
        for f in funcionarios
    ]

def validar_nome(nome):
    nome = (nome or "").strip()
    if len(nome) < 3:
        return False, "Nome deve ter pelo menos 3 caracteres."
    if not nome.replace(" ", "").isalpha():
        return False, "Nome deve conter apenas letras e espaços."
    return True, nome

def validar_cargo(cargo):
    cargo = (cargo or "").strip()
    if len(cargo) < 2:
        return False, "Cargo deve ter pelo menos 2 caracteres."
    permitido = set(" -")
    for ch in cargo:
        if not (ch.isalpha() or ch in permitido):
            return False, "Cargo deve conter apenas letras, espaços ou hífen."
    return True, cargo

def ler_int(msg):
    valor = input(msg).strip()
    if not valor.isdigit():
        return None
    return int(valor)
