import streamlit as st

st.title("Kelompok 3 - Visualisasi Data")
st.write("these are our members' names")
st.write("- Aisyah Nurul Fitiriah - 0110223172")
st.write("- Nama Azkiya Zahra - 0110223307")
st.write("- Syavira Aulia Syamsi - 0110121127")

st.write("Hello World!!!")
st.title("This is our Title")
st.header("""This is our Header""")
st.subheader("""This is our Sub-header""")
st.caption("""This is our Caption""")

#Displaying Plain Text
st.text("Hi, \nPeople\t!!!!!!!!!")
st.text('Welcome to')
st.text("""Streamlit's World""")

#Displaying Markdown
st.markdown("# Hi, \n# ***People*** \t!!!!!!!!")
st.markdown("##Welcome to")
st.markdown("""### Stramlit's World""")

#Displaying Latex
st.latex(r'''cos^2 \theta = 1 - 2\sin^2 \theta''')
st.latex(r'''(a+b)^2 = a^2 + b^2 + 2ab''')
st.latex(r'''
    \frac{\partial u}{\partial t} 
    = h^2 \left( 
        \frac{\partial^2 u}{\partial x^2} 
        + \frac{\partial^2 u}{\partial y^2} 
        + \frac{\partial^2 u}{\partial z^2} 
    \right)
''')

#Displaying Python Kode
st.subheader("""Python Code""")
code = '''def hello():
print("Hello, Streamlit!")'''
st.code(code, language='python')

#Displaying Java Code
st.subheader("""Java Code""")
st.code("""public class GFG {
        public static void main(String args[])
        {
        syustem.out.println("Hello World);
        }
        }""", language='javascript')
st.subheader("""Javascript Code""")
st.code(""" <p id="demo"></p>
        <script>
        try {
        adddlert("Welcomeguest!");
        }
        catch(err) {
        document.getElementById("demo").innerHTML = err.message;
        }
        </script>""")