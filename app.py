import streamlit as st

# Streamlit layout
st.set_page_config(layout="wide")


def main():
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Use st.sidebar to create the sidebar
    with st.sidebar:
        # Center-aligned headers
        st.markdown(
            "<h1 style='text-align: center;'> Run Tracker </h1>",
            unsafe_allow_html=True,
        )

    # User input box - Query
    user_input_query = st.text_input(
        "Question",
        # key="user_input_1",
        value="",
        placeholder="Please enter your question here",
        key="input_text_key",
    )

    # Setting columns to control size of the dropdowns
    col, col2, buff = st.columns([1, 1, 3])

    # User input drop down - Demo Type
    plan_type = col.selectbox(  # noqa Streamlit widget declaration
        "Plan Type", ("Medicare", "Medicaid", "Commercial"), key="drop_down_1"
    )

    # # User input drop down - Policy Type
    state = col2.selectbox(  # noqa Streamlit widget declaration
        "Policy Type", ("AZ", "IL", "CA", "MI"), key="drop_down_2_key"
    )

    submit = st.button("Submit", key="button_key")

    if submit:
        st.markdown(f"You have netered: {user_input_query}")

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
