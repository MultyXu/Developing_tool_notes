#!/usr/bin/env bash
# Automated new-machine setup for AWS instances.
# See auto_setup_script.md for the source spec.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "==> Updating apt package index"
sudo apt update

echo "==> Installing curl, tmux, git, fzf, zsh"
sudo apt install -y curl tmux git fzf zsh

echo "==> Configuring git global user"
git config --global user.name "multyxu"
git config --global user.email "multyxu@gmail.com"

echo "==> Installing oh-my-zsh"
if [ -d "$HOME/.oh-my-zsh" ]; then
  echo "    oh-my-zsh already installed, skipping"
else
  RUNZSH=no CHSH=no sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
fi

ZSH_CUSTOM="${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}"

echo "==> Installing zsh-autosuggestions plugin"
if [ -d "$ZSH_CUSTOM/plugins/zsh-autosuggestions" ]; then
  echo "    zsh-autosuggestions already installed, skipping"
else
  git clone https://github.com/zsh-users/zsh-autosuggestions "$ZSH_CUSTOM/plugins/zsh-autosuggestions"
fi

echo "==> Installing zsh-syntax-highlighting plugin"
if [ -d "$ZSH_CUSTOM/plugins/zsh-syntax-highlighting" ]; then
  echo "    zsh-syntax-highlighting already installed, skipping"
else
  git clone https://github.com/zsh-users/zsh-syntax-highlighting.git "$ZSH_CUSTOM/plugins/zsh-syntax-highlighting"
fi

echo "==> Installing .zshrc config"
if [ -f "$HOME/.zshrc" ]; then
  cp "$HOME/.zshrc" "$HOME/.zshrc.bak.$(date +%Y%m%d%H%M%S)"
fi
cp "$SCRIPT_DIR/resource/.zshrc" "$HOME/.zshrc"

echo "==> Setting zsh as default shell"
if [ "$SHELL" != "$(which zsh)" ]; then
  sudo chsh -s "$(which zsh)" "$USER"
fi

echo "==> Installing amazon-efs-utils (S3/EFS client)"
curl https://amazon-efs-utils.aws.com/efs-utils-installer.sh | sudo sh -s -- --install

echo "==> Installing unzip"
sudo apt install -y unzip

echo "==> Installing AWS CLI v2"
cd "$HOME"
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip -o awscliv2.zip
sudo ./aws/install --update

echo "==> Setup complete! Log out and back in (or run 'zsh') for the shell change to take effect."
