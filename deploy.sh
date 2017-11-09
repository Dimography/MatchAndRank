#!/bin/bash

# dev
# https://slack.com/oauth/authorize?&client_id=209739519776.216051158775&scope=bot,commands,chat:write:bot
# prod
# https://slack.com/oauth/authorize?&client_id=209739519776.212249095591&scope=incoming-webhook,commands,stars:read,bot

# rsync --include *.js  --exclude 'node_modules' -vr --exclude 'cert' --exclude '.git' .  root@ssh.lmsbothq.com:/srv/ideabot
rsync --include *.js --include *.py --include csv  --exclude 'node_modules' -vr --exclude 'cert' --exclude 'logs'  --exclude '.git' .  root@ssh.lmsbothq.com:/srv/stanbot --delete-after
