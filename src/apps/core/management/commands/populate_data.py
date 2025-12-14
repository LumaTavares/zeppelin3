from django.core.management.base import BaseCommand
from apps.sth.models import Stage
from apps.questionnaire.models import AdoptedLevel, Statement
from apps.organization.models import Organization, Region, Size, OrganizationType, OrganizationCategory, State
from apps.employee.models import (
    Position, AcademicDegreeCategory, AcademicDegree, AcademicDegreeStatus,
    Employee, EmployeeKnowledge, ExperienceLevel, KnwoledgeLevel,
    SthStageExperienceLevel, SthStageKnwoledgeLevel, Team
)
from apps.continuousstar.models import ContinuousPhase, ContinuousActivity


class Command(BaseCommand):
    help = 'Popula o banco de dados com dados iniciais'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Populando banco de dados com dados iniciais...'))
        self.stdout.write('')

        # ============================================================
        # 1. Criar Estágios STH
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Estágios STH...'))
        stages_data = [
            {
                'id': 1,
                'name': 'Desenvolvimento Ágil',
                'description': 'Primeira etapa da capacidade de desenvolvimento contínuo, focando em práticas ágeis'
            },
            {
                'id': 2,
                'name': 'Integração Contínua',
                'description': 'Segunda etapa com integração contínua de código e automação'
            },
            {
                'id': 3,
                'name': 'Entrega Contínua',
                'description': 'Terceira etapa com entrega contínua de software'
            },
            {
                'id': 4,
                'name': 'P&D como Sistema de Inovação',
                'description': 'Quarta etapa com foco em inovação e pesquisa & desenvolvimento'
            },
        ]

        for stage_data in stages_data:
            stage, created = Stage.objects.get_or_create(
                id=stage_data['id'],
                defaults={
                    'name': stage_data['name'],
                    'description': stage_data['description']
                }
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: {stage.name}')

        # ============================================================
        # 2. Criar Categorias de Organização
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Categorias de Organização...'))
        categories_data = [
            {'id': 1, 'name': 'Startup'},
            {'id': 2, 'name': 'Fábrica de Software'},
            {'id': 3, 'name': 'Empresa com departamento de TI'},
        ]

        for cat_data in categories_data:
            cat, created = OrganizationCategory.objects.get_or_create(
                id=cat_data['id'],
                defaults={'name': cat_data['name']}
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: {cat.name}')

        # ============================================================
        # 3. Criar Tipos de Organização
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Tipos de Organização...'))
        types_data = [
            {'id': 1, 'name': 'Fábrica de Software', 'description': 'Fábrica de Software', 'category_organization_type_id': 2},
            {'id': 2, 'name': 'Startup', 'description': 'Startup', 'category_organization_type_id': 1},
            {'id': 3, 'name': 'Empresa Privada com departamento de TI', 'description': 'Empresa Privada com departamento de TI', 'category_organization_type_id': 3},
            {'id': 4, 'name': 'Empresa Pública com departamento de TI', 'description': 'Empresa Pública com departamento de TI', 'category_organization_type_id': 3},
            {'id': 5, 'name': 'Empresa em que um único produto de software representa o negócio (ex., PicPay, Airbnb, Uber)', 'description': 'Empresa em que um único produto de software representa o negócio (ex., PicPay, Airbnb, Uber)', 'category_organization_type_id': 1},
            {'id': 6, 'name': 'Instituto de P&D com vários departamentos de TI', 'description': 'Instituto de P&D com vários departamentos de TI', 'category_organization_type_id': None},
            {'id': 7, 'name': 'Instituto Federal de Educação', 'description': 'Instituto Federal de Educação', 'category_organization_type_id': None},
            {'id': 8, 'name': 'Empresa Privada com foco em inovação e tranformação digital - business agility', 'description': 'Empresa Privada com foco em inovação e tranformação digital - business agility', 'category_organization_type_id': 2},
            {'id': 9, 'name': 'Empresa de serviços e consultoria de TI (Sustentação de infraestrutura e aplicações, desenvolvimento de projetos e etc)', 'description': 'Empresa de serviços e consultoria de TI (Sustentação de infraestrutura e aplicações, desenvolvimento de projetos e etc)', 'category_organization_type_id': 3},
            {'id': 10, 'name': 'Fundação Pública com departamento de TI', 'description': 'Fundação Pública com departamento de TI', 'category_organization_type_id': 3},
        ]

        for type_data in types_data:
            org_type, created = OrganizationType.objects.get_or_create(
                id=type_data['id'],
                defaults={
                    'name': type_data['name'],
                    'description': type_data['description'],
                    'category_organization_type_id': type_data['category_organization_type_id']
                }
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: {org_type.name}')

        # ============================================================
        # 4. Criar Regiões
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Regiões...'))
        regions_data = [
            {'id': 1, 'name': 'Norte'},
            {'id': 2, 'name': 'Nordeste'},
            {'id': 3, 'name': 'Sudeste'},
            {'id': 4, 'name': 'Sul'},
            {'id': 5, 'name': 'Centro-Oeste'},
        ]

        for region_data in regions_data:
            region, created = Region.objects.get_or_create(
                id=region_data['id'],
                defaults={'name': region_data['name']}
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: {region.name}')

        # ============================================================
        # 5. Criar Estados
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Estados...'))
        states_data = [
            {'id': 1, 'name': 'Acre', 'region_id': 1},
            {'id': 2, 'name': 'Alagoas', 'region_id': 2},
            {'id': 3, 'name': 'Amapá', 'region_id': 1},
            {'id': 4, 'name': 'Amazonas', 'region_id': 1},
            {'id': 5, 'name': 'Bahia', 'region_id': 2},
            {'id': 6, 'name': 'Ceará', 'region_id': 2},
            {'id': 7, 'name': 'Distrito Federal', 'region_id': 5},
            {'id': 8, 'name': 'Espírito Santo', 'region_id': 3},
            {'id': 9, 'name': 'Goiás', 'region_id': 5},
            {'id': 10, 'name': 'Maranhão', 'region_id': 2},
            {'id': 11, 'name': 'Mato Grosso', 'region_id': 5},
            {'id': 12, 'name': 'Mato Grosso do Sul', 'region_id': 5},
            {'id': 13, 'name': 'Minas Gerais', 'region_id': 3},
            {'id': 14, 'name': 'Pará', 'region_id': 1},
            {'id': 15, 'name': 'Paraíba', 'region_id': 2},
            {'id': 16, 'name': 'Paraná', 'region_id': 4},
            {'id': 17, 'name': 'Pernambuco', 'region_id': 2},
            {'id': 18, 'name': 'Piauí', 'region_id': 2},
            {'id': 19, 'name': 'Rio de Janeiro', 'region_id': 3},
            {'id': 20, 'name': 'Rio Grande do Norte', 'region_id': 2},
            {'id': 21, 'name': 'Rio Grande do Sul', 'region_id': 4},
            {'id': 22, 'name': 'Rondônia', 'region_id': 1},
            {'id': 23, 'name': 'Roraima', 'region_id': 1},
            {'id': 24, 'name': 'Santa Catarina', 'region_id': 4},
            {'id': 25, 'name': 'São Paulo', 'region_id': 3},
            {'id': 26, 'name': 'Sergipe', 'region_id': 2},
            {'id': 27, 'name': 'Tocantins', 'region_id': 1},
        ]

        for state_data in states_data:
            state, created = State.objects.get_or_create(
                id=state_data['id'],
                defaults={'name': state_data['name'], 'region_state_id': state_data['region_id']}
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: {state.name}')

        # ============================================================
        # 6. Criar Tamanhos de Organização
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Tamanhos de Organização...'))
        sizes_data = [
            {'id': 1, 'name': '01 a 09 funcionários'},
            {'id': 2, 'name': '10 a 49 funcionários'},
            {'id': 3, 'name': '50 a 99 funcionários'},
            {'id': 4, 'name': 'Mais de 99 funcionários'},
        ]

        for size_data in sizes_data:
            size, created = Size.objects.get_or_create(
                id=size_data['id'],
                defaults={'name': size_data['name']}
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: {size.name}')

        # ============================================================
        # 7. Criar Níveis de Adoção
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Níveis de Adoção...'))
        adoption_levels = [
            {'id': 1, 'name': 'Not Adopted', 'percentage': 0},
            {'id': 2, 'name': 'Partially Adopted', 'percentage': 25},
            {'id': 3, 'name': 'Mostly Adopted', 'percentage': 75},
            {'id': 4, 'name': 'Fully Adopted', 'percentage': 100},
        ]

        for level_data in adoption_levels:
            level, created = AdoptedLevel.objects.get_or_create(
                id=level_data['id'],
                defaults={
                    'name': level_data['name'],
                    'percentage': level_data['percentage']
                }
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: {level.name} ({level.percentage}%)')

        # ============================================================
        # 8. Criar Organizações
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Organizações...'))
        organizations_data = [
            {'id': 547, 'name': 'Org1', 'age': 1, 'location_id': 8, 'organization_size_id': 1, 'organization_type_id': 2},
            {'id': 548, 'name': 'Org2', 'age': 24, 'location_id': 25, 'organization_size_id': 4, 'organization_type_id': 1},
            {'id': 549, 'name': 'Org3', 'age': 4, 'location_id': 8, 'organization_size_id': 2, 'organization_type_id': 2},
            {'id': 550, 'name': 'Org4', 'age': 45, 'location_id': 16, 'organization_size_id': 4, 'organization_type_id': 3},
            {'id': 551, 'name': 'Org5', 'age': 48, 'location_id': 14, 'organization_size_id': 4, 'organization_type_id': 1},
            {'id': 552, 'name': 'Org6', 'age': 5, 'location_id': 8, 'organization_size_id': 2, 'organization_type_id': 2},
            {'id': 553, 'name': 'Org7', 'age': 3, 'location_id': 25, 'organization_size_id': 2, 'organization_type_id': 2},
            {'id': 554, 'name': 'Org8', 'age': 70, 'location_id': 8, 'organization_size_id': 4, 'organization_type_id': 3},
            {'id': 555, 'name': 'Org9', 'age': 3, 'location_id': 8, 'organization_size_id': 1, 'organization_type_id': 2},
            {'id': 556, 'name': 'Org10', 'age': 5, 'location_id': 5, 'organization_size_id': 3, 'organization_type_id': 2},
            {'id': 557, 'name': 'Org11', 'age': 26, 'location_id': 14, 'organization_size_id': 2, 'organization_type_id': 1},
            {'id': 558, 'name': 'Org12', 'age': 47, 'location_id': 19, 'organization_size_id': 4, 'organization_type_id': 4},
            {'id': 559, 'name': 'Org13', 'age': 79, 'location_id': 8, 'organization_size_id': 4, 'organization_type_id': 3},
            {'id': 560, 'name': 'Org14', 'age': 19, 'location_id': 4, 'organization_size_id': 4, 'organization_type_id': 6},
            {'id': 561, 'name': 'Org15', 'age': 112, 'location_id': 8, 'organization_size_id': 4, 'organization_type_id': 7},
            {'id': 562, 'name': 'Org16', 'age': 35, 'location_id': 21, 'organization_size_id': 4, 'organization_type_id': 1},
            {'id': 563, 'name': 'Org17', 'age': 6, 'location_id': 25, 'organization_size_id': 4, 'organization_type_id': 5},
            {'id': 564, 'name': 'Org18', 'age': 87, 'location_id': 8, 'organization_size_id': 4, 'organization_type_id': 3},
            {'id': 565, 'name': 'Org19', 'age': 13, 'location_id': 13, 'organization_size_id': 4, 'organization_type_id': 8},
            {'id': 566, 'name': 'Org20', 'age': 80, 'location_id': 8, 'organization_size_id': 4, 'organization_type_id': 3},
            {'id': 567, 'name': 'Org21', 'age': 6, 'location_id': 5, 'organization_size_id': 1, 'organization_type_id': 2},
            {'id': 568, 'name': 'Org22', 'age': 40, 'location_id': 16, 'organization_size_id': 4, 'organization_type_id': 3},
            {'id': 569, 'name': 'Org23', 'age': 49, 'location_id': 13, 'organization_size_id': 4, 'organization_type_id': 3},
            {'id': 570, 'name': 'Org24', 'age': 21, 'location_id': 8, 'organization_size_id': 2, 'organization_type_id': 5},
            {'id': 571, 'name': 'Org25', 'age': 2, 'location_id': 13, 'organization_size_id': 3, 'organization_type_id': 2},
            {'id': 572, 'name': 'Org26', 'age': 38, 'location_id': 13, 'organization_size_id': 4, 'organization_type_id': 9},
            {'id': 573, 'name': 'Org27', 'age': 56, 'location_id': 10, 'organization_size_id': 3, 'organization_type_id': 10},
            {'id': 574, 'name': 'Org28', 'age': 29, 'location_id': 8, 'organization_size_id': 4, 'organization_type_id': 1},
            {'id': 575, 'name': 'Org29', 'age': 30, 'location_id': 12, 'organization_size_id': 4, 'organization_type_id': 1},
            {'id': 576, 'name': 'Org30', 'age': 6, 'location_id': 12, 'organization_size_id': 4, 'organization_type_id': 3},
        ]

        for org_data in organizations_data:
            org, created = Organization.objects.get_or_create(
                id=org_data['id'],
                defaults={
                    'name': org_data['name'],
                    'age': org_data['age'],
                    'location_id': org_data['location_id'],
                    'organization_size_id': org_data['organization_size_id'],
                    'organization_type_id': org_data['organization_type_id'],
                }
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: {org.name}')

        # ============================================================
        # 9. Criar Posições
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Posições...'))
        positions_data = [
            {'id': 1, 'name': 'Gerente de Projeto'},
            {'id': 2, 'name': 'Scrum Master'},
            {'id': 3, 'name': 'Product Owner'},
            {'id': 4, 'name': 'Desenvolvedor'},
            {'id': 5, 'name': 'Líder Técnico'},
            {'id': 6, 'name': 'Diretor'},
            {'id': 7, 'name': 'Squad Leader'},
            {'id': 8, 'name': 'Gerente Sênior'},
            {'id': 9, 'name': 'SME - Lider Técnico - Gerente de Projetos - Scrum Master'},
            {'id': 10, 'name': 'Professor EBTT'},
            {'id': 11, 'name': 'Gerente de TI'},
            {'id': 12, 'name': 'Coordenador de Engenharia de Software'},
        ]

        for pos_data in positions_data:
            pos, created = Position.objects.get_or_create(
                id=pos_data['id'],
                defaults={'name': pos_data['name']}
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: {pos.name}')

        # ============================================================
        # 10. Criar Categorias de Grau Acadêmico
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Categorias de Grau Acadêmico...'))
        academic_categories_data = [
            {'id': 1, 'name': 'Ensino Superior'},
            {'id': 2, 'name': 'Mestre'},
            {'id': 3, 'name': 'Doutor'},
        ]

        for cat_data in academic_categories_data:
            cat, created = AcademicDegreeCategory.objects.get_or_create(
                id=cat_data['id'],
                defaults={'name': cat_data['name']}
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: {cat.name}')

        # ============================================================
        # 11. Criar Graus Acadêmicos
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Graus Acadêmicos...'))
        academic_degrees_data = [
            {'id': 1, 'name': 'Ensino Médio', 'category_id': None},
            {'id': 2, 'name': 'Ensino Técnico', 'category_id': None},
            {'id': 3, 'name': 'Ensino Superior', 'category_id': 1},
            {'id': 4, 'name': 'Especialização', 'category_id': 1},
            {'id': 5, 'name': 'Mestrado', 'category_id': 2},
            {'id': 6, 'name': 'Doutorado', 'category_id': 3},
        ]

        for deg_data in academic_degrees_data:
            deg, created = AcademicDegree.objects.get_or_create(
                id=deg_data['id'],
                defaults={'name': deg_data['name'], 'academic_degree_category_id': deg_data['category_id']}
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: {deg.name}')

        # ============================================================
        # 12. Criar Status de Grau Acadêmico
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Status de Grau Acadêmico...'))
        degree_status_data = [
            {'id': 1, 'name': 'Incompleto'},
            {'id': 2, 'name': 'Completo'},
        ]

        for status_data in degree_status_data:
            status_obj, created = AcademicDegreeStatus.objects.get_or_create(
                id=status_data['id'],
                defaults={'name': status_data['name']}
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: {status_obj.name}')

        # ============================================================
        # 13. Criar Níveis de Experiência
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Níveis de Experiência...'))
        experience_levels_data = [
            {'id': 1, 'name': 'Nenhuma', 'description': 'Não conhece o tema.', 'value': 0},
            {'id': 2, 'name': 'Baixa', 'description': 'tem experiência de até 1 ano no tema', 'value': 1},
            {'id': 3, 'name': 'Moderada', 'description': 'tem experiência de 1 a 3 anos no tema.', 'value': 3},
            {'id': 4, 'name': 'Alta', 'description': 'tem mais de 3 anos de experiência no tema.', 'value': 5},
        ]

        for exp_data in experience_levels_data:
            exp, created = ExperienceLevel.objects.get_or_create(
                id=exp_data['id'],
                defaults={'name': exp_data['name'], 'description': exp_data['description'], 'value': exp_data['value']}
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: {exp.name}')

        # ============================================================
        # 14. Criar Níveis de Conhecimento
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Níveis de Conhecimento...'))
        knowledge_levels_data = [
            {'id': 1, 'name': 'Nenhum', 'description': 'não conhece o tema', 'value': 1},
            {'id': 2, 'name': 'Baixo', 'description': 'conhecimento pela leitura de materiais ou em curso de curta duração (até 4 horas)', 'value': 0},
            {'id': 3, 'name': 'Moderado', 'description': 'conhecimento por disciplina, projeto de graduação ou Iniciação Científica no tema, ou curso com duração superior a 4 horas;', 'value': 3},
            {'id': 4, 'name': 'Alto', 'description': 'é especialista no tema, tem certificação ou desenvolveu pesquisa de mestrado ou doutorado.', 'value': 5},
        ]

        for know_data in knowledge_levels_data:
            know, created = KnwoledgeLevel.objects.get_or_create(
                id=know_data['id'],
                defaults={'name': know_data['name'], 'description': know_data['description'], 'value': know_data['value']}
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: {know.name}')

        # ============================================================
        # 15. Criar Funcionários
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Funcionários...'))
        employees_data = [
            {'id': 465, 'email': 'org1@org.com', 'organization_id': 547, 'position_id': 6},
            {'id': 466, 'email': 'org2@org.com', 'organization_id': 548, 'position_id': 5},
            {'id': 467, 'email': 'org3@org.com', 'organization_id': 549, 'position_id': 5},
            {'id': 468, 'email': 'org4@org.com', 'organization_id': 550, 'position_id': 7},
            {'id': 469, 'email': 'org5@org.com', 'organization_id': 551, 'position_id': 1},
            {'id': 470, 'email': 'org6@org.com', 'organization_id': 552, 'position_id': 4},
            {'id': 471, 'email': 'org7@org.com', 'organization_id': 553, 'position_id': 6},
            {'id': 472, 'email': 'org8@org.com', 'organization_id': 554, 'position_id': 8},
            {'id': 473, 'email': 'org9@org.com', 'organization_id': 555, 'position_id': 6},
            {'id': 474, 'email': 'org10@org.com', 'organization_id': 556, 'position_id': 6},
            {'id': 475, 'email': 'org11@org.com', 'organization_id': 557, 'position_id': 6},
            {'id': 476, 'email': 'org12@org.com', 'organization_id': 558, 'position_id': 5},
            {'id': 477, 'email': 'org13@org.com', 'organization_id': 559, 'position_id': 9},
            {'id': 478, 'email': 'org14@org.com', 'organization_id': 560, 'position_id': 4},
            {'id': 479, 'email': 'org15@org.com', 'organization_id': 561, 'position_id': 10},
            {'id': 480, 'email': 'org16@org.com', 'organization_id': 562, 'position_id': 3},
            {'id': 481, 'email': 'org17@org.com', 'organization_id': 563, 'position_id': 5},
            {'id': 482, 'email': 'org18@org.com', 'organization_id': 564, 'position_id': 1},
            {'id': 483, 'email': 'org19@org.com', 'organization_id': 565, 'position_id': 6},
            {'id': 484, 'email': 'org20@org.com', 'organization_id': 566, 'position_id': 5},
            {'id': 485, 'email': 'org21@org.com', 'organization_id': 567, 'position_id': 4},
            {'id': 486, 'email': 'org22@org.com', 'organization_id': 568, 'position_id': 11},
            {'id': 487, 'email': 'org23@org.com', 'organization_id': 569, 'position_id': 12},
            {'id': 488, 'email': 'org24@org.com', 'organization_id': 570, 'position_id': 6},
            {'id': 489, 'email': 'org25@org.com', 'organization_id': 571, 'position_id': 1},
            {'id': 490, 'email': 'org26@org.com', 'organization_id': 572, 'position_id': 5},
            {'id': 491, 'email': 'org27@org.com', 'organization_id': 573, 'position_id': 6},
            {'id': 492, 'email': 'org28@org.com', 'organization_id': 574, 'position_id': 2},
            {'id': 493, 'email': 'org29@org.com', 'organization_id': 575, 'position_id': 3},
            {'id': 494, 'email': 'org30@org.com', 'organization_id': 576, 'position_id': 3},
        ]

        for emp_data in employees_data:
            emp, created = Employee.objects.get_or_create(
                id=emp_data['id'],
                defaults={
                    'e_mail': emp_data['email'],
                    'employee_organization_id': emp_data['organization_id'],
                    'employee_position_id': emp_data['position_id'],
                }
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: {emp.e_mail}')

        # ============================================================
        # 16. Criar Conhecimento de Funcionários
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Conhecimento de Funcionários...'))
        knowledge_data = [
            {'id': 492, 'academic_degree_id': 6, 'academic_degree_status_id': 2, 'employee_id': 465},
            {'id': 493, 'academic_degree_id': 3, 'academic_degree_status_id': 2, 'employee_id': 466},
            {'id': 494, 'academic_degree_id': 3, 'academic_degree_status_id': 2, 'employee_id': 467},
            {'id': 495, 'academic_degree_id': 4, 'academic_degree_status_id': 1, 'employee_id': 468},
            {'id': 496, 'academic_degree_id': 4, 'academic_degree_status_id': 2, 'employee_id': 469},
            {'id': 497, 'academic_degree_id': 5, 'academic_degree_status_id': 1, 'employee_id': 470},
            {'id': 498, 'academic_degree_id': 5, 'academic_degree_status_id': 2, 'employee_id': 471},
            {'id': 499, 'academic_degree_id': 5, 'academic_degree_status_id': 2, 'employee_id': 472},
            {'id': 500, 'academic_degree_id': 5, 'academic_degree_status_id': 2, 'employee_id': 473},
            {'id': 501, 'academic_degree_id': 4, 'academic_degree_status_id': 2, 'employee_id': 474},
            {'id': 502, 'academic_degree_id': 6, 'academic_degree_status_id': 1, 'employee_id': 475},
            {'id': 503, 'academic_degree_id': 6, 'academic_degree_status_id': 1, 'employee_id': 476},
            {'id': 504, 'academic_degree_id': 4, 'academic_degree_status_id': 2, 'employee_id': 477},
            {'id': 505, 'academic_degree_id': 5, 'academic_degree_status_id': 2, 'employee_id': 478},
            {'id': 506, 'academic_degree_id': 5, 'academic_degree_status_id': 2, 'employee_id': 479},
            {'id': 507, 'academic_degree_id': 4, 'academic_degree_status_id': 2, 'employee_id': 480},
            {'id': 508, 'academic_degree_id': 4, 'academic_degree_status_id': 1, 'employee_id': 481},
            {'id': 509, 'academic_degree_id': 5, 'academic_degree_status_id': 2, 'employee_id': 482},
            {'id': 510, 'academic_degree_id': 4, 'academic_degree_status_id': 2, 'employee_id': 483},
            {'id': 511, 'academic_degree_id': 5, 'academic_degree_status_id': 1, 'employee_id': 484},
            {'id': 512, 'academic_degree_id': 5, 'academic_degree_status_id': 2, 'employee_id': 485},
            {'id': 513, 'academic_degree_id': 4, 'academic_degree_status_id': 2, 'employee_id': 486},
            {'id': 514, 'academic_degree_id': 5, 'academic_degree_status_id': 1, 'employee_id': 487},
            {'id': 515, 'academic_degree_id': 4, 'academic_degree_status_id': 2, 'employee_id': 488},
            {'id': 516, 'academic_degree_id': 3, 'academic_degree_status_id': 2, 'employee_id': 489},
            {'id': 517, 'academic_degree_id': 5, 'academic_degree_status_id': 2, 'employee_id': 490},
            {'id': 518, 'academic_degree_id': 5, 'academic_degree_status_id': 1, 'employee_id': 491},
            {'id': 519, 'academic_degree_id': 3, 'academic_degree_status_id': 1, 'employee_id': 492},
            {'id': 520, 'academic_degree_id': 3, 'academic_degree_status_id': 1, 'employee_id': 493},
            {'id': 521, 'academic_degree_id': 3, 'academic_degree_status_id': 1, 'employee_id': 494},
        ]

        for know_emp_data in knowledge_data:
            know_emp, created = EmployeeKnowledge.objects.get_or_create(
                id=know_emp_data['id'],
                defaults={
                    'academic_degree_id': know_emp_data['academic_degree_id'],
                    'academic_degree_status_id': know_emp_data['academic_degree_status_id'],
                    'employee_id': know_emp_data['employee_id'],
                }
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: Conhecimento {know_emp.id}')

        # ============================================================
        # 17. Criar Questionnaire Statements
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Questionnaire Statements...'))
        statements_data = [
            {'id': 1, 'code': 'AO.01', 'text': 'Papéis envolvidos no processo de desenvolvimento ágil (e.g., Scrum Master, Product Owner, Desenvolvedor e Tester) existem na organização.', 'sth_stage_id': 1},
            {'id': 2, 'code': 'AO.02', 'text': 'As equipes dos projetos incluem um papel (p.ex., product owner) que é responsável por representar o cliente e participa ativamente nos projetos.', 'sth_stage_id': 1},
            {'id': 3, 'code': 'AO.03', 'text': 'As equipes dos projetos são pequenas (geralmente entre 4 e 8 desenvolvedores), autoorganizadas e multidisciplinares.', 'sth_stage_id': 1},
            {'id': 4, 'code': 'AO.04', 'text': 'Com o intuito de entregar valor para o cliente, os requisitos são definidos e priorizados de acordo com as necessidades do cliente, são periodicamente revisados e mudanças são absorvidas em iterações do processo de desenvolvimento.', 'sth_stage_id': 1},
            {'id': 5, 'code': 'AO.05', 'text': 'O escopo do projeto é definido gradativamente, utilizando-se um Product Backlog (ou artefato equivalente).', 'sth_stage_id': 1},
            {'id': 6, 'code': 'AO.06', 'text': 'Estimativas de esforço são realizadas pela equipe de desenvolvimento (ou em conjunto com ela) considerando-se tarefas curtas para implementar um conjunto de requisitos selecionados (e não o projeto como um todo).', 'sth_stage_id': 1},
            {'id': 7, 'code': 'AO.07', 'text': 'Estimativas de custos são estabelecidas com base nas estimativas de esforço, considerando-se o esforço necessário para implementar um conjunto de requisitos selecionados (e não o projeto como um todo).', 'sth_stage_id': 1},
            {'id': 8, 'code': 'AO.08', 'text': 'O processo de desenvolvimento é ágil, sendo realizado de forma iterativa, em ciclos curtos (p.ex., duas semanas), nos quais requisitos do produto definidos em um Product Backlog (ou artefato equivalente) são selecionados, registrados em um Sprint Backlog (ou artefato equivalente) e desenvolvidos.', 'sth_stage_id': 1},
            {'id': 9, 'code': 'AO.09', 'text': 'Há critérios de aceitação claros para os requisitos do software e eles são usados para avaliar os artefatos produzidos (p.ex., funcionalidades) e definir se estão "prontos".', 'sth_stage_id': 1},
            {'id': 10, 'code': 'AO.10', 'text': 'O cliente recebe novas versões do produto com frequência (após um ou mais ciclos curtos de desenvolvimento), incluindo novas funcionalidades definidas de acordo com as necessidades do cliente.', 'sth_stage_id': 1},
            {'id': 11, 'code': 'AO.11', 'text': 'O processo de desenvolvimento (ágil) está alinhado ao negócio da organização e isso é percebido pela entrega de valor ao cliente e pela sua satisfação com o produto entregue.', 'sth_stage_id': 1},
            {'id': 12, 'code': 'AO.12', 'text': 'Há pelo menos um papel (p.ex., tech lead, analista de qualidade) responsável pela qualidade dos artefatos produzidos e do produto final.', 'sth_stage_id': 1},
            {'id': 13, 'code': 'AO.13', 'text': 'Os stakeholders do projeto (incluindo o cliente) são estimulados a refletir sobre seu sobre seu papel e suas responsabilidades no projeto.', 'sth_stage_id': 1},
            {'id': 14, 'code': 'AO.14', 'text': 'A equipe do projeto possui autonomia para tomar decisões técnicas no projeto.', 'sth_stage_id': 1},
            {'id': 15, 'code': 'AO.15', 'text': 'Frequentemente (p.ex.., diariamente, a cada dois ou três dias) a equipe se reúne e reflete sobre o progresso do desenvolvimento no âmbito do que foi definido para o time-box corrente e ajusta as tarefas se necessário (p.ex., em daily ou stand up meetings).', 'sth_stage_id': 1},
            {'id': 16, 'code': 'AO.16', 'text': 'A equipe se reúne com frequência ao longo do projeto para discutir sobre melhorias no produto, no processo ou nas ferramentas usadas (p.ex., em reunião de retrospectiva).', 'sth_stage_id': 1},
            {'id': 17, 'code': 'AO.17', 'text': 'A equipe se reúne com frequência ao longo do projeto para discutir sobre melhorias nas competências dos membros da equipe (p.ex., em reunião de retrospectiva).', 'sth_stage_id': 1},
            {'id': 18, 'code': 'AO.18', 'text': 'O processo de desenvolvimento (ágil) é avaliado e melhorado continuamente.', 'sth_stage_id': 1},
            {'id': 19, 'code': 'AO.19', 'text': 'Boas práticas de programação são adotadas (p.ex., código coletivo, codificação padronizada, programação em pares, revisão de código).', 'sth_stage_id': 1},
            {'id': 20, 'code': 'AO.20', 'text': 'Boas práticas de testes (p.ex., teste automatizado, desenvolvimento orientado a testes) são adotadas.', 'sth_stage_id': 1},
            {'id': 21, 'code': 'AO.21', 'text': 'Dados são coletados para métricas que permitem avaliar aspectos da qualidade dos artefatos produzidos e do produto (p.ex., complexidade ciclomática, quantidade de code smells).', 'sth_stage_id': 1},
            {'id': 22, 'code': 'AO.22', 'text': 'Dados são coletados para métricas que permitem avaliar aspectos de desempenho do processo de desenvolvimento ágil (p.ex., work in progress, velocidade).', 'sth_stage_id': 1},
            {'id': 23, 'code': 'AO.23', 'text': 'Dados produzidos ao longo do processo de desenvolvimento (p.ex., data de início das tarefas, data de conclusão das tarefas, pontos de história das tarefas) são armazenados em um (ou mais) repositório de dados.', 'sth_stage_id': 1},
            {'id': 24, 'code': 'AO.24', 'text': 'Dados armazenados no(s) repositório(s) de dados são usados para melhorar o produto e o processo de desenvolvimento ágil.', 'sth_stage_id': 1},
            {'id': 25, 'code': 'AO.25', 'text': 'Decisões nos projetos são tomadas com base em dados presentes no(s) repositório(s) de dados.', 'sth_stage_id': 1},
            {'id': 26, 'code': 'AO.26', 'text': 'São realizadas ações para compartilhar conhecimento relevante ao desenvolvimento ágil (p.ex., palestras internas, tutoriais, repositórios de conhecimento, implementação de guilds).', 'sth_stage_id': 1},
            {'id': 27, 'code': 'CI.01', 'text': 'A arquitetura do software é modular de forma a permitir a realização de testes automatizados.', 'sth_stage_id': 2},
            {'id': 28, 'code': 'CI.02', 'text': 'A arquitetura do software é modular de forma a permitir a realização de builds automatizados.', 'sth_stage_id': 2},
            {'id': 29, 'code': 'CI.03', 'text': 'O código é integrado constantemente e automaticamente.', 'sth_stage_id': 2},
            {'id': 30, 'code': 'CI.04', 'text': 'Testes são executados automaticamente, periodicamente (p.ex., sempre que código novo é integrado), em um ambiente de teste, para verificar a qualidade do código (p.ex., cobertura, corretude).', 'sth_stage_id': 2},
            {'id': 31, 'code': 'CI.05', 'text': 'Testes automatizados são utilizados para avaliar se o software implementado atende os requisitos estabelecidos.', 'sth_stage_id': 2},
            {'id': 32, 'code': 'CI.06', 'text': 'Builds ocorrem frequentemente e automaticamente.', 'sth_stage_id': 2},
            {'id': 33, 'code': 'CI.07', 'text': 'Builds são cancelados caso um ou mais testes falhem.', 'sth_stage_id': 2},
            {'id': 34, 'code': 'CI.08', 'text': 'Há controle de versões dos artefatos de software (p.ex., código, teste, scripts etc.) em um repositório.', 'sth_stage_id': 2},
            {'id': 35, 'code': 'CI.09', 'text': 'Boas práticas de check in são aplicadas no trunk de desenvolvimento (p.ex., uso de ferramentas como GitFlow e Toogle Feature).', 'sth_stage_id': 2},
            {'id': 36, 'code': 'CI.10', 'text': 'Há práticas que permitem que organizações ou pessoas externas ao projeto atuem na implementação do produto (i.e., produzam e integrem código ao produto sendo desenvolvido).', 'sth_stage_id': 2},
            {'id': 37, 'code': 'CI.11', 'text': 'Dados são coletados para métricas que permitem avaliar o processo de integração contínua (p.ex., quantidade de builds cancelados, quantidade de integrações de código realizadas).', 'sth_stage_id': 2},
            {'id': 38, 'code': 'CI.12', 'text': 'Dados produzidos nos ambientes de integração contínua (p.ex., data das builds, quantidade de testes executados e percentual de cobertura)  são armazenados em um (ou mais) repositório de dados.', 'sth_stage_id': 2},
            {'id': 39, 'code': 'CI.13', 'text': 'O processo de integração contínua (incluindo a realização de testes automatizados) é avaliado e melhorado continuamente.', 'sth_stage_id': 2},
            {'id': 40, 'code': 'CI.14', 'text': 'Dados armazenados no(s) repositório(s) de dados são usados para melhorar o produto e o processo de integração contínua.', 'sth_stage_id': 2},
            {'id': 41, 'code': 'CI.15', 'text': 'São realizadas ações para compartilhar conhecimento relacionado a integração contínua (p.ex., palestras internas, tutoriais, repositórios de conhecimento, implementação de guilds).', 'sth_stage_id': 2},
            {'id': 42, 'code': 'CD.01', 'text': 'Os principais clientes/consumidores são identificados e participam do processo de desenvolvimento, influenciando nas funcionalidades que serão produzidas e entregues.', 'sth_stage_id': 3},
            {'id': 43, 'code': 'CD.02', 'text': 'Há um fluxo de informação claro entre Desenvolvimento e Operação, permitindo que novas funcionalidades desenvolvidas entrem em operação automaticamente.', 'sth_stage_id': 3},
            {'id': 44, 'code': 'CD.03', 'text': 'A entrega de novas funcionalidades é realizada automaticamente e por releases.', 'sth_stage_id': 3},
            {'id': 45, 'code': 'CD.04', 'text': 'Há um fluxo de informação claro entre Operação e Negócio, permitindo que novas necessidades dos clientes/consumidores e oportunidades de negócio sejam identificadas a partir da entrega de novas funcionalidades.', 'sth_stage_id': 3},
            {'id': 46, 'code': 'CD.05', 'text': 'A arquitetura do software permite realizar entrega (deploy) de funcionalidades de forma independente.', 'sth_stage_id': 3},
            {'id': 47, 'code': 'CD.06', 'text': 'Clientes/consumidores recebem novas funcionalidades com frequência, inclusive, em ciclos mais curtos do que o time-box que costuma ser estabelecido no processo de desenvolvimento.', 'sth_stage_id': 3},
            {'id': 48, 'code': 'CD.07', 'text': 'Os clientes podem realizar testes no produto assim que é feita a entrega (deploy) de novas funcionalidades.', 'sth_stage_id': 3},
            {'id': 49, 'code': 'CD.08', 'text': 'O modelo de negócio da organização é constantemente avaliado e revisto (quando necessário) com base em informações dos clientes/consumidores.', 'sth_stage_id': 3},
            {'id': 50, 'code': 'CD.09', 'text': 'Estratégias de marketing são constantemente avaliadas e revistas (quando necessário) com base em informações dos lead customers (clientes/consumidores mais relevantes para a organização).', 'sth_stage_id': 3},
            {'id': 51, 'code': 'CD.10', 'text': 'Estratégias de venda são constantemente avaliadas e revistas (quando necessário) com base em informações dos lead customers (clientes/consumidores mais relevantes para a organização).', 'sth_stage_id': 3},
            {'id': 52, 'code': 'CD.11', 'text': 'Alinhamento entre o desenvolvimento dos produtos e o negócio da organização é mantido através de verificações contínuas, em ciclos curtos.', 'sth_stage_id': 3},
            {'id': 53, 'code': 'CD.12', 'text': 'Alinhamento entre o desenvolvimento dos produtos e o negócio da organização é mantido através de verificações contínuas, em ciclos curtos e baseando-se em dados.', 'sth_stage_id': 3},
            {'id': 54, 'code': 'CD.13', 'text': 'Dados são coletados para métricas que permitem avaliar o processo de entrega contínua  (p.ex., quantidade de releases, densidade de defeitos nas releases).', 'sth_stage_id': 3},
            {'id': 55, 'code': 'CD.14', 'text': 'Dados produzidos nos ambientes de entrega contínua (p.ex., data das releases e versão do software entregue)  são armazenados em um (ou mais) repositório de dados.', 'sth_stage_id': 3},
            {'id': 56, 'code': 'CD.15', 'text': 'O  processo de entrega contínua é avaliado e melhorado continuamente.', 'sth_stage_id': 3},
            {'id': 57, 'code': 'CD.16', 'text': 'Dados armazenados no(s) repositório(s) de dados são usados para melhorar o produto e o processo de entrega contínua.', 'sth_stage_id': 3},
            {'id': 58, 'code': 'CD.17', 'text': 'São realizadas ações para compartilhar conhecimento relacionado a entrega contínua (e.g., palestras internas, tutoriais, repositórios de conhecimento, implementação de guilds).', 'sth_stage_id': 3},
            {'id': 59, 'code': 'IS.01', 'text': 'Feedbacks (dados e opiniões) dos clientes/consumidores são capturados contínua e automaticamente e armazenados em um (ou mais) repositório de dados de clientes/consumidores.', 'sth_stage_id': 4},
            {'id': 60, 'code': 'IS.02', 'text': 'Feedbacks (dados e opiniões) dos clientes/consumidores (capturados contínua e automaticamente) são utilizados para melhorar os produtos (melhorar funcionalidades existentes e identificar novas).', 'sth_stage_id': 4},
            {'id': 61, 'code': 'IS.03', 'text': 'A organização identifica novas oportunidades de negócio com base nos feedbacks capturados automaticamente dos clientes/consumidores.', 'sth_stage_id': 4},
            {'id': 62, 'code': 'IS.04', 'text': 'Feedbacks (dados e opiniões) dos clientes/consumidores (capturados contínua e automaticamente) são usados para experimentação e inovação.', 'sth_stage_id': 4},
            {'id': 63, 'code': 'IS.05', 'text': 'Experimentos (p.ex., testes A/B) são realizados com os clientes/consumidores para melhorar os produtos.', 'sth_stage_id': 4},
            {'id': 64, 'code': 'IS.06', 'text': 'São adotadas tecnologias (p.ex.., tecnologias de nuvem) que permitem potencializar a experimentação.', 'sth_stage_id': 4},
            {'id': 65, 'code': 'IS.07', 'text': 'A organização continuamente experimenta novas tecnologias e metodologias.', 'sth_stage_id': 4},
            {'id': 66, 'code': 'IS.08', 'text': 'Há um fluxo de informação claro entre o nível estratégico e a área de desenvolvimento da organização, permitindo que dados dos clientes/consumidores (capturados contínua e automaticamente) sejam utilizados de forma alinhada na tomada de decisões técnicas e de negócio.', 'sth_stage_id': 4},
            {'id': 67, 'code': 'IS.09', 'text': 'Dados do repositório de dados dos clientes/consumidores são usados na tomada de decisão pela área de desenvolvimento de software.', 'sth_stage_id': 4},
            {'id': 68, 'code': 'IS.10', 'text': 'Dados do(s) repositório(a) de dados dos clientes/consumidores são usados na tomada de decisão pela área de negócios.', 'sth_stage_id': 4},
            {'id': 69, 'code': 'IS.11', 'text': 'Alinhamento entre o desenvolvimento dos produtos e o negócio da organização é mantido através de verificações contínuas, em ciclos curtos e baseando-se em dados do(s) repositório(a) de dados dos clientes/consumidores.', 'sth_stage_id': 4},
            {'id': 70, 'code': 'IS.12', 'text': 'O processo de experimentação contínua é avaliado e melhorado continuamente.', 'sth_stage_id': 4},
            {'id': 71, 'code': 'IS.13', 'text': 'São realizadas ações para compartilhar conhecimento relacionado a experimentação  contínua (e.g., palestras internas, tutoriais, repositórios de conhecimento, implementação de guilds).', 'sth_stage_id': 4},
        ]

        for stmt_data in statements_data:
            stmt, created = Statement.objects.get_or_create(
                id=stmt_data['id'],
                defaults={
                    'code': stmt_data['code'],
                    'text': stmt_data['text'],
                    'sth_stage_id': stmt_data['sth_stage_id'],
                }
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: {stmt.code}')

        # ============================================================
        # 18. Criar Questionnaire Answers
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Questionnaire Answers...'))
        from apps.questionnaire.models import Answer
        
        # Criar respostas para cada organização e cada statement
        answer_id = 11881
        for org_id in range(547, 577):  # 30 organizations (547-576)
            for stmt_id in range(1, 72):  # 71 statements
                # Variar os adopted_level_id entre 1-4 para cada statement
                adopted_level_id = ((stmt_id + org_id) % 4) + 1
                
                answer, created = Answer.objects.get_or_create(
                    id=answer_id,
                    defaults={
                        'statement_answer_id': stmt_id,
                        'adopted_level_answer_id': adopted_level_id,
                        'organization_answer_id': org_id,
                        'comment_answer': ''
                    }
                )
                answer_id += 1
                if answer_id % 100 == 0:
                    self.stdout.write(f'  ✓ Criadas {answer_id - 11881} respostas...')

        # ============================================================
        # 19. Criar Feedback Questionnaires
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Feedback Questionnaires...'))
        from apps.questionnaire.models import FeedbackQuestionnaire
        from datetime import datetime, timedelta
        
        feedback_questionnaires_data = [
            {'id': 1, 'feedback_date': datetime(2023, 1, 15)},
            {'id': 2, 'feedback_date': datetime(2023, 2, 20)},
            {'id': 3, 'feedback_date': datetime(2023, 3, 10)},
            {'id': 4, 'feedback_date': datetime(2023, 4, 25)},
            {'id': 5, 'feedback_date': datetime(2023, 5, 15)},
        ]
        
        for fq_data in feedback_questionnaires_data:
            fq, created = FeedbackQuestionnaire.objects.get_or_create(
                id=fq_data['id'],
                defaults={'feedback_date': fq_data['feedback_date']}
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: FeedbackQuestionnaire {fq.id}')

        # ============================================================
        # 20. Criar Questionnaires
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Questionnaires...'))
        from apps.questionnaire.models import Questionnaire
        
        questionnaires_data = [
            {'id': 1, 'employee_id': 465, 'applied_date': datetime(2023, 1, 10)},
            {'id': 2, 'employee_id': 466, 'applied_date': datetime(2023, 2, 15)},
            {'id': 3, 'employee_id': 467, 'applied_date': datetime(2023, 3, 20)},
            {'id': 4, 'employee_id': 468, 'applied_date': datetime(2023, 4, 10)},
            {'id': 5, 'employee_id': 469, 'applied_date': datetime(2023, 5, 15)},
        ]
        
        for q_data in questionnaires_data:
            q, created = Questionnaire.objects.get_or_create(
                id=q_data['id'],
                defaults={
                    'employee_questionnaire_id': q_data['employee_id'],
                    'applied_date': q_data['applied_date'],
                    'document': f'questionnaire_{q_data["id"]}.pdf'
                }
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: Questionnaire {q.id}')

        # ============================================================
        # 21. Criar Questionnaire Excels
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Questionnaire Excels...'))
        from apps.questionnaire.models import QuestionnaireExcel
        
        excel_questionnaires_data = [
            {'id': 6, 'employee_id': 470, 'feedback_id': 1, 'applied_date': datetime(2023, 1, 15)},
            {'id': 7, 'employee_id': 471, 'feedback_id': 2, 'applied_date': datetime(2023, 2, 20)},
            {'id': 8, 'employee_id': 472, 'feedback_id': 3, 'applied_date': datetime(2023, 3, 15)},
            {'id': 9, 'employee_id': 473, 'feedback_id': 4, 'applied_date': datetime(2023, 4, 20)},
            {'id': 10, 'employee_id': 474, 'feedback_id': 5, 'applied_date': datetime(2023, 5, 20)},
        ]
        
        for excel_data in excel_questionnaires_data:
            excel_q, created = QuestionnaireExcel.objects.get_or_create(
                id=excel_data['id'],
                defaults={
                    'employee_questionnaire_id': excel_data['employee_id'],
                    'feedback_questionnaire_id': excel_data['feedback_id'],
                    'applied_date': excel_data['applied_date'],
                    'document': f'questionnaire_excel_{excel_data["id"]}.xlsx'
                }
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: QuestionnaireExcel {excel_q.id}')

        # ============================================================
        # 22. Criar Continuous Phases
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Continuous Phases...'))
        phases_data = [
            {'id': 1, 'name': 'Planejamento', 'description': 'Fase de planejamento das atividades contínuas'},
            {'id': 2, 'name': 'Implementação', 'description': 'Fase de implementação das atividades contínuas'},
            {'id': 3, 'name': 'Monitoramento', 'description': 'Fase de monitoramento e avaliação contínua'},
            {'id': 4, 'name': 'Melhoria', 'description': 'Fase de melhoria contínua baseada em feedbacks'},
        ]
        
        for phase_data in phases_data:
            phase, created = ContinuousPhase.objects.get_or_create(
                id=phase_data['id'],
                defaults={
                    'name': phase_data['name'],
                    'description': phase_data['description']
                }
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: {phase.name}')

        # ============================================================
        # 23. Criar Continuous Activities
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Continuous Activities...'))
        activities_data = [
            {'id': 1, 'name': 'Reuniões de planejamento', 'description': 'Reuniões periódicas para planejamento de atividades', 'phase_id': 1},
            {'id': 2, 'name': 'Definição de objetivos', 'description': 'Definição clara dos objetivos das atividades contínuas', 'phase_id': 1},
            {'id': 3, 'name': 'Desenvolvimento de soluções', 'description': 'Desenvolvimento prático das soluções planejadas', 'phase_id': 2},
            {'id': 4, 'name': 'Integração de mudanças', 'description': 'Integração das mudanças e melhorias implementadas', 'phase_id': 2},
            {'id': 5, 'name': 'Coleta de métricas', 'description': 'Coleta contínua de métricas e indicadores', 'phase_id': 3},
            {'id': 6, 'name': 'Análise de resultados', 'description': 'Análise dos resultados obtidos nas atividades', 'phase_id': 3},
            {'id': 7, 'name': 'Identificação de melhorias', 'description': 'Identificação de oportunidades de melhoria', 'phase_id': 4},
            {'id': 8, 'name': 'Implementação de melhorias', 'description': 'Implementação das melhorias identificadas', 'phase_id': 4},
        ]
        
        for activity_data in activities_data:
            activity, created = ContinuousActivity.objects.get_or_create(
                id=activity_data['id'],
                defaults={
                    'name': activity_data['name'],
                    'description': activity_data['description'],
                    'continuous_phase_id': activity_data['phase_id']
                }
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: {activity.name}')

        # ============================================================
        # 24. Criar STH Stage Experience Levels
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando STH Stage Experience Levels...'))
        sth_exp_level_id = 1
        for stage_id in range(1, 5):  # 4 STH stages
            for emp_id in range(465, 495):  # 30 employees
                exp_level_id = ((stage_id + emp_id) % 4) + 1  # Vary between 1-4
                
                sth_exp, created = SthStageExperienceLevel.objects.get_or_create(
                    id=sth_exp_level_id,
                    defaults={
                        'stage_experience_level_id': stage_id,
                        'experience_level_id': exp_level_id,
                        'employee_experience_level_id': emp_id
                    }
                )
                sth_exp_level_id += 1
                if sth_exp_level_id % 50 == 0:
                    self.stdout.write(f'  ✓ Criados {sth_exp_level_id - 1} STH Stage Experience Levels...')

        # ============================================================
        # 25. Criar STH Stage Knowledge Levels
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando STH Stage Knowledge Levels...'))
        sth_know_level_id = 1
        for stage_id in range(1, 5):  # 4 STH stages
            for emp_id in range(465, 495):  # 30 employees
                know_level_id = ((stage_id + emp_id) % 4) + 1  # Vary between 1-4
                
                sth_know, created = SthStageKnwoledgeLevel.objects.get_or_create(
                    id=sth_know_level_id,
                    defaults={
                        'stage_id': stage_id,
                        'Knwoledge_level_id': know_level_id,
                        'employee_id': emp_id
                    }
                )
                sth_know_level_id += 1
                if sth_know_level_id % 50 == 0:
                    self.stdout.write(f'  ✓ Criados {sth_know_level_id - 1} STH Stage Knowledge Levels...')

        # ============================================================
        # 26. Criar Teams
        # ============================================================
        self.stdout.write(self.style.WARNING('➤ Criando Teams...'))
        teams_data = [
            {'id': 1, 'name': 'Team Backend', 'organization_id': 547, 'responsible_id': 465},
            {'id': 2, 'name': 'Team Frontend', 'organization_id': 548, 'responsible_id': 466},
            {'id': 3, 'name': 'Team DevOps', 'organization_id': 549, 'responsible_id': 467},
            {'id': 4, 'name': 'Team QA', 'organization_id': 550, 'responsible_id': 468},
            {'id': 5, 'name': 'Team Data Science', 'organization_id': 551, 'responsible_id': 469},
        ]
        
        for team_data in teams_data:
            team, created = Team.objects.get_or_create(
                id=team_data['id'],
                defaults={
                    'name': team_data['name'],
                    'organization_team_id': team_data['organization_id'],
                    'responsible_id': team_data['responsible_id']
                }
            )
            status = '✓ Criado' if created else '→ Existente'
            self.stdout.write(f'  {status}: {team.name}')

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('✓ Banco de dados populado com sucesso!'))
