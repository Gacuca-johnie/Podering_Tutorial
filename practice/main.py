import streamlit as st
from streamlit_option_menu import option_menu
import about, account, home, trending, your_post

st.set_page_config(
    page_title="Pondering"
)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function 
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='Pondering',
                options=['Home', 'Account', 'Trending', 'Your Post', 'About'],
                icons=['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px"},
                    "nav-link-selected": {"background-color": "#02ab21"}
                }
            )

        if app == 'Home':
            st.write(' HOME')
            if hasattr(home, 'app'):
                home.app()
            else:
                st.write("Error: home module does not have an app function.")
        elif app == 'Account':
            st.write("ACCOUNT")
            if hasattr(account, 'app'):
                account.app()
            else:
                st.write("Error: account module does not have an app function.")
        elif app == 'Trending':
            st.write("TRENDING")
            if hasattr(trending, 'app'):
                trending.app()
            else:
                st.write("Error: trending module does not have an app function.")
        elif app == 'Your Post':
            st.write("YOUR POST")
            if hasattr(your_post, 'app'):
                your_post.app()
            else:
                st.write("Error: your_post module does not have an app function.")
        elif app == 'About':
            st.write("ABOUT")
            if hasattr(about, 'app'):
                about.app()
            else:
                st.write("Error: about module does not have an app function.")

# Create an instance of the MultiApp class
app = MultiApp()
app.run()
