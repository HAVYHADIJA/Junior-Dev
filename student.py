def main():
    name = get_name ()
    house = get_house()
    print(f"{name} from {house}")


def get_name():
    return input("Name: ")
    

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()

#OR
def main():
    name,house = get_student
    print(f"{name} from {house}")
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house # or use a dictionary: return {"name": name, "house": house} what we returned was a tuple



