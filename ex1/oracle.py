import os


def main() -> None:
    try:
        try:
            from dotenv import load_dotenv
            from dotenv import dotenv_values
        except ImportError:
            print(
                "dotenv is not installed\n"
                "$> pip install -r ex1/requirements.txt"
            )
            return

        current_path = os.path.abspath(__file__)
        current_dir = current_path.rsplit("/", 1)[0]
        env_path = os.path.join(current_dir, ".env")
        load_dotenv(env_path)
        print("\nORACLE STATUS: Consulting the configuration...\n")
        print("Configuration loaded:")

        mode = os.getenv('MATRIX_MODE')
        if not mode:
            print(
                "[WARNING] Mode: MATRIX_MODE is not set\n"
                "Default value is 'development'"
            )
            mode = "development"
        elif mode == "development" or mode == "production":
            if mode == "production":
                print("[!本番モードです!]")
            print(f"Mode: {mode}")
        else:
            print(
                "[WARNING] unexpected mode\n"
                "Default value is 'development'"
            )
            mode = "development"

        db_url = os.getenv("DATABASE_URL")
        if not db_url:
            print(
                "[WARNING] Database: DATABASE_URL is not set"
            )
        elif "production" == mode and "localhost" in db_url:
            print(
                "[WARNING] Database: It's a production mode,"
                " but the DB is on localhost."
                " Is that really okay?"
            )
        elif "localhost" in db_url:
            print("Database: Connected to local instance")
        else:
            print("Database: Connected to remote instance")

        api = os.getenv("API_KEY")
        if not api:
            print("[WARNING] API Access: API_KEY is not set")
        else:
            print("API Access: Authenticated")

        log_level = os.getenv("LOG_LEVEL")
        if not log_level:
            print(
                "[WARNING] Log Level: LOG_LEVEL is not set\n"
                "Default value is 'DEBUG'"
            )
            log_level = "DEBUG"
        else:
            print(f"Log Level: {log_level}")

        url = os.getenv("ZION_ENDPOINT")
        if not url:
            print("[WARNING] Remote Network: ZION_ENDPOINT is not set")
        else:
            print("Remote Network: Online")

        print("\nConfiguration security check:")

        try:
            with open(current_path, mode="r") as f:
                text = f.read()
        except OSError as e:
            print(f"[ERROR] when opening error: {e}")

        else:
            secrets = [api, db_url]
            exclusion_none = [f for f in secrets if f]
            if not exclusion_none:
                print("[INFO] secrets not found")
            elif any(w in text for w in exclusion_none):
                print("[KO] hardcoded secrets detected")
            else:
                print("[OK] No hardcoded secrets detected")

        gitignore_path = os.path.join(current_dir, ".gitignore")
        try:
            with open(gitignore_path, mode="r") as f:
                gitignore_content = f.read()
        except FileNotFoundError:
            print("[KO] .gitignore not found")
        except OSError as e:
            print(f"[ERROR] when opening error: {e}")
        else:
            content_list = gitignore_content.splitlines()
            if ".env" in content_list:
                print("[OK] .env file properly ignored by git")
            else:
                print("[KO] .env file not ignored by git")

        env_content = dotenv_values(env_path)
        os_environ = os.environ
        if env_content.items() <= os_environ.items():
            print("[INFO] No overwrite detected.")
        else:
            print("[OK] Production overrides available")

        print("\nThe Oracle sees all configurations.")

    except Exception as e:
        print(f"unexpected error: {e}")


if __name__ == "__main__":
    main()
