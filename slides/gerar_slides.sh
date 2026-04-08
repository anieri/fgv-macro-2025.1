#!/bin/bash

# Script para gerar slides usando marp-cli
# Requer Node.js instalado (npx)

echo "Gerando slides..."

# PDF
npx @marp-team/marp-cli@latest apresentacao_coreia.md --allow-local-files -o apresentacao_coreia.pdf

# PPTX
npx @marp-team/marp-cli@latest apresentacao_coreia.md --allow-local-files -o apresentacao_coreia.pptx

echo "Concluído! Arquivos gerados em slides/"
