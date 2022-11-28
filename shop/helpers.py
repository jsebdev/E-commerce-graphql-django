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


def edit_image(path):
    minimize_image(path)
    # print('executing minimize_image')
    # image_auto_rotate(path)


def minimize_image(path):
    base = 400
    with Image.open(path) as image:
        file_format = image.format
        width, height = image.size
        if width >= base and height >= base:
            print('minimizing image: ', path)
            print('width: ', width, ' height: ', height)
            file_format = image.format
            exif = image._getexif()
            if width > height:
                new_height = base
                new_width = int(width * new_height / height)
            else:
                new_width = base
                new_height = int(height * new_width / width)

            image = image.resize(
                (new_width, new_height), PIL.Image.Resampling.HAMMING)
            # new_name = f'{get_file_dir(path)}/{get_file_name(path)}.{get_file_extension(path)}'
            print('new sizes:')
            print('width: ', image.size[0], ' height: ', image.size[1])
            image.save(path, file_format)

            orientation_key = 274  # cf ExifTags
            if exif and orientation_key in exif:
                orientation = exif[orientation_key]
                print('74: orientation >>>', orientation)

                rotate_values = {
                    3: Image.ROTATE_180,
                    6: Image.ROTATE_270,
                    8: Image.ROTATE_90
                }

                if orientation in rotate_values:
                    image = image.transpose(rotate_values[orientation])

                image.save(path, file_format)

    return path


def image_auto_rotate(path):
    with Image.open(path) as image:
        print('64: path >>>', path)
        file_format = image.format
        print('62: file_format >>>', file_format)
        exif = image._getexif()
        print('63: exif: ', exif)

        # if image has exif data about orientation, let's rotate it
        orientation_key = 274  # cf ExifTags
        if exif and orientation_key in exif:
            orientation = exif[orientation_key]
            print('74: orientation >>>', orientation)

            rotate_values = {
                3: Image.ROTATE_180,
                6: Image.ROTATE_270,
                8: Image.ROTATE_90
            }

            if orientation in rotate_values:
                image = image.transpose(rotate_values[orientation])

        new_name = f'{get_file_dir(path)}/{get_file_name(path)}_rotate.{get_file_extension(path)}'
        image.save(new_name, file_format)
