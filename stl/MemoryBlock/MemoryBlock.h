// MemoryBlock.h
#pragma once

#include <iostream>
#include <algorithm>

class MemoryBlock
{
 protected:
   size_t _length;
   int *_data;

 public:
   explicit MemoryBlock(size_t length)
       : _length(length), _data(new int[_length]) { 
       std::cout << "In MemoryBlock(size_t). length = " << _length << std::endl;
   }
   // destructor
   ~MemoryBlock() { 
      std::cout << "In ~MemoryBlock() - deleting " << _length << std::endl;
      delete[] _data;
   }
   // copy constructor
   MemoryBlock(const MemoryBlock& other) { 
      std::cout << "In MemoryBlock(MemoryBlock&) - length = " << _length << std::endl;
      _length = other._length;
      _data = new int[_length];
      std::copy(other._data, other._data + _length, _data);
   }
   // copy move constructor
   MemoryBlock(MemoryBlock &&other) noexcept : _length(0), _data(nullptr)
   {
      std::cout << "In MemoryBlock(MemoryBlock&&) - length = " << other._length 
         << " Removing resources." << std::endl;
      // copy the data
      _length = other._length;
      _data = other._data;
      // release other's resources
      other._length = 0;
      other._data = nullptr;  // don't delete!!
   }
   // = copy operator
   MemoryBlock& operator = (const MemoryBlock &other)
   {
      std::cout << "In operator = (MemoryBlock&) - length = " << _length << std::endl;
      if (this != &other) {
         delete[] _data;
         _length = other._length;
         _data = new int[_length];
         std::copy(other._data, other._data + _length, _data);
      }
      return *this;
   }
   // = move operator
   MemoryBlock &operator=(MemoryBlock &&other) noexcept
   {
      std::cout << "In operator = (MemoryBlock&&) - length = " << other._length << std::endl;
      if (this != &other) {
         delete[] _data;
         _length = other._length;
         _data = other._data;
         // and release other's resources
         other._length = 0;
         other._data = nullptr;
      }
      return *this;
   }
};
