from setuptools import setup, find_packages

setup(
    name='caesium_image_compressor',
    version='0.19.3',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'download_caesium=caesium.downloader:download_and_extract_caesium',
        ],
    },
)
