import sys
import site


def main() -> None:

    if sys.prefix == sys.base_prefix:
        print()
        print("LABORATORY STATUS: You are working in the open")
        print()
        print("Current Python:", sys.executable)
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")
        print()
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print(r"source lab_env/bin/activate # On Unix")
        print(r"lab_env\Scripts\activate # On Windows")
        print()
        print("Then run this program again.")
    else:
        print()
        print("LABORATORY STATUS: The laboratory is sealed")
        print()
        print("Current Python:", sys.executable)
        virtual_environment_path = sys.prefix
        virtual_environment_path_list = virtual_environment_path.split("/")
        print(f"Virtual Environment: {virtual_environment_path_list[-1]}")
        print("Environment Path:", virtual_environment_path)
        print()
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.")
        print()
        print("Reagent installation path:")
        all_sitepackages_list = site.getsitepackages()
        sitepackages = [f for f in all_sitepackages_list
                        if "site-packages" in f]
        if sitepackages:
            print(sitepackages[0])
        else:
            print("site-packages not found!")


if __name__ == "__main__":
    main()
