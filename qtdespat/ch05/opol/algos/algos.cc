// algos.cc - STL algos
#include <iostream>
#include <vector>
#include <algorithm>
#include "employee.h"

bool compare_by_empName(const Employee& emp1, const Employee& emp2)
{
  return emp1.lastName() < emp2.lastName();
}

wostream& operator << (wostream& ost, const Employee& emp)
{
  ost << emp.empId() << " - " << emp.lastName().c_str() << ", "
    << emp.firstName().c_str() << " - " << emp.salary();
  return ost;
}

int main(void)
{
  Employee _emps[] = {
    {100, L"Manish", L"Bhobe", 1245.67},
    {200, L"Anupa",  L"Sardesai", 2546.78},
    {300, L"Aarti",  L"Mulgaonkar", 4278.43},
    {400, L"Surjit", L"Arur", 6543.45},
  };
  size_t numEmps = sizeof(_emps)/sizeof(_emps[0]);

  std::vector<Employee> emps;
  // copy array to vector
  std::copy(&_emps[0], &_emps[numEmps], back_inserter(emps));
  // display vector
  for (const auto iter = emps.begin(); iter != emps.end(); ++iter)
    std::cout << *iter << std::endl;

}

