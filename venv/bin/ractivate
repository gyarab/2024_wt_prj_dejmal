vnv=$VIRTUAL_ENV
vnvbin=$vnv/bin
hm=$vnv/..
prj=$hm/prj

addkey() {
    ssh-add $1
}

addkmm() {
    addkey mmm
}

mng() {
    $prj/manage.py $*
}

srvr() {
    mng runserver
}

migr() {
    mng migrate
}

mkmigr() {
    mng makemigrations
}

mkmigrm() {
    mkmigr
    migr
}

da () {
    deactivate
    unset p3
    unset pi
    unset pir
    unset py
}

aaa() {
    source $vnvbin/activate
}

p3() {
    pip3 $*
}
pi() {
    pip3 install $*
}
pir() {
    pip3 -r $hm/requirements.txt
}
py() {
    python3 $*
}

gta() {
    git add $*
}
gtaa() {
    gta -A
}

gcomi() {
    git commit
}
gpush() {
    git push $*
}
