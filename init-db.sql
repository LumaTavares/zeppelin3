-- ============================================================
-- Script de inicialização do banco de dados Zeppelin
-- ============================================================
-- Este arquivo é executado automaticamente pelo PostgreSQL
-- quando o container é iniciado pela primeira vez

-- Habilita extensões necessárias
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Cria o schema padrão se não existir
CREATE SCHEMA IF NOT EXISTS public;

-- Define o proprietário do schema
ALTER SCHEMA public OWNER TO zeppelin;

-- Concede permissões ao usuário zeppelin
GRANT ALL PRIVILEGES ON SCHEMA public TO zeppelin;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO zeppelin;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO zeppelin;

-- ============================================================
-- Observação importante:
-- As tabelas reais serão criadas pelas migrações do Django
-- quando a aplicação iniciar. Este arquivo apenas prepara
-- o banco de dados para recebê-las.
-- ============================================================
