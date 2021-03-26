def chek_data_type(type, data):
    if type == "int":
        print(int(data) * 2)
    elif type == "real":
        print(f"{(float(data) * 1.5):.2f}")
    elif type == "string":
        print(f"${data}$")


type_data = input()
input_data = input()

chek_data_type(type_data, input_data)