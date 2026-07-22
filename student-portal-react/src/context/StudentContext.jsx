import { createContext, useState } from "react";

export const StudentContext = createContext();

function StudentProvider({ children }) {
  const [studentName, setStudentName] = useState("Harini");

  return (
    <StudentContext.Provider value={{ studentName, setStudentName }}>
      {children}
    </StudentContext.Provider>
  );
}

export default StudentProvider;