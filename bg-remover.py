from rembg import remove, new_session
import os


def remove_background_from_image(input_path: str, output_path: str, session=None):
    """
    Remove background from a single image file.
    """
    # Read input as bytes
    with open(input_path, "rb") as f:
        input_data = f.read()

    # The rembg API remove() takes parameters: input, session, etc.
    # Force output as bytes
    output_data = remove(input_data, session=session, force_return_bytes=True)

    # Write output bytes
    with open(output_path, "wb") as f:
        f.write(output_data)


def batch_process(input_dir: str, output_dir: str, model_name: str = None):
    """
    Process all image files in a folder, save with backgrounds removed
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create a session once, to speed up repeated calls
    session = new_session(model_name)

    for fname in os.listdir(input_dir):
        basename, extension = os.path.splitext(fname)
        extension_lower = extension.lower()
        if extension_lower in [".png", ".jpg", ".jpeg", ".webp", ".bmp"]:
            input_path = os.path.join(input_dir, fname)
            output_path = os.path.join(
                output_dir, f"{basename}_no_bg.png"
            )  # use PNG to retain transparency
            print(f"Processing {input_path} -> {output_path}")
            remove_background_from_image(input_path, output_path, session=session)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Remove backgrounds using rembg")
    parser.add_argument(
        "--input", "-i", type=str, required=True, help="Input image file or directory"
    )
    parser.add_argument(
        "--output", "-o", type=str, required=True, help="Output file or directory"
    )
    parser.add_argument(
        "--model",
        "-m",
        type=str,
        default=None,
        help="Model name (e.g. u2net, u2netp, etc)",
    )
    args = parser.parse_args()

    if os.path.isdir(args.input):
        batch_process(args.input, args.output, model_name=args.model)
    else:
        # assume single file
        remove_background_from_image(args.input, args.output)


if __name__ == "__main__":
    main()
