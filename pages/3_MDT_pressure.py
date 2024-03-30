import streamlit as st
from scipy import spatial

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
        .result {
            font-size: 24px;
            color: #008000;
            margin-top: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    # Set custom CSS style
    set_custom_style()

    st.title("Utilisation de Scipy")
    st.markdown("---")

    # Exemple d'utilisation de la fonction de distance euclidienne
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = spatial.distance.euclidean(point1, point2)

    st.markdown("### Distance Euclidienne")
    st.markdown("---")
    st.write(f"**Point 1:** {point1}")
    st.write(f"**Point 2:** {point2}")
    st.markdown(f"**Distance:** {distance:.2f}")

    

if __name__ == "__main__":
    main()
