import streamlit as st

st.header('Energy Calculator')

col1, col2 = st.columns(2)

with col1:
    st.subheader(':red[kinetic Energy]')
    m= st.number_input('Mass:',key = 'a')
    v= st.number_input('Velocity:', key = 'b')
    if st.button('Calculate',key = 'abc'):
        st.write('Kinetic Energy is:', 0.5 * m * v**2)

with col2:
    st.subheader(':blue[potential Energy]')
    ma= st.number_input('Mass:', key = 'c')
    h= st.number_input('Height:', key = 'd')
    if st.button('Calculate',key = 'xyz'):
        st.write('Potential Energy is:', ma* 10 * h)
