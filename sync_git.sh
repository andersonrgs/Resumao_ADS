#!/usr/bin/env bash
# Script para sincronizar alterações com o repositório GitHub Resumao_ADS
# Uso: ./sync_git.sh "mensagem do commit"

GIT_DIR="/home/anderson/.git_Resumao_ADS"
WORK_TREE="$(pwd)"

MSG="${1:-Atualização dos materiais de estudo ADS}"

echo "📦 Sincronizando alterações com o GitHub..."
git --git-dir="$GIT_DIR" --work-tree="$WORK_TREE" add .
git --git-dir="$GIT_DIR" --work-tree="$WORK_TREE" commit -m "$MSG"
git --git-dir="$GIT_DIR" --work-tree="$WORK_TREE" push origin main

echo "✅ Sincronização concluída com sucesso!"
