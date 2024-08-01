import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate('pondering-tutorial-1a5ce-979794598388.json')
    firebase_admin.initialize_app(cred)

# Get a reference to the Firestore service
db = firestore.client()

def app():
    st.write('Latest Posts')
    
    # Initialize session state variables
    if "username" not in st.session_state:
        st.session_state.username = ""
    if "usermail" not in st.session_state:
        st.session_state.usermail = ""
    if "signedout" not in st.session_state:
        st.session_state.signedout = True
    if "name" not in st.session_state:
        st.session_state.name = ""

    if st.session_state.signedout:
        st.text('Please Login first')
    else:
        st.title(f'Posted by: {st.session_state["username"]}')
        try:
            # Fetch posts for the current user
            result = db.collection('Posts').document(st.session_state['username']).get()
            if result.exists:
                r = result.to_dict()
                content = r['content']

                def delete_post(k):
                    c = int(k)
                    h = content[c]
                    try:
                        db.collection('Posts').document(st.session_state['username']).update({"content": firestore.ArrayRemove([h])})
                        st.warning('Post deleted')
                    except Exception as e:
                        st.error(f'Something went wrong: {e}')

                for c in range(len(content) - 1, -1, -1):
                    st.text_area(label='', value=content[c], key=f'post_{c}')
                    st.button('Delete Post', on_click=delete_post, args=(c,), key=f'delete_{c}')
            else:
                st.info('No posts available.')
        except Exception as e:
            st.error(f'Error fetching posts: {e}')

# Example to demonstrate the `app` function
if __name__ == '__main__':
    app()
