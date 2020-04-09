import string
import random

def get_details():
    first_name = input(str('Please Enter your First Name: '))
    last_name = input(str('Please Enter your Last Name: '))
    email_add = input(str('Please Enter your email Address: '))

    userdetails = {
        'first_name' : first_name, 
        'last_name' : last_name,
        'email_add' :  email_add
        }

    return userdetails

def gen_password(details):
    alphabets = string.ascii_letters
    length = 5
    random_password = ''.join(random.choice(alphabets) for i in range(length))
    
    password = str(userdetails['first_name'][0:2] + userdetails['last_name'][-2:] + random_password)
    
    return password

status = True
container = []


while status:
    userdetails = get_details()
    password = gen_password(userdetails)

    print('Your System Generated Password is : ' + str(password))

    password_loop = True

    while password_loop:
        password_like = input(str('Do you like your Password? If Yes, Enter Yes. If No, Enter No: ')).lower()
        if password_like == 'yes':
            userdetails['password'] = password
            container.append(userdetails)
            password_loop = False

        elif password_like == 'no':
            pass_len = True

            while pass_len:
                user_password = input(str('Please Enter Password Longer than 7 characters: '))
                if len(user_password) >= 7:
                    userdetails['password'] = password
                    container.append(userdetails)
                    pass_len = False
                    password_loop = False

    while True:
        new_user = input(str('New User? Yes or No : ')).lower()
        if(new_user == 'no'):
            status = False
            for i in range(len(container)):
                output = (f"""
                    firstname: {container[i]['first_name']}
                    lastname: {container[i]['last_name']}
                    email: {container[i]['email_add']}
                    password: {container[i]['password']}
                    {'-'*40}""")

                print(output)
            break

        elif new_user == 'yes':
            status = True
            break




