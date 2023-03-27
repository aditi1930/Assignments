# A function to print username and domain
def print_user_info(user, domain_name):
    print("Username:", user)
    print("Domain Name:", domain_name)

# A function to extract username from email
def extract_username(email_address):
    username = ""
    for i in email_address:
        if i != '.' and i != '@' and not i.isdigit():
            username += i
        else:
            break
    return username

# A function to extract domain name from email
def extract_domain(email_address):
    flag = False
    domain_name = ""

    for i in range(len(email_address)):
        if flag:
            domain_name += email_address[i]
        if email_address[i] == '@':
            flag = True

    return domain_name

# Main function
if __name__ == "__main__":
    email_address = input("Enter your email address: ")
    username = extract_username(email_address)
    domain_name = extract_domain(email_address)
    print_user_info(username, domain_name)

