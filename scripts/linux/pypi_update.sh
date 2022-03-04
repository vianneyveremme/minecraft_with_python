# Run the setup verification script.
python3 verify_setup.py

cd ../..

# Ask the user if the setup is correct.
read -p "Is the setup correct? (y/n) " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
then
    # If the setup is correct, run the setup.
    echo
    python3 setup.py sdist
else
    echo "Setup needs further modification."
    break
fi

read -p "Do you want to upload the package to PyPI? (y/n) " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
then
    # If the user wants to upload the package, run the upload script.
    echo
    python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
else
    echo "Package not uploaded."
    break
fi

read -p "Do you want to remove the generated package? (y/n) " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
then
    rm -rf dist
    rm -rf mcwpy.egg-info
else
    echo "Package not removed."
    break
fi
