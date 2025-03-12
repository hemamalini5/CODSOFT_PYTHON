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
        self.search_entry = tk.Entry(root, textvariable=self.search_var, width=40, fg='grey')
        self.search_entry.pack(pady=10, padx=10)
        self.search_entry.insert(0, 'Search Contact...')
        self.search_entry.bind("<FocusIn>", self.clear_placeholder)
        self.search_entry.bind("<FocusOut>", self.add_placeholder)
        self.search_entry.bind("<Return>", self.search_contact)

        # Contact Listbox
        self.contact_listbox = tk.Listbox(root, width=50, height=15, bg='light sky blue')
        self.contact_listbox.pack(pady=10)

        # Buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Contact", command=self.add_contact, bg='green', fg='white')
        self.add_button.pack(side="left", padx=5)

        self.update_button = tk.Button(self.button_frame, text="Update Contact", command=self.update_contact, bg='blue', fg='white')
        self.update_button.pack(side="left", padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact, bg='red', fg='white')
        self.delete_button.pack(side="left", padx=5)

        self.view_button = tk.Button(self.button_frame, text="View Contacts", command=self.view_contacts, bg='orange', fg='white')
        self.view_button.pack(side="left", padx=5)

        self.contact_listbox.bind('<<ListboxSelect>>', self.on_select)

    def clear_placeholder(self, event):
        if self.search_entry.get() == 'Search Contact...':
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(fg='black')

    def add_placeholder(self, event):
        if not self.search_entry.get():
            self.search_entry.insert(0, 'Search Contact...')
            self.search_entry.config(fg='grey')

    def on_select(self, event):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            self.selected_contact = self.contact_listbox.get(selected_index)
    
    def add_contact(self):
        dialog = ContactDialog(self.root)
        self.root.wait_window(dialog.top)
        if dialog.result:
            name, phone, email, address = dialog.result
            if name and phone:
                contacts[name] = {'phone': phone, 'email': email, 'address': address}
                self.view_contacts()
            else:
                messagebox.showwarning("Input Error", "Name and phone number are required.")
        
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
            dialog = ContactDialog(self.root, name, contacts[name]['phone'], contacts[name]['email'], contacts[name]['address'])
            self.root.wait_window(dialog.top)
            if dialog.result:
                new_name, phone, email, address = dialog.result
                contacts[new_name] = {'phone': phone, 'email': email, 'address': address}
                if new_name != name:
                    del contacts[name]
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

class ContactDialog:
    def __init__(self, parent, name="", phone="", email="", address=""):
        self.top = tk.Toplevel(parent)
        self.top.title("Contact Information")
        
        tk.Label(self.top, text="Name:").pack(pady=5)
        self.name_entry = tk.Entry(self.top)
        self.name_entry.pack(pady=5)
        self.name_entry.insert(0, name)
        
        tk.Label(self.top, text="Phone:").pack(pady=5)
        self.phone_entry = tk.Entry(self.top)
        self.phone_entry.pack(pady=5)
        self.phone_entry.insert(0, phone)
        
        tk.Label(self.top, text="Email:").pack(pady=5)
        self.email_entry = tk.Entry(self.top)
        self.email_entry.pack(pady=5)
        self.email_entry.insert(0, email)
        
        tk.Label(self.top, text="Address:").pack(pady=5)
        self.address_entry = tk.Entry(self.top)
        self.address_entry.pack(pady=5)
        self.address_entry.insert(0, address)
        
        self.submit_button = tk.Button(self.top, text="OK", command=self.on_submit)
        self.submit_button.pack(pady=10)
        
        self.result = None

    def on_submit(self):
        self.result = (self.name_entry.get(), self.phone_entry.get(), self.email_entry.get(), self.address_entry.get())
        self.top.destroy()

# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()