from PIL import Image
import PIL


def get_image_format(path):
    """
    Get the image format from the path
    """
    return path.split('.')[-1]


def fix_spaces(text):
    """
    Replace all spaces with underscores
    """
    return text.replace(' ', '_')


def replace_format(path, new_format):
    """
    Replace the image format with the new format
    """
    return '.'.join(path.split('.')[:-1]) + f'.{new_format}'


def get_file_name(path):
    return path.split('/')[-1].split('.')[0]


def get_file_extension(path):
    return path.split('.')[-1]


def get_file_dir(path):
    return '/'.join(path.split('/')[:-1])


def minimize_image(path):
    base = 400
    image = Image.open(path)
    width, height = image.size
    if width <= base and height <= base:
        return path
    if width > height:
        new_height = base
        new_width = int(width * new_height / height)
    else:
        new_width = base
        new_height = int(height * new_width / width)
    image = image.resize((new_width, new_height), PIL.Image.Resampling.LANCZOS)
    # new_name = f'{get_file_dir(path)}/{get_file_name(path)}.{get_file_extension(path)}'
    image.save(path)
    return path
