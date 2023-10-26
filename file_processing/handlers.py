import magic


def get_file_type(file):
    mime = magic.from_file(file, mime=True)
    file_name = mime.split('/')
    file_type = file_name[1]
    return file_type
