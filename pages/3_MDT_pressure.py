import streamlit as st
from scipy import spatial

def main():
    st.title("Utilisation de Scipy")

    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = spatial.distance.euclidean(point1, point2)
    st.write(f"Distance euclidienne entre {point1} et {point2} : {distance}")

if __name__ == "__main__":
    main()
