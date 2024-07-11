import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

__version__ ="0.0.0"

REPO_NAME="text_summerizer_project"
AUTHER_USER_NAME="nishshanka20"
SRC_REPO="textSummerizer"
AUTHER_EMAIL_URL="nishshankawla@gmail.com" 

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHER_USER_NAME,
    author_email=AUTHER_EMAIL_URL,
    description="A small package to summerize text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/" + AUTHER_USER_NAME + "/" + REPO_NAME,
    project_urls={"Bug Tracker":f"https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}/issues",
},
    packages=setuptools.find_packages(),
)