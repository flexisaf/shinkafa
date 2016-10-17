#!/bin/bash -e

function usage(){
    echo "Usage: $0 <staging|production>"
}



HEROKU_APP='flexisaf'
ENV_MODE='prod'


function set_heroku_environment_to_prod() {
    echo "Setting configuration"
    heroku config:set ENV=prod --app ${HEROKU_APP}
    heroku config:set DEBUG_COLLECTSTATIC=1 --app ${HEROKU_APP}

}


function enable_shell_echo(){
    set -x
}


function deploy_code_to_heroku(){
    echo "###### Deployment process started ###"
    if [ "" != "$(git remote |grep -e '^heroku$')" ]; then
        git remote rm heroku
    fi
    heroku git:remote -a ${HEROKU_APP}
    #git -c core.askpass=true push https://git.heroku.com/${HEROKU_APP}.git HEAD:master -f
    git push -u heroku master
}

function run_database_migration() {
    echo "###### Running database migration ###"
    heroku run python manage.py migrate --noinput --app ${HEROKU_APP}
}


enable_shell_echo
deploy_code_to_heroku
run_database_migration