def adicionar_contato(contatos, nome_contato, tel_contato, email_contato ):
  contato = {"nome": nome_contato, "telefone": tel_contato, "email": email_contato, "favorito": False}

  contatos.append(contato)
  print(f"O contato {nome_contato} foi adicionado com sucesso!")
  return

def ver_contatos(contatos):
  print("\nLista de contatos:")
  for indice, contato in enumerate(contatos, start=1):
    favorito = "★" if contato["favorito"] else "☆" 
    nome_contato = contato["nome"]
    tel_contato = contato["telefone"]
    email = contato["email"]
    print(f"{indice}. {favorito} | Nome: {nome_contato} - Tel: {tel_contato} - Email: {email}")
  return

def atualizar_nome_contato(contatos, indice_contato, novo_nome_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["nome"] = novo_nome_contato
    print(f"Contato {indice_contato} atualizado para {novo_nome_contato}")
  else: 
    print("Indice de contato inválido.")
  return

def atualizar_tel_contato(contatos, indice_contato, novo_tel_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["telefone"] = novo_tel_contato
    print(f"Numero do tel do contato {indice_contato} atualizado para {novo_tel_contato}")
  else: 
    print("Indice de contato inválido.")
  return

def atualizar_email_contato(contatos, indice_contato, novo_email_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["email"] = novo_email_contato
    print(f"Email do contato {indice_contato} atualizado para {novo_email_contato}")
  else: 
    print("Indice de contato inválido.")
  return

def favoritar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1

  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["favorito"] = True
    print(f"Contato {indice_contato} Favoritado")
  else: 
    print("Indice de contato inválido.")
  return

def editar_contato(contatos, indice_contato, novo_nome_contato=None, novo_tel_contato=None, novo_email_contato=None):
  while True:
    print("\nO que você quer editar nesse contato?")
    print("1. Nome")
    print("2. Telefone")
    print("3. Email")
    print("4. Favorito")
    print("5. Voltar")

    resposta = input("\nDigite sua escolha: ")

    if resposta == '1':
      novo_nome_contato = input("\nDigite o novo nome para esse contato: ")
      atualizar_nome_contato(contatos, indice_contato, novo_nome_contato)
    
    elif resposta == '2':
      novo_tel_contato = input("\nDigite o novo numero para esse contato: ")
      atualizar_tel_contato(contatos, indice_contato, novo_tel_contato)
      
    elif resposta == '3':
      novo_email_contato = input("\nDigite o novo email para esse contato: ")
      atualizar_email_contato(contatos, indice_contato, novo_email_contato)

    elif resposta == '4':
      favoritar_contato(contatos, indice_contato,)
    
    elif resposta == '5':
      break

def visualizar_favoritos(contatos):
  print("\nLista de contatos favoritados:")
  for indice, contato in enumerate(contatos, start=1):
    if contato["favorito"]:
      favorito = "★"
      nome_contato = contato["nome"]
      tel_contato = contato["telefone"]
      email = contato["email"]
      print(f"{indice}. {favorito} | Nome: {nome_contato} - Tel: {tel_contato} - Email: {email}")
  return

def deletar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1

  contato_removido = contatos[indice_contato_ajustado]
  contatos.remove(contato_removido)
  print(f"\nContato {indice_contato} removido com sucesso.")
  return

contatos = []

while True:
  print("\nMenu da agenda:")
  print("1. Adicionar contato")
  print("2. Ver contatos")
  print("3. Editar contato")
  print("4. Marcar contato como favorito")
  print("5. Ver contatos favoritos")
  print("6. Deletar um contato")
  print("7. Sair")

  escolha = input("\nDigite a sua escolha: ")

  if escolha == "1":
    nome_contato = input("\nDigite o nome do contato: ")
    telefone = input("\nDigite o telefone do contato: ")
    email = input("\nDigite o email do contato: ")
    adicionar_contato(contatos, nome_contato, telefone, email)

  elif escolha == "2":
    ver_contatos(contatos)

  elif escolha == "3":
    ver_contatos(contatos)
    indice_contato = input("\nDigite o numero do contato que você deseja editar: ")
    editar_contato(contatos, indice_contato)
  
  elif escolha == "4":
    ver_contatos(contatos)
    indice_contato = input("\nDigite o numero do contato que você deseja favoritar: ")
    favoritar_contato(contatos, indice_contato)

  elif escolha == "5":
    visualizar_favoritos(contatos)

  elif escolha == "6":
    ver_contatos(contatos)
    indice_contato = input('\nDigite o numero do contato que você deseja Remover: ')
    deletar_contato(contatos, indice_contato)
    ver_contatos(contatos)

  elif escolha == "7":
    break
