#include <stdio.h>
#include <string>
#include <vector>

using namespace std;
typedef struct block {
  char* data;
  char* prevHash;
  char* hash;
} block;

block makeBlock(char* data, char* prevHash) {
  string Data = data. +  prevHash;
  block b  {}
}

int main(int argc, char** argv) {

}
