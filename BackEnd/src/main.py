from CareGiver import CareGiver
from Patient import Patient
from Scheduler import Scheduler
import names

TREATMENTS = ['PT', 'OT', 'GYM', 'Psych', 'Doctor']


def create_fake_obj():
    care_giver_amount = 10
    patient_amount = 40
    care_givers = list()
    patients = list()
    for i in range(care_giver_amount):
        care_givers.append(
            CareGiver(
                names.get_first_name(),
                names.get_last_name()))
    for i in range(patient_amount):
        patients.append(
            Patient(names.get_first_name(),
                    names.get_last_name()))
    return care_givers, patients


if __name__ == '__main__':
    cg, pa = create_fake_obj()
