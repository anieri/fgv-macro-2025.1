#!/bin/bash

# Navigate to the report directory to ensure relative image paths are resolved correctly
cd "$(dirname "$0")"

echo "Gerando Relatório de Impactos Econômicos (DOCX)..."

# Use pandoc to convert Markdown to DOCX
# --toc: Include table of contents
# --number-sections: Include section numbering
# --highlight-style: For any code blocks (though unlikely in this report)
pandoc Relatorio_Impactos_Economicos.md \
    -o ../Relatorio_Impactos_Economicos.docx \
    --toc \
    --number-sections \
    --highlight-style pygments

if [ $? -eq 0 ]; then
    echo "Sucesso! O DOCX foi gerado na raiz do projeto: Relatorio_Impactos_Economicos.docx"
else
    echo "Erro ao gerar o DOCX."
    exit 1
fi
