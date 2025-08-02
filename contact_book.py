import streamlit as st

# Use session_state to store data between interactions
if 'contacts' not in st.session_state:
    st.session_state.contacts = []

def add_contact():
    st.subheader("Add New Contact")
    name = st.text_input("Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email")
    address = st.text_area("Address")

    if st.button("Add Contact"):
        if name and phone:
            st.session_state.contacts.append({
                'name': name,
                'phone': phone,
                'email': email,
                'address': address
            })
            st.success("Contact added successfully!")
        else:
            st.warning("Name and Phone are required.")

def view_contacts():
    st.subheader("Contact List")
    if st.session_state.contacts:
        for i, c in enumerate(st.session_state.contacts):
            st.write(f"**{i+1}. {c['name']}** - {c['phone']}")
    else:
        st.info("No contacts found.")

def search_contact():
    st.subheader("Search Contact")
    query = st.text_input("Enter name or phone to search")
    if query:
        found = False
        for c in st.session_state.contacts:
            if query.lower() in c['name'].lower() or query in c['phone']:
                st.success(f"Contact Found: {c['name']}")
                st.write(f"📞 Phone: {c['phone']}")
                st.write(f"📧 Email: {c['email']}")
                st.write(f"🏠 Address: {c['address']}")
                found = True
                break
        if not found:
            st.error("Contact not found.")

def update_contact():
    st.subheader("Update Contact")
    names = [c['name'] for c in st.session_state.contacts]
    if names:
        selected = st.selectbox("Select contact to update", names)
        contact = next(c for c in st.session_state.contacts if c['name'] == selected)

        new_phone = st.text_input("Phone", value=contact['phone'])
        new_email = st.text_input("Email", value=contact['email'])
        new_address = st.text_area("Address", value=contact['address'])

        if st.button("Update"):
            contact['phone'] = new_phone
            contact['email'] = new_email
            contact['address'] = new_address
            st.success("Contact updated.")
    else:
        st.info("No contacts available to update.")

def delete_contact():
    st.subheader("Delete Contact")
    names = [c['name'] for c in st.session_state.contacts]
    if names:
        selected = st.selectbox("Select contact to delete", names)
        if st.button("Delete"):
            st.session_state.contacts = [c for c in st.session_state.contacts if c['name'] != selected]
            st.success("Contact deleted.")
    else:
        st.info("No contacts to delete.")

# --------- Streamlit App UI ---------
st.title("📒 Contact Book")

menu = st.sidebar.radio("Menu", ["Add", "View", "Search", "Update", "Delete"])

if menu == "Add":
    add_contact()
elif menu == "View":
    view_contacts()
elif menu == "Search":
    search_contact()
elif menu == "Update":
    update_contact()
elif menu == "Delete":
    delete_contact()
