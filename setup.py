import setuptools

with open('README.md') as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name="streamlit-mermaid",
    version="0.1.0",
    author="nakanat",
    author_email="nekanat.stock@gmail.com",
    description="A streamlit component, to visualize mermaid",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/AI-Yash/st-chat",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords="mermaid streamlit streamlit-component",
    python_requires=">=3.10",
    install_requires=[
        "streamlit >= 1.24.1",
    ],
)
