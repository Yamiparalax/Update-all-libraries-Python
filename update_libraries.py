import subprocess

def atualizar_bibliotecas():
    """
    Lists all installed libraries and updates them to the latest version.
    """

    # List all installed libraries
    try:
        result = subprocess.run(['pip', 'list'], capture_output=True, text=True, check=True)
        pacotes_instalados = result.stdout.splitlines()[2:]  # Skip header lines
        print("Pacotes instalados:")
        print("\n".join(pacotes_instalados))
    except subprocess.CalledProcessError as e:
        print(f"Erro ao listar pacotes: {e}")
        return

    # Update each package
    for pacote in pacotes_instalados:
        pacote_nome = pacote.split()[0]
        try:
            subprocess.run(['pip', 'install', '--upgrade', pacote_nome], capture_output=True, text=True, check=True)
            print(f"Pacote {pacote_nome} atualizado com sucesso!")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao atualizar o pacote {pacote_nome}: {e}")

if __name__ == "__main__":
    atualizar_bibliotecas()
