import csv

def get_age_stats_for_current_smokers(data):
    ages = []
    for pid, patient in data.items():
        smoke = patient.get('Smoking Status', '').strip().lower()
        age = patient.get('Age', '').strip()
        if smoke in ['yes', '1']:
            try:
                age_val = float(age)
                ages.append(age_val)
            except ValueError:
                continue
    if not ages:
        return {"average_age": None, "count": 0}
    return {
        "average_age": round(sum(ages) / len(ages), 2),
        "count": len(ages)
    }

def get_age_stats_for_hypertension_patients(data):
    ages = []
    for pid, patient in data.items():
        hypertension = patient.get('Hypertension', '').strip()
        age = patient.get('Age', '').strip()
        if hypertension == '1':
            try:
                age_val = float(age)
                ages.append(age_val)
            except ValueError:
                continue
    if not ages:
        return {"average_age": None, "count": 0}
    return {
        "average_age": round(sum(ages) / len(ages), 2),
        "count": len(ages)
    }

def get_age_stats_for_smokers_with_hypertension_and_stroke(data):
    ages = []
    for pid, patient in data.items():
        smoke = patient.get('Smoking Status', '').strip().lower()
        hypertension = patient.get('Hypertension', '').strip()
        stroke = patient.get('Stroke Occurrence', '').strip()
        age = patient.get('Age', '').strip()
        if smoke in ['yes', '1'] and hypertension == '1' and stroke == '1':
            try:
                age_val = float(age)
                ages.append(age_val)
            except ValueError:
                continue
    if not ages:
        return {"average_age": None, "count": 0}
    return {
        "average_age": round(sum(ages) / len(ages), 2),
        "count": len(ages)
    }

def get_stats_for_heart_disease_with_stroke(data):
    count_with_both = 0
    total_with_heart_disease = 0
    for pid, patient in data.items():
        heart_disease = patient.get('Heart Disease', '').strip()
        stroke = patient.get('Stroke Occurrence', '').strip()
        if heart_disease == '1':
            total_with_heart_disease += 1
            if stroke == '1':
                count_with_both += 1
    percentage = round((count_with_both / total_with_heart_disease) * 100, 2) if total_with_heart_disease else 0
    return {
        "heart_disease_and_stroke_count": count_with_both,
        "heart_disease_total": total_with_heart_disease,
        "percentage_with_stroke": percentage
    }

def get_gender_age_stats_for_hypertension_stroke_groups(data):
    result = {"male": [], "female": []}
    for pid, patient in data.items():
        gender = patient.get('Gender', '').strip().lower()
        hypertension = patient.get('Hypertension', '').strip()
        stroke = patient.get('Stroke Occurrence', '').strip()
        age = patient.get('Age', '').strip()
        if hypertension == '1' and stroke == '1':
            try:
                age_val = float(age)
                if gender in result:
                    result[gender].append(age_val)
            except ValueError:
                continue
    output = {}
    for g in ["male", "female"]:
        lst = result[g]
        output[g] = round(sum(lst) / len(lst), 2) if lst else None
    return output

def get_age_stats_by_smoking_and_stroke(data):
    result = {
        "smoker_stroke": [],
        "smoker_no_stroke": [],
        "non_smoker_stroke": [],
        "non_smoker_no_stroke": [],
    }
    for pid, patient in data.items():
        smoke = patient.get('Smoking Status', '').strip().lower()
        stroke = patient.get('Stroke Occurrence', '').strip()
        age = patient.get('Age', '').strip()
        try:
            age_val = float(age)
        except ValueError:
            continue
        if smoke in ['yes', '1']:
            if stroke == '1':
                result["smoker_stroke"].append(age_val)
            elif stroke == '0':
                result["smoker_no_stroke"].append(age_val)
        else:
            if stroke == '1':
                result["non_smoker_stroke"].append(age_val)
            elif stroke == '0':
                result["non_smoker_no_stroke"].append(age_val)
    output = {}
    for k in result:
        lst = result[k]
        output[k] = round(sum(lst) / len(lst), 2) if lst else None
    return output

def get_age_stats_by_residence_for_stroke(data):
    residence = {}
    for pid, patient in data.items():
        stroke = patient.get('Stroke Occurrence', '').strip()
        res = patient.get('Residence Type', '').strip().lower()
        age = patient.get('Age', '').strip()
        if stroke == '1':
            try:
                age_val = float(age)
            except ValueError:
                continue
            if res not in residence:
                residence[res] = []
            residence[res].append(age_val)
    output = {}
    for r in residence:
        lst = residence[r]
        output[r] = round(sum(lst) / len(lst), 2) if lst else None
    return output

def get_patients_with_hypertension_and_stroke(data):
    results = {}
    for pid, patient in data.items():
        hypertension = patient.get('Hypertension', '').strip()
        stroke = patient.get('Stroke Occurrence', '').strip()
        if hypertension == '1' and stroke == '1':
            results[pid] = patient
    return results

def get_patients_by_hypertension_stroke_outcome(data):
    with_stroke = {}
    without_stroke = {}
    for pid, patient in data.items():
        hypertension = patient.get('Hypertension', '').strip()
        stroke = patient.get('Stroke Occurrence', '').strip()
        if hypertension == '1':
            if stroke == '1':
                with_stroke[pid] = patient
            elif stroke == '0':
                without_stroke[pid] = patient
    return {
        "hypertension_with_stroke": with_stroke,
        "hypertension_without_stroke": without_stroke,
    }

def get_patients_with_heart_disease_and_stroke(data):
    results = {}
    for pid, patient in data.items():
        heart_disease = patient.get('Heart Disease', '').strip()
        stroke = patient.get('Stroke Occurrence', '').strip()
        if heart_disease == '1' and stroke == '1':
            results[pid] = patient
    return results

def get_descriptive_stats(data):
    import math
    ages = []
    sleeps = []
    for pid, patient in data.items():
        try:
            ages.append(float(patient.get('Age', '').strip()))
        except Exception:
            pass
        try:
            sleeps.append(float(patient.get('Sleep Hours', '').strip()))
        except Exception:
            pass
    def stats(lst):
        if not lst:
            return None
        mean = sum(lst) / len(lst)
        minimum = min(lst)
        maximum = max(lst)
        std = (sum((x - mean) ** 2 for x in lst) / len(lst)) ** 0.5
        return {"mean": round(mean, 2), "min": minimum, "max": maximum, "std": round(std, 2)}
    return {
        "age_stats": stats(ages),
        "sleep_hours_stats": stats(sleeps)
    }

def get_average_sleep_by_stroke(data):
    sleep_with_stroke = []
    sleep_without_stroke = []
    for pid, patient in data.items():
        stroke = patient.get('Stroke Occurrence', '').strip()
        sleep = patient.get('Sleep Hours', '').strip()
        try:
            sleep_hours = float(sleep)
        except ValueError:
            continue
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
