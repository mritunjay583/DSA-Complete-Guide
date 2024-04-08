#include<bits/stdc++.h>


using namespace std;

void OneDimentionalArray(){
    int staticArray[5] = {1, 2, 3, 4, 5}; // Declaration and Initialization of a Static Array
    int array1[] = {1, 2, 3, 4, 5};
    int array2[5] = {1, 2, 3, 4, 5};
    int array3[5] = {1, 2}; // Initializes first two elements, rest will be 0


    // Dynamically Allocate Memory for a 1D Array
    int size = 5;
    int *dynamicArray = new int[size];
    delete[] dynamicArray; // Deallocate Memory
    
}

void TwoDimentionalArray(){
    
    // Dynamically Allocate Memory for a 2D Array
    int rows = 3, cols = 4;
    int **dynamic2DArray = new int*[rows]; // Allocate memory for rows

    for (int i = 0; i < rows; ++i) {
        dynamic2DArray[i] = new int[cols]; // Allocate memory for each row
    }

    // Deallocate Memory
    for (int i = 0; i < rows; ++i) {
        delete[] dynamic2DArray[i]; // Deallocate memory for each row
    }
    delete[] dynamic2DArray; // Deallocate memory for rows



    int *dynamicArray = new int[5]{1, 2, 3, 4, 5};
    int dynamic2DArray2[3][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
}

int main(){
    return 0;
}