import os
import platform
import tarfile
import zipfile
import requests

# https://github.com/Lymphatus/caesium-clt/releases/download/0.19.3/caesiumclt-0.19.3-x86_64-pc-windows-msvc.zip
CAESIUM_URL = "https://github.com/Lymphatus/caesium-clt/releases/download/0.19.3/"


def get_download_url():
    system = platform.system().lower()
    arch = platform.machine()

    if system == "darwin":
        if arch == "x86_64":
            filename = "caesiumclt-0.19.3-x86_64-apple-darwin.tar.gz"
        else:
            filename = "caesiumclt-0.19.3-aarch64-apple-darwin.tar.gz"
    elif system == "linux":
        filename = f"caesiumclt-0.19.3-{arch}-unknown-linux-musl.tar.gz"
    elif system == "windows":
        filename = "caesiumclt-0.19.3-x86_64-pc-windows-msvc.zip"
    else:
        raise ValueError("Unsupported operating system")

    return CAESIUM_URL + filename


def download_and_extract_caesium():
    url = get_download_url()
    filename = url.split('/')[-1]
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)

        if filename.endswith(".tar.gz"):
            with tarfile.open(filename, "r:gz") as tar:
                tar.extractall()
        elif filename.endswith(".zip"):
            with zipfile.ZipFile(filename, "r") as zip_ref:
                zip_ref.extractall()
        os.remove(filename)
    else:
        raise Exception("Failed to download Caesium binary")


if __name__ == "__main__":
    download_and_extract_caesium()
