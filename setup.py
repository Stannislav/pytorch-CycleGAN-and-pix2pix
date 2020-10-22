from setuptools import find_packages, setup


setup(
    name="pix2pix",
    version="0.0.1",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        "torch>=1.4.0",
        "torchvision>=0.5.0",
        "dominate>=2.4.0",
        "visdom>=0.1.8.8",
    ]
)
