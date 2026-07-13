# Goal 
Write a shell script that automatically perform some custom system setups, the new script will be especially for setting up a system for AWS. 

# Things to setup 
sudo apt update

## curl 
sudo apt install curl 

## tmux 
install tmux: sudo apt install tmux

## git and config  
sudo apt install git -y 
config global user and email to multyxu and multyxu@gmail.com

## oh-my-zsh
We we should install oh-my-zsh and use zsh as the default shell: sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)". 

And we will use the ./resource/.zshrc as the zsh config. In there there are several plugins we need to install 
1. fzf: sudo apt install fzf
2. zsh-autosuggestions: git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
3. zsh-syntax-highlighting: git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

## S3 file client
curl https://amazon-efs-utils.aws.com/efs-utils-installer.sh | sudo sh -s -- --install

# You task 
create a shell script under this directory that we can run directly to setup all above packages. 
