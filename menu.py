import streamlit as st


def authenticated_menu():
    # Show a navigation menu for authenticated users
    st.sidebar.page_link("app.py", label="Home")
    st.sidebar.page_link("pages/waste_data.py", label="생활 폐기물 발생 현황")
    st.sidebar.page_link("pages/predicting_waste_generation.py", label="폐기물 발생량 데이터 전처리")
    st.sidebar.page_link("pages/predicting_model.py", label="폐기물 발생량 예측 모델 생성")
    st.sidebar.page_link("pages/predicting_waste.py", label="시도/시군구 폐기물 발생량 예측")
    st.sidebar.page_link("pages/arima_model.py", label="ARIMA 모델")
    # if st.session_state.role in ["admin", "super-admin"]:
    #     st.sidebar.page_link("pages/admin.py", label="Manage users")
    #     st.sidebar.page_link(
    #         "pages/super-admin.py",
    #         label="Manage admin access",
    #         disabled=st.session_state.role != "super-admin",
    #     )


# def unauthenticated_menu():
#     # Show a navigation menu for unauthenticated users
#     st.sidebar.page_link("app.py", label="Log in")


def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        authenticated_menu()
        # unauthenticated_menu()
        return
    authenticated_menu()


def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("app.py")
    menu()