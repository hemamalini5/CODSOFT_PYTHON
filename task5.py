import tkinter as tk
from tkinter import messagebox, simpledialog

# Contact Data Structure
contacts = {}

# Main Application Class
class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x500")

        # Search Field
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(root, textvariable=self.search_var, width=40)
        self.search_entry.pack(pady=10, padx=10)
        self.search_entry.bind("<Return>", self.search_contact)

        # Contact Listbox
        self.contact_listbox = tk.Listbox(root, width=50, height=15)
        self.contact_listbox.pack(pady=10)

        # Buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Contact", command=self.add_contact)
        self.add_button.pack(side="left")

        self.update_button = tk.Button(self.button_frame, text="Update Contact", command=self.update_contact)
        self.update_button.pack(side="left")

        self.delete_button = tk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(side="left")

        self.view_button = tk.Button(self.button_frame, text="View Contacts", command=self.view_contacts)
        self.view_button.pack(side="left")

        self.contact_listbox.bind('<<ListboxSelect>>', self.on_select)

    def on_select(self, event):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            self.selected_contact = self.contact_listbox.get(selected_index)
    
    def add_contact(self):
        name = simpledialog.askstring("Add Contact", "Enter Name:")
        phone = simpledialog.askstring("Add Contact", "Enter Phone Number:")
        email = simpledialog.askstring("Add Contact", "Enter Email:")
        address = simpledialog.askstring("Add Contact", "Enter Address:")
        if name and phone:
            contacts[name] = {'phone': phone, 'email': email, 'address': address}
            self.view_contacts()
        
    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for name in contacts:
            self.contact_listbox.insert(tk.END, name)
    
    def search_contact(self, event):
        search_query = self.search_var.get().lower()
        self.contact_listbox.delete(0, tk.END)
        for name in contacts:
            if search_query in name.lower():
                self.contact_listbox.insert(tk.END, name)

    def update_contact(self):
        if hasattr(self, 'selected_contact'):
            name = self.selected_contact
            phone = simpledialog.askstring("Update Contact", "Enter New Phone Number:", initialvalue=contacts[name]['phone'])
            email = simpledialog.askstring("Update Contact", "Enter New Email:", initialvalue=contacts[name]['email'])
            address = simpledialog.askstring("Update Contact", "Enter New Address:", initialvalue=contacts[name]['address'])
            contacts[name] = {'phone': phone, 'email': email, 'address': address}
            self.view_contacts()
        else:
            messagebox.showwarning("Select Contact", "Please select a contact to update.")

    def delete_contact(self):
        if hasattr(self, 'selected_contact'):
            del contacts[self.selected_contact]
            self.view_contacts()
            messagebox.showinfo("Delete Contact", f"{self.selected_contact} deleted.")
        else:
            messagebox.showwarning("Select Contact", "Please select a contact to delete.")

# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()