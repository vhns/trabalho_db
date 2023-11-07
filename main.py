from utils.create_db import create_db
from models import *
from services.database import session, engine

if __name__ == "__main__":
    blood_bags = Blood_bags()
    blood_storage = Blood_storage()
    descount = Descount()
    donation_center = Donation_center()
    employee = Employee()
    pacient = Pacient()
    pacient_center = Pacient_center()
    payment = Payment()
    payment_descounts = Payment_descounts()
    person = Person()
    receiver = Receiver()
    receiver_center = Receiver_center()
    storage = Storage()

    create_db()

    #Insert
    person.insert_person(engine)
    donation_center.insert_center(engine)
    employee.insert_employee(engine)
    descount.insert_descount(engine)
    receiver.insert_receiver(engine)
    pacient.insert_pacient(engine)
    pacient_center.insert_pacient_center(engine)
    blood_bags.insert_blood_bags(engine)
    storage.insert_storage(engine)
    blood_storage.insert_blood_storage(engine)
    payment.insert_payment(engine)
    payment_descounts.insert_payment_desconts(engine)
    receiver_center.insert_receiver_center(engine)

    #Update
    person.update_person(engine)
    donation_center.update_donation_center(engine)
    employee.update_employee(engine)

    #Delete
    payment.delete_payment(engine)
    receiver.delete_receiver(engine)
    blood_bags.delete_blood_bags(engine)
    donation_center.delete_donation_center(engine)
    person.delete_person(engine)


    #Select
    # 1
    blood_bags.total_pacients_per_dmy(session)

    # 2
    blood_bags.total_bb(session)

    # 3
    blood_bags.total_bb_per_type(session)

    # 4
    blood_bags.expiring_bb(session)

    # 5
    blood_bags.expiring_bb_per_type(session)

    # 6
    payment.total_month_salary(session)

    # 7
    payment.total_year_salary(session)

    # 8
    employee.total_employees(session)

    # 10
    storage.free_space_storage(session)

    # 11
    storage.occupied_space_storage(session)

    # 12
    pacient_center.total_pacient_per_center(session)

    # 13
    blood_storage.departured_bb_per_center(session)

    # 14
    blood_bags.total_liters_bb(session)

    # 15
    blood_bags.total_liters_bb_per_type(session)

    # 16
    blood_bags.average_bb_per_pacient(session)

    # 17
    pacient.pacient_per_blood_type(session)

    # 18
    blood_bags.bb_per_year_and_type(session)

    # 19
    payment.average_payment_per_type_employee(session)

    # 20
    receiver_center.total_receiver_per_center(session)
    