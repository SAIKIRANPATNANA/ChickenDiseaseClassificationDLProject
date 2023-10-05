import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
__version__ = '0.0.0'
REPO_NAME = "ChickenDiseaseClassificationDLProject"
AUTHOR_USER_NAME = "SAIKIRANPATNANA"
SRC_REPO = "ChickenDiseaseClassificationDLProject"
AUTHOR_EMAIL = "saikiranpatnana5143@gmail.com"
setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for CNN app",
    long_description = 'long_description',
    long_description_content = "text/markdown",
    url = f"",
    project_urls={
    'Documentation': 'https://docs.example.com',
    'Source Code': 'https://github.com/username/reponame',},
    package_dir  = {"":"src"},
    packages = setuptools.find_packages(where = "src")
)

