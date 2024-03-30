import streamlit as st

def main():
    st.set_page_config(page_title="Welcome to PetroSaaS", page_icon=":oil_drum:")

    st.title("Welcome to PetroSaaS: Your Data-Driven Solution for Oil & Gas Exploration")

    st.header("Unlocking Insights in the Oil & Gas Sector")

    st.write("Welcome to PetroSaaS, the premier Software as a Service (SaaS) platform designed specifically for the oil and gas industry. PetroSaaS empowers engineers, geologists, and analysts to harness the power of data in their exploration and production endeavors. Our intuitive platform offers a suite of tools and features tailored to the unique needs of the petrochemical sector, providing users with valuable insights and actionable intelligence.")

    st.image("/workspaces/saas/pages/gg.jpg", caption="Oil and Gas", use_column_width=True)

    st.write("At PetroSaaS, we understand the challenges and complexities of the oil and gas industry. That's why we've developed a comprehensive solution to streamline data analysis, visualization, and decision-making processes. Whether you're conducting reservoir modeling, evaluating drilling prospects, or optimizing production strategies, PetroSaaS equips you with the tools you need to succeed in today's dynamic energy landscape.")

    if st.button("Get Started"):
        st.write("Join thousands of industry professionals who rely on PetroSaaS to drive innovation, efficiency, and success in their oil and gas operations. Whether you're a seasoned industry veteran or a newcomer to the field, PetroSaaS offers a wealth of resources, training materials, and support to help you maximize the value of your data. Experience the power of PetroSaaS today and unlock new opportunities for growth and discovery in the oil and gas industry.")

if __name__ == "__main__":
    main()
