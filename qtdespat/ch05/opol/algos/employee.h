// employee.h
#ifndef __Employee_h__
#define __Employee_h__

#include <string>

class Employee {
   public:
      Employee(long empId, const std::wstring& firstName, const std::wstring& lastName, double salary); 
      
      // getters & setters
      long empId() const { return m_empId; }
      void setEmpId(long empId) { m_empId = empId; }
      const std::wstring& firstName() const { return m_firstName; }
      void  setFirstName(const std::string& firstName) { m_firstName = firstName; }
      const std::wstring& lastName() const { return m_lastName; }
      void  setLastName(const std::string& lastName) { m_lastName = lastName; }
      double salary() const { return m_salary; }
      void setSalary(double salary) { m_salary = salary; }

   protected:
      long m_empId;
      std::wstring m_firstName, m_lastName;
      double m_salary;
};


#endif   // __Employee_h__
