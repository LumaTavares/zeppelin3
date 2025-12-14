#!/bin/bash
# Script para popular o banco de dados com dados iniciais

echo "Populando banco de dados com dados iniciais..."

# Você pode usar este script para carregar fixtures ou dados iniciais
# Exemplo: python manage.py loaddata fixture_file.json

# Ou você pode criar os dados programaticamente via Django shell
python manage.py shell << EOF
import django
django.setup()

from sth.models import Stage
from continuousstar.models import ContinuousPhase, ContinuousActivity
from cseframework.models import Process
from practitioners_eye.models import Dimension, Element
from questionnaire.models import AdoptedLevel, Statement
from employee.models import AcademicDegreeCategory, Position, ExperienceLevel, KnowledgeLevel
from organization.models import Organization
from core.models import User

# Criar Estágios STH
stages_data = [
    {'name': 'Initial', 'description': 'Initial stage'},
    {'name': 'Managed', 'description': 'Managed stage'},
    {'name': 'Defined', 'description': 'Defined stage'},
    {'name': 'Quantitatively Managed', 'description': 'Quantitatively Managed stage'},
    {'name': 'Optimizing', 'description': 'Optimizing stage'},
]

for stage_data in stages_data:
    Stage.objects.get_or_create(**stage_data)
    print(f"✓ Criado/Atualizado estágio: {stage_data['name']}")

# Criar Fases Contínuas
continuous_phases = [
    {'name': 'Planning', 'description': 'Planning phase'},
    {'name': 'Development', 'description': 'Development phase'},
    {'name': 'Testing', 'description': 'Testing phase'},
    {'name': 'Deployment', 'description': 'Deployment phase'},
]

for phase_data in continuous_phases:
    ContinuousPhase.objects.get_or_create(**phase_data)
    print(f"✓ Criada/Atualizada fase contínua: {phase_data['name']}")

# Criar Níveis de Adoção
adoption_levels = [
    {'name': 'Not Adopted', 'percentage': 0},
    {'name': 'Partially Adopted', 'percentage': 25},
    {'name': 'Mostly Adopted', 'percentage': 75},
    {'name': 'Fully Adopted', 'percentage': 100},
]

for level_data in adoption_levels:
    AdoptedLevel.objects.get_or_create(**level_data)
    print(f"✓ Criado/Atualizado nível de adoção: {level_data['name']}")

# Criar Organização Padrão
org, created = Organization.objects.get_or_create(
    name='Default Organization',
    defaults={'description': 'Default organization for testing'}
)
if created:
    print(f"✓ Criada organização: {org.name}")
else:
    print(f"✓ Organização existente: {org.name}")

print("\n✓ Banco de dados populado com sucesso!")
EOF

echo ""
echo "Banco de dados pronto com dados iniciais!"
