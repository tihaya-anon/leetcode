submit() {
    git add . && git commit -m "${@}: submit"
}

init() {
    git add . && git commit -m "${@}: init"
}
