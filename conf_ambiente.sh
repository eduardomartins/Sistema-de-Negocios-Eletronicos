# !/bin/bash

echo "Iniciando ambiente..."
virtualenv -p python3 env
echo "Ativando ambiente..."
source env/bin/activate
echo "Instalando dependências..."
pip install -r req.txt


