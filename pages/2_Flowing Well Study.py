import streamlit as st
import matplotlib.pyplot as plt

# Custom CSS styling
def set_custom_style():
    st.markdown(
        """
        <style>
        .title {
            font-size: 36px;
            color: #0066cc;
            text-align: center;
            margin-bottom: 30px;
        }
        .content {
            font-size: 18px;
            color: #333333;
            margin-bottom: 20px;
        }
        .plot-container {
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            background-color: #f9f9f9;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    # Set custom CSS style
    set_custom_style()

    st.title("Visualisation avec Matplotlib")
    st.markdown("---")

    st.markdown("### Exemple de tracé interactif avec Matplotlib")
    st.markdown("Ceci est un exemple de tracé interactif utilisant Matplotlib.")
    st.markdown("Le graphique est affiché ci-dessous :")

    # Plot interactive chart with Matplotlib
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Display the plot inside a styled container
    st.markdown("---")
    st.markdown('<div class="plot-container">', unsafe_allow_html=True)
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
