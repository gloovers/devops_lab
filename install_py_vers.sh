#! /bin/bash

# variables
vers1=2.7
vers2=3.5.0
name1=Proj1
name2=Proj2
dir1=$HOME/$name1
dir2=$HOME/$name2

# install versions 2.7 and 3.5 of Python
if ! ( pyenv versions | grep -q "$vers1") ; then
    pyenv install $vers1 > /dev/null 2>&1
    if [ $? == 0 ]; then
        echo "Version $vers1 installed successfully."
    else 
        echo "Installing of Version $vers1 was failed."
    fi
else
    echo "Version $vers1 is already installed."
fi

if ! ( pyenv versions | grep -q "$vers2") ; then
    pyenv install $vers2 > /dev/null 2>&1
    if [ $? == 0 ]; then
        echo "Version $vers2 installed successfully."
    else
        echo "Installing of Version $vers2 was failed."
    fi
else
    echo "Version $vers2 is already installed."
fi

# Create environments
mkdir $dir1 $dir2 > /dev/null 2>&1

cd $dir1 && pyenv local $vers1 && pyenv virtualenv $name1 > /dev/null 2>&1
if [ $? == 0 ]; then
    echo "Py environment $name1 with version $vers1 was created."
else
    echo "Creating of Py environment $name1 with version $vers1 was failed or environment with this name is already created."
fi

cd $dir2 && pyenv local $vers2 && pyenv virtualenv $name2 > /dev/null 2>&1
if [ $? == 0 ]; then
    echo "Py environment $name2 with version $vers2 was created."
else
    echo "Creating of Py environment $name2 with version $vers2 was failed or environment with this name is already created."
fi

