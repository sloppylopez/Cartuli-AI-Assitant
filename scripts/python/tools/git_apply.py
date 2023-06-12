import subprocess
import sys

def apply_git_patch(patch_file):
    try:
        command = ['pwd']
        subprocess.run(command, check=True)
        print("Patch applied successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to apply patch. Error: {e}")
        sys.exit(1)

# Example usage
if __name__ == "__main__":
    apply_git_patch("C:\\Users\\sergi\\PycharmProjects\\Cartuli-AI-Assitant\\scripts\\python\\code_to_be_refactored\\ai_refactored\\diff.patch")
