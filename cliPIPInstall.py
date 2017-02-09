sudo -H pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 sudo -H pip install -U

#pip list --outdated --format=freeze

#http://stackoverflow.com/questions/2720014/upgrading-all-packages-with-pip
