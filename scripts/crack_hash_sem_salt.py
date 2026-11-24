import hashlib

# Pares de email e hash extraidos pela vulnerabilidade da Secao 4
HASHES_VAZADOS = [
    ("msilva@universidade.br", "8699a8a64e81d56ae094073ed415847462ef72052b73b0b77ac1d9b74851078b86402992f9a9efbf2e489521eac529185127a1c51d8f8319a4187313b823deca", "professor"),
    ("dsantos@universidade.br", "ca5ec5311586264d520802f9850e57019c38901db7621b78aba490304f02d64f4e257a00fa4adf1b6d65c2be9cef2aae30fa54782127fab06cf4796d4431f943", "professor"),
    ("cmelo@universidade.br", "5b6fd29927d593f97fa4e5bbb7bf12ad08c00a0dfddf695b915cde46c9420bb937e6c28edcd8f1d72c7805be0316d3264c69570602199ce472ce2fd38f66b249", "professor"),
    ("sspark@universidade.br", "6d855ae2ae3547e208e3ec1278eb22f2d5de9f7ac19216720a5285394a42257c24413808e117bb6fb9f79bb5e048de630d66b0399e9d42a10423f392d4964e29", "aluno"),
    ("tsleep@universidade.br", "48d21aca9daa47b7e1b12dc5c94467b49c2240a0faa0d3f2239a5234cdf7e1e35f4ec34a2e230f92dcf226a19d024818c86e9898e0d53fb56bef122e0161838f", "aluno"),
    ("fhope@universidade.br", "40309367eee8d3bb9cf4c9a9fb018a0f4e017fcaf4f420e59cc9f4bd7e52a41b6f9bddd155ace908c453021e61fecfdc9f459a73763e4adb1bed2f618c0e8b05", "aluno"),
]

# Mesmo dicionario de senhas candidatas utilizado no ataque da Secao 5
PASSWORD_LIST = [
    "Senh@123",
    "Admin#0o0",
    "Prof$123",
    "Unidin@1",
    "Teste#28",
    "Mar1ng@",
    "Aluno#67",
    "s$A159cc",
]

def quebrar_hashes():
    encontrados = {}
    for senha in PASSWORD_LIST:
        hash_candidato = hashlib.sha512(senha.encode("utf-8")).hexdigest()
        for email, hash_vazado, role in HASHES_VAZADOS:
            if hash_candidato == hash_vazado:
                encontrados[email] = (senha, role)

    print("Senhas recuperadas a partir dos hashes vazados\n")
    for email, (senha, role) in encontrados.items():
        print(f"{email} ({role}), senha {senha}")

    if not encontrados:
        print("Nenhuma senha do dicionario correspondeu aos hashes vazados.")

if __name__ == "__main__":
    quebrar_hashes()
