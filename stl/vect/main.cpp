// vec1.cc - vector example
// compile: g++ -std=c++20 [other compiler flags...] vec1.cc -o vec1 -lstdc++
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

void display_vector(const auto &vec)
{
   // use auto for parameters, so you can use
   // with any type of vector
   for (auto e : vec)
      // NOTE: this will work if each element of
      // vector overloads << operator (ok for all std data types)
      cout << e << " ";
   cout << endl;
}

// my custom class
class Employee
{
 protected:
   string _name;
   int _age;
   double _salary;

 public:
   Employee() : _name{""}, _age{0}, _salary{0.0}
   { /* nothing more */
   }

   Employee(const string &name, const int &age, const double &salary)
   {
      _name = name;
      _age = age;
      _salary = salary;
   }

   Employee(const Employee &other)
   {
      if (this != &other) {
         this->_name = other._name;
         this->_age = other._age;
         this->_salary = other._salary;
      }
   }

   Employee &operator=(const Employee &other)
   {
      if (this != &other) {
         this->_name = other._name;
         this->_age = other._age;
         this->_salary = other._salary;
      }
      return *this;
   }

   // getter & setters
   string name() const { return _name; }
   void setName(const string &name) { _name = name; }
   int age() const { return _age; }
   void setAge(const int &age) { _age = age; }
   double salary() const { return _salary; }
   void setSalary(const double &salary) { _salary = salary; }

   // helper functions
   friend ostream &operator<<(ostream &ost, const Employee &emp);
};

// friend
ostream &operator<<(ostream &ost, const Employee &emp)
{
   ost << "Employee: name - " << emp.name() << " age - " << emp.age() 
      << " salary - " << emp.salary() << endl;
   return ost;
}

int main(void)
{
   vector<int> v{1, 2, 3, 4, 5}; // new C++ syntax for initializing vector

   // display vector
   display_vector(v);

   // square each element of vector inline
   std::transform(v.begin(), v.end(), v.begin(), [](int i) -> int { return i * i; });
   display_vector(v);

   // vector with custom class - new style of initialization
   vector<Employee> emps{{"Manish", 52, 5500.75},
                         // equivalent to Employee("Manish", 52, 5500.75);
                         {"Anupa", 45, 7500.45},
                         {"Sunila", 81, 102567.99}};
   display_vector(emps);

   // double the salary for each employee
   std::transform(emps.begin(), emps.end(), emps.begin(),
                  [](Employee &emp) -> Employee { return Employee(emp.name(), emp.age(), emp.salary() * 2); });
   display_vector(emps);

   return EXIT_SUCCESS;
}
