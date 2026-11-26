import importlib.metadata


def main() -> None:
    print("\nREAGENT STATUS: Loading reagents...\n"
          "Checking dependencies:")

    librarys: dict[str, str] = {"pandas": "- Data manipulation ready",
                                "numpy": "- Numerical computation ready"}
    need_instruction = False
    for lib_name, message in librarys.items():
        try:
            importlib.import_module(lib_name)
            version = importlib.metadata.version(lib_name)
            print(f"[OK] {lib_name} ({version}) {message}")

        except ImportError:
            print(f"[KO] {lib_name} is not installed!")
            need_instruction = True

    if need_instruction:
        print("\ninstallation instructions:")
        print("$> pip install -r ex0/requirements.txt")
        print("or")
        print("$> poetry install -P ex0\n"
              "$> poetry -P ex0 run python ex0/loading.py")

    else:
        print()
        print("pip vs Poetry:")
        print("  requirements.txt declares what to install; "
              "pip resolves it at install time.\n"
              "  pyproject.toml declares the same constraints,"
              " and Poetry pins the resolved\n"
              "  versions in poetry.lock so every install is identical.")
        print()
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    main()
