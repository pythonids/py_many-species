while getopts "t:" tag
do
    case "${tag}" in
        t) TAG=${OPTARG};;
    esac
done

startApp(){
    pm2 start app.js -i 1
    if [ $? -eq 0 ]; then
        echo "\n \n ### START RELEASE ${TAG} - SUCCESS ### \n \n"
    else
        echo "\n \n ### START RELEASE ${TAG} - FAILURE ### \n \n"
        exit 1
    fi
}

reloadApp(){
    pm2 delete HeyCMO
    if [ $? -eq 0 ]; then
        startApp
        echo "\n \n ### DELETE OLD APP - OK ### \n \n"
    else
        echo "\n \n ### DELETE OLD APP - FAIL ### \n \n"
        exit 1
    fi
}

install(){
    npm install .
    if [ $? -eq 0 ]; then
        echo "\n \n ### NPM INSTALL - OK ### \n \n"
    else
        echo "\n \n ### NPM INSTALL - FAIL ### \n \n"
        exit 1
    fi
}

run(){
    echo "\n \n ### RUN RELEASE ${TAG} ### \n \n"
    cd py_many_species_$TAG
    ls -la
    install
    if [ $? -eq 0 ]; then
        reloadApp
    fi
}

run
