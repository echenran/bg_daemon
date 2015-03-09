import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "bg_daemon",
    version = "0.0.1",
    author = "Santiago Torres",
    author_email = "torresariass@gmail.com",
    description = ("An extensible set of classes that can programatically "
        "update the desktop wallpaper"),
    license = "GPLv2",
    keywords = "imgur desktop wallpapaer background",
    url = "https://github.com/santiagotorres/bg_daemon",
    packages = ["bg_daemon", "bg_daemon.fetchers"],
    package_dir = {"bg_daemon": "src/bg_daemon",
                   "bg_daemon.fetchers": "src/bg_daemon/fetchers"},
    scripts = ["src/bg_daemon/background_daemon.py"],
    include_package_data = True,
    data_files = [('bg_daemon', ['src/bg_daemon/settings.json'])],
    long_description = read("README.md"),
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: ",
        "Environment :: No Input/Output (Daemon)",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: Unix",
        "Topic :: Multimedia",
        ],
    install_requires = [
        "imgurpython",
        "requests",
        ],
)


