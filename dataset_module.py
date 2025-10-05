import csv

def load_data(filepath):
    data = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for idx, row in enumerate(reader):
                data[f"PID{idx+1}"] = row
    except Exception as e:
        print(f"Error loading data: {e}")
    return data

def get_average_sleep_by_stroke(data):
    sleep_with_stroke = []
    sleep_without_stroke = []

    for pid, patient in data.items():
        stroke = patient.get('Stroke Occurrence', '').strip()
        sleep = patient.get('Sleep Hours', '').strip()

        try:
            sleep_hours = float(sleep)
        except ValueError:
            continue  # Skip invalid sleep hour entries

        if stroke == '1':
            sleep_with_stroke.append(sleep_hours)
        elif stroke == '0':
            sleep_without_stroke.append(sleep_hours)

    def avg(lst):
        return round(sum(lst) / len(lst), 2) if lst else None

    return {
        "average_sleep_with_stroke": avg(sleep_with_stroke),
        "average_sleep_without_stroke": avg(sleep_without_stroke),
        "count_with_stroke": len(sleep_with_stroke),
        "count_without_stroke": len(sleep_without_stroke)
    }
