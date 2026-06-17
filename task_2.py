class UserData:
    def __init__(self, name, age):
        self.user_name = name
        self.age = age

    def print_info(self):
        print(f"User: {self.user_name}, Age: {self.age}")


def process_data(data_list):
    result = []
    for data in data_list:
        if data.age > 18:
            result.append(data.user_name.upper())
    return result
