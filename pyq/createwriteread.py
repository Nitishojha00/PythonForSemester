file_path="file.txt"
with open(file_path,"w") as file:
    file.write("YourName:Aryan Patel\n")
    file.write("Your fathers name:Ved Prakash \n")
with open(file_path,"r") as file:
    content=file.read
    print("content of file:")
    print(content)

    # nitish bhai comment