cd ../../mcwpy/tests

for e in (
    datapack,
    pack_meta
) {
    echo "Running $e"
    python3 -m unittest $e
}
