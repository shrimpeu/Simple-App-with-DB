import mysql.connector
import streamlit as st

# Establish a connection to mysql server
db_config = mysql.connector.connect(
    # Replace these values with your database connection details
    host='localhost',
    user='root',
    password='mYsT4nd4rdQu3rYL4ngu4g3',
    database='simpleapp_db',
)

# Create a cursor for executing queries
mycursor = db_config.cursor()

def main():
    st.title("Simple CRUD App with MySQL")

    # Operation selection (Create, Read, Update, Delete) using select box
    operation = st.sidebar.selectbox("Select an Operation", ("Create", "Read", "Update", "Delete"))

    # Main logic based on the selected operation
    if operation == "Create":
        st.subheader("Create a Record")
        student_id = st.text_input("Enter Student ID")
        name = st.text_input("Enter Student's Name")
        webmail = st.text_input("Enter Student's Webmail")

        if st.button("Create"):
            # SQL query for inserting a new record
            sql = "Insert into students(name,webmail,student_id) values(%s, %s, %s)"
            val = (name, webmail, student_id)

            # Execute the query and commit the changes
            mycursor.execute(sql, val)
            db_config.commit()

            st.success("Record Created Successfully!")
    elif operation == "Read":
        st.subheader("Read a Record")
        mycursor.execute("SELECT * FROM students")

        # Fetch all records and display them
        result = mycursor.fetchall()
        for row in result:
            st.write(row)
    elif operation == "Update":
        st.subheader("Update a Record")
        student_id = st.text_input("Enter Student ID")
        name = st.text_input("Enter New Student Name")
        webmail = st.text_input("Enter New Webmail")

        if st.button("Update"):
            # SQL query for updating an existing record
            sql = "UPDATE students set name=%s, webmail=%s where student_id=%s"
            val = (name, webmail, student_id)

            # Execute the query and commit the changes
            mycursor.execute(sql, val)
            db_config.commit()

            st.success("Record Updated Successfully")
    elif operation == "Delete":
        st.subheader("Delete a Record")
        student_id = st.text_input("Enter Student ID")

        if st.button("Delete"):
            # SQL query for deleting a record
            sql = "DELETE FROM students WHERE student_id=%s"
            val = (student_id,)

            # Execute the query and commit the changes
            mycursor.execute(sql, val)
            db_config.commit()

            st.success("Record Deleted Successfully!")

if __name__ == "__main__":
    main()