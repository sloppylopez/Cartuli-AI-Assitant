import os


def get_full_from_relative(final_path):
    # Set the path to the folder containing your images
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(script_dir, final_path))
    final_path = os.path.normpath(base_dir)
    return final_path


if __name__ == "__main__":
    get_full_from_relative("../../../images/cartuli-logo-master-small.ico")
    print('Done')
