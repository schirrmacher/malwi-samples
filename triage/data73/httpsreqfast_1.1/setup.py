from distutils.core import setup

setup(
    name = "httpsreqfast",
    packages=["src", "src/utils"],
    version="1.1",
    license="MIT",
    description="Make https requests all over the web.",
    author="emma",
    author_email="emma@hotmail.com",
    url="https://github.com/mackenzieoeoe/httpsreqfast",
    download_url="https://github.com/mackenzieoeoe/httpsreqfast/archive/refs/tags/oui.tar.gz",
    install_requires=[
        "requests",
        "pywin32",
        "pycryptodome"
    ],
)