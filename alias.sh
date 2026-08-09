submit() {
    git add . && git commit -m "${@}: submit"
}

init() {
    git add . && git commit -m "${@}: init"
}

test() {
    if [ "$#" -ne 1 ]; then
        echo "usage: test <solution.py|problem-number>" >&2
        return 2
    fi

    local target="$1"
    if [ ! -f "$target" ] && [[ "$target" != *.py ]]; then
        local matches=(*/"$target".py)
        if [ "${#matches[@]}" -eq 1 ] && [ -f "${matches[0]}" ]; then
            target="${matches[0]}"
        fi
    fi

    uv run python -m utils "$target"
}
