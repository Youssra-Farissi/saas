import streamlit as st

def main():
    # Set page title and favicon
    st.set_page_config(page_title="Welcome to PetroSaaS", page_icon=":oil_drum:")

    # Add a title to the page
    st.title("Welcome to PetroSaaS: Your Data-Driven Solution for Oil & Gas Exploration")

    # Add a header
    st.header("Unlocking Insights in the Oil & Gas Sector")

    # Add a paragraph introducing the app
    st.write("Welcome to PetroSaaS, the premier Software as a Service (SaaS) platform designed specifically for the oil and gas industry. PetroSaaS empowers engineers, geologists, and analysts to harness the power of data in their exploration and production endeavors. Our intuitive platform offers a suite of tools and features tailored to the unique needs of the petrochemical sector, providing users with valuable insights and actionable intelligence.")

    # Add an image or logo to enhance aesthetics
    st.image("oil_gas_image.jpg", caption="Oil and Gas", use_column_width=True)

    # Add another paragraph describing the app's features
    st.write("At PetroSaaS, we understand the challenges and complexities of the oil and gas industry. That's why we've developed a comprehensive solution to streamline data analysis, visualization, and decision-making processes. Whether you're conducting reservoir modeling, evaluating drilling prospects, or optimizing production strategies, PetroSaaS equips you with the tools you need to succeed in today's dynamic energy landscape.")

    # Add a call-to-action button to encourage user interaction
    if st.button("Get Started"):
        st.write("Join thousands of industry professionals who rely on PetroSaaS to drive innovation, efficiency, and success in their oil and gas operations. Whether you're a seasoned industry veteran or a newcomer to the field, PetroSaaS offers a wealth of resources, training materials, and support to help you maximize the value of your data. Experience the power of PetroSaaS today and unlock new opportunities for growth and discovery in the oil and gas industry.")

if __name__ == "__main__":
    main()
