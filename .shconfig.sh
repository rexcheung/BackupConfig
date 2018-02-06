# git auto-complete
if [ -f ~/.git-completion.bash ]; then
  . ~/.git-completion.bash
fi


alias ls='ls -G'
alias ll='ls -Glh'
alias la='ls -Ga'
alias cls='clear'
alias g.b='git branch'
alias g.c='git checkout'
alias g.s='git status'
alias g.pull='git pull'
alias g.push='git add --all && git commit -a && git push'

alias go.work='cd ~/apps/android/workspace'
