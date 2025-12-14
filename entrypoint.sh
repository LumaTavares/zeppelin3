#!/bin/bash
set -e

echo "==============================================="
echo "Iniciando aplica??o Zeppelin"
echo "==============================================="

echo ""
echo " Aguardando PostgreSQL estar pronto..."
while ! nc -z db_zeppelin 5432; do
  echo "  PostgreSQL ainda n?o est? pronto... aguardando..."
  sleep 2
done
echo " PostgreSQL est? pronto!"

echo ""
echo " Executando makemigrations..."
python manage.py makemigrations --noinput

echo ""
echo " Executando migrate..."
python manage.py migrate --noinput

echo ""
echo " Coletando arquivos est?ticos..."
python manage.py collectstatic --noinput --no-post-process

echo ""
echo " Populando banco de dados com dados iniciais..."
python manage.py populate_data

echo ""
echo " Banco de dados pronto!"
echo "==============================================="
echo "Iniciando aplica??o..."
echo "==============================================="
echo ""

exec "$@"
