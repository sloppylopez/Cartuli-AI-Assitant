import os


def get_file_from_path(final_path):
    # Set the path to the folder containing your images
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(script_dir, final_path))
    final_path = os.path.normpath(base_dir)
    return final_path


if __name__ == "__main__":
    get_file_from_path("../../../images/cartuli-logo-master-small.ico")
    print('Done')
