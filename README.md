# Tesserae Ubuntu Installer Creator

This code generates a .deb file for installing Tesserae.
It uses `dh-virtualenv` to do so.
This code was made on Ubuntu 18.04.4.

If you want to understand how to build Ubuntu packages, there's a lot to read.
First note that Ubuntu is built on top of Debian, so the foundations for building a Debian package are the same as those for building an Ubuntu package.
I found <https://www.debian.org/doc/manuals/packaging-tutorial/packaging-tutorial.pdf> a helpful start.
The [`dh-virtualenv` manual](https://dh-virtualenv.readthedocs.io/en/1.1/index.html) was important.
The example projects using `dh-virtualenv` (such as <https://github.com/1and1/debianized-jupyterhub> and <https://github.com/1and1/debianized-sentry>) were helpful, particularly in configuring `dh-virtualenv` to use Python 3.
Playing with `dh-make` to see what sorts of files came out was also helpful.
Finally, the nitty-gritty details were in chapters 4 and 5 of the [Debian policy manual](https://www.debian.org/doc/debian-policy/index.html) as well as the manpages for the various Debian packaging scripts.

## Preparing Your Environment

Make sure that you have all of the preliminary dependencies:
```
sudo apt-get install python3-dev python3-venv devscripts git dh-virtualenv build-essential debhelper equivs
```

Create a directory where you want your .deb file to appear, clone this repository there, then enter the repository directory:
```
mkdir /place/for/deb-file
cd /place/for/deb-file
git clone https://github.com/tesserae/debinstall-tesserae.git
cd debinstall-tesserae
```

Make sure that you have all of the build dependencies and build the binary-only .deb file:
```
sudo mk-build-deps -ri
dpkg-buildpackage -us -uc -b
```

If nothing went wrong, you should see a .deb file in the directory you wanted it to appear.
At this point, you can install the package with `sudo dpkg -i`, play around to make sure that Tesserae was installed, and uninstall the package with `sudo dpkg -r`.
