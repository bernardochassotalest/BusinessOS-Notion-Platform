#!/usr/bin/env python3
"""
Script para popular a base de Colaboradores no Notion com 50 colaboradores realistas
Utiliza a API do Notion para criar registros na database de Colaboradores
"""

import requests
import json
from datetime import datetime, timedelta
import random

# Configuração da API do Notion
NOTION_TOKEN = "ntn_****"  # Substituir pelo token real
DATABASE_ID = "267d6174-4f45-81d8-8bd3-d3c27e224e1d"
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# Dados realistas para geração
NOMES = [
    "Ana Silva", "Bruno Costa", "Carla Santos", "Daniel Oliveira", "Elena Rodrigues",
    "Felipe Almeida", "Gabriela Lima", "Henrique Ferreira", "Isabela Martins", "João Pereira",
    "Karina Souza", "Lucas Barbosa", "Mariana Gomes", "Nicolas Ribeiro", "Olivia Cardoso",
    "Pedro Nascimento", "Queila Moreira", "Rafael Dias", "Sofia Teixeira", "Thiago Araújo",
    "Ursula Mendes", "Victor Hugo", "Wanda Freitas", "Xavier Campos", "Yasmin Torres",
    "Zeca Monteiro", "Amanda Rocha", "Bernardo Chassot", "Camila Nunes", "Diego Lopes",
    "Eduarda Pinto", "Fabio Correia", "Giovana Reis", "Hugo Carvalho", "Ingrid Melo",
    "Julio Cesar", "Kelly Andrade", "Leonardo Silva", "Monica Vieira", "Nathan Borges",
    "Otavio Cunha", "Patricia Ramos", "Quintino Farias", "Roberta Castro", "Samuel Moura",
    "Tatiana Brito", "Ulisses Macedo", "Vanessa Porto", "William Sá", "Ximena Duarte", "Yuri Tavares"
]

DEPARTAMENTOS = {
    "676612c1-0cb9-471a-8fa2-9b03bea62923": "Executivo",
    "35c78e36-a1bd-401c-8ee0-ac6021d90ed5": "Tecnologia", 
    "c205d4d5-2a8f-4c05-9c3f-11d40f7f134e": "RH",
    "98f666f5-48e8-4abf-add8-7bebea382ac8": "Comercial",
    "93b489c4-9c43-4f93-8bd9-a1fa5ba9cb61": "Operações"
}

CARGOS = {
    "bafd31f2-a42f-4e8b-85cd-91ae6ca05c7d": "CVO",
    "ad031047-184d-4d3a-999d-291d88a0ade2": "CTO", 
    "754a6a37-1fc7-4063-b19d-c19e959f3685": "Gerente",
    "308ad646-99c1-415f-b80a-baefd11df8a0": "Desenvolvedor",
    "9d08723a-554c-4fd8-b051-f5307414fd92": "Designer",
    "e635e184-1661-40ad-a650-f43a03121d99": "Analista"
}

STATUS_OPTIONS = {
    "eb52e03e-c294-42c2-b1f9-7fea707084de": "Ativo",
    "d55af342-7adf-4041-9b62-d9d3c738a822": "Inativo", 
    "624e14fe-d020-4261-ad28-d6f182a44213": "Férias"
}

def gerar_email(nome):
    """Gera email baseado no nome"""
    nome_limpo = nome.lower().replace(" ", ".").replace("ã", "a").replace("ç", "c")
    return f"{nome_limpo}@alest.com.br"

def gerar_data_admissao():
    """Gera data de admissão aleatória nos últimos 3 anos"""
    hoje = datetime.now()
    inicio = hoje - timedelta(days=3*365)
    dias_aleatorios = random.randint(0, 3*365)
    data = inicio + timedelta(days=dias_aleatorios)
    return data.strftime("%Y-%m-%d")

def gerar_performance():
    """Gera performance entre 0.6 e 1.0"""
    return round(random.uniform(0.6, 1.0), 2)

def gerar_nps():
    """Gera NPS interno entre 6 e 10"""
    return random.randint(6, 10)

def criar_colaborador(nome):
    """Cria um colaborador na database do Notion"""
    
    # Distribuição realista por departamento
    dept_weights = [0.05, 0.35, 0.15, 0.25, 0.20]  # Executivo, Tech, RH, Comercial, Operações
    dept_id = random.choices(list(DEPARTAMENTOS.keys()), weights=dept_weights)[0]
    
    # Cargo baseado no departamento
    if dept_id == "676612c1-0cb9-471a-8fa2-9b03bea62923":  # Executivo
        cargo_id = "bafd31f2-a42f-4e8b-85cd-91ae6ca05c7d"  # CVO
    elif dept_id == "35c78e36-a1bd-401c-8ee0-ac6021d90ed5":  # Tecnologia
        cargo_options = ["ad031047-184d-4d3a-999d-291d88a0ade2", "308ad646-99c1-415f-b80a-baefd11df8a0", "9d08723a-554c-4fd8-b051-f5307414fd92"]
        cargo_id = random.choice(cargo_options)
    else:
        cargo_options = ["754a6a37-1fc7-4063-b19d-c19e959f3685", "e635e184-1661-40ad-a650-f43a03121d99"]
        cargo_id = random.choice(cargo_options)
    
    # Status (95% ativo)
    status_weights = [0.95, 0.02, 0.03]
    status_id = random.choices(list(STATUS_OPTIONS.keys()), weights=status_weights)[0]
    
    payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Nome": {
                "title": [{"text": {"content": nome}}]
            },
            "Email": {
                "email": gerar_email(nome)
            },
            "Departamento": {
                "select": {"id": dept_id}
            },
            "Cargo": {
                "select": {"id": cargo_id}
            },
            "Status": {
                "select": {"id": status_id}
            },
            "Data Admissão": {
                "date": {"start": gerar_data_admissao()}
            },
            "Performance Atual": {
                "number": gerar_performance()
            },
            "NPS Interno": {
                "number": gerar_nps()}
        }
    }
    
    try:
        response = requests.post(
            "https://api.notion.com/v1/pages",
            headers=HEADERS,
            json=payload
        )
        
        if response.status_code == 200:
            print(f"✅ Colaborador criado: {nome}")
            return True
        else:
            print(f"❌ Erro ao criar {nome}: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Exceção ao criar {nome}: {str(e)}")
        return False

def main():
    """Função principal para popular todos os colaboradores"""
    print("🚀 Iniciando população da base de Colaboradores...")
    print(f"📊 Total de colaboradores a criar: {len(NOMES)}")
    
    sucessos = 0
    falhas = 0
    
    for i, nome in enumerate(NOMES, 1):
        print(f"\n[{i}/{len(NOMES)}] Criando: {nome}")
        
        if criar_colaborador(nome):
            sucessos += 1
        else:
            falhas += 1
    
    print(f"\n📈 Resumo da Execução:")
    print(f"✅ Sucessos: {sucessos}")
    print(f"❌ Falhas: {falhas}")
    print(f"📊 Taxa de Sucesso: {(sucessos/len(NOMES)*100):.1f}%")
    
    if sucessos > 0:
        print(f"\n🎉 Base de Colaboradores populada com {sucessos} registros!")
    else:
        print(f"\n⚠️ Nenhum colaborador foi criado. Verifique o token e permissões.")

if __name__ == "__main__":
    main()
