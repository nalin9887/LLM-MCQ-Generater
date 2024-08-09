from setuptools import find_packages,setup
setup(
    name='mcqgenrator',
    version='0.1',
    author='Nalin Sharma',
    author_email='nalinsharma201@gmail.com',
    description='A simple MCQ generator for educational purposes',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)