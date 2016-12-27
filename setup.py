from setuptools import setup

__version__ = "0.1.0"
__author__ = "Nao Yonashiro <owan.orisano@gmail.com>"
__author_email__ = "owan.orisano@gmail.com"
__license__ = "MIT License"

setup(
    name="kptool",
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    url="https://github.com/orisano/kptool",
    description="kintone plugin tool.",
    py_modules=["kptool"],
    install_requires=["pyopenssl", "six"],
    keywords="kintone",
    license=__license__,
    entry_points={"console_scripts": ["kptool = kptool:main"]},
)
