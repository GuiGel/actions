import os

def main():
  print("Hello from GitHub Actions!")
  token = os.environ.get("BEGIN_WITH_ACTION_SECRET_TOKEN")
  if not token:
    raise RunTimeError("BEGIN_ACTION_SECRET_TOKEN env var is not set!")
  print("All good! We found our env var")

if __name__ == "__main__":
  main()
