import json

import pandas as pd
import requests
import streamlit as st

API_BASE_URL = "http://127.0.0.1:8000/api/users/"


def fetch_users():
    response = requests.get(API_BASE_URL)
    response.raise_for_status()
    return response.json()


def create_user(first_name, last_name, email, phone):
    data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
    }
    response = requests.post(API_BASE_URL, json=data)
    response.raise_for_status()
    return response.json()


def update_user(user_id, first_name, last_name, email, phone):
    data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
    }
    response = requests.patch(f"{API_BASE_URL}{user_id}/", json=data)
    response.raise_for_status()
    return response.json()


def delete_user(user_id):
    response = requests.delete(f"{API_BASE_URL}{user_id}/")
    response.raise_for_status()
    return response.status_code


def get_user_options(users):
    return [f"{user['id']} - {user['first_name']} {user['last_name']}" for user in users]


def parse_selected_id(selection):
    return int(selection.split(" - ")[0])


def main():
    st.set_page_config(
        page_title="User CRUD Dashboard",
        page_icon="🧑‍💻",
        layout="wide",
    )

    st.header("🌟 User CRUD Dashboard")
    st.write(
        "This dashboard connects to the Django backend and lets you view, create, update, and delete users in a polished UI."
    )

    try:
        users = fetch_users()
        users_df = pd.DataFrame(users)
    except requests.RequestException as error:
        st.error("Unable to connect to the backend API. Make sure the Django server is running at http://127.0.0.1:8000/")
        st.write(error)
        return

    action = st.sidebar.selectbox(
        "Choose action",
        ["View users", "Create user", "Update user", "Delete user"],
    )

    if action == "View users":
        st.subheader("User list")
        if users:
            st.dataframe(users_df[['id', 'first_name', 'last_name', 'email', 'phone', 'created_at', 'updated_at']])
            st.metric("Total users", len(users))
        else:
            st.info("No users found. Create your first user using the sidebar.")

    elif action == "Create user":
        st.subheader("Create a new user")
        with st.form(key="create_form"):
            first_name = st.text_input("First name")
            last_name = st.text_input("Last name")
            email = st.text_input("Email")
            phone = st.text_input("Phone")
            submitted = st.form_submit_button("Create user")

        if submitted:
            try:
                created = create_user(first_name, last_name, email, phone)
                st.success(f"User created: {created['first_name']} {created['last_name']}")
                st.json(created)
            except requests.RequestException as error:
                st.error("Failed to create user. Please check the input and backend server.")
                st.write(error)

    elif action == "Update user":
        st.subheader("Update an existing user")
        if users:
            selected = st.selectbox("Choose user", get_user_options(users))
            user_id = parse_selected_id(selected)
            selected_user = next(user for user in users if user["id"] == user_id)
            with st.form(key="update_form"):
                first_name = st.text_input("First name", value=selected_user["first_name"])
                last_name = st.text_input("Last name", value=selected_user["last_name"])
                email = st.text_input("Email", value=selected_user["email"])
                phone = st.text_input("Phone", value=selected_user["phone"])
                submitted = st.form_submit_button("Update user")

            if submitted:
                try:
                    updated = update_user(user_id, first_name, last_name, email, phone)
                    st.success("User updated successfully")
                    st.json(updated)
                except requests.RequestException as error:
                    st.error("Failed to update user.")
                    st.write(error)
        else:
            st.info("No users available to update.")

    elif action == "Delete user":
        st.subheader("Delete a user")
        if users:
            selected = st.selectbox("Choose user", get_user_options(users))
            user_id = parse_selected_id(selected)
            if st.button("Delete user"):
                try:
                    status = delete_user(user_id)
                    if status == 204:
                        st.success("User deleted successfully")
                    else:
                        st.warning(f"Unexpected status code: {status}")
                except requests.RequestException as error:
                    st.error("Failed to delete user.")
                    st.write(error)
        else:
            st.info("No users available to delete.")

    st.sidebar.markdown("---")
    st.sidebar.markdown("Built with Streamlit and Django REST Framework.")


if __name__ == "__main__":
    main()
