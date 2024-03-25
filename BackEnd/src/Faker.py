from CareGiver import CareGiver
from Patient import Patient
import random
import names

TREATMENTS = ['PT', 'OT', 'GYM', 'Psych', 'Doctor']
PATIENTS = 40
CARE_GIVERS = 10
WORKING_DAYS = 5


def get_fake_care_givers():
    care_givers = list()
    for i in range(CARE_GIVERS):
        care_givers.append(
            CareGiver(
                names.get_first_name(),
                names.get_last_name())),
    return care_givers


def get_fake_patients():
    patients = list()
    for i in range(PATIENTS):
        patients.append(
            Patient(
                names.get_first_name(),
                names.get_last_name()))
    return patients


if __name__ == '__main__':
    pass
