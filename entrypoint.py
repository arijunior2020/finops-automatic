import subprocess

scripts = [
    "scripts/gerar_avaliacao_maturidade.py",
    "scripts/gerar_papeis_personas.py",
    "scripts/gerar_ferramentas_aws.py",
    "scripts/gerar_execucao_piloto.py",
    "scripts/gerar_governanca_indicadores.py",
    "scripts/gerar_finops_executivo.py"
]

for script in scripts:
    print(f"Executando: {script}")
    subprocess.run(["python", script], check=True)
