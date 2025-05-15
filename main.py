from faker import Faker

fake = Faker("pt_BR")

pessoas = []

for _ in range(50):
    nome = fake.first_name()
    sobrenome = fake.last_name()
    dominio = fake.free_email_domain()
    email = nome.replace(' ', '').lower() + sobrenome.replace(' ', '').lower()+ '@' + dominio.replace(' ', '').lower()
    pessoas.append({
        "nome": nome +" "+ sobrenome,
        "data_nascimento": fake.date_of_birth(minimum_age=0, maximum_age=140).strftime("%d/%m/%Y"),
        "email": email,
        "telefone": fake.msisdn(),
    })

for pessoa in pessoas:
    print(pessoa)