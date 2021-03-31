import setuptools

with open("README.md",'r') as pr:
    long_description = pr.read()

setuptools.setup(
    name = "Mathsimple",
    version = "0.0.1",
    author = "Chandra Prakash Mewari",
    author_email= "Prakash.mewari@yahoo.com",
    description = "A very small math library ",
    long_description = long_description,
    url = "https://github.com/DPrakashMewari/Mathsimple",
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)    
