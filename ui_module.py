from colorama import init, Fore, Style
from dataset_module import load_data
from query_module import (
    get_age_stats_for_current_smokers,
    get_age_stats_for_hypertension_patients,
    get_age_stats_for_smokers_with_hypertension_and_stroke,
    get_stats_for_heart_disease_with_stroke,
    get_gender_age_stats_for_hypertension_stroke_groups,
    get_age_stats_by_smoking_and_stroke,
    get_age_stats_by_residence_for_stroke,
    get_patients_with_hypertension_and_stroke,
    get_patients_by_hypertension_stroke_outcome,
    get_patients_with_heart_disease_and_stroke,
    get_descriptive_stats,
    get_average_sleep_by_stroke
)

init(autoreset=True)

def display_menu():
    print(Fore.CYAN + "\n==== 🧠 Stroke Data Analytics Menu ====")
    print(Fore.YELLOW + "1. Age stats for current smokers")
    print("2. Age stats for hypertension patients")
    print("3. Age stats for smokers + hypertension + stroke")
    print("4. Age & glucose stats for heart disease + stroke")
    print("5. Gender-wise age stats (hypertension & stroke)")
    print("6. Age stats by smoking habits vs stroke")
    print("7. Age stats by residence (stroke only)")
    print("8. Patients with hypertension + stroke")
    print("9. Hypertension patients (stroke vs no-stroke)")
    print("10. Heart disease + stroke patients")
    print("11. Descriptive stats for a numeric feature")
    print("12. Average sleep hours by stroke")
    print(Fore.RED + "0. Exit")

def run_ui():
    print(Fore.GREEN + "Welcome to Stroke Analytics System 🩺")
    path = input(Fore.CYAN + "Enter the full path to your CSV file: ").strip()
    data = load_data(path)

    if not data:
        print(Fore.RED + "Failed to load dataset. Please check your file path.")
        return

    options = {
        '1': get_age_stats_for_current_smokers,
        '2': get_age_stats_for_hypertension_patients,
        '3': get_age_stats_for_smokers_with_hypertension_and_stroke,
        '4': get_stats_for_heart_disease_with_stroke,
        '5': get_gender_age_stats_for_hypertension_stroke_groups,
        '6': get_age_stats_by_smoking_and_stroke,
        '7': get_age_stats_by_residence_for_stroke,
        '8': get_patients_with_hypertension_and_stroke,
        '9': get_patients_by_hypertension_stroke_outcome,
        '10': get_patients_with_heart_disease_and_stroke,
        '11': get_descriptive_stats,
        '12': get_average_sleep_by_stroke
    }

    while True:
        display_menu()
        choice = input(Fore.CYAN + "\nSelect an option (0-12): ").strip()

        if choice == '0':
            print(Fore.MAGENTA + "Goodbye! Stay healthy. 🫀")
            break

        func = options.get(choice)
        if not func:
            print(Fore.RED + "Invalid choice. Please try again.")
            continue

        try:
            result = func(data)
            print(Fore.BLUE + "\n📊 Result:\n", result)
        except Exception as e:
            print(Fore.RED + f"Error while processing query: {e}")
            continue

        save = input(Fore.GREEN + "\nDo you want to save the result as a CSV file? (y/n): ").strip().lower()
        if save in ['y', 'yes']:
            filename = input("Enter filename (e.g., result.csv): ").strip()
            save_result_to_csv(filename, result)

def save_result_to_csv(filename, result_dict):
    try:
        with open(filename, 'w') as f:
            if isinstance(result_dict, dict):
                for key, value in result_dict.items():
                    if isinstance(value, dict):
                        row = [key] + [f"{k}={v}" for k, v in value.items()]
                        f.write(','.join(row) + '\n')
                    else:
                        f.write(f"{key},{value}\n")
            else:
                f.write("Unsupported format\n")
        print(f"✅ Results saved to: {filename}")
    except Exception as e:
        print(f"❌ Error saving CSV: {e}")
