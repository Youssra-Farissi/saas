import streamlit as st
import matplotlib.pyplot as plt

def main():
    st.title("Visualisation avec Matplotlib")

    # Exemple de tracé interactif avec Matplotlib
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    st.pyplot(fig)

if __name__ == "__main__":
    main()
