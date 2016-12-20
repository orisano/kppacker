from setuptools import setup

__version__ = "0.1.0"
__author__ = "Nao Yonashiro <owan.orisano@gmail.com>"
__author_email__ = "owan.orisano@gmail.com"
__license__ = "MIT License"

setup(
    name="kppacker",
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    url="https://github.com/orisano/kppacker",
    description="kintone plugin packer.",
    py_modules=["kppacker"],
    install_requires=["pyopenssl", "six"],
    keywords="kintone",
    license=__license__,
    entry_points={"console_scripts": ["kppacker = kppacker:main"]},
)
