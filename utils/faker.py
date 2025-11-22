from faker import Faker


fake = Faker() # FAKER ME GENERA DATOS ALEATOREAMENTE

def get_login_faker(num_casos=5):


    casos = []
    usuarios_validos = [ "standard_user", "locked_out_user"]
    password_valido = "secret_sauce"
 
    for _ in range(num_casos):
       username = fake.user_name() #aleatorio
       password = fake.password(length=12)
       login_example = fake.boolean(chance_of_getting_true=50) #50% de prob = TRUE

       if fake.boolean(chance_of_getting_true=50):
           username = fake.random.choice(usuarios_validos)
           password = password_valido
           login_example = True
       else:
            username = fake.user_name() #aleatorio
            password = fake.password(length=12)
            login_example = False
    

       casos.append((username, password, login_example))

    return casos