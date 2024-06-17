import subprocess
import logging
import asyncio
import sys

CAESIUM_BINARY_PATH = "./caesiumclt"  # Update this based on the actual binary path


async def compress_image(
    input_path: str,
    output_path: str = None,
    quality: int = 80,
    lossless: bool = False,
    exif: bool = True,
    verbose: bool = False
):
    if output_path is None:
        output_path = input_path

    if lossless:
        quality = 0

    command = [
        CAESIUM_BINARY_PATH,
        "--file", input_path,
        "--output", output_path,
        "--overwrite", "bigger",
        "--quality", str(quality)
    ]

    if exif:
        command.append("--exif")
    if not verbose:
        command.append("--quiet")

    try:
        process = await asyncio.create_subprocess_exec(
            *command,
            stdout=asyncio.subprocess.PIPE if verbose else subprocess.DEVNULL,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        if verbose and stdout:
            logging.info(stdout.decode())
        if process.returncode != 0 and stderr:
            logging.error(stderr.decode())

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m caesium.compressor <input_path> [output_path] [quality] [lossless] [exif] [verbose]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    quality = int(sys.argv[3]) if len(sys.argv) > 3 else 80
    lossless = sys.argv[4].lower() == 'true' if len(sys.argv) > 4 else False
    exif = sys.argv[5].lower() != 'false' if len(sys.argv) > 5 else True
    verbose = sys.argv[6].lower() == 'true' if len(sys.argv) > 6 else False

    asyncio.run(compress_image(input_path, output_path, quality, lossless, exif, verbose))


if __name__ == "__main__":
    main()
