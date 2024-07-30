import customtkinter


# functions
counter = 1
def handleClick(event="none"):
    global counter
    taskText = addTask.get("1.0", "end-1c")
    print(f"Task: {taskText}")
   
    
    if taskText.strip():
        newTask = customtkinter.CTkLabel(taskList, text=(f"{counter}. {taskText}"), width=400, height=50, font=("Arial", 20))
        newTask.pack(pady=2, padx=2, anchor="w")
        counter = counter+1
        addTask.delete("1.0", "end")
        

# App frame
app = customtkinter.CTk()
app.geometry("720x520")
app.title("To Do List")


# UI Elements
label = customtkinter.CTkLabel(app, text="To Do List", font=("Arial", 32))
label.pack(padx=10, pady=20)

addTask = customtkinter.CTkTextbox(app, width=400, height=50)
addTask.pack()
addTask.bind("<Return>", handleClick)

button = customtkinter.CTkButton(app, text="Add", fg_color="green", width=80, height=25, font=("Arial", 22), command=handleClick)
button.pack(padx=10,pady=15)


taskList = customtkinter.CTkFrame(app, width=400, height=400)
taskList.pack(padx=10, pady=2, fill="both", expand=True)

# Run app
app.mainloop()