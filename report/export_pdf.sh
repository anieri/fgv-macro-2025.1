#!/bin/bash

# Navigate to the report directory to ensure relative image paths are resolved correctly
# The images in the Markdown are referenced as ../plots/pt-br/...
cd "$(dirname "$0")"

echo "Gerando Relatório de Impactos Econômicos (PDF)..."

# Use pandoc to convert Markdown to PDF
# --pdf-engine=xelatex is preferred for Portuguese characters and better font support if available
# but we'll fall back to default if needed. 
# We'll use the default engine first as requested.

pandoc Relatorio_Impactos_Economicos.md \
    -o ../Relatorio_Impactos_Economicos.pdf \
    --variable geometry:margin=1in \
    --toc \
    --number-sections \
    --highlight-style pygments

if [ $? -eq 0 ]; then
    echo "Sucesso! O PDF foi gerado na raiz do projeto: Relatorio_Impactos_Economicos.pdf"
else
    echo "Erro ao gerar o PDF. Verifique se o LaTeX (pdflatex ou xelatex) está instalado corretamente."
    exit 1
fi
