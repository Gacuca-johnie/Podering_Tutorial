import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate('pondering-tutorial-1a5ce-979794598388.json')
    firebase_admin.initialize_app(cred)

def app():
    st.title('Welcome to :violet[Pondering]👩‍🦱')

    # Initialize session state
    if "username" not in st.session_state:
        st.session_state.username = ""
    if "usermail" not in st.session_state:
        st.session_state.usermail = ""
    if "signedout" not in st.session_state:
        st.session_state.signedout = True
    if "name" not in st.session_state:
        st.session_state.name = ""

    if st.session_state.signedout:
        choice = st.selectbox('Login/Signup', ['Login', 'Sign up'])
        
        if choice == 'Login':
            email = st.text_input('Email Address')
            password = st.text_input('Password', type='password')

            def login():
                try:
                    user = auth.get_user_by_email(email)
                    st.success('Login Successful')
                    st.write(f'Welcome back, {user.display_name}!')
                    st.session_state.username = user.uid
                    st.session_state.usermail = user.email
                    st.session_state.name = user.display_name
                    st.session_state.signedout = False
                except Exception as e:
                    st.warning(f'Login Failed: {e}')
            
            st.button('Login', on_click=login)

        elif choice == 'Sign up':
            name = st.text_input('Name')
            email = st.text_input('Email Address')
            password = st.text_input('Password', type='password')
            username = st.text_input('Enter your unique username')

            if st.button('Create my account'):
                try:
                    user = auth.create_user(
                        email=email,
                        password=password,
                        uid=username,
                        display_name=name
                    )
                    st.success('Account created successfully!')
                    st.markdown('Please Login using your email and password')
                    st.balloons()
                except Exception as e:
                    st.error(f'Error: {e}')

    else:
        st.write(f'Logged in as: {st.session_state.name} ({st.session_state.username})')
        if st.button('Sign out'):
            st.session_state.username = ""
            st.session_state.usermail = ""
            st.session_state.name = ""
            st.session_state.signedout = True
            st.success('Signed out successfully!')

# Example to demonstrate the `app` function
if __name__ == '__main__':
    app()
