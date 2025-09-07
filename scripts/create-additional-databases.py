#!/usr/bin/env python3
"""
Script para criar bases adicionais da jornada do colaborador no Notion
Cria databases para: Onboarding, Performance, Feedback 360, Clima Organizacional
"""

import requests
import json

# Configuração da API do Notion
NOTION_TOKEN = "ntn_****"  # Substituir pelo token real
PARENT_PAGE_ID = "267d6174-4f45-8198-aba2-f0f91e396274"  # ID da página Gestão de Pessoas
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# Definição das databases adicionais
DATABASES = {
    "onboarding": {
        "title": "Checklist Onboarding",
        "properties": {
            "Colaborador": {
                "type": "relation",
                "relation": {"database_id": "267d6174-4f45-81d8-8bd3-d3c27e224e1d"}
            },
            "Etapa": {
                "type": "select",
                "select": {
                    "options": [
                        {"name": "Pré-admissão", "color": "gray"},
                        {"name": "Primeiro Dia", "color": "blue"},
                        {"name": "Primeira Semana", "color": "yellow"},
                        {"name": "Primeiro Mês", "color": "orange"},
                        {"name": "Período Probatório", "color": "green"},
                        {"name": "Integração Completa", "color": "purple"}
                    ]
                }
            },
            "Tarefa": {
                "type": "title",
                "title": {}
            },
            "Status": {
                "type": "select",
                "select": {
                    "options": [
                        {"name": "Pendente", "color": "red"},
                        {"name": "Em Progresso", "color": "yellow"},
                        {"name": "Concluído", "color": "green"},
                        {"name": "Não Aplicável", "color": "gray"}
                    ]
                }
            },
            "Responsável": {
                "type": "select",
                "select": {
                    "options": [
                        {"name": "RH", "color": "green"},
                        {"name": "Gestor Direto", "color": "blue"},
                        {"name": "TI", "color": "purple"},
                        {"name": "Colaborador", "color": "orange"},
                        {"name": "Buddy", "color": "yellow"}
                    ]
                }
            },
            "Data Limite": {
                "type": "date",
                "date": {}
            },
            "Data Conclusão": {
                "type": "date",
                "date": {}
            },
            "Observações": {
                "type": "rich_text",
                "rich_text": {}
            }
        }
    },
    "performance": {
        "title": "Avaliações Performance",
        "properties": {
            "Colaborador": {
                "type": "relation",
                "relation": {"database_id": "267d6174-4f45-81d8-8bd3-d3c27e224e1d"}
            },
            "Período": {
                "type": "title",
                "title": {}
            },
            "Tipo Avaliação": {
                "type": "select",
                "select": {
                    "options": [
                        {"name": "Trimestral", "color": "blue"},
                        {"name": "Semestral", "color": "green"},
                        {"name": "Anual", "color": "purple"},
                        {"name": "Probatório", "color": "orange"},
                        {"name": "Extraordinária", "color": "red"}
                    ]
                }
            },
            "Nota Geral": {
                "type": "number",
                "number": {"format": "number"}
            },
            "Competências Técnicas": {
                "type": "number",
                "number": {"format": "number"}
            },
            "Competências Comportamentais": {
                "type": "number",
                "number": {"format": "number"}
            },
            "Entrega de Resultados": {
                "type": "number",
                "number": {"format": "number"}
            },
            "Status": {
                "type": "select",
                "select": {
                    "options": [
                        {"name": "Supera Expectativas", "color": "green"},
                        {"name": "Atende Expectativas", "color": "blue"},
                        {"name": "Parcialmente Atende", "color": "yellow"},
                        {"name": "Não Atende", "color": "red"}
                    ]
                }
            },
            "Avaliador": {
                "type": "select",
                "select": {
                    "options": [
                        {"name": "Gestor Direto", "color": "blue"},
                        {"name": "RH", "color": "green"},
                        {"name": "Diretor", "color": "purple"},
                        {"name": "Autoavaliação", "color": "orange"}
                    ]
                }
            },
            "Data Avaliação": {
                "type": "date",
                "date": {}
            },
            "Pontos Fortes": {
                "type": "rich_text",
                "rich_text": {}
            },
            "Pontos Melhoria": {
                "type": "rich_text",
                "rich_text": {}
            },
            "Plano Ação": {
                "type": "rich_text",
                "rich_text": {}
            }
        }
    },
    "feedback360": {
        "title": "Feedback 360°",
        "properties": {
            "Colaborador Avaliado": {
                "type": "relation",
                "relation": {"database_id": "267d6174-4f45-81d8-8bd3-d3c27e224e1d"}
            },
            "Ciclo": {
                "type": "title",
                "title": {}
            },
            "Avaliador": {
                "type": "select",
                "select": {
                    "options": [
                        {"name": "Gestor", "color": "blue"},
                        {"name": "Par", "color": "green"},
                        {"name": "Subordinado", "color": "yellow"},
                        {"name": "Cliente Interno", "color": "orange"},
                        {"name": "Autoavaliação", "color": "purple"}
                    ]
                }
            },
            "Comunicação": {
                "type": "number",
                "number": {"format": "number"}
            },
            "Liderança": {
                "type": "number",
                "number": {"format": "number"}
            },
            "Trabalho em Equipe": {
                "type": "number",
                "number": {"format": "number"}
            },
            "Inovação": {
                "type": "number",
                "number": {"format": "number"}
            },
            "Orientação Resultados": {
                "type": "number",
                "number": {"format": "number"}
            },
            "Nota Geral": {
                "type": "formula",
                "formula": {"expression": "(prop(\"Comunicação\") + prop(\"Liderança\") + prop(\"Trabalho em Equipe\") + prop(\"Inovação\") + prop(\"Orientação Resultados\")) / 5"}
            },
            "Status": {
                "type": "select",
                "select": {
                    "options": [
                        {"name": "Pendente", "color": "red"},
                        {"name": "Em Progresso", "color": "yellow"},
                        {"name": "Concluído", "color": "green"}
                    ]
                }
            },
            "Data Feedback": {
                "type": "date",
                "date": {}
            },
            "Comentários": {
                "type": "rich_text",
                "rich_text": {}
            }
        }
    },
    "clima": {
        "title": "Pesquisa Clima Organizacional",
        "properties": {
            "Colaborador": {
                "type": "relation",
                "relation": {"database_id": "267d6174-4f45-81d8-8bd3-d3c27e224e1d"}
            },
            "Período": {
                "type": "title",
                "title": {}
            },
            "Satisfação Geral": {
                "type": "number",
                "number": {"format": "number"}
            },
            "Ambiente Trabalho": {
                "type": "number",
                "number": {"format": "number"}
            },
            "Relacionamento Equipe": {
                "type": "number",
                "number": {"format": "number"}
            },
            "Liderança": {
                "type": "number",
                "number": {"format": "number"}
            },
            "Crescimento Profissional": {
                "type": "number",
                "number": {"format": "number"}
            },
            "Reconhecimento": {
                "type": "number",
                "number": {"format": "number"}
            },
            "Work-Life Balance": {
                "type": "number",
                "number": {"format": "number"}
            },
            "NPS Interno": {
                "type": "number",
                "number": {"format": "number"}
            },
            "Recomendaria Empresa": {
                "type": "select",
                "select": {
                    "options": [
                        {"name": "Definitivamente Sim", "color": "green"},
                        {"name": "Provavelmente Sim", "color": "blue"},
                        {"name": "Neutro", "color": "yellow"},
                        {"name": "Provavelmente Não", "color": "orange"},
                        {"name": "Definitivamente Não", "color": "red"}
                    ]
                }
            },
            "Data Pesquisa": {
                "type": "date",
                "date": {}
            },
            "Sugestões": {
                "type": "rich_text",
                "rich_text": {}
            },
            "Status": {
                "type": "select",
                "select": {
                    "options": [
                        {"name": "Pendente", "color": "red"},
                        {"name": "Respondido", "color": "green"},
                        {"name": "Não Respondeu", "color": "gray"}
                    ]
                }
            }
        }
    }
}

def criar_database(nome, config):
    """Cria uma database no Notion"""
    
    payload = {
        "parent": {"page_id": PARENT_PAGE_ID},
        "title": [{"text": {"content": config["title"]}}],
        "properties": config["properties"]
    }
    
    try:
        response = requests.post(
            "https://api.notion.com/v1/databases",
            headers=HEADERS,
            json=payload
        )
        
        if response.status_code == 200:
            database_id = response.json()["id"]
            print(f"✅ Database criada: {config['title']} (ID: {database_id})")
            return database_id
        else:
            print(f"❌ Erro ao criar {config['title']}: {response.status_code} - {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Exceção ao criar {config['title']}: {str(e)}")
        return None

def main():
    """Função principal para criar todas as databases"""
    print("🚀 Iniciando criação das bases adicionais da jornada do colaborador...")
    print(f"📊 Total de databases a criar: {len(DATABASES)}")
    
    sucessos = 0
    falhas = 0
    database_ids = {}
    
    for nome, config in DATABASES.items():
        print(f"\n📋 Criando database: {config['title']}")
        
        database_id = criar_database(nome, config)
        if database_id:
            sucessos += 1
            database_ids[nome] = database_id
        else:
            falhas += 1
    
    print(f"\n📈 Resumo da Execução:")
    print(f"✅ Sucessos: {sucessos}")
    print(f"❌ Falhas: {falhas}")
    print(f"📊 Taxa de Sucesso: {(sucessos/len(DATABASES)*100):.1f}%")
    
    if sucessos > 0:
        print(f"\n🎉 Bases adicionais criadas com sucesso!")
        print(f"\n📋 IDs das Databases Criadas:")
        for nome, db_id in database_ids.items():
            print(f"   • {DATABASES[nome]['title']}: {db_id}")
        
        print(f"\n💡 Próximos Passos:")
        print(f"   1. Popular as databases com dados de exemplo")
        print(f"   2. Configurar views e filtros personalizados")
        print(f"   3. Criar automações entre as databases")
        print(f"   4. Configurar dashboards de RH")
    else:
        print(f"\n⚠️ Nenhuma database foi criada. Verifique o token e permissões.")

if __name__ == "__main__":
    main()
