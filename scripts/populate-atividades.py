#!/usr/bin/env python3
"""
Script para popular a base de Atividades do Projeto no Notion com 30 atividades detalhadas
Utiliza a API do Notion para criar registros na database de Atividades do Projeto
"""

import requests
import json
from datetime import datetime, timedelta
import random

# Configuração da API do Notion
NOTION_TOKEN = "ntn_****"  # Substituir pelo token real
DATABASE_ID = "267d6174-4f45-8138-9b4e-c8b5b8b9b8b8"  # ID da database Atividades do Projeto
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# Atividades detalhadas do projeto BusinessOS
ATIVIDADES = [
    {
        "nome": "Arquitetura de Dados - Modelagem ERD",
        "descricao": "Criar diagramas de relacionamento entre entidades para todas as 5 bases de dados principais",
        "fase": "Fase 1 - Fundação",
        "responsavel": "Bernardo Chassot",
        "prioridade": "Alta",
        "status": "Concluído",
        "data_inicio": "2025-09-09",
        "data_fim": "2025-09-13",
        "estimativa_horas": 32,
        "categoria": "Arquitetura"
    },
    {
        "nome": "Setup Workspace Notion Enterprise",
        "descricao": "Configurar workspace principal com permissões, estrutura de páginas e databases iniciais",
        "fase": "Fase 1 - Fundação", 
        "responsavel": "Tech Lead",
        "prioridade": "Alta",
        "status": "Em Progresso",
        "data_inicio": "2025-09-09",
        "data_fim": "2025-09-11",
        "estimativa_horas": 16,
        "categoria": "Infraestrutura"
    },
    {
        "nome": "Database Colaboradores - Estrutura",
        "descricao": "Criar database de colaboradores com todas as propriedades, relações e validações necessárias",
        "fase": "Fase 1 - Fundação",
        "responsavel": "Tech Lead",
        "prioridade": "Alta", 
        "status": "Concluído",
        "data_inicio": "2025-09-11",
        "data_fim": "2025-09-12",
        "estimativa_horas": 8,
        "categoria": "Database"
    },
    {
        "nome": "Database Projetos - Estrutura",
        "descricao": "Criar database de projetos com pipeline, status, responsáveis e métricas de acompanhamento",
        "fase": "Fase 1 - Fundação",
        "responsavel": "Tech Lead",
        "prioridade": "Alta",
        "status": "Pendente",
        "data_inicio": "2025-09-12",
        "data_fim": "2025-09-13",
        "estimativa_horas": 12,
        "categoria": "Database"
    },
    {
        "nome": "Database Clientes - Estrutura",
        "descricao": "Criar database de clientes com jornada, touchpoints e histórico de interações",
        "fase": "Fase 1 - Fundação",
        "responsavel": "Tech Lead",
        "prioridade": "Média",
        "status": "Pendente",
        "data_inicio": "2025-09-13",
        "data_fim": "2025-09-16",
        "estimativa_horas": 16,
        "categoria": "Database"
    },
    {
        "nome": "Integração HubSpot - Clientes",
        "descricao": "Configurar sincronização automática entre HubSpot CRM e database de Clientes no Notion",
        "fase": "Fase 2 - Integrações",
        "responsavel": "Tech Lead",
        "prioridade": "Alta",
        "status": "Pendente",
        "data_inicio": "2025-09-16",
        "data_fim": "2025-09-20",
        "estimativa_horas": 24,
        "categoria": "Integração"
    },
    {
        "nome": "Dashboard Executivo - Wireframes",
        "descricao": "Criar wireframes detalhados para dashboard executivo com KPIs principais e métricas de ROI",
        "fase": "Fase 1 - Fundação",
        "responsavel": "Designer",
        "prioridade": "Média",
        "status": "Pendente",
        "data_inicio": "2025-09-11",
        "data_fim": "2025-09-13",
        "estimativa_horas": 16,
        "categoria": "Design"
    },
    {
        "nome": "Dashboard RH - Implementação",
        "descricao": "Implementar dashboard de RH com métricas de performance, NPS interno e jornada do colaborador",
        "fase": "Fase 2 - Integrações",
        "responsavel": "RH Manager",
        "prioridade": "Alta",
        "status": "Pendente",
        "data_inicio": "2025-09-18",
        "data_fim": "2025-09-25",
        "estimativa_horas": 32,
        "categoria": "Dashboard"
    },
    {
        "nome": "Automação Onboarding",
        "descricao": "Criar fluxo automatizado de onboarding com templates, checklists e notificações",
        "fase": "Fase 2 - Integrações",
        "responsavel": "RH Manager",
        "prioridade": "Média",
        "status": "Pendente",
        "data_inicio": "2025-09-20",
        "data_fim": "2025-09-27",
        "estimativa_horas": 20,
        "categoria": "Automação"
    },
    {
        "nome": "Sistema de Feedback 360°",
        "descricao": "Implementar sistema de feedback 360° com formulários, coleta e análise automática",
        "fase": "Fase 3 - Otimização",
        "responsavel": "RH Manager",
        "prioridade": "Média",
        "status": "Pendente",
        "data_inicio": "2025-09-25",
        "data_fim": "2025-10-02",
        "estimativa_horas": 28,
        "categoria": "RH"
    },
    {
        "nome": "Pipeline Comercial - Configuração",
        "descricao": "Configurar pipeline comercial com stages, probabilidades e automações de follow-up",
        "fase": "Fase 2 - Integrações",
        "responsavel": "Account Manager",
        "prioridade": "Alta",
        "status": "Pendente",
        "data_inicio": "2025-09-23",
        "data_fim": "2025-09-30",
        "estimativa_horas": 24,
        "categoria": "Comercial"
    },
    {
        "nome": "Relatórios Executivos - Templates",
        "descricao": "Criar templates de relatórios executivos mensais com métricas automatizadas",
        "fase": "Fase 3 - Otimização",
        "responsavel": "PM",
        "prioridade": "Média",
        "status": "Pendente",
        "data_inicio": "2025-09-30",
        "data_fim": "2025-10-04",
        "estimativa_horas": 16,
        "categoria": "Relatórios"
    },
    {
        "nome": "Treinamento Equipe - Módulo 1",
        "descricao": "Treinamento inicial da equipe nas funcionalidades básicas do BusinessOS",
        "fase": "Fase 3 - Otimização",
        "responsavel": "PM",
        "prioridade": "Alta",
        "status": "Pendente",
        "data_inicio": "2025-10-02",
        "data_fim": "2025-10-04",
        "estimativa_horas": 12,
        "categoria": "Treinamento"
    },
    {
        "nome": "Migração Dados Colaboradores",
        "descricao": "Migrar dados históricos de colaboradores dos sistemas legados para o Notion",
        "fase": "Fase 2 - Integrações",
        "responsavel": "Tech Lead",
        "prioridade": "Alta",
        "status": "Pendente",
        "data_inicio": "2025-09-16",
        "data_fim": "2025-09-18",
        "estimativa_horas": 16,
        "categoria": "Migração"
    },
    {
        "nome": "Testes de Performance - 50 Usuários",
        "descricao": "Executar testes de performance com 50 usuários simultâneos e validar limites do Notion",
        "fase": "Fase 3 - Otimização",
        "responsavel": "QA",
        "prioridade": "Alta",
        "status": "Pendente",
        "data_inicio": "2025-10-07",
        "data_fim": "2025-10-09",
        "estimativa_horas": 20,
        "categoria": "Testes"
    },
    {
        "nome": "Backup e Recuperação - Estratégia",
        "descricao": "Implementar estratégia de backup automático e procedimentos de recuperação de dados",
        "fase": "Fase 4 - Produção",
        "responsavel": "Tech Lead",
        "prioridade": "Alta",
        "status": "Pendente",
        "data_inicio": "2025-10-09",
        "data_fim": "2025-10-11",
        "estimativa_horas": 12,
        "categoria": "Infraestrutura"
    },
    {
        "nome": "Monitoramento e Alertas",
        "descricao": "Configurar sistema de monitoramento de uso, performance e alertas automáticos",
        "fase": "Fase 4 - Produção",
        "responsavel": "Tech Lead",
        "prioridade": "Média",
        "status": "Pendente",
        "data_inicio": "2025-10-11",
        "data_fim": "2025-10-14",
        "estimativa_horas": 16,
        "categoria": "Monitoramento"
    },
    {
        "nome": "Documentação Técnica Completa",
        "descricao": "Finalizar documentação técnica completa com arquitetura, APIs e procedimentos",
        "fase": "Fase 4 - Produção",
        "responsavel": "PM",
        "prioridade": "Média",
        "status": "Pendente",
        "data_inicio": "2025-10-14",
        "data_fim": "2025-10-16",
        "estimativa_horas": 20,
        "categoria": "Documentação"
    },
    {
        "nome": "Validação LGPD - Compliance",
        "descricao": "Validar compliance LGPD com auditoria de dados pessoais e procedimentos de privacidade",
        "fase": "Fase 4 - Produção",
        "responsavel": "RH Manager",
        "prioridade": "Alta",
        "status": "Pendente",
        "data_inicio": "2025-10-16",
        "data_fim": "2025-10-18",
        "estimativa_horas": 8,
        "categoria": "Compliance"
    },
    {
        "nome": "Go-Live Produção",
        "descricao": "Lançamento oficial em produção com todos os usuários e sistemas integrados",
        "fase": "Fase 4 - Produção",
        "responsavel": "CVO",
        "prioridade": "Alta",
        "status": "Pendente",
        "data_inicio": "2025-10-18",
        "data_fim": "2025-10-18",
        "estimativa_horas": 4,
        "categoria": "Lançamento"
    },
    {
        "nome": "Métricas Baseline - Coleta",
        "descricao": "Coletar métricas baseline atuais para comparação pós-implementação",
        "fase": "Fase 1 - Fundação",
        "responsavel": "PM",
        "prioridade": "Média",
        "status": "Em Progresso",
        "data_inicio": "2025-09-09",
        "data_fim": "2025-09-11",
        "estimativa_horas": 8,
        "categoria": "Métricas"
    },
    {
        "nome": "Templates Padrão - Criação",
        "descricao": "Criar templates padrão para projetos, reuniões, relatórios e documentos",
        "fase": "Fase 2 - Integrações",
        "responsavel": "PM",
        "prioridade": "Baixa",
        "status": "Pendente",
        "data_inicio": "2025-09-25",
        "data_fim": "2025-09-27",
        "estimativa_horas": 12,
        "categoria": "Templates"
    },
    {
        "nome": "Integração Google Workspace",
        "descricao": "Integrar Google Workspace com Notion para sincronização de calendários e documentos",
        "fase": "Fase 2 - Integrações",
        "responsavel": "Tech Lead",
        "prioridade": "Média",
        "status": "Pendente",
        "data_inicio": "2025-09-27",
        "data_fim": "2025-10-02",
        "estimativa_horas": 20,
        "categoria": "Integração"
    },
    {
        "nome": "Dashboard Projetos - Implementação",
        "descricao": "Implementar dashboard de acompanhamento de projetos com Gantt e métricas de entrega",
        "fase": "Fase 3 - Otimização",
        "responsavel": "PM",
        "prioridade": "Alta",
        "status": "Pendente",
        "data_inicio": "2025-10-02",
        "data_fim": "2025-10-07",
        "estimativa_horas": 24,
        "categoria": "Dashboard"
    },
    {
        "nome": "Automação Relatórios Mensais",
        "descricao": "Criar automação para geração de relatórios mensais executivos e operacionais",
        "fase": "Fase 3 - Otimização",
        "responsavel": "Tech Lead",
        "prioridade": "Média",
        "status": "Pendente",
        "data_inicio": "2025-10-04",
        "data_fim": "2025-10-07",
        "estimativa_horas": 16,
        "categoria": "Automação"
    },
    {
        "nome": "Treinamento Avançado - Módulo 2",
        "descricao": "Treinamento avançado em automações, integrações e funcionalidades específicas por área",
        "fase": "Fase 4 - Produção",
        "responsavel": "PM",
        "prioridade": "Média",
        "status": "Pendente",
        "data_inicio": "2025-10-09",
        "data_fim": "2025-10-11",
        "estimativa_horas": 16,
        "categoria": "Treinamento"
    },
    {
        "nome": "Otimização Performance",
        "descricao": "Otimizar performance das databases e queries para melhor experiência do usuário",
        "fase": "Fase 4 - Produção",
        "responsavel": "Tech Lead",
        "prioridade": "Baixa",
        "status": "Pendente",
        "data_inicio": "2025-10-11",
        "data_fim": "2025-10-14",
        "estimativa_horas": 12,
        "categoria": "Performance"
    },
    {
        "nome": "Análise ROI - Primeira Medição",
        "descricao": "Primeira análise de ROI após 30 dias de uso com métricas de eficiência e produtividade",
        "fase": "Fase 4 - Produção",
        "responsavel": "CVO",
        "prioridade": "Alta",
        "status": "Pendente",
        "data_inicio": "2025-11-18",
        "data_fim": "2025-11-20",
        "estimativa_horas": 8,
        "categoria": "Análise"
    },
    {
        "nome": "Roadmap Futuro - Planejamento",
        "descricao": "Planejar roadmap de melhorias e novas funcionalidades para os próximos 6 meses",
        "fase": "Fase 4 - Produção",
        "responsavel": "CVO",
        "prioridade": "Baixa",
        "status": "Pendente",
        "data_inicio": "2025-10-16",
        "data_fim": "2025-10-18",
        "estimativa_horas": 12,
        "categoria": "Planejamento"
    },
    {
        "nome": "Validação Usuários - Feedback",
        "descricao": "Coletar feedback detalhado dos usuários e implementar melhorias prioritárias",
        "fase": "Fase 4 - Produção",
        "responsavel": "PM",
        "prioridade": "Alta",
        "status": "Pendente",
        "data_inicio": "2025-10-14",
        "data_fim": "2025-10-16",
        "estimativa_horas": 16,
        "categoria": "Validação"
    }
]

def criar_atividade(atividade):
    """Cria uma atividade na database do Notion"""
    
    payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Nome": {
                "title": [{"text": {"content": atividade["nome"]}}]
            },
            "Descrição": {
                "rich_text": [{"text": {"content": atividade["descricao"]}}]
            },
            "Fase": {
                "select": {"name": atividade["fase"]}
            },
            "Responsável": {
                "select": {"name": atividade["responsavel"]}
            },
            "Prioridade": {
                "select": {"name": atividade["prioridade"]}
            },
            "Status": {
                "select": {"name": atividade["status"]}
            },
            "Data Início": {
                "date": {"start": atividade["data_inicio"]}
            },
            "Data Fim": {
                "date": {"start": atividade["data_fim"]}
            },
            "Estimativa (h)": {
                "number": atividade["estimativa_horas"]
            },
            "Categoria": {
                "select": {"name": atividade["categoria"]}
            }
        }
    }
    
    try:
        response = requests.post(
            "https://api.notion.com/v1/pages",
            headers=HEADERS,
            json=payload
        )
        
        if response.status_code == 200:
            print(f"✅ Atividade criada: {atividade['nome']}")
            return True
        else:
            print(f"❌ Erro ao criar {atividade['nome']}: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Exceção ao criar {atividade['nome']}: {str(e)}")
        return False

def main():
    """Função principal para popular todas as atividades"""
    print("🚀 Iniciando população da base de Atividades do Projeto...")
    print(f"📊 Total de atividades a criar: {len(ATIVIDADES)}")
    
    sucessos = 0
    falhas = 0
    
    for i, atividade in enumerate(ATIVIDADES, 1):
        print(f"\n[{i}/{len(ATIVIDADES)}] Criando: {atividade['nome']}")
        
        if criar_atividade(atividade):
            sucessos += 1
        else:
            falhas += 1
    
    print(f"\n📈 Resumo da Execução:")
    print(f"✅ Sucessos: {sucessos}")
    print(f"❌ Falhas: {falhas}")
    print(f"📊 Taxa de Sucesso: {(sucessos/len(ATIVIDADES)*100):.1f}%")
    
    if sucessos > 0:
        print(f"\n🎉 Base de Atividades populada com {sucessos} registros!")
        print(f"📋 Distribuição por Fase:")
        fases = {}
        for atividade in ATIVIDADES:
            fase = atividade["fase"]
            fases[fase] = fases.get(fase, 0) + 1
        
        for fase, count in fases.items():
            print(f"   • {fase}: {count} atividades")
    else:
        print(f"\n⚠️ Nenhuma atividade foi criada. Verifique o token e permissões.")

if __name__ == "__main__":
    main()
